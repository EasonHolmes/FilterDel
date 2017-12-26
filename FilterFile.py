# coding=utf-8
import os
import shutil
import FilterParameter


def currentDirFile(dir):
    fileNames = os.listdir(dir)
    for fn in fileNames:
        fullFileName = os.path.join(dir, fn)
        if not os.path.isdir(fullFileName):
            delFile(fullFileName)
        else:
            currentDirFile(fullFileName)


def delFile(filePath):
    # 分隔后缀名
    formatName = os.path.splitext(filePath)[1]
    if not FilterParameter.formatFiles.__contains__(formatName) and \
                    filePath.split('/')[-1] != '.DS_Store':  # mac下每个文件夹都有个.DS_Store隐藏文件这个不需要动
        # print(filePath)
        shutil.move(filePath, '/Users/cuiyang/.Trash')# 移动到废纸篓


currentDirFile(FilterParameter.dir)
