import os


class UserInputHandler:
    @staticmethod
    def change_choice_of_directory():
        repeat = input('Do you want to change directories? (y, n) ')
        while repeat != 'y' and repeat != 'n':
            print("Wrong input! You may type only 'y' or 'n'.")
            repeat = input('Do you want to change directories you chose? (y, n) ')
        return repeat

    @staticmethod
    def choose_page_number():
        page_number = input('The files above are the files in the directory.\n'
                            'What page do you want to have access to? (1-10) ')
        page_numbers = list(range(1, 11))
        page_numbers = str(page_numbers)
        while page_number not in page_numbers:
            print("Wrong input! You may type only numbers from 1 to 10.")
            page_number = input('The files above are the files in the directory.\n'
                                'What page do you want to have access to? (1-10) ')

        return page_number

    @staticmethod
    def choose_different_file():
        repeat = input('Do you want to choose a different file? (y, n) ')
        while repeat != 'y' and repeat != 'n':
            print("Wrong input! You may type only 'y' or 'n'.")
            repeat = input('Do you want to choose a different file? (y, n) ')
        return repeat

    @staticmethod
    def delete_unaltered_file(file_name):
        delete_un_file = input('Do you want to delete the unaltered file version? (y, n) ')
        while delete_un_file != 'y' and delete_un_file != 'n':
            print("Wrong input! You may type only 'y' or 'n'.")
            delete_un_file = input('Do you want to DELETE the unaltered file version? (y, n) ')
        if delete_un_file == 'y':
            os.remove(file_name)
        return

    @staticmethod
    def modify_another_file():
        another_alteration = input('Do you want to make modifications to another file? (y, n) ')
        while another_alteration != 'y' and another_alteration != 'n':
            print("Wrong input! You may type only 'y' or 'n'.")
            another_alteration = input('Do you want to make modifications to another file? (y, n) ')
        return another_alteration

