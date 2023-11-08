#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

try:
    s_data = '{"id": 12, "num": 4, "holberton" }'
    data = from_json_string(s_data)
    print(data)
    print(type(data))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
