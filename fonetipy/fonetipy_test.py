# -*- coding: utf-8 -*-
"""A simple test for fonetipy module."""

import unittest
from functools import wraps
from fonetipy import fonetipy


def verbose_decorator(func):
    """Add a automatic verbose, when running via python module_name.py."""
    @wraps(func)
    def print_doc(*args, **kwargs):
        print func.__doc__
        return func(*args, **kwargs)

    return print_doc


class FonetiPyTest(unittest.TestCase):
    """Start a simple test case."""

    def assert_phonetic(self, *args):
        """Assert shortcut."""
        args = [fonetipy(w) for w in args]
        self.assertEqual(*args)

    @verbose_decorator
    def test_casa_kasa(self):
        """Phonect test for `casa` and `kasa`."""
        self.assert_phonetic('casa', 'kasa')

    @verbose_decorator
    def test_pollyana_poliana(self):
        """Phonect test for `pollyana` and `poliana`."""
        self.assert_phonetic("pollyana", "poliana")

    @verbose_decorator
    def test_wallysson_uallison(self):
        """Phonect test for `Wallysson` and `Uallison`."""
        self.assert_phonetic("Wallysson", "Uallison")

    @verbose_decorator
    def test_orgaozinho(self):
        u"""Phonect test for `órgãozinho` and `órgaozinho`."""
        self.assert_phonetic("órgãozinho", "órgaozinho")

    @verbose_decorator
    def test_chuchu_xuxu(self):
        u"""Phonect test for `xuxu` and `Chuchu`."""
        self.assert_phonetic("xuxu", "Chuchu")

    @verbose_decorator
    def test_wilson_and_uilson(self):
        """Phonect test for `Wilson` and `uilson`."""
        self.assert_phonetic("Wilson", "uilson")

    @verbose_decorator
    def test_passoca_and_pacoca(self):
        u"""Phonect test for `passoca` and `paçoca`."""
        self.assert_phonetic("passoca", "paçoca")


if __name__ == "__main__":
    unittest.main()
