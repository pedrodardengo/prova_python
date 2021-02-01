import os
from tkinter import filedialog  # This library allow the use of Windows dialog boxes.


class FileHandler:
    """
    This class is used for handling file methods.
    """
    @staticmethod
    def save_file_as(file_name, new_file_name):
        """
        This method uses the tkinter library to save files using Microsoft Windows dialog boxes.
        It is able o copy a file named as file_name and save it with a new name
        given by new_file_name
        :param file_name: directory path where file should be saved
        :param new_file_name: new name to be used
        :return: None
        """
        new_file = filedialog.asksaveasfilename(initialfile=new_file_name, defaultextension='.pdf',
                                                confirmoverwrite=True)
        with open(file_name, 'rb') as opened_file:
            data = opened_file.read()
            with open(new_file, 'wb') as new_file_opened:
                new_file_opened.write(data)
                new_file_opened.close()
            opened_file.close()
        return

    @staticmethod
    def choose_directory():
        """
        This method asks the user which directory should be used.
        :return: directory path
        """
        working_directory_path = filedialog.askdirectory(mustexist=True, initialdir=os.getcwd())
        directory_name = os.path.basename(working_directory_path)
        while directory_name != 'RPA - Artigo':
            print('ERROR! You must choose the RPA - Artigo folder')
            working_directory_path = filedialog.askdirectory(mustexist=True, initialdir=os.getcwd())
            directory_name = os.path.basename(working_directory_path)

        return working_directory_path
