import subprocess


def test_main():
    assert subprocess.check_output(["copyq-lib", "foo", "foobar"], text=True) == "foobar\n"
