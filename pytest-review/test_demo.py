""" Some pytest practice code

    use -k for regex type test selection based on test name

    use @pytest.mark for grouping based on smoke, regression, etc """

import pytest


@pytest.mark.smoke
def test_quicktest():
    print('Hello from pytest')

@pytest.mark.burnin
def test_anotherquicktest():
    print('Hello again from pytest')
