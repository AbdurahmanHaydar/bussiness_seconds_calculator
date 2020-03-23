#!/bin/bash
# 
# echo "creating virtualenv and installing packages..."
# echo "=========================================================================="
#
# virtualenv --no-site-packages --distribute .env && source .env/bin/activate && pip install -r requirements.txt
#
# echo "done installing packages.."
# echo "=========================================================================="
# echo "running tests"
#
# pytest
# echo "done running tests"
#
# echo "=========================================================================="
# echo "starting server.."

python deploy.py
