#!/usr/bin/env python3

"""Сортировщик скриншотов т программы NVSIP

Этот скрипт рекурсивно перебирает каталоги в каталоге, где он находится,
и переносит оттуда картинки в заданный каталог.

Пример запуска:
    SortPhoto.py
"""

import os
import datetime
import sys

def modification_time (path_to_file):
    t = os.path.getmtime(path_to_file)
    return datetime.datetime.fromtimestamp(t).time()

RootDir = sys.argv[0][0:sys.argv[0].rfind("/")] #Получаем рабочий каталог
OutputDir = "/storage/emulated/0/video"
#OutputDir = "out"
print("Обрабатываем каталог: " + RootDir)
filelist = os.listdir(RootDir)

if not os.path.exists(OutputDir):
    os.makedirs(OutputDir)
for i in filelist:
    if i == "out":
        continue
    if i == ".nomedia":
        continue
    if i.find(".py") > -1:
        continue
    fullfile = os.path.join (RootDir,i)
    if os.path.isdir(fullfile):#Если каталог с фотками
        dataList = i.split("-")
        god = dataList[0]
        mes = dataList[1]
        den = dataList[2]
        FilePrefix = god + mes + den
        #print(modification_date(fullfile))
        list_file_in_dir = os.listdir(fullfile)
        if len(list_file_in_dir) == 0:
            os.rmdir(fullfile)
        else:
            for k in list_file_in_dir:
                os.rename(os.path.join (fullfile,k), os.path.join (OutputDir, god+mes+den+"-"+k))
            os.rmdir(fullfile)
    else:
        nameList = i.split("-")
        den = nameList[1]
        strtime = modification_time(fullfile)
        
        strtime = str(strtime).replace(':', '-')
        os.rename(fullfile, os.path.join (OutputDir, den + "-" + strtime + ".jpg"))
print ("Обработка завершена!")
input()
sys.exit(0)