import shutil
import os
import csv


def create_dir(dir_name: str) -> str:
    '''This function create dir where we must copy our dataset'''
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    return dir_name


def create_copy_dataset(base: str, dir_copy: str, annotation_name: str) -> None:
    '''This function copy our dataset in another directory and create csv file with 2 parameters: filename and file's class name'''
    create_dir(dir_copy)
    for dataset_item in os.listdir(os.path.join(base, "dataset")):
        files_list = os.listdir(os.path.join(base, "dataset", dataset_item))
        for file_name in files_list:
            shutil.copy(os.path.join(os.path.join(base, "dataset", dataset_item),
                        file_name), os.path.join(dir_copy, f"{dataset_item}_{file_name}"))
        with open(os.path.join(dir_copy, annotation_name), mode="a", encoding="UTF-16", newline='') as file:
            file_writer = csv.writer(file, delimiter=",")
            file_writer.writerow(['file name', 'Dataset name'])
            for file_name in files_list:
                file_writer.writerow(
                    [f"{dataset_item}_{file_name}", dataset_item])


def runtask2(base: str, dir_copy: str, annotation_name: str) -> None:
    ''' This function call previous to run it in main'''
    create_copy_dataset(base, dir_copy, annotation_name)
