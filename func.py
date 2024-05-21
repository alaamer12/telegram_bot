import os
ALLOWED_EXTENSIONS = ['.txt', '.text']

def get_file_extension(file_name):
    return os.path.splitext(file_name)[1].lower()

FILE_PATH = os.path.join(".", "Utils", "src", "filtered.txt")
RAW_INPUT_PATH = os.path.join(".", "Utils", "src", "RAWinput.txt")


