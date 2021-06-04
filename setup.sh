#! /usr/bin/bash
echo "install poetry if not in path"
if ! command -v poetry &> /dev/null
then
    echo "poetry is missing. Installing ..."
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
fi

echo "setting up poetry config"
poetry config virtualenvs.path .venv
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true

echo "installing dependencies"
poetry install --no-interaction --no-root

echo "installing libraries"
poetry install --no-interaction

echo "setup tab completion for invoke"
#see http://docs.pyinvoke.org/en/stable/invoke.html#shell-tab-completion
poetry run invoke --print-completion-script zsh > .invoke-completion.sh
#then run this in you console to activate the tab completion
#source .invoke-completion.sh