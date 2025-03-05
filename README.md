# doodler-generator

https://emily-li.github.io/doodler/

UI repo https://github.com/emily-li/doodler

# Dependencies

## Required

Python 3.10

### Required dependencies
`pip install -r requirements.txt`

### Dev dependencies
`pip install -r requirements-dev.txt`


## Optional

[Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

# Build

## Run tests
`python -m pytest tests`

## Run server
`python src/run.py`

# API

## Request schema
```
model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v0.6"
max_new_tokens: int = 20
do_sample: bool = True
temperature: float = 0.7
top_p: float = 0.9
repetition_penalty: float = 1.2
```

## Example Request
curl    -X POST localhost:5000/api/v1/idea \
        -H "Content-Type: application/json"   \
        -d '{ "model_name": "TinyLlama/TinyLlama-1.1B-Chat-v0.6" }' \
--write-out "\nLatency: %{time_total}"

## Example Response
`{"idea":Two animals on an adventure - A bear scaling trees to reach high up"}
Latency: 5.937801`
