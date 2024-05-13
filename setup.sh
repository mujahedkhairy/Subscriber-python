#!/bin/bash

# Check for Python installation
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3."
    exit 1
fi

# Check for pip installation
if ! command -v pip3 &> /dev/null
then
    echo "pip3 is not installed. Please install pip3."
    exit 1
fi

# Create a virtual environment named 'env' in the current directory
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install requirements from requirements.txt
pip3 install -r requirements.txt

python3 real_time.py

echo "Setup complete. the terminal is now waiting for changes form the supabase database"
