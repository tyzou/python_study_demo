# 文件操作示例
# 写入文件
with open("D:\\AAA\\aaa.txt","w",encoding="utf-8") as file:
    file.write("这是第1行\n")
    file.write("这是第2行\n")
    file.write("这是第3行\n")
print("文件写入完成")

print("\n 读取整个文件：")
with open("D:\\AAA\\aaa.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)

with open("D:\\AAA\\aaa.txt","r",encoding="utf-8") as file:
    for line in file:
        # strip() 去除行尾的换行符
        print(line.strip())
# 追加内容
with open("D:\\AAA\\aaa.txt","a",encoding="utf-8") as file:
    file.write("这是第4行\n")
    file.write("这是第5行\n")
    file.write("这是第6行\n")
print("文件追加完成")

print("\n\n追加后读取的文件：")
with open("D:\\AAA\\aaa.txt","r",encoding="utf-8") as file:
    print(file.read())

