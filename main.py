"""
Name : main.py
Author : Oussama BRICH
Contact : brich.oussama@gmail.com
Date    : 01/01/2021
Desc: apply a One-Time Pad cipher to a given message
"""
import os
import random


def write_file(path, text):
    f = open(path, "w")
    f.write(text)
    f.close()


def generate_pads(path):
    """
    Generate pads to be used to encrypt text
    :param path: path to parent directory
    :return: N/A
    """
    # Create new dir taking in consideration the olds ones
    old_dirs = os.listdir(path)

    i = 0
    new_dir_name = ""

    while True:
        new_dir_name = str(i).zfill(4)
        # Create new dir if already exist
        if new_dir_name not in old_dirs:
            new_dir_name = path + new_dir_name
            os.mkdir(new_dir_name)
            break
        i += 1

        if i == 9999:
            print("Max dir achieved!")
            break

    for j in range(100):
        # Get a random number 12 digit = 48 bytes
        random_number = random.randint(100000000000, 999999999999)

        p_path = new_dir_name + "/" + str(j).zfill(2) + "p"
        s_path = new_dir_name + "/" + str(j).zfill(2) + "s"
        c_path = new_dir_name + "/" + str(j).zfill(2) + "c"

        write_file(p_path, str(random_number))
        write_file(s_path, str(random_number))
        write_file(c_path, str(random_number))


def main():
    """
    main function
    :return: status
    """

    pads_path = "./pads/"
    generate_pads(pads_path)
    return 0


if __name__ == "__main__":
    main()
