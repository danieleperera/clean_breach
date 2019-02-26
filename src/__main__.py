from . import filestream
from . import MEDIA
import argparse

parser = argparse.ArgumentParser(description='Breach data cleanner')
parser.add_argument('-s','--size', type=int, help='Please insert the size of the file that you want to read')
args = parser.parse_args()

files = filestream.get_files(MEDIA)


for fp in files:
    text = filestream.get_data(fp,args.size)
    result = filestream.get_frequencies(text)

print(result)




