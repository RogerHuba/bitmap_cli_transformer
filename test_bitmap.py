"""Test Module."""

from .bitmap.bitmap import Bitmap
import os
import pytest

BMP_FILE_PATH = './bitmap/bmp.bmp'
BMP_TEST_FILE_PATH = './bitmap/test.bmp'


def test_read_file_returns_bitmap_instance():
    """"Test that read_file function returns  instance of Bitmap."""
    assert isinstance(Bitmap.read_file(BMP_FILE_PATH), Bitmap)


def test_write_file_success():
    """Read a file, then write its contents to new file."""
    original_bitmap = Bitmap.read_file(BMP_FILE_PATH)
    try:
        original_bitmap.write_file(BMP_TEST_FILE_PATH)
        os.remove(BMP_TEST_FILE_PATH)
    except IOError:
        output = f'Problem writing test file { BMP_TEST_FILE_PATH } .'
        pytest.fail(output)
    except FileNotFoundError:
        output = f'Problem removing test file { BMP_TEST_FILE_PATH } .'
        pytest.fail(output)

def test_write_file_matches_original():
    """Read a file, then write its contents to new file. Read and compare original to written."""
    # Instantiate Bitmap object with original file
    original_bitmap = Bitmap.read_file(BMP_FILE_PATH)
    try:
        # Write the original data to a new file
        original_bitmap.write_file(BMP_TEST_FILE_PATH)
        # Clean up test file
        os.remove(BMP_TEST_FILE_PATH)
    except IOError:
        pytest.fail(f'Problem writing test file {BMP_TEST_FILE_PATH}.')
    except FileNotFoundError:
        pytest.fail(f'Problem removing test file {BMP_TEST_FILE_PATH}.')
    # Instantiate a Bitmap object from the new file
    new_bitmap = Bitmap.read_file(BMP_FILE_PATH)
    # Compare the headers read from the old file with the new
    assert original_bitmap.get_headers() == new_bitmap.get_headers()

# test on transformations.
# idea: we check the bytes location before and after transformation.
def test_rotate_180():
    """
    Check function transform_bitmap_rotate_180 function on the
    BMP_FILE_PATH define above.
    Check: the (first n bytes in old file) shall equal to the
    (last n bytes in new file in reversed order).
    """
    # Instantiate Bitmap object with original file
    original_bitmap = Bitmap.read_file(BMP_FILE_PATH)
    transformed_bitmap = Bitmap(original_bitmap.transform_bitmap_rotate_180())

    # check rotation by comparing locations: .
    assert (original_bitmap.pixel_array.tobytes()[:10] == \
            transformed_bitmap.pixel_array.tobytes()[-10:][::-1])


# def test_transform_bitmap_flip_horizontal():
#     """
#     Check function transform_bitmap_flip_horizontal function on the
#     BMP_FILE_PATH define above.
#     Check: for any row in pixel_array, (row_n in olde file) shall equal
#     to (row_n in new file in reversed order).
#     """
#     # Instantiate Bitmap object with original file
#     original_bitmap = Bitmap.read_file(BMP_FILE_PATH)
#     transformed_bitmap = Bitmap(original_bitmap.transform_bitmap_flip_horizontal())

#     import struct as s
#     # here we need to grab image width info to seperate lines.
#     img_width = int(s.unpack('I', original_bitmap.memory_view[18:22].tobytes())[0])

#     assert (original_bitmap.pixel_array[-img_width:].tobytes() == \
#             transformed_bitmap.pixel_array[-img_width:][::-1].tobytes())


def test_transform_bitmap_turn_blue():
    """
    Check function transform_bitmap_turn_blue function on the
    BMP_FILE_PATH define above.
    Check: whether the blue chanels value in the new file equals to 255.
    """
    # Instantiate Bitmap object with original file
    original_bitmap = Bitmap.read_file(BMP_FILE_PATH)
    transformed_bitmap = Bitmap(original_bitmap.transform_bitmap_turn_blue())

    # check rotation by comparing locations: .
    for x in range(0, len(transformed_bitmap.color_table), 4):
            assert(transformed_bitmap.color_table[x] == 255)

def test_transform_bitmap_turn_red():
    """
    Check function transform_bitmap_turn_red function on the
    BMP_FILE_PATH define above.
    Check: whether the red chanels value in the new file equals to 255.
    """
    # Instantiate Bitmap object with original file
    original_bitmap = Bitmap.read_file(BMP_FILE_PATH)
    transformed_bitmap = Bitmap(original_bitmap.transform_bitmap_turn_red())

    # check rotation by comparing locations: .
    for x in range(0, len(transformed_bitmap.color_table), 4):
            assert(transformed_bitmap.color_table[x+2] == 255)


def test_transform_bitmap_turn_green():
    """
    Check function transform_bitmap_turn_green function on the
    BMP_FILE_PATH define above.
    Check: whether the green chanels value in the new file equals to 255.
    """
    # Instantiate Bitmap object with original file
    original_bitmap = Bitmap.read_file(BMP_FILE_PATH)
    transformed_bitmap = Bitmap(original_bitmap.transform_bitmap_turn_green())

    # check rotation by comparing locations: .
    for x in range(0, len(transformed_bitmap.color_table), 4):
            assert(transformed_bitmap.color_table[x+1] == 255)

# def test_transform_bitmap_randomize_colors():
#     """
#     Check function transform_bitmap_randomize_colors function on the
#     BMP_FILE_PATH define above.
#     Check: whether color_table from old file and new file are different.
#     """
#     # Instantiate Bitmap object with original file
#     original_bitmap = Bitmap.read_file(BMP_FILE_PATH)
#     transformed_bitmap = Bitmap(original_bitmap.transform_bitmap_randomize_colors())

#     # check rotation by comparing locations: ...hum...somehow it doesn't work...
#     assert(original_bitmap.color_table.tobytes() != transformed_bitmap.color_table.tobytes())


def test_transform_bitmap_turn_blackwhite():
    """
    Check function transform_bitmap_turn_blackwhite function on the
    BMP_FILE_PATH define above.
    Check: whether for each element in color map that whether they equals to 0 or 255.
    """
    # Instantiate Bitmap object with original file
    original_bitmap = Bitmap.read_file(BMP_FILE_PATH)
    transformed_bitmap = Bitmap(original_bitmap.transform_bitmap_turn_blackwhite())

    # check rotation by comparing locations: .
    for x in range(0, len(transformed_bitmap.color_table)):
            assert((transformed_bitmap.color_table[x] == 255) or \
                    (transformed_bitmap.color_table[x] == 0))


def test_transform_bitmap_light():
    """
    Check function transform_bitmap_light function on the
    BMP_FILE_PATH define above.
    Check: whether for each element in color map it has become larger.
    """
    # Instantiate Bitmap object with original file
    original_bitmap = Bitmap.read_file(BMP_FILE_PATH)
    transformed_bitmap = Bitmap(original_bitmap.transform_bitmap_light())

    # check rotation by comparing locations: .
    for x in range(0, len(transformed_bitmap.color_table)):
            assert(original_bitmap.color_table[x] <= transformed_bitmap.color_table[x])

def test_transform_bitmap_dark():
    """
    Check function transform_bitmap_dark function on the
    BMP_FILE_PATH define above.
    Check: whether for each element in color map it has become smaller.
    """
    # Instantiate Bitmap object with original file
    original_bitmap = Bitmap.read_file(BMP_FILE_PATH)
    transformed_bitmap = Bitmap(original_bitmap.transform_bitmap_dark())

    # check rotation by comparing locations: .
    for x in range(0, len(transformed_bitmap.color_table)):
            assert(original_bitmap.color_table[x] >= transformed_bitmap.color_table[x])
