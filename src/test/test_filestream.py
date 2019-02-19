from pathlib import Path

from .. import filestream as fs

res = Path('res')
testfile = res / 'testdoc.txt'


def test_get_data():
    """Asserts the data read is expected size."""
    with testfile.open() as fp:
        data = fp.read(10)

    assert data == fs.get_data(testfile, 10)


def test_get_files():
    """Asserts all files are accounted for."""
    files = list(res.iterdir())
    assert files == fs.get_files(res)


def test_get_frequencies():
    """Asserts frequency data is formatted correctly."""
    pass
