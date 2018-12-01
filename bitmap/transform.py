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

        get_file_in()
        get_file_out()
        get_menu_option()

    def emptyline(self):
        """Handles when the user presses enter and submits an empty line"""
        print('Type help or ? to list commands.\n')

    def help_exit(self):
        """User enters help exit """
        print('\nType "exit" to leave the program\n')

    def help_transform(self):
        """User enters help transform
        transform input-file output-file
        Will then prompt user for type of transformation to apply.
        """
        print('\nEnter transform. Prompt for files and type of \
        transformation\n')

    def help_get_headers(self):
        """User enters help get_headers.
        After the user enters the file-in and file out will select the type
        of transformation to take place on the file.
        """
        print('\nEnter the command transform. Will be prompted for "file-in" \
        "file-out"\n')

    @staticmethod
    def do_exit(args):
        """
        To use this type in 'exit' and the CLI tool will cleanly exit the
        running application.
        """
        sys.exit('Thank you for using the application')


def get_file_in():
    """Will take in user entered file and verify that the file exists.
    """
    file_in_message = 'Enter file to transform: '
    is_file = False
    while is_file is False:
        source = input(file_in_message)
        if (os.path.isfile(source)):
            is_file = True
            print('File Verified\n')
            return source
        else:
            file_in_message = '\nInvalid file.  Enter a file to transform:  '


def get_file_out():
    """Will take user entered file for saving the transformed file
    """
    file_out = False
    file_out_message = 'Enter name of the file to save to:  '
    while file_out is False:
        input(file_out_message)
        if file_out_message:
            file_out = True
            print('\nFile out verified\n')
            return file_out
        else:
            file_out_message = 'Please enter a valid file name'


def get_menu_option():
    """Users will enter a number from 1 -6 to select action."""
    transform_menu = 0
    transform_message = 'Select an Action to take on the picture: '
    while ((transform_menu < 1) or (transform_menu > 6)):
        print('\n1) Rotate Picture 180 Deg')
        print('2) Flip Horizontally')
        print('3) Turn Picture Blue')
        print('4) Turn Picture Green')
        print('5) Turn Picture Red')
        print('6) Randomize Picture Colors\n')
        transform_menu = int(input(transform_message))
        if ((transform_menu < 1) or (transform_menu > 6)):
            transform_message = 'Invalid action. Please select again'
        else:
            return transform_menu


if __name__ == '__main__':
    os.system('clear')
    BitmapManipulator().cmdloop()
