"""
    test_serializinghtml
    ~~~~~~~~~~~~~~~~~~~~

    Test for serializinghtml extension.

    :copyright: Copyright 2007-2019 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import pytest


@pytest.mark.sphinx('json', testroot='basic')
def test_json(app, status, warning):
    app.builder.build_all()


@pytest.mark.sphinx('pickle', testroot='basic')
def test_pickle(app, status, warning):
    app.builder.build_all()
