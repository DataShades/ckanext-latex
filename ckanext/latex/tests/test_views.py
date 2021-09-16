"""Tests for views.py."""

import pytest

import ckanext.latex.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "latex")
@pytest.mark.usefixtures("with_plugins")
def test_latex_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("latex.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, latex!"
