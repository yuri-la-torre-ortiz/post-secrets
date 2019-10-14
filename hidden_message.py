import os
import string

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir("/home/codedoor/Desktop/pythonic-programming-foundations/backup")
    #print(file_list)
    #saved_path = os.getcwd()
    #print("Current Working Directory is" + saved_path)
    os.chdir("/home/codedoor/Desktop/pythonic-programming-foundations/backup")
    #(2) for each file, rename filename

    for file_name in file_list:
        translation_table = str.maketrans("0123456789", "          ", "0123456789")
        os.rename(file_name, file_name.translate(translation_table))

rename_files()
