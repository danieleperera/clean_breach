# This is how we import code from another file
# The `.` represents this module, so we are saying:
# "From this module, import filestream.py"
from . import filestream


if __name__ == '__main__':
    # We can access filestream.py using the `.` operator.
    # For example, we'd call the `get_files` function with
    # `filestream.get_files(path)`
    ...  # TODO Move your working logic here


filepath = filestream.get_files(root)
filestream.get_data(filepath)


# moved the working logic to __main__.py as you said
