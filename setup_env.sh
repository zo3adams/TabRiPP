#!/bin/bash
# setup_env.sh: Create a Python venv, install requirements, run downloader.py, and clean up.
set -e

ENV_NAME=".venv-tabRiPP"

# create virtual environment
python3 -m venv "$ENV_NAME"
source "$ENV_NAME/bin/activate"

# install dependencies
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

echo "Running..."
python3 downloader.py

echo "Cleaning up the environment..."
deactivate
rm -rf "$ENV_NAME"
echo "tabRiPP environment removed."
