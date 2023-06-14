#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file.
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_list():
    """
    Adds command-line arguments to a Python list and saves them to a file.
    """

    filename = "add_item.json"
    try:
        item_list = load_from_json_file(filename)
    except FileNotFoundError:
        item_list = []

        item_list.extend(sys.argv[1:])
        save_to_json_file(item_list, filename)

        add_items_to_list()
