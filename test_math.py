import pytest

def add(a, b):
    return a + b

###Test-Case-01
@pytest.mark.parametrize(
    "a,b,expected",
    [
        #integer numbers
        pytest.param(2, 3, 5, id="positive_integers"),
        pytest.param(-1, 1, 0, id="negative_and_positive_integers"),
        pytest.param(0, 0, 0, id="zero_integers"),
        pytest.param(-1, -1, -2, id="negative_integers"),
    ],
)
def test_add_integers(a, b, expected):    
    assert add(a, b) == expected
    print(f"Assertion OK ✅: a: {a}, b: {b}, Expected Result: {expected}, Actual Result: {add(a, b)}")


###Test-Case-02
@pytest.mark.parametrize(
    "a,b,expected",
    [
        #floats numbers
        pytest.param(1.5, 2.5, 4.0, id="positive_floats"),
        pytest.param(-0.5, 0.5, 0.0, id="negative_and_positive_floats"),
        pytest.param(0.5, 0.5, 1.0, id="zero_floats"),
        pytest.param(0.1, 0.1, 0.2, id="negative_floats"),
    ],
)
def test_add_floats(a, b, expected):
    assert add(a, b) == pytest.approx(expected)
    print(f"Assertion OK ✅: a: {a}, b: {b}, Expected Result: {expected}, Actual Result: {add(a, b)}")