import os
from pathlib import Path
from tkinter import messagebox
import subprocess
import shutil
def clear_cache():
    files = 0
    size = 0
    tmpsiz = 0
    dirs = ["C:\\Windows\\Temp",f"{Path.home()}\\AppData\\Local\\Temp","C:\\Windows\\Prefetch"]
    try:
        for dir in dirs:
            folder = dir
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        tmpsiz = os.path.getsize(file_path)
                        os.unlink(file_path)
                        size += tmpsiz
                        files+=1
                        print(size,files,file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        pass
                        # files+=1
                except Exception as e:
                    print(f'Failed to delete {file_path}.')
                    pass
    except PermissionError:
        print("Mising access")
        explor = messagebox.askquestion("",f'Mising access. Open folders?')
        print(explor)
        if explor=="yes":
            for dir in dirs:
                subprocess.Popen(f'explorer "{dir}"')
    # print(f"Deleted {files} files permanently")
    if (size>(1024*1024*1024)):
        messagebox.showinfo("",f"Deleted {files} files permanently. Total size {int(size/(1024*1024*1024))} GB Aprox")
        print("a")
    elif(size>(1024*1024)):
        messagebox.showinfo("",f"Deleted {files} files permanently. Total size {int(size/(1024*1024))} MB Aprox")
        print("b")
    elif(size>(1024)):
        messagebox.showinfo("",f"Deleted {files} files permanently. Total size {int(size/(1024))} KB Aprox")
        print("c")

clear_cache()