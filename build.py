#!/usr/bin/env python

"""
The build.py is the single point containing the build logic. Thus this script can be used to build locally or methods from the file can be used in the github actions.
The github actions shall just call methods from this file so we are not locked in the the build server solution.
"""
import os
import shutil


def run(cmd, assert_error=False):
    print("*********** Running: %s" % cmd)
    ret = os.system(cmd)
    if ret == 0 and assert_error:
        raise Exception("Command unexpectedly succeeded: %s" % cmd)
    if ret != 0 and not assert_error:
        raise Exception("Failed command: %s" % cmd)


def install_dependencies():
    run("poetry install --no-interaction --no-root")


def install_libraries():
    run("poetry install --no-interaction")


def check_format_with_black():
    run("poetry run black -l 120 --check .")


def sort_imports_with_isort():
    run("poetry run isort --profile black --check .")


def lint_with_flake8():
    # stop the build if there are Python syntax errors or undefined names
    run("poetry run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics  --extend-exclude=.venv")
    # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
    run(
        "poetry run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --extend-exclude=.venv"
    )


def lint_with_bandit():
    run("poetry run bandit -r src/ --exclude .venv")


def run_tests():
    run(
        "poetry run pytest --cov=src --junitxml=reports/xunit.xml --cov src/ --cov-report term --cov-report html:reports/html --cov-report xml:reports/coverage.xml"
    )
    # todo define threshold and fail if coverage is below


def build():
    run("poetry build")


def publish(pypi_username, pypi_password, dry_run=False):
    if dry_run:
        run(f"poetry publish --username '{pypi_username}'  --password '{pypi_password}' --dry-run")
    else:
        run(f"poetry publish --username '{pypi_username}'  --password '{pypi_password}'")


def clean():
    shutil.rmtree(".venv", ignore_errors=True)
    shutil.rmtree(".pytest_cache", ignore_errors=True)
    shutil.rmtree(".mypy_cache", ignore_errors=True)
    shutil.rmtree("dist", ignore_errors=True)
    shutil.rmtree("reports", ignore_errors=True)
    try:
        os.remove(".coverage")
    except OSError:
        pass


if __name__ == "__main__":
    clean()
    run("poetry config virtualenvs.path .venv")
    run("poetry config virtualenvs.create true")
    run("poetry config virtualenvs.in-project true")
    check_format_with_black()
    sort_imports_with_isort()
    install_dependencies()
    install_libraries()
    lint_with_flake8()
    lint_with_bandit()
    # todo add mypy
    run_tests()
    # todo add Fix Code Coverage Paths and sonar scann
    build()
    publish(os.environ.get("secrets.PYPI_USERNAME "), os.environ.get("secrets.PYPI_PASSWORD"))
