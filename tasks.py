#!/usr/bin/env python

"""
The build.py is the single point containing the build logic. Thus this script can be used to build locally or
methods from the file can be used in the github actions.
The github actions shall just call methods from this file so we are not locked in the the build server solution.
"""
import contextlib
import os
import shutil

from invoke import task


@task
def check_format_with_black(c, fix=False):
    format_cmd = "black ."
    check_cmd = format_cmd + " --check"
    if fix:
        c.run(format_cmd)
    c.run(check_cmd)


@task
def sort_imports_with_isort(c, fix=False):
    if fix:
        c.run("isort .")
    c.run("isort --check .")


@task
def lint_with_pylint(c):
    c.run("pylint ./src")


@task
def lint_with_flake8(c):
    c.run("flake8 .")


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
    files = [".coverage"]
    for file in files:
        with contextlib.suppress(FileNotFoundError):  # -> like ignore_errors=True
            os.remove(file)
