import cmd
import sys
import os


class BitmapManipulator(cmd.Cmd):
    intro = 'Welcome to the bitmap manipulator.  Type help or ? to list commands.\n'
    prompt = '> '

    @staticmethod
    def do_get_headers(source):
        """
        To use this type 'get_headers' followed by the file location's source.

        get_headers <source>

        Returns a line-item response of the file's header data.
        """
        # TODO: Complete these CLI methods for performing described actions
        #here we pass the file_in to get headers

    def do_transform(self, arg):
        """
        To use this type in 'transform' followed by
        the original file location and the new file location
        and the type of change you would like to do.

        transform <original> <new> <transform>

        Creates a new file at 'new' location with the provided 'transform'
        applied to the new file.
        """
        # TODO: Complete these CLI methods for performing described actions
        file_in = input('Enter file to transform:  ')
        file_out = input('Enter name of the file to save to:  ')
        # Need to add duplicate file checking
        print('\n1) Change Color')
        print('2) Change Size')
        print('3) Rotate Picture')
        print('4) Flip Picture \n')


    def emptyline(self):
        '''Handles when the user presses enter and submits an empty line'''
        print('Type help or ? to list commands.\n')

    def help_exit(self):
        """ User enters help exit """
        print('Type "exit" to leave the program')

    def help_transform(self):
        """ User enters help transform
        transform input-file output-file
        Will then prompt user for type of transformation to apply
        """
        print('Enter transform. Prompt for files and type of transformation')

    def help_get_headers(self):
        """ User enters help get_headers
        After the user enters the file-in and file out will select the type
        of transformation to take place on the file
        """
        print('Enter the command transform "file-in" "file-out"')

    @staticmethod
    def do_exit(args):
        """
        To use this type in 'exit' and the CLI tool will cleanly exit the
        running application.
        """
        print('Thank you for using the application')
        sys.exit()


if __name__ == '__main__':
    os.system('clear')
    BitmapManipulator().cmdloop()
