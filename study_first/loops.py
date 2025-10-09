print("for 循环示例：")
for i in range(5):
    print(f"当前循环：{i}")

print("\r\nwhile循环示例")
count = 0
while count < 5:
    print(f"当前循环：{count}")
    count += 1

print("\n遍历列表：")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(fruit, end='  ')

print("\n\nbreak示例: ")
for i in range(10):
    if i == 5:
        break
    print(i)

print("\ncontinue示例: ")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)