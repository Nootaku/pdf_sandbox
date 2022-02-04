"""
1. Open file
2. Read file and copy content
3. Close file
4. Create new file with identical content
5. Save file as new_name
6. Close file
"""


def rename(text, new_name):
    """Save string to file.

    **param text**: STR
    **param new_name**: STR - path to destination
    """
    # Validate destination path (new_name)
    if not new_name.endswith(".txt"):
        # if not valid: add '.txt' to destination path
        new_name += ".txt"

    with open(new_name, 'w') as new_file:
        new_file.write(text)


def main(path, new_name):
    # 1 Open file at path and get text
    with open(path, 'rt') as file:
        file_text = file.read()

    # 2 Check if new_name in text
    if 'Apple' in file_text:
        rename(file_text, new_name)
    else:
        print('Apples not in string')


if __name__ == '__main__':
    my_path = 'sample.txt'
    my_name = 'apple'

    main(my_path, my_name)
