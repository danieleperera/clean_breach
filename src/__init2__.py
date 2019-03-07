from pathlib import Path
import os
# __file__ points to this file no matter where you run it from
# Using this, we can build our paths safely.
SRC = Path(__file__).parent
ROOT = SRC.parent
RES = ROOT / 'res'
MEDIA = RES / 'media'

#print(MEDIA)
"""
finisce qui
"""
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

files = get_files(MEDIA)
print(files)