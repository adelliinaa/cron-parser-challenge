# Deliveroo Cron Parser

## Overview

This tool is designed to parse and validate cron expressions. 
The project includes validation logic to ensure the cron fields are within acceptable ranges and provides detailed
error messages when values are out of range.

### Project Structure

The project is organised into the following files:

- `cli.py`: The command-line interface for parsing cron expressions.
- `cron_parser.py`: Main script handling the parsing logic.
- `models.py`: Contains the `CronExpression` model with validation logic.
- `utils.py`: Utility functions used across the project.
- `validators.py`: Validation functions for the cron fields.

### Validation Rules

The cron fields must adhere to the following ranges:

- `minute`: 0-59
- `hour`: 0-23
- `day_of_month`: 1-31
- `month`: 1-12
- `day_of_week`: 0-6


## Requirements

- Python 3.9 or higher
- `pip` package manager

## Setup Instructions

### Step 1: Clone the Repository

Clone the repo to your local machine using the following command:

```sh
git clone https://github.com/adelliinaa/cron-parser-challenge.git
cd cron-parser-challenge
```

### Step 2: Set Up a Virtual Environment

Now set up a virtual environment to manage dependencies:

```sh
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
Install the required dependencies using pip:

```sh
pip install -r requirements.txt
```

### Step 4: Run with CLI
To use the parser in your CLI, navigate to `cron_parser/src` and run
the following command:

```sh
python cli.py "*/15 0 1,15 * 1-5 /usr/bin/find"

```

Replace the cron string with your desired expression.

### Running Tests

To run the tests and ensure everything is working correctly, you can use pytest:

```sh
pytest
```
