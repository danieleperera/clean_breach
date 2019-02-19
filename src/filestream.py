import os
from pathlib import Path
from typing import List, Mapping

root = Path(r'C:\Users\daniele.perera\Desktop\progetti vari\clean_breach\res\media\various_collection')

def get_data(fp,size):
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
                if files.suffix == '.txt':
                    listpath.append(files)
    return listpath  # the list has this format [WindowsPath('C:/../../.txt'), WindowsPath(...)]
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


# It starts to get messy to put your "working" logic at the bottom of your file
# Lets do this in the __main__.py file, so everything is in one place

# TODO Move this to the __main__.py file
