# -*- coding: utf-8 -*-
# @Time    : 2/8/2022 4:54 PM
# @Author  : taltalasuka
# @File    : sub.py
# @Software: PyCharm

import os
import tkinter as tk
from tkinter import filedialog

class sub:

    def getFileDir(self):
        root = tk.Tk()
        root.withdraw()

        # pathFolder = filedialog.askdirectory()
        pathFile = filedialog.askopenfilename()

        # print(pathFolder)
        print(pathFile)

        return pathFile

    def clearBlankLine(self, path):
        file1 = open(path, 'r', encoding = 'utf-8')
        pathDesktop = os.path.join(os.path.expanduser('~'),"Desktop")
        file2 = open(pathDesktop + "/2.txt", 'w', encoding = 'utf-8')
        try:
            for line in file1.readlines():
                if (line != "\n"):
                    newLine = line.replace("\n", "\\N" + "\n")
                    file2.write(newLine)

        except PermissionError:
            print(PermissionError)
        finally:
            file1.close()
            file2.close()


if __name__ == '__main__':
    start = sub()
    path = start.getFileDir()
    start.clearBlankLine(path)