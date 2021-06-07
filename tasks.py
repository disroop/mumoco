#!/usr/bin/env python

"""
The build.py is the single point containing the build logic. Thus this script can be used to build locally or
methods from the file can be used in the github actions.
The github actions shall just call methods from this file so we are not locked in the the build server solution.
"""
import shutil

from invoke import task

# Configurations
# Note: configuration in pyproject.toml is the prefered solution
# because IDE can integrate in pyproject.toml but will not integrate to our custom tasks.py
LINE_LENGTH = 120
MAX_COMPLEXITY = 10


@task
def check_format_with_black(c, fix=False):
    # Note: picks the LINE_LENGTH from pyproject.toml
    format_cmd = f"black ."
    check_cmd = format_cmd + " --check"
    if fix:
        c.run(format_cmd)
    c.run(check_cmd)


@task
def sort_imports_with_isort(c, fix=False):
    if fix:
        c.run("isort --check .")
    c.run("isort .")


@task
def lint_with_pylint(c):
    c.run("pylint ./src")


@task
def lint_with_flake8(c):
    errors = ["E9", "F63", "F7", "F82"]
    # stop the build if there are Python syntax errors or undefined names
    flake8_syntax_cmd = "flake8 . --count --select={}".format(",".join(errors))
    flake8_syntax_cmd += "--show-source --statistics --extend-exclude=.venv"
    c.run(flake8_syntax_cmd)

    # exit-zero treats all errors as warnings. The GitHub editor is 120 chars wide
    flake8_complexity_cmd = "flake8 . --count --exit-zero --max-complexity={} --max-line-length={}".format(
        MAX_COMPLEXITY, LINE_LENGTH
    )
    flake8_complexity_cmd += " --statistics --extend-exclude=.venv"
    c.run(flake8_complexity_cmd)


@task
def lint_with_bandit(c):
    c.run("bandit -r src/ --exclude .venv")


@task
def lint_with_mypy(c):
    c.run("mypy")


@task
def run_tests(c):
    pytest_cmd = "pytest --cov=src --junitxml=reports/xunit.xml --cov src/"
    pytest_cmd = pytest_cmd + " --cov-report term --cov-report html:reports/html --cov-report xml:reports/coverage.xml"
    c.run(pytest_cmd)


@task
def clean(c):
    folders = [".venv", ".pytest_cache", ".mypy_cache", "dist", "reports", "coverage"]
    for folder in folders:
        shutil.rmtree(folder, ignore_errors=True)
