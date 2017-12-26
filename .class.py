#!/usr/bin/env python
import os
import sys
import json
from time import sleep
from shutil import move
base_dir = "Classify"

config_path = ".formats.json"
unknow_dir = "Unknow files"
message_dir = "Cannot create directory!"


def error(mess="Unknown error!"):
    sys.stderr.write("Error! " + mess + "\n")
    exit()


def loadData(cp=config_path):
    global data
    try:
        with open(cp, "r") as jf:
            data = json.loads(jf.read())
    except:
        error("Cannot read config!")
    return data


def init(data_cfg, bd=base_dir, ud=unknow_dir):
    base_path = bd + "/"
    os.mkdir(bd)
    os.mkdir(base_path + ud)
    for cat in data_cfg:
        os.mkdir(base_path + cat)


def makeLst(data_cfg, bd=base_dir, ud=unknow_dir):
    dir_lst = os.listdir(bd)
    for cat in data_cfg:
        dir_lst.remove(cat)
    dir_lst.remove(ud)
    return dir_lst


def mov(src, dst, bd=base_dir):
    try:
        move(bd + "/" + src, bd + "/" + dst + "/" + src)
    except:
        error("Cannot move directory!")


def classify(ext, data_cfg, ud=unknow_dir):
    for cat, exts in data_cfg.items():
        if ext in exts:
            return exts[0]
    return ud


def mainLoop(ud=unknow_dir):
    while 1:
        lst = makeLst(data)
        for f in lst:
            if "." in f and not len(f.split(".")) > 2:
                name, ext = f.split(".")
                cathegory = classify(ext, data)
            else:
                cathegory = ud
            mov(f, cathegory)
        sleep(10)


def main():
    loadData()
    try:
        init(data)
    except:
        pass
    mainLoop()


if __name__ == "__main__":
    main()
