#!/usr/bin/python3
""" this module bundle all arguments to a list and save on file"""


import sys
import json
save_json = __import__('5-save_to_json_file').save_to_json_file
return_json = __import__('6-load_from_json_file').load_from_json_file

try:
    pyobj = return_json("add_item.json")
    save_json(pyobj + sys.argv[1:], "add_item.json")
except FileNotFoundError:
    if (sys.argv is not None):
        save_json(sys.argv[1:], "add_item.json")
