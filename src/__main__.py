from . import filestream
from . import MEDIA
import argparse  # sys https://www.pythonforbeginners.com/system/python-sys-argv
from . import dbhandler
from tqdm import tqdm
from tqdm._utils import _term_move_up
from termcolor import colored
import os

'''
test1 Measure-Command { pipenv run start -s 102400000000 } - OverflowError: cannot fit 'int' into an index-sized integer
test2 Measure-Command { pipenv run start -s 1024000000 } -     data = content.read(size_to_read) MemoryError
test2 pc scuola thinkpad Measure-Command { pipenv run start -s 200000000 } - max thinkpad usa 250 MB di memoria 50 MB/s 25% del cpu - il risultato è maggiore

Days              : 0
Hours             : 0
Minutes           : 23
Seconds           : 33
Milliseconds      : 816
Ticks             : 14138168555
TotalDays         : 0,0163636210127315
TotalHours        : 0,392726904305556
TotalMinutes      : 23,5636142583333
TotalSeconds      : 1413,8168555
TotalMilliseconds : 1413816,8555

test 3 work pc Measure-Command { pipenv run start -s 1024000 } database size = 1.749.136 KB
Days              : 0
Hours             : 6
Minutes           : 28
Seconds           : 54
Milliseconds      : 462
Ticks             : 233344624091
TotalDays         : 0,27007479640162
TotalHours        : 6,48179511363889
TotalMinutes      : 388,907706818333
TotalSeconds      : 23334,4624091
TotalMilliseconds : 23334462,4091



Measure-Command { pipenv run start -s 200000000 }
UnicodeEncodeError: 'charmap' codec can't encode characters in position 5-8: character maps to <undefined>



Days              : 0
Hours             : 0
Minutes           : 12
Seconds           : 26
Milliseconds      : 948
Ticks             : 7469483538
TotalDays         : 0,00864523557638889
TotalHours        : 0,207485653833333
TotalMinutes      : 12,44913923
TotalSeconds      : 746,9483538
TotalMilliseconds : 746948,3538
'''


db = dbhandler.DbHandler()


parser = argparse.ArgumentParser(description='data cleanner')
parser.add_argument('-s', '--size', type=int, help='Please insert the size of the file that you want to read')
args = parser.parse_args()

files = filestream.get_files(MEDIA)
# print(type(files))
db.setup()

# start going into files
firstprogressbar = tqdm(list(files), ascii=True, unit="files")
border = "="*100
clear_border = _term_move_up() + "\r" + " "*len(border) + "\r"
excl = colored("[!] ", "yellow")

for fp in firstprogressbar:
    text = filestream.get_data(fp, args.size)
    results = filestream.get_email(text)
    secondprogressbar = tqdm(list(results), ascii=False, unit="lines")
    # start parsing data and saving to db
    for email in secondprogressbar:
        db.add_item(email)
        _term_move_up()
        secondprogressbar.update()
    db.store_items()
    
    firstprogressbar.write(clear_border + excl+"%s saved to database" % str(os.path.basename(fp)))
    firstprogressbar.write(border)
    firstprogressbar.update()
