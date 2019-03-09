from . import filestream
from . import MEDIA
import argparse  # sys https://www.pythonforbeginners.com/system/python-sys-argv
from . import dbhandler

'''
test1 Measure-Command { pipenv run start -s 102400000000 } - OverflowError: cannot fit 'int' into an index-sized integer
test2 Measure-Command { pipenv run start -s 1024000000 } -     data = content.read(size_to_read) MemoryError
test2 Measure-Command { pipenv run start -s 102400000 } - max thinkpad usa 250 MB di memoria 50 MB/s 25% del cpu - il risultato è maggiore

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

'''



db = dbhandler.DbHandler()


parser = argparse.ArgumentParser(description='Breach data cleanner')
parser.add_argument('-s', '--size', type=int, help='Please insert the size of the file that you want to read')
args = parser.parse_args()

files = filestream.get_files(MEDIA)

db.setup()


for fp in files:
    text = filestream.get_data(fp, args.size)
    results = filestream.get_frequencies(text)
    db.add_items(results)


