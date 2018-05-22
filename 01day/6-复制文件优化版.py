#打开原来的文件
#把原来的文件内容读出来
#新建一个文件
#把内容写进去
#关闭

#1.txt 5G - 4G
file_name = input("请输入文件的名字要带后缀名")
old_file = open(file_name,'r')

#1.txt--->1复制.txt
#1.txt.txt

position = file_name.rfind(".")
new_file_name = file_name[0:position]+"备份"+file_name[position:]
new_file = open(new_file_name,'w')

while True:
	content = old_file.read(1024)
	
	if len(content) == 0:
		break

	new_file.write(content)

old_file.close()
new_file.close()

