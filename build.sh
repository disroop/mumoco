#!/usr/bin/env bash

invoke --list

invoke clean
invoke configure-poetry
invoke check-format-with-black
invoke sort-imports-with-isort
invoke install-dependencies
invoke install-libraries
invoke lint-with-pylint
invoke lint-with-flake8
invoke lint-with-bandit
#invoke # todo add mypy
invoke run-tests
# todo add Fix Code Coverage Paths and sonar scann
poetry build
poetry publish --username '123' --password '123' --dry_run
