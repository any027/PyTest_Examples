import pytest

def test_basic():
    assert 'hello' in 'hello world'
    assert 2 != 1
    assert "same" != "no"

@pytest.mark.parametrize (
    'a, b, expected', [
        (1, 1, 2),
        (2, 1, 3)
    ]
)
def test_with_param(a, b, expected):
    assert a + b == expected