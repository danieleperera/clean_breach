import csv
from . import filestream
from . import MEDIA
import argparse #sys https://www.pythonforbeginners.com/system/python-sys-argv
'''
first open tesssst.csv from visual code 
run Measure-Command { pipenv run start -s 1024 } to see time too
see the magic
'''
def save(frequency):
    csvfile = (r'C:\Users\daniele.perera.CYBAZE\Desktop\progetti vari\clean_breach\res\media\various_collection\collection_1\collection1_sub1\tesssst.csv')
    with open(csvfile, 'a', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in frequency.items():
            writer.writerow([key, value])



parser = argparse.ArgumentParser(description='Breach data cleanner')
parser.add_argument('-s','--size', type=int, help='Please insert the size of the file that you want to read')
args = parser.parse_args()

files = filestream.get_files(MEDIA)



for fp in files:
    text = filestream.get_data(fp,args.size)
    result = filestream.get_frequencies(text)
    save(result)
