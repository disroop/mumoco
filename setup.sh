#! /usr/bin/bash
echo "setting up poetry config"
poetry config virtualenvs.path .venv
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true

echo "installing dependencies"
poetry install --no-interaction --no-root

echo "installing libraries"
poetry install --no-interaction

# tab completion for invoke
#see http://docs.pyinvoke.org/en/stable/invoke.html#shell-tab-completion
inv --print-completion-script zsh > .invoke-completion.sh
source .invoke-completion.sh