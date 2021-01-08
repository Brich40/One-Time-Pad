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


def get_random_number(size):
    """
    :param size: with of the random int
    :return: random int
    randint() function uses /dev/random, I used this code to get the random manually :

    <with open("/dev/random", 'rb') as f:
        random_number = int.from_bytes(f.read(12), 'big')>

    but it takes a long time to get it.
    """
    min_int = pow(10, size-1)
    max_int = pow(10, size) - 1
    return random.randint(min_int, max_int)


def generate_pads(path):
    """
    Generate pads to be used to encrypt text
    :param path: path to parent directory
    :return new_dir_name: new pads dir path
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

        # Get a random number from /dev/random 12 digit = 48 bytes
        random_number = get_random_number(12)

        p_path = new_dir_name + "/" + str(j).zfill(2) + "p"
        s_path = new_dir_name + "/" + str(j).zfill(2) + "s"
        c_path = new_dir_name + "/" + str(j).zfill(2) + "c"

        write_file(p_path, str(random_number))
        write_file(s_path, str(random_number))
        write_file(c_path, str(random_number))

    return new_dir_name

def encrypt(string, pad_path):
    """
    Encrypt srting using pads
    :param string: string to be encrypted
    :param pad_path: pad path
    :return:
    """
    f = open(pad_path, "r")
    pads = f.read()
    encrypted_str = ""

    for char in string:
        if not pads[0]:
            print("Pad is empty!")
            return ""

        # Get pad value and remove it from pads
        pad_value = int(pads[0])
        pads = pads[1:]
        char_ord = ord(char)
        encrypted_str = encrypted_str + str(chr(char_ord + pad_value))

    return encrypted_str


def decrypt(string, pad_path):
    """
    Decrypt string using pad
    :param string: string to be decryted
    :param pad_path:
    :return:
    """
    f = open(pad_path, "r")
    pads = f.read()
    decrypted_str = ""

    for char in string:
        if not pads[0]:
            print("Pad is empty!")
            return ""

        # Get pad value and remove it from pads
        pad_value = int(pads[0])
        pads = pads[1:]
        char_ord = ord(char)
        decrypted_str = decrypted_str + str(chr(char_ord - pad_value))

    return decrypted_str


def main():
    """
    main function
    :return: status
    """

    pads_path = "./pads"
    pad = "./pads/0000/00c"
    # generate_pads(pads_path)

    test_str = "test"
    print("Test word : " + test_str)
    encrypted_str = encrypt("Test", pad)
    print(encrypted_str)

    decrypted_str = decrypt(encrypted_str, pad)
    print(decrypted_str)

    return 0


if __name__ == "__main__":
    main()
