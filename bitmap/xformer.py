from bitmap import *
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

BITMAP_FILE_NAME = os.path.join(SCRIPT_DIR, 'bmp.bmp')
BITMAP_TRANSFORMED_FILE_NAME = os.path.join(SCRIPT_DIR, 'new_bmp.bmp')

# print(Bitmap.get_headers(Bitmap.read_file(BITMAP_FILE_NAME)))

bm = Bitmap.read_file(BITMAP_FILE_NAME)
new_bm = Bitmap(bm.transform_bitmap_flip_horizontal())
new_bm.write_file(BITMAP_TRANSFORMED_FILE_NAME)
# print(Bitmap.get_headers(Bitmap.read_file(BITMAP_TRANSFORMED_FILE_NAME)))
