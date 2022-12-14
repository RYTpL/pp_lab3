from typing import Optional
import random
import os
import shutil
from task2 import create_dir
import csv


def get_element(base: str, class_name: str) -> Optional[str]:
    '''This function return us list of names in dataset class'''
    for file_name in os.listdir(os.path.join(base, "dataset", class_name)):
        yield file_name


def create_randomname_file(base: str, annotation_name: str, dir_copy: str) -> None:
    '''This function create the copy of dataset in another directory with names which are random numbers 
    and create csv file with 2 parameters: file name(random number) and class of that file'''
    file_number = list(range(10001))
    random.shuffle(file_number)
    counter = 1
    create_dir(dir_copy)
    for base_class in os.listdir(os.path.join(base, "dataset")):
        for file_name in get_element(base, base_class):
            shutil.copy(os.path.join(os.path.join(base, "dataset", base_class),
                        file_name),  os.path.join(dir_copy, f"{file_number[counter]}.jpg"))

            with open(os.path.join(dir_copy, annotation_name), mode="a", newline='') as file:
                file_writer = csv.writer(file, delimiter=" ")
                file_writer.writerow(['file name', 'Dataset name'])
                file_writer.writerow(
                    [f"{file_number[counter]}.jpg", base_class])
            counter += 1


def runtask3(base: str, dir_copy: str, annotation_name: str) -> None:
    ''' This function call previous to run it in main'''
    create_randomname_file(base, annotation_name, dir_copy)
