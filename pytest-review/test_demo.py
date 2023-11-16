""" Some pytest practice code

    use -k for regex type test selection based on test name

    use @pytest.mark for grouping based on smoke, regression, etc """

import pytest

@pytest.fixture()  # typically put this in conftest.py file
def resource():
    print("setup")
    yield "resource"
    print("teardown")


@pytest.mark.smoke
def test_quicktest(resource):
    print('Hello from pytest')

@pytest.mark.burnin
def test_anotherquicktest():
    print('Hello again from pytest')
