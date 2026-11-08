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

GitHub Actions runs this same suite on Python 3.12 and 3.15 for pull requests
and pushes to `main`. No third-party packages, credentials or external services
are needed. The workflow tests the existing exercises; it does not deploy or
publish anything.

Run the original demonstration directly:

```sh
python3 Intermediate/Algorithms/GapInPrimes/gap.py
```
