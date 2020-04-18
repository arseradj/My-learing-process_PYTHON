# print(letters)
# print(len(letters))
# letters5 = letters*5
# print(letters5)
# # numbers = list(range(8))
# # print(numbers)

# for x in range(8):
#     x += 1
#     for count in range(x):
#         count += 1
#         print(x, count)

# numbers = list(range(8))
# numbers = numbers[::-1]
# # first, *others, last = numbers
# print(numbers)
# # print(others)


# letters = ["a", "b", "c"]
# # *others, last = letters
# # print(last)
# # print(others)
# # for index, letter in enumerate(letters):
# #     print(index, letter)

# # # add
# # letters.append("d")
# # letters.insert(0, "_")

# # # Remove
# # letters.pop(0)
# # letters.remove("b")
# # del letters[0:1]
# # letters.clear()
# # print(letters)
# letters.append("d")
# letters.insert(0, "d")
# print(letters.index("a"))
# print(letters.count("d"))
# print(letters)
# letters.remove("d")
# print(letters)
# for letter in letters:
#     if "d" == letter:
#         letters.remove("d")
# # print(letters)
# numbers = [3, 51, 2, 8, 6]
# # numbers.sort()
# numbers.sort(reverse=True)
# print(numbers)
# print(numbers)
# # print(numbers[::-1])
# items = [("P1", 324,4,3), ("P2", 48444,5,2), ("P3", 757,6,1), ]
# letters = [("a", 1), ("b", 2), ("c", 3), ]


# # def soit(name):
# #     return name[1]


# # items.sort(key=soit, reverse=True)
# # items.sort(key=lambda price: price[1])
# # print(items)

# # price = []
# # for value in items:
# #     price.append(value[1])
# f = list(map(lambda value: value[3], items))
# # ff = list(map(lambda e: e[1], letters))
# print(f)
# #print([*f, *ff])
# # x = f
# # for value in ff:
# #     x.append(value)
# print(x)
# letters2 = ["adasdafa", "basfafaf", "casfasfasf"]
# letters2.append("ddsdfsdf")
# print(letters2)
# letters2.sort(key=lambda value: value[0])
# print(letters2)
# print(list(map(lambda e: e[1], letters2)))

# numbers = list(range(8))
# print(numbers)

# li = []
# for x in numbers:
#     y = x + 1
#     li.append(y)
# print(li)

# items = [("P1", 324, 4, 3), ("P2", 48444, 5, 2), ("P3", 757, 6, 1), ]
# first, second, third = items
# # print(first)
# # x1, x2, x3, x4 = first
# # x5, x6, x7, x8 = second
# # x9, x10, x11, x12 = third
# # f = []
# # f.append(x1)
# # f.append(x5)
# # f.append(x9)
# # print(f)

# # print(list(map(lambda tuple: tuple[0], items)))

# y = []
# for x in first:
#     y.append(x)
# print(y)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # first, *rest = list(map(lambda mat: mat[1], matrix))
# # print(first)
# # matrix[0][1] = 20
# # print(matrix)
# print(list(map(lambda mat: mat[1], matrix)))

# prices = [("a", 200), ("b", 50), ("c", 300), ]

# filtered = []
# for items in prices:
#     if items[1] >= 200:
#         filtered.append(items)
# print(filtered)

# print(list(filter(lambda item: item[1] >= 200, prices)))
# print([item for item in prices if item[1] >= 200 and item[0] != "a"])
# prices.sort(key=lambda item: item[1])
# print(prices)
# x = sorted(prices, key=lambda item: item[1])
# print(x)
# print(prices)

# list1 = [1, 2, 3]
# list2 = ["mive", "sabzi", "goosht"]
# # print([item for item in (list1, list2)])
# # print([item for items in (list1, list2) for item in items])
# # print(list(zip(list1, list2)))
# # new = []
# # for item in list1:
# #     new.append(item)
# # for par in list2:
# #     new.append(par)
# # print(new)

# print([*list1, *list2])
# f, *u = list1
# print(u)

# from pprint import pprint
# sentence = "This is a common interview question"

# freq = {}
# for char in sentence:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# print(freq)

# freq = {char: sentence.count(char) for char in sentence}
# freq2 = freq.items()
# # freq3 = list(freq2)
# # freq3.sort(key=lambda kv: kv[1], reverse=True)
# # pprint(freq3[0:2])
# pprint(sorted(freq2, key=lambda char: char[1], reverse=True)[0])

#

# letters2 = ["adasdafa", "basfafaf", "casfasfasf"]
# a, b, c = letters2
# print(list(zip(a, b, c)))
# y = []
# for item in letters2:
#     for i in item:
#         y.append(i)
# print(y)
# # print(list(filter(lambda g: g[0] != "a", y)))
# print([item for item in y if item != "a" and item != "f"])
# # while True:
#     if "a" in y:
#         y.remove("a")
#     elif "f" in y:
#         y.remove("f")
#     else:
#         break
# print(y)

# letters2 = ["adasdafa", "basfafaf", "casfasfasf"]
# del y[1:5]
# print(y)
# items = [("P1", 324, 4, 3), ("P2", 48444, 5, 2), ("P3", 757, 6, 1), ]


# def ff(item):
#     return item[1]


# items.sort(key=ff)
# # c = ff(items)
# # print(items)

# items = [("P1", 324, 4, 3), ("P2", 48444, 5, 2), ("P3", 757, 6, 1), ]

# # for item in letters2:
# # print(list(map(lambda i: i[1], items)))

# letters2 = ["adasdafa", "basfafaf", "casfasfasf"]
# for item in letters2:
#     x = ([i for i in item])
#     # print(x)
#     while True:
#         if "a" in x:
#             x.remove("a")
#         else:
#             break
#     # print(x)
#     strin = ""
#     for i in x:
#         strin += i
#     x = ([strin])
#     strin.join(strin)
#     print(strin)

# x = 10
# y = 11
# z = x
# x = y
# y = z
# print(f"now, X: {x} and y: {y}")

# letters2 = ["adasdafa", "basfafaf", "casfasfasf"]
# y = []
# for item in letters2:
#     for letter in item:
#         y.append(letter)
# print([x for x in y if x != "a"])

# for item in letters2:
#     x = [letter for letter in item if letter != "a"]
#     z = []
#     for line in x:
#         z.append(line)
#     print(z)


x = dict(g=3, f=4, s=1, c=2)
print(x)
# x["f"]
# print(x["f"])
