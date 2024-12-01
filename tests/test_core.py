from copyq_lib import compute


def test_compute():
    assert compute(["a", "bc", "abc"]) == "abc"
