import re


def get_data(fp, size):

    size_to_read = size
    with open(str(fp), mode="r", encoding='utf8', errors='replace') as content:
        data = content.read(size_to_read)
        while data:
            yield data
            data = content.read(size_to_read)


def get_files(filedir):
    return filedir.rglob('*.txt')
    pass


def get_email(data):
    string = ''.join(data)
    match_pattern = re.findall(r'[-\+\.\w]+@[\w\.-]+\.\w+', string)  # [-\+\.\w]+@[\w\.-]+\.\w+ for entire email ::: only domain @[\w\.-]+
    return match_pattern
    pass
