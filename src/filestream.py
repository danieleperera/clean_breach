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
    with open(str(fp), mode="r", encoding='utf8', errors='replace') as content:
        data = content.read(size_to_read)
        while data:
            yield data
            data = content.read(size_to_read)


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
        #print(collection)
        if not collection.is_dir():
            continue  # For safety
        for subdir in collection.iterdir():
            if not collection.is_dir():
                continue  # For safety
            #print(subdir)
            for files in subdir.iterdir():
                #print(files)
                if not collection.is_dir():
                    continue  # For safety
                
                for subfiles in files.iterdir():
                    if subfiles.suffix == '.txt':
                        #print(subfiles)
                        listpath.append(subfiles)
                    if not collection.is_dir():
                        continue  # For safety
                    
    return listpath  # the list has this format [WindowsPath('C:/../../.txt'), WindowsPath(...)]
    pass
def get_frequencies(data):
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
    string = ''.join(data)
    match_pattern = re.findall(r'[-\+\.\w]+@[\w\.-]+\.\w+', string) #[-\+\.\w]+@[\w\.-]+\.\w+ for entire email ::: only domain @[\w\.-]+
    for domain in match_pattern:
        count = frequency.get(domain, 0)
        frequency[domain] = count + 1
    
    return frequency
    pass
