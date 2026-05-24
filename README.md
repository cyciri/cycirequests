# cycirequests

**cycirequests** is a Python library for making simple web requests and pretty-printing results, starting with extracting and printing all `<h1>` tags from a given webpage.

## Installation

```bash
pip install cycirequests
```

## Usage

Here's a simple example:

```python
from cycirequests import h1_printer

url = "https://cyciri.github.io/cyciri/"
h1_printer(url)
```

This will fetch the webpage and print out all `<h1>` headers found.

## Features

- Fetch a webpage and print its `<h1>` tags to the console.