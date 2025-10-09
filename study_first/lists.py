fruits = ["apple", "banana", "cherry"]
print(f"\n原始列表：{fruits}")

fruits.append("葡萄")
print(f"\n添加元素后的列表：{fruits}")


fruits.insert(1, "橘子")
print(f"\n插入元素后的列表：{fruits}")

fruits.remove("cherry")
print(f"\n删除元素后的列表：{fruits}")

fruits.pop(2)
print(f"\n删除下标{2}元素后的列表：{fruits}")


popped = fruits.pop()
print(f"\n删除最后一个元素后的列表：{fruits}")
print(f"\n被删除的元素：{popped}")

joinStr = ",".join(fruits)
print(f"\n转成字符串，并用逗号分隔后的字符串：{joinStr}")

numbers = [1, 2, 3, 4, 5]
print(f"\n原始列表：{numbers}")


print(f"\n前3个元素:{numbers[:3]}")
print(f"\n第1到第3个元素:{numbers[0:3]}")
print(f"\n最后三个元素：{numbers[-3:]}")
print(f"\n前面两个元素：{numbers[:2]}")
print(f"\n隔两个取一个：{numbers[::2]}")



numbers.reverse()
print(f"\n反转后的列表：{numbers}")