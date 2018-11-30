"""Test Module."""

from .bitmap.bitmap import Bitmap
import os
import pytest

BMP_FILE_PATH = '../bitmap/bitmap.bmp'
BMP_TEST_FILE_PATH = '../bitmap/test.bmp'


def test_read_file_returns_bitmap_instance():
    """"Test that read_file function returns  instance of Bitmap."""
    assert isinstance(Bitmap.read_file(BMP_FILE_PATH), Bitmap)


def test_write_file_success():
    """Read a file, then write its contents to new file."""
    original_bitmap = Bitmap.read_file(BMP_FILE_PATH)
    try:
        original_bitmap.write_file(BMP_TEST_FILE_PATH)
        os.remove()
    except IOError:
        pytest.fails(f'Problem writing test file {BMP_TEST_FILE_PATH}.')


def test_write_file_matches_original():
    """Read a file, then write its contents to new file. Read and compare original to written."""
    original_bitmap = Bitmap.read_file(BMP_FILE_PATH)
    try:
        original_bitmap.write_file(BMP_TEST_FILE_PATH)
        os.remove()
    except IOError:
        pytest.fails(f'Problem writing test file {BMP_TEST_FILE_PATH}.')
    new_bitmap = Bitmap.read_file(BMP_TEST_FILE_PATH)
    assert original_bitmap.get_headers() == new_bitmap.get_headers()
