"""Tests for helpers.py."""

import ckanext.latex.helpers as helpers


def test_latex_hello():
    assert helpers.latex_hello() == "Hello, latex!"
