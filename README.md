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

## Local mode

The server can be run in LOCAL (default) or REMOTE mode. LOCAL mode will allow you to test multiple LLM with the huggingface pipeline API but will download more dependencies and LLM locally taking up disk space. REMOTE mode avoids this by calling a remote API but with model choice limitations.

`pip install -e ".[local]"`

## Remote mode

For REMOTE mode, you will need to insert your API key in the `.env` file

```
API=aimlapi
API_KEY=api_key_here
SERVER_MODE=REMOTE
```

`pip install -e .`

## Install with development dependencies

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
