from pathlib import Path
from .. import filestream as fs

res = Path('res')
testfile = res / 'testdoc.txt'


def test_get_data():
    with testfile.open() as fp:
        data = fp.read(10)

    assert data == fs.get_data(testfile, 10)


def test_get_files():
    files = list(res.iterdir())
    assert files == fs.get_files(res)
