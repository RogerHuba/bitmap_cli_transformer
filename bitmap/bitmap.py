import random
import struct


class Bitmap(object):
    def __init__(self, file_data):
        """Initialization method for Bitmap instance.
        Provides itemized data related to consumed Bitmap file through the use of a MemoryView object.
        """
        self.source = bytearray(file_data)
        self.memory_view = memoryview(self.source)

        self.offset = struct.unpack('I', self.memory_view[10:14].tobytes())[0]
        self.color_table = self.memory_view[54:self.offset]
        self.pixel_array = self.memory_view[self.offset:]

    @classmethod
    def read_file(cls, origin):
        """
        Class Method which consumes a file path as input, and returns a Bitmap instance.
        input-origin: a path of the origin file (string)
        output: a Bitmap instance (class object)
        """
        with open(origin, 'rb') as source:
            raw = source.read()
        return Bitmap(raw)

    def write_file(self, target):
        """
        Instance Method which accepts a target file path and writes the instance source data to target path.
        """
        with open(target, 'bw+') as f:
            f.write(self.memory_view.tobytes())

    def get_headers(self):
        """Instance Method which provides instance source data as readable output to std out.
        """
        import struct as s
        result = f'''
            Type: {self.memory_view[0:2].tobytes().decode()}
            Size: {s.unpack('I', self.memory_view[2:6].tobytes())[0]}
            Reserved 1: {s.unpack('H', self.memory_view[6:8].tobytes())[0]}
            Reserved 2: {s.unpack('H', self.memory_view[8:10].tobytes())[0]}
            Offset: {s.unpack('I', self.memory_view[10:14].tobytes())[0]}
            DIB Header Size: {s.unpack('I', self.memory_view[14:18].tobytes())[0]}
            Width: {s.unpack('I', self.memory_view[18:22].tobytes())[0]}
            Height: {s.unpack('I', self.memory_view[22:26].tobytes())[0]}
            Colour Planes: {s.unpack('H', self.memory_view[26:28].tobytes())[0]}
            Bits per Pixel: {s.unpack('H', self.memory_view[28:30].tobytes())[0]}
            Compression Method: {s.unpack('I', self.memory_view[30:34].tobytes())[0]}
            Raw Image Size: {s.unpack('I', self.memory_view[34:38].tobytes())[0]}
            Horizontal Resolution: {s.unpack('I', self.memory_view[38:42].tobytes())[0]}
            Vertical Resolution: {s.unpack('I', self.memory_view[42:46].tobytes())[0]}
            Number of Colours: {s.unpack('I', self.memory_view[46:50].tobytes())[0]}
            Important Colours: {s.unpack('I', self.memory_view[50:54].tobytes())[0]}
            '''
        return result

    # TODO: Write your instance methods for transformations here as part of the Bitmap class.

    def transform_bitmap_rotate_180(self):
        """Instance method on Bitmap objects that reverses the order of self.pixel_array and concatentates
        it back into the binary data, causing the bitmap image to appear rotated 180 degrees.

        input: none
        output: binary data representing bitmap
        p"""
        bitmap_data = self.memory_view[:self.offset].tobytes(
        ) + self.pixel_array[::-1].tobytes()
        return bitmap_data

    def transform_bitmap_flip_horizontal(self):
        """Instance method on Bitmap objects that reverses the order each row of pixels in
        self.pixel_array and concatentates it back into the binary data, causing the
        bitmap image to appear rotated 180 degrees.

        input: none
        output: binary data representing bitmap
        """
        import struct as s
        # Need image width to determine pixel rows
        img_width = s.unpack('I', self.memory_view[18:22].tobytes())[0]
        # New byte string to hold modified pixel array
        mod_pixel_array = bytes()
        # Iterate over self.pixel_array img_width pixels at a time
        for i in range(0, len(self.pixel_array), img_width):
            # Add a reversed slice of self.pixel_array to the new pixel array
            mod_pixel_array += self.pixel_array[i: i +
                                                img_width][::-1].tobytes()
        # Concatenate the data up to the pixel array, then the pixel array
        bitmap_data = self.memory_view[:self.offset].tobytes(
        ) + mod_pixel_array
        return bitmap_data

    def transform_bitmap_turn_blue(self):
        """Instance method on Bitmap that sets the blue byte in the bitmap color table to 255.

        input: none
        output: binary data representing bitmap
        """
        print(type(self.color_table[0]))
        for x in range(0, len(self.color_table), 4):
            self.color_table[x] = 255
        bitmap_data = self.memory_view[:54].tobytes(
        ) + self.color_table + self.pixel_array.tobytes()
        return bitmap_data

    def transform_bitmap_turn_red(self):
        """Instance method on Bitmap that sets the red byte in the bitmap color table to 255.

        input: none
        output: binary data representing bitmap
        """
        print(type(self.color_table[0]))
        for x in range(0, len(self.color_table), 4):
            self.color_table[x + 2] = 255
        bitmap_data = self.memory_view[:54].tobytes(
        ) + self.color_table + self.pixel_array.tobytes()
        return bitmap_data

    def transform_bitmap_turn_green(self):
        """Instance method on Bitmap that sets the green byte in the bitmap color table to 255.

        input: none
        output: binary data representing bitmap
        """
        for x in range(0, len(self.color_table), 4):
            self.color_table[x + 1] = 255
        bitmap_data = self.memory_view[:54].tobytes(
        ) + self.color_table + self.pixel_array.tobytes()
        return bitmap_data

    def transform_bitmap_randomize_colors(self):
        """Instance method on Bitmap objects that randomizes every byte in the color table.

        input: none
        output: binary data representing bitmap
        """
        for x in range(0, len(self.color_table)):
            self.color_table[x] = random.randint(0, 255)
        bitmap_data = self.memory_view[:54].tobytes(
        ) + self.color_table + self.pixel_array.tobytes()
        return bitmap_data

    def transform_bitmap_turn_blackwhite(self):
        """Instance method on Bitmap that makes each set of color table either black or white.
        No gray area!

        input: none
        output: binary data representing bitmap
        """
        for x in range(0, len(self.color_table), 4):
            # building a threshold based on input rgb values
            color_sum = self.color_table[x] + self.color_table[x+1] +\
            self.color_table[x+2]

            # this criterion can be arbitrary.
            if color_sum >= (255*3//2):
                self.color_table[x] = 255
                self.color_table[x+1] = 255
                self.color_table[x+2] = 255

                # didn't work this way...
                # self.color_table[x:x+2] = 255,255,255
            else:
                self.color_table[x] = 0
                self.color_table[x+1] = 0
                self.color_table[x+2] = 0

                # didn't work this way...
                # self.color_table[x:x+2] = 0,0,0
        bitmap_data = self.memory_view[:54].tobytes(
        ) + self.color_table + self.pixel_array.tobytes()
        return bitmap_data

    def transform_bitmap_light(self):
        """Instance method on Bitmap that makes bitmap file brighter and lighter.

        input: none
        output: binary data representing bitmap
        """
        for x in range(0, len(self.color_table), 4):
            self.color_table[x] = min(255, self.color_table[x]*2)
            self.color_table[x+1] = min(255, self.color_table[x+1]*2)
            self.color_table[x+2] = min(255, self.color_table[x+2]*2)
        bitmap_data = self.memory_view[:54].tobytes(
        ) + self.color_table + self.pixel_array.tobytes()
        return bitmap_data

    def transform_bitmap_dark(self):
        """Instance method on Bitmap that makes bitmap file grimmer and darker.

        input: none
        output: binary data representing bitmap
        """
        for x in range(0, len(self.color_table), 4):
            self.color_table[x] //= 2
            self.color_table[x+1] //= 2
            self.color_table[x+2] //= 2
        bitmap_data = self.memory_view[:54].tobytes(
        ) + self.color_table + self.pixel_array.tobytes()
        return bitmap_data

    # def transform_bitmap_whatif(self):
    #     """Instance method on Bitmap that sets the green byte in the bitmap color table to 255.

    #     input: none
    #     output: binary data representing bitmap
    #     """
    #     for x in range(0, len(self.color_table), 4):
    #         # ok..memoryview will complain for invalid input
    #         self.color_table[x] = -123
    #         self.color_table[x+1] = 234
    #         self.color_table[x+2] = 345
    #     bitmap_data = self.memory_view[:54].tobytes(
    #     ) + self.color_table + self.pixel_array.tobytes()
    #     return bitmap_data
