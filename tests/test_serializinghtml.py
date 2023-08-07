"""Test for serializinghtml extension."""

import pytest


@pytest.mark.sphinx('json', testroot='basic')
def test_json(app, status, warning):
    app.builder.build_all()


@pytest.mark.sphinx('pickle', testroot='basic')
def test_pickle(app, status, warning):
    app.builder.build_all()
