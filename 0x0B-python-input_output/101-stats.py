#!/usr/bin/python3
""" read stdin and compute file metrics"""


file_size = 0
info_dict = {}
count = 1
while (1):
    try:
        x = str(input())
        file_size += int(x.split(" ")[-1])
        if x.split(" ")[-2] in info_dict:
            info_dict[x.split(" ")[-2]] += 1
        else:
            info_dict[x.split(" ")[-2]] = 1
        if count % 10 == 0:
            print("File size: {}".format(file_size))
            info_dict = dict(sorted(info_dict.items()))
            for key, value in info_dict.items():
                print("{}: {}".format(key, value))
        count += 1
    except KeyboardInterrupt:
        info_dict = dict(sorted(info_dict.items()))
        print("File size: {}".format(file_size))
        for key, value in info_dict.items():
            print("{}: {}".format(key, value))
