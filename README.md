# doodler-generator

https://emily-li.github.io/doodler/

UI repo https://github.com/emily-li/doodler

# Dependencies

## Required

Python 3.13

`pip install -r requirements.txt`

## Optional

[Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

# Build

## Run tests
`python -m pytest tests`

## Run server
`python src/app.py`

# API

## Request
`curl -X POST localhost:5000/api/v1/idea`

## Response
`{"idea":"a fish with a dish"}`
