# Python Challenges

A collection of Python coding challenges, tests, exercises, and practice problems.

Each challenge is contained within its own directory.

## Regression tests

From the repository root, run the dependency-free standard-library suite:

```sh
python3 -m unittest discover -s tests -v
```

The current suite covers the prime-gap exercise: first matching pair, inclusive
interval bounds, ranges without pairs, consecutive-prime semantics, perfect
squares, and importing the solution without running its demonstration prints.
It does not yet cover all exercises in this repository.

Run the original demonstration directly:

```sh
python3 Intermediate/Algorithms/GapInPrimes/gap.py
```
