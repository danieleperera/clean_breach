from pathlib import Path

# __file__ points to this file no matter where you run it from
# Using this, we can build our paths safely.
SRC = Path(__file__).parent
ROOT = SRC.parent
RES = ROOT / 'res'
MEDIA = RES / 'media'

#print(MEDIA)
