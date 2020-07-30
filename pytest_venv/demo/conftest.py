import pytest

@pytest.fixture
def my_fixture():
    #Here realistically we can put in a database connection or something.
    return 69
#You can have a hierarchy here

@pytest.fixture
def captured_print(capsys):
    print("hello there")