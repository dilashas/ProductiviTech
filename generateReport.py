from os import path, mkdir, listdir, system, name
import shutil
import time


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def sleep():
    num = 0
    for i in range(0, 10):
        if i % 3 == 0:
            num = 1
        else:
            num = num + 1
        clear()
        print("Processing".ljust(10 + num, "."))
        time.sleep(1)
    clear()
    print("Report Successfully Generated")
    time.sleep(2)


sleep()
desktop = path.normpath(path.expanduser("~/Desktop/Botathon"))
files = listdir(desktop)
latest_video_file = files[len(files) - 1]
if latest_video_file.split(".")[1] != "xlsx":
    file_name_only = latest_video_file.split('.')[0]
    new_folder_name = f"{file_name_only} Report"
    if path.exists(desktop + "/" + new_folder_name):
        shutil.rmtree(desktop + "/" + new_folder_name, ignore_errors=True)
    mkdir(desktop + "/" + new_folder_name)
    folder_path = path.normpath(path.expanduser(f"~/Desktop/Botathon/{new_folder_name}"))
    file_to_save_name = file_name_only + "_report.xlsx"

    curr_dir = path.normpath(path.expanduser("~/PycharmProjects/FaceAndEyeDetection"))
    shutil.copy(f"{curr_dir}/student_report.xlsx", folder_path + f"/{file_to_save_name}")
