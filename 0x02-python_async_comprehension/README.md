# Python Async Comprehension

## Overview
This project covers the basics of asynchronous comprehensions in Python. You will learn how to use `async` and `await` keywords to write asynchronous code and how to use asynchronous comprehensions to handle asynchronous iterators.

## Learning Objectives
- Understand the concept of asynchronous programming in Python.
- Learn how to use `async` and `await` keywords.
- Implement asynchronous comprehensions.
- Handle asynchronous iterators.

## Requirements
- Python 3.7 or higher
- Basic knowledge of Python programming

## Project Structure
- `0-async_generator.py`: Contains a coroutine called `async_generator` that loops 10 times, each time asynchronously waits 1 second, then yields a random number between 0 and 10.
- `1-async_comprehension.py`: Contains a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehensing over `async_generator`, then returns the 10 random numbers.
- `2-measure_runtime.py`: Contains a function called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather` and measures the total runtime.

## Usage
To run the scripts, use the following commands:
```bash
python3 0-async_generator.py
python3 1-async_comprehension.py
python3 2-measure_runtime.py
```

## Author
Joe404
