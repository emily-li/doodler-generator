# doodler-generator

https://emily-li.github.io/doodler/

UI repo https://github.com/emily-li/doodler

# Dependencies

## Required

Python 3.10

## Optional

[Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

# Build

## Install required dependencies
`pip install -r requirements.txt`

## Install dev dependencies
`pip install -r requirements-dev.txt`

## Run tests
`python -m pytest tests`

## Run server
`python src/run.py`

# API

## Request
curl -X POST localhost:5000/api/v1/idea --write-out "Latency: %{time_total}"

## Response
`{"idea":Two animals on an adventure - A bear scaling trees to reach high up"}
Latency: 5.937801`
