#!/usr/bin/env bash

invoke --list

#invoke clean
#invoke configure_poetry
invoke check-format-with-black
invoke sort-imports-with-isort
invoke install-dependencies
invoke install-libraries
invoke lint-with-flake8
invoke lint-with-bandit
#invoke # todo add mypy
invoke run-tests
# todo add Fix Code Coverage Paths and sonar scann
invoke build
invoke publish  --pypiusername='123'  --pypipassword='123' --dry_run