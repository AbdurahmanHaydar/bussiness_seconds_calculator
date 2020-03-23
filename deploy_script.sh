#!/bin/bash

echo "Pushing to heroku..."
heroku login
heroku create
git push heroku master
