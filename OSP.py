import os
from os.path import join, getsize
import time
import datetime


class file_path():

    """ T O  C A L L

          Step1. Create an object like this--> file_path_1=file_path("Drive>User/Desktop/folder/file")

          Step2. Call your object like this--> try:
                                                  file_path_1.is_real_file()
                                               except:
                                                  print("file path does not exist)

          Final Note: If you would like to add more os functions visit     https://docs.python.org/3/library/os.path.html#os 
                                                       (Source repository) https://github.com/python/cpython/blob/3.11/Lib/ntpath.py
                                                                       
    """                                                                                            
    def __init__(self, path):
        self.path=path
    
    def is_real_file_path(self):
        is_this_a_real_file_path=os.path.exists(self.path)             #Is this a real file path?
        return is_this_a_real_file_path

    def is_real_file(self):
        is_file_True_or_False=os.path.isfile(self.path)                #Is this a real file?
        return is_file_True_or_False

    def norm_path(self):
        norm_path=os.path.normpath(self.path)                          #normal path    -->  Drive>User\Desktop\Folder\File
        return norm_path

    def formatted_path(self):
        formatted_path = self.path.replace("\\","/")                   #Formatted path -->  Drive>User/Desktop/Folder/File
        return formatted_path

    def split_path(self):
        split_path=os.path.split(self.path)                            #File Name    or    End of Path Name
        return split_path

    def split_drive(self):
        split_drive=os.path.splitdrive(self.path)                      #Drive used  like  C:
        return split_drive

    def file_type(self):
        file_type=os.path.splitext(self.path)                          # Get a file's type   .txt   .py     .jpg    ect
        return file_type

    def dir_name(self):
        dir_name=os.path.dirname(self.path)                            # Get the current working directory
        return dir_name

    def last_modification_time(self):
        time_of_last_modification_to_path=os.path.getctime(self.path)
        dt_object = datetime.datetime.fromtimestamp(time_of_last_modification_to_path)           #Last time path was modified
        formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_time

    def last_access_time(self):
        last_time_this_file_was_accessed=os.path.getatime(self.path)
        dt_object2 = datetime.datetime.fromtimestamp(last_time_this_file_was_accessed)          #Last time a file was accessed
        formatted_time2 = dt_object2.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_time2
    
    def last_time_changed(self):
        changed_time=os.path.getctime(new_path)
        dt_object3 = datetime.datetime.fromtimestamp(changed_time)                              #Last time the file was changed.
        formatted_time3 = dt_object3.strftime('%Y-%m-%d %H:%M:%S')
        return(formatted_time3)


cwd= os.getcwd()
print("My current working directory is            :",cwd)
paths=["Desktop","data.txt"]
print("Paths inserted into (",cwd,") are : ", paths)
new_path=os.path.join(cwd, *paths)


print("Filepath created. OR insert filepath here-->:",new_path)

file_path_1=file_path(new_path)
print("Our new filepath object was created and is\nnow callable with file_path_1!\n" )

print("Checking if the file path is real          : ",file_path_1.is_real_file_path())


print("Checking if the file is real               : ",file_path_1.is_real_file())

print("The normal path                            :",file_path_1.norm_path())

print("The formatted path                         :",file_path_1.formatted_path())

file_name_or_end_of_path= file_path_1.split_path()
print("The file or end of path                    : ",file_name_or_end_of_path[1])

drive=(file_path_1.split_drive())
print("The path's/file's drive is                 : ",drive[0])

type_of_file=file_path_1.file_type()
print("The file type is a                         : ",type_of_file[1]," file.")

print("The current working directory is           : ",file_path_1.dir_name())
print("The last time someone moved this file was  : ",file_path_1.last_modification_time())
print("The last time thie file as accessed was    : ", file_path_1.last_access_time())
print("This file was changed on                   : ",file_path_1.last_time_changed())