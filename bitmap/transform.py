import cmd
import sys
import os
from bitmap import Bitmap


class BitmapManipulator(cmd.Cmd):
    intro = 'Welcome to bitmap manipulator.\nType help or ? to list commands.\n'
    prompt = '$ >'

    @staticmethod
    def do_get_headers(source):
        """
        To use this type 'get_headers' followed by the file location's source.

        get_headers <source>

        Returns a line-item response of the file's header data.
        """
        bitmap = Bitmap.read_file(source)
        print(bitmap.get_headers())

    def do_transform(self, arg):
        """
        To use this type in 'transform' followed by
        the original file location and the new file location
        and the type of change you would like to do.

        transform <original> <new> <transform>

        Creates a new file at 'new' location with the provided 'transform'
        applied to the new file.
        """

        # Parse input to this function, check for 3 arguments
        args = arg.split()
        if len(args) != 3:
            print('Sorry. Error parsing arguments. Type `help transform` for usage of this command.')
            return
        # Unpack arguments
        original, new, transform = args

        # Create Bitmap object from original. Return on FNF.
        try:
            bm = Bitmap.read_file(original)
        except FileNotFoundError:
            print(f'Couldn\'t locate bitmap file {original}. Type `help transform` for usage of this command.')
            return

        # Perform selected transform, creating new Bitmap instance with transformed data.
        if transform == '1':
            new_bm = Bitmap(bm.transform_bitmap_rotate_180())
        elif transform == '2':
            new_bm = Bitmap(bm.transform_bitmap_flip_horizontal())
        elif transform == '3':
            new_bm = Bitmap(bm.transform_bitmap_turn_blue())
        elif transform == '4':
            new_bm = Bitmap(bm.transform_bitmap_turn_red())
        elif transform == '5':
            new_bm = Bitmap(bm.transform_bitmap_turn_green())
        elif transform == '6':
            new_bm = Bitmap(bm.transform_bitmap_randomize_colors())
        elif transform == '7':
            new_bm = Bitmap(bm.transform_bitmap_turn_blackwhite())
        elif transform == '8':
            new_bm = Bitmap(bm.transform_bitmap_light())
        elif transform == '9':
            new_bm = Bitmap(bm.transform_bitmap_dark())
        else:
            print(f'{transform} is not a valid transform. Type `list_transforms` to see the available transforms.')
            return
        print('Transform success.')

        # Write new Bitmap object data to file. Return on IOError.
        try:
            new_bm.write_file(new)
            print(f'Wrote new bitmap file {new}')
        except IOError:
            print(f'There was a problem writing the file {new}')

    def do_list_transforms(self, arg):
        print()
        print('Available transforms are:')
        print('1) Rotate Picture 180 Deg')
        print('2) Flip Horizontally')
        print('3) Turn Picture Blue')
        print('4) Turn Picture Red')
        print('5) Turn Picture Green')
        print('6) Randomize Picture Colors')
        print('7) Turn image black and white')
        print('8) Lighten image')
        print('9) Darken image')
        print()

    def emptyline(self):
        """Handles when the user presses enter and submits an empty line"""
        print('Type help or ? to list commands.\n')

    def help_exit(self):
        """User enters help exit """
        print('\nType "exit" to leave the program\n\n')
        print('Usage: exit\n')

    def help_transform(self):
        """User enters help transform
        transform input-file output-file
        Will then prompt user for type of transformation to apply.
        """
        print('\nTransform a bitmap file and save to a new file.\n\n')
        print('Usage: transform <path_to_source_file> <path_to_destination_file> <transform>\n')

    def help_get_headers(self):
        """User enters help get_headers.
        After the user enters the file-in and file out will select the type
        of transformation to take place on the file.
        """
        print('\nView the extracted headers from a bitmap file.\n\n')
        print('Usage: get_headers <path_to_source_bitmap>\n')

    def help_list_transforms(self):
        """Documentation for list_transforms command."""
        print('\nDisplays a list of the available transforms. The number of the transform should be supplied in combination with `transform` to apply the associated transform.\n\n')
        print('Usage: list_transforms\n')

    @staticmethod
    def do_exit(args):
        """
        To use this type in 'exit' and the CLI tool will cleanly exit the
        running application.
        """
        sys.exit('Thank you for using the application')


# def get_file_in():
#     """Will take in user entered file and verify that the file exists.
#     """
#     file_in_message = 'Enter file to transform: '
#     is_file = False
#     while is_file is False:
#         source = input(file_in_message)
#         if (os.path.isfile(source)):
#             is_file = True
#             print('File Verified\n')
#             return source
#         else:
#             file_in_message = '\nInvalid file.  Enter a file to transform:  '


# def get_file_out():
#     """Will take user entered file for saving the transformed file
#     """
#     file_out = False
#     file_out_message = 'Enter name of the file to save to:  '
#     while file_out is False:
#         input(file_out_message)
#         if file_out_message:
#             file_out = True
#             print('\nFile out verified\n')
#             return file_out
#         else:
#             file_out_message = 'Please enter a valid file name'


# def get_menu_option():
#     """Users will enter a number from 1 -6 to select action."""
#     transform_menu = 0
#     transform_message = 'Select an Action to take on the picture: '
#     while ((transform_menu < 1) or (transform_menu > 6)):
#         print('\n1) Rotate Picture 180 Deg')
#         print('2) Flip Horizontally')
#         print('3) Turn Picture Blue')
#         print('4) Turn Picture Green')
#         print('5) Turn Picture Red')
#         print('6) Randomize Picture Colors\n')
#         transform_menu = int(input(transform_message))
#         if ((transform_menu < 1) or (transform_menu > 6)):
#             transform_message = 'Invalid action. Please select again'
#         else:
#             return transform_menu


if __name__ == '__main__':
    try:
        os.system('clear')
        BitmapManipulator().cmdloop()
    except KeyboardInterrupt:
        os._exit(0)
