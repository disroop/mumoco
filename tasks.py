#!/usr/bin/env python

"""
The build.py is the single point containing the build logic. Thus this script can be used to build locally or
methods from the file can be used in the github actions.
The github actions shall just call methods from this file so we are not locked in the the build server solution.
"""
import os
import shutil

from invoke import run, task


@task
def install_dependencies(c):
    c.run("poetry install --no-interaction --no-root")


@task
def install_libraries(c):
    c.run("poetry install --no-interaction")


@task
def check_format_with_black(c):
    c.run("poetry run black -l 120 --check .")


@task
def sort_imports_with_isort(c):
    c.run("poetry run isort --profile black --check .")


@task
def lint_with_pylint(c):
    c.run("poetry run pylint ./src --enable=W0611,W0614 -disable=C0114,C0115,C0116,W0511 --max-line-length=120")


@task
def lint_with_flake8(c):
    # stop the build if there are Python syntax errors or undefined names
    c.run("poetry run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics  --extend-exclude=.venv")
    # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
    c.run(
        "poetry run flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --extend-exclude=.venv"
    )


@task
def lint_with_bandit(c):
    c.run("poetry run bandit -r src/ --exclude .venv")


@task
def run_tests(c):
    run(
        "poetry run pytest --cov=src --junitxml=reports/xunit.xml --cov src/ --cov-report term --cov-report html:reports/html --cov-report xml:reports/coverage.xml"
    )
    # todo define threshold and fail if coverage is below


@task
def build(c):
    c.run("poetry build")


@task
def publish(c, pypiusername, pypipassword, dryrun=False):
    if dryrun:
        c.run(f"poetry publish --username '{pypiusername}'  --password '{pypipassword}' --dry-run")
    else:
        c.run(f"poetry publish --username '{pypiusername}'  --password '{pypipassword}'")


@task
def clean(c):
    shutil.rmtree(".venv", ignore_errors=True)
    shutil.rmtree(".pytest_cache", ignore_errors=True)
    shutil.rmtree(".mypy_cache", ignore_errors=True)
    shutil.rmtree("dist", ignore_errors=True)
    shutil.rmtree("reports", ignore_errors=True)
    try:
        os.remove(".coverage")
    except OSError:
        pass


@task
def configure_poetry(c):
    c.run("poetry config virtualenvs.path .venv")
    c.run("poetry config virtualenvs.create true")
    c.run("poetry config virtualenvs.in-project true")
