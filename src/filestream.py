from pathlib import Path
from typing import List, Mapping
import re

def get_data(fp,size):
    """
    Return the data up to `size` in file.

    param
        fp: Path -- Location of file.
        size: int -- The number of bytes to get.

    return
        str -- The file data up to size.
    """
    size_to_read = size
    with io.open(str(fp), mode="r", encoding='utf8', errors='replace') as content:
        f_content = content.read(size_to_read)

        while len(f_content) > 0:
            string = (f_content, end='')
            return string
            f_content = content.read(size_to_read)



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


def get_frequencies(text):
    """
    Return a dictionary of the `domain: count` found in text.

    param
        text: str -- The text data to look in.

    return
        Mapping[str, int] -- A dictionary of frequencies
            key - domain
            value - count
    """
    frequency = {}
    match_pattern = re.findall(r'@[\w\.-]+', text())
                for domain in match_pattern:
                    count = frequency.get(domain, 0)
                    frequency[domain] = count + 1
    return frequency
    pass
