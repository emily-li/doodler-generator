# doodler-generator

https://emily-li.github.io/doodler/

UI repo https://github.com/emily-li/doodler

# Try it out

```
curl -X POST https://emilyli.pythonanywhere.com/api/v1/idea -H "Content-Type: application/json" -d '{}'
```

# Dependencies

## Required

Python 3.10

## Optional

[Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

# Build

## Install with local LLM

`pip install -e ".[local]"`

The remote service uses Arli AI API for generation. Please see documentation at https://www.arliai.com/docs

For remote LLM, you will need to insert your API key for AIML in the `.env` file

```
API_KEY=api_key_here
SERVER_MODE=REMOTE
```

# Install with development dependencies

`pip install -e ".[dev]"`

## Run tests

`python -m pytest -v tests`

## Run server

`python src/run.py`

# API

| Status code | Result                  |
| ----------- | ----------------------- |
| 200         | JSON response with idea |
| 500         | Server runtime error    |
| 503         | Idea generation failure |

## Request schema

```
model_name: str
temperature: float
top_p: float
repetition_penalty: float
```

## Example Request

```
curl    -X POST localhost:5000/api/v1/idea \
        -H "Content-Type: application/json"   \
        -d '{}' \
--write-out "\nLatency: %{time_total}"
```

## Example Response

`{"idea":Two animals on an adventure - A bear scaling trees to reach high up"}
Latency: 5.937801`
