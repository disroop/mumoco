#!/usr/bin/env python

"""
The build.py is the single point containing the build logic. Thus this script can be used to build locally or
methods from the file can be used in the github actions.
The github actions shall just call methods from this file so we are not locked in the the build server solution.
"""
import shutil

from invoke import task

LINE_LENGTH = 120
MAX_COMPLEXITY = 10


@task
def check_format_with_black(c, fix=False):
    format_cmd = "black -l {} .".format(LINE_LENGTH)
    check_cmd = format_cmd + " --check"
    if fix:
        c.run(format_cmd)
    c.run(check_cmd)


@task
def sort_imports_with_isort(c, fix=False):
    isort_fix_cmd = "isort --profile black ."
    isort_check_cmd = isort_fix_cmd + " --check"
    if fix:
        c.run(isort_fix_cmd)
    c.run(isort_check_cmd)


@task
def lint_with_pylint(c):
    enabled_warnings = ["W0611", "W0614"]
    disabled_warnings = ["C0114", "C0115", "C0116", "W0511"]
    pylint_cmd = "pylint ./src --enable={} -disable={} --max-line-length={}".format(
        ",".join(enabled_warnings), ",".join(disabled_warnings), LINE_LENGTH
    )
    c.run(pylint_cmd)


@task
def lint_with_flake8(c):
    errors = ["E9", "F63", "F7", "F82"]
    # stop the build if there are Python syntax errors or undefined names
    flake8_syntax_cmd = "flake8 . --count --select={}".format(",".join(errors))
    flake8_syntax_cmd = flake8_syntax_cmd + "--show-source --statistics --extend-exclude=.venv"
    c.run(flake8_syntax_cmd)

    # exit-zero treats all errors as warnings. The GitHub editor is 120 chars wide
    flake8_complexity_cmd = "flake8 . --count --exit-zero --max-complexity={} --max-line-length={}".format(
        MAX_COMPLEXITY, LINE_LENGTH
    )
    flake8_complexity_cmd = flake8_complexity_cmd + " --statistics --extend-exclude=.venv"
    c.run(flake8_complexity_cmd)


@task
def lint_with_bandit(c):
    c.run("bandit -r src/ --exclude .venv")


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
