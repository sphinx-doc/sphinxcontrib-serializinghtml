"""Test for serializinghtml extension."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from sphinx.application import Sphinx


@pytest.mark.sphinx('json', testroot='basic')
def test_json(app: Sphinx) -> None:
    app.builder.build_all()


@pytest.mark.sphinx('pickle', testroot='basic')
def test_pickle(app: Sphinx) -> None:
    app.builder.build_all()
