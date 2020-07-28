import pytest

from demo import Demo

demo = Demo()

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

#python will look at the registries of fixtures and then try to pass it
def test_fixture(my_fixture):
    assert my_fixture == 69

#Capsys capture the system log
def test_capsys(capsys):
    print("hello")
    #print("world") <- capsys still captures it! How cool
    out, err = capsys.readouterr()
    assert out == "hello\n"

#Python is so dynamic, you can change anything about it at runtime, you can even change the function running
def test_monkeypatch(monkeypatch):
    #I don't wanna run an expensive computation, I just want a fast test to test an interaction b/n two functions
    #I want to dynamically swap stuff.
    def fake_add(a,b):
        return 69
    monkeypatch.setattr(demo, "add", fake_add)
    assert demo.add(2,3) == 69

#tmpdir is a temporary directory in a secure way
def test_tmpdir(tmpdir):
    some_file = tmpdir.join('something.txt')
    some_file.write('{"Hello": "world"}')
    result = demo.read_json(str(some_file))

    assert result["Hello"] == "world"

def test_fixture_with_fixtures(capsys, captured_print):
    print("more")
    out, err = capsys.readouterr()
    assert out == "hello\nmore\n"