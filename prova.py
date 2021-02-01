import xlsxwriter as xl  # This library gives us access to methods related to Microsoft Excel.
import os  # This library provides us methods to work with files and directories.
import subprocess  # This library allows us to open the pdf file.
from services.function_press_enter_to_continue import FunctionPressEnterToContinue
from services.file_handler import FileHandler
from services.user_input_handler import UserInputHandler

function_press_enter_to_continue = FunctionPressEnterToContinue()
working_directory_path = None
file_name = None
page_number = None
alterations = []


# Console Description --------------------------------------------------
print("This code is able to change names of files in the RPA - Artigo folder.\n"
      "It also stores all the changed files in a xlsx file.")
# -----------------------------------------------------------------------
function_press_enter_to_continue.should_proceed()

repeat_step_1 = 'y'
while repeat_step_1 == 'y':
    # Step 1 - Choose directory -------------------------------------------
    print('Select the directory where RPA - Artigo folder is located')
    working_directory_path = FileHandler.choose_directory()
    os.chdir(working_directory_path)
    print('You are currently working at the directory ' + working_directory_path)
    repeat_step_1 = UserInputHandler.change_choice_of_directory()
    # ---------------------------------------------------------------------

another_alteration = 'y'
while another_alteration == 'y':
    repeat_step_2 = 'y'
    while repeat_step_2 == 'y':
        # Step 2 - Choose file ------------------------------------------------
        for files in os.listdir(os.getcwd()):
            print(files)
        files_list = os.listdir(working_directory_path)
        page_number = UserInputHandler.choose_page_number()
        file_name = page_number + '_PDFsam_DUP_Signals_Robotic-process-automation.pdf'
        print(f'You choose the file: {file_name}')

        repeat_step_2 = UserInputHandler.choose_different_file()
        # ---------------------------------------------------------------------

    # Step 3 - Open file in a pdf reader ----------------------------------
    subprocess.Popen(file_name, shell=True)
    print('The file has just opened in your pdf reader')
    # ---------------------------------------------------------------------

    function_press_enter_to_continue.should_proceed()

    # Step 4 & 5 & 6 - Open window and save new file with new name --------
    print('Please save the file with a new name')
    new_file_name = 'Pagina ' + page_number + ' - Modificado'
    FileHandler.save_file_as(file_name, new_file_name)
    print(f'The new file was saved with the new name {new_file_name}')
    alterations.append([file_name, 'Documento alterado'])
    UserInputHandler.delete_unaltered_file(file_name)

    # ---------------------------------------------------------------------
    another_alteration = UserInputHandler.modify_another_file()

# Step 7 & 10 - Create a xlsx file and  save it with given name -------
xlsx_file_name = 'Relatório de execução.xlsx'
os.chdir(working_directory_path)
workbook = xl.Workbook(xlsx_file_name)
worksheet = workbook.add_worksheet()
print(f'An xlsx file named {xlsx_file_name} was created in the directory {working_directory_path}')
# ---------------------------------------------------------------------

function_press_enter_to_continue.should_proceed()

# Step 8 & 9 - Add data to the cells ----------------------------------
i = 0
for alteration in alterations:
    worksheet.write(i, 0, alteration[0])
    worksheet.write(i, 1, alteration[1])
    i += 1

workbook.close()
print(f'All alterations made in the files has been stored in the {xlsx_file_name} file')
# ---------------------------------------------------------------------
