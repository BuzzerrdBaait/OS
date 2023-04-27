import os
import time
import datetime
from os.path import join, getsize

cwd= os.getcwd()
paths=["Desktop","Data.txt"]
new_path=os.path.join(cwd, *paths)

print(new_path,"<---------NEWPATH")
is_this_a_real_file_path=os.path.exists(new_path)
print("Checking to see if this is a real file path (",is_this_a_real_file_path,") <-------------Is this a real file path? If Yes print True, If False Print No.")

is_file_True_or_False=os.path.isfile(new_path)

print("Checking to see if this is a real file or not(",is_file_True_or_False,")<--------------Is the file a a real file? If Yes print True, If False Print No.")


print(new_path,"<--------------------------------NEW PATH")

messed_up_path=cwd+"/Desktop\\Venvs"
norm_path=os.path.normpath(messed_up_path)
print("Norm path = ", norm_path, "from this mess -----> ", messed_up_path)



formatted_path = cwd.replace("\\","/")

print(formatted_path,"<-------IF YOU NEED TO OPEN PATH")


split_path=os.path.split(new_path)


print(split_path,"<-----------SPLIT PATH")

print(os.path.splitdrive(new_path),"<---------SPLIT DRIVE")

example= "foo.bar.exe"
example2= "foo/bar.exe"
print(os.path.splitext(example),"<---------SPLITTEXT using ",example)

print(os.path.splitext(example2),"<---------SPLITTEXT_2 using ", example2)

print(os.path.dirname(new_path),"<------Directory Name of the a file path..",new_path)


time_of_last_modification_to_path=os.path.getmtime(new_path)
dt_object = datetime.datetime.fromtimestamp(time_of_last_modification_to_path)
formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')


print("The last time the path",new_path,"Was modified was ", formatted_time)


last_time_this_file_was_accessed=os.path.getatime(new_path)

dt_object2 = datetime.datetime.fromtimestamp(last_time_this_file_was_accessed)
formatted_time2 = dt_object2.strftime('%Y-%m-%d %H:%M:%S')

print("The last time this file was accessed was.....",formatted_time2)



changed_time=os.path.getctime(new_path)
dt_object3 = datetime.datetime.fromtimestamp(changed_time)
formatted_time3 = dt_object3.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_time3,"<<----time file was changed")
