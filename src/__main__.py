from . import filestream
from . import MEDIA
import argparse  # sys https://www.pythonforbeginners.com/system/python-sys-argv
from . import dbhandler
import os
from tqdm import tqdm

db = dbhandler.DbHandler()


parser = argparse.ArgumentParser(description='data cleanner')
parser.add_argument('-s', '--size', type=int, help='Please insert the size of the file that you want to read')
args = parser.parse_args()

files = filestream.get_files(MEDIA)

db.setup()

from . import filestream
from . import MEDIA
import argparse  # sys https://www.pythonforbeginners.com/system/python-sys-argv
from . import dbhandler
import os
from tqdm import tqdm

db = dbhandler.DbHandler()


parser = argparse.ArgumentParser(description='data cleanner')
parser.add_argument('-s', '--size', type=int, help='Please insert the size of the file that you want to read')
args = parser.parse_args()

files = filestream.get_files(MEDIA)
print(type(files))
db.setup()

for fp in tqdm(list(files), ascii=True):
    text = filestream.get_data(fp, args.size)
    results = filestream.get_email(text)
    for email in tqdm(list(results), ascii=True):
        db.add_item(email)
    db.store_items()
    os.unlink(fp)  # to delete the files after reading them
    #print("Deleting: {}".format(fp))
