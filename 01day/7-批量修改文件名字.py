#请输入要的文件假的名字
#取出文件夹所以文件 os.listdir("")
#遍历修改文件的名字 os.rename(old,new)
import os
dir_name = input("请输入文件夹名字")
files = os.listdir(dir_name)
#os.chdir(dir_name)
for file in files:
	old_file_name = dir_name+'/'+file
	new_file_name = dir_name+'/'+"精品"+file
	#os.rename(file,"精品"+file)
	os.rename(old_file_name,new_file_name)


