from pathlib import Path
from typing import List, Mapping

root = Path(r'C:\Users\daniele.perera\Desktop\progetti vari\clean_breach\res\media\various_collection')

def get_data(fp: Path, size: int) -> str:
    """
    Return the data up to `size` in file.

    param
        fp: Path -- Location of file.
        size: int -- The number of bytes to get.

    return
        str -- The file data up to size.
    """
    pass


def get_files(filedir):
    """
    Return a list of files found in `filedir`.

    param
        filedir: Path -- The directory to look in.

    return
        List[Path] -- A list of files found in `filedir`
    """
    listpath=[]
    for collection in filedir.iterdir():
        for subdir in collection.iterdir():
            for files in subdir.iterdir():
                listpath.append(files)
    return listpath            
    pass


def get_frequencies(text: str) -> Mapping[str, int]:
    """
    Return a dictionary of the `domain: count` found in text.

    param
        text: str -- The text data to look in.

    return
        Mapping[str, int] -- A dictionary of frequencies
            key - domain
            value - count
    """
    pass


test = get_files(root)
print(test)