"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.latex.logic import validators


def test_latex_reauired_with_valid_value():
    assert validators.latex_required("value") == "value"


def test_latex_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.latex_required(None)
