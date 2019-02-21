from . import filestream
from . import MEDIA

files = filestream.get_files(MEDIA)
for fp in files:
    filestream.get_data(fp)
