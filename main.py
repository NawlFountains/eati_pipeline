""" Module that encapsule main function """
import os


def main():
    """ Creates an folder build with an index.html file """
    os.mkdir("build")
    with open("build/index.html", "x", encoding="utf-8") as file_handler:
        file_handler.close()
