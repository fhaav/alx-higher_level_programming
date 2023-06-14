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
    new_items = sys.argv[1:]
    existing_items = []

    try:
        with open(filename, 'r') as file:
            content = file.read()
            if len(content) > 0:
                existing_items = load_from_json_file(filename)
    except FileNotFoundError:
        existing_items = []

    updated_items = existing_items + new_items

    save_to_json_file(updated_items, filename)
