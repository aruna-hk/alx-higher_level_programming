#!/usr/bin/python3
""" this module bundle all arguments to a list except file name"""
import sys
save_json = __import__('5-save_to_json_file').save_to_json_file
return_json = __import__('6-load_from_json_file').load_from_json_file


lis = sys.argv[1:]
save_json(lis, "add_item.json")
return_json("add_item.json")
