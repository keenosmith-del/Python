"""Regression tests for the documented consecutive-prime gap contract."""

import contextlib
import io
from pathlib import Path
import subprocess
import sys
import unittest

with contextlib.redirect_stdout(io.StringIO()):
    from Intermediate.Algorithms.GapInPrimes.gap import gap


class PrimeGapTests(unittest.TestCase):
    def test_returns_first_matching_pair(self):
        self.assertEqual(gap(2, 3, 50), [3, 5])
        self.assertEqual(gap(4, 130, 200), [163, 167])

    def test_both_interval_endpoints_are_inclusive(self):
        self.assertEqual(gap(2, 5, 7), [5, 7])

    def test_single_point_and_composite_only_ranges_have_no_pair(self):
        self.assertIsNone(gap(2, 5, 5))
        self.assertIsNone(gap(2, 14, 16))

    def test_intervening_primes_disqualify_equal_distance_pairs(self):
        # 101 and 107 are six apart, but 103 lies between them.
        self.assertIsNone(gap(6, 100, 110))

    def test_perfect_square_is_not_mistaken_for_intervening_prime(self):
        self.assertIsNone(gap(2, 47, 53))
        self.assertEqual(gap(6, 47, 53), [47, 53])

    def test_import_has_no_example_output(self):
        result = subprocess.run(
            [sys.executable, "-c", "import Intermediate.Algorithms.GapInPrimes.gap"],
            cwd=Path(__file__).resolve().parents[1],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
