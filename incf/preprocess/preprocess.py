import os
from incf.convert import convert

IDS = []
start = 1


def create_uuid():
    global start

    if start in IDS:
        start += 1

    new = f'0{start}' if start < 10 else start

    IDS.append(start)
    return new


def reset_index():
    global start, IDS
    start = 1
    IDS = []

