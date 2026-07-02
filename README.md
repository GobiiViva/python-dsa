# Python DSA

![Python](https://img.shields.io/badge/Python-3-blue) ![Tests](https://img.shields.io/badge/Tests-20%20Passing-success) ![Pytest](https://img.shields.io/badge/Tested%20With-pytest-green)

A collection of Python examples demonstrating common language features, data structures, algorithms, and problem-solving techniques.

This repository was created as part of a Python review exercise to strengthen my understanding of Python fundamentals while preparing for technical interviews. The examples focus on writing clean, readable, and well-tested code using common backend-oriented scenarios.

---

## Project Structure

```
python-dsa/
├── src/
│   ├── collections_examples.py
│   ├── comprehensions_examples.py
│   ├── hashing_examples.py
│   └── heap_examples.py
│
├── tests/
│   ├── test_collections_examples.py
│   ├── test_comprehensions_examples.py
│   ├── test_hashing_examples.py
│   └── test_heap_examples.py
│
├── requirements.txt
└── README.md
```

---

## Topics Covered

Current examples include:

- Hash tables and dictionaries
- Sets
- List and dictionary comprehensions
- `Counter`
- `defaultdict`
- `deque`
- Priority queues (`heapq`)
- Type hints
- Unit testing with `pytest`

The examples intentionally use simple backend-inspired scenarios such as login events, alerts, IP addresses, and user activity to demonstrate practical applications of these language features.

---

## Getting Started

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the test suite:

```bash
python -m pytest -v
```

---

## Future Improvements

Potential additions include:

- Sliding Window
- Binary Search
- Graph Traversal (DFS/BFS)
- Trees
- Dynamic Programming
- Sorting Algorithms
- String Algorithms
- Additional LeetCode-style problems

---

## Development Notes

This repository was created as a personal learning project.

I used ChatGPT as a learning companion to discuss Python concepts, compare implementation approaches, and help draft portions of the accompanying unit tests and documentation. All source code, tests, and documentation were reviewed, validated, and, where necessary, modified before being committed.

---

## License

This repository is provided for educational purposes.
