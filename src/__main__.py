from . import filestream
from . import MEDIA
import argparse  # sys https://www.pythonforbeginners.com/system/python-sys-argv
from . import dbhandler

db = dbhandler.DbHandler()


parser = argparse.ArgumentParser(description='Breach data cleanner')
parser.add_argument('-s', '--size', type=int, help='Please insert the size of the file that you want to read')
args = parser.parse_args()

files = filestream.get_files(MEDIA)

db.setup()

for fp in files:
    text = filestream.get_data(fp, args.size)
    results = filestream.get_frequencies(text)
    for email in results:
        db.add_item(email)
    db.store_items()
    