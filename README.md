# Decision System

A configurable rule-based decision engine built in Python.

## Project Structure

decision-system
│
├── app
│   ├── engine
│   │   └── rule_engine.py
│   ├── config
│   │   └── rules.json
│   └── models
│       └── request_model.py
│
├── tests
│   └── test_rules.py
│
└── requirements.txt

## Features

- Configurable rules using JSON
- Rule evaluation engine
- Input validation using Pydantic
- Unit testing using Pytest

## Installation

pip install -r requirements.txt

## Run Tests

python -m pytest

## Example

Input:
income = 60000  
credit_score = 750  

Output:
Approved