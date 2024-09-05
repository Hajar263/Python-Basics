#1_name
import os
print(os.name)


#2_getcwd
import os
cwd = os.getcwd()
print("Current working directory:", cwd)

#3_chdir
import os
def current_path():
	print("Current working directory before")
	print(os.getcwd())
current_path()
os.chdir('c:/Users/E-M-T/PycharmProjects/pythonProject6')
current_path()


#4_listdir
import os
print(os.listdir())

#5_mkdir   && makedirs
import os
os.mkdir('main.py_10')
print(os.listdir())
os.makedirs('main.py_12/sub_dir_1')

# 6_rmdir && removedirs
import os
os.rmdir('main.py_2')
print(os.listdir())
os.removedir("'main.py_3/sub_dir_1'")



#7_rename
import os
os.rename('Pictures','file_1.py')
print(os.listdir())


#8_stat
import os
print(os.stat('PrintHood'))

#9_walk
import os
print(os.walk("C:\Users\E-M-T"))

#10_popen   &&    close
import os
fd = "python.txt"
file = open(fd, 'w')
file.write("This is awesome")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
file = os.popen(fd, 'w')
file.write("This is awesome")




