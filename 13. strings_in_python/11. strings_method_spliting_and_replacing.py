# text = "sayali koli is coder"
# print(text.split("a"))
# print(len(text.split()))


# my_list = ["s", "a", "y", "a", "l", "i", "k", "o", "l", "i"]
# print("".join(my_list))
# print(len("".join(my_list)))
# print(type("".join(my_list)))


my_list = ["s", "a", "y", "a", "l", "i", "k", "o", "l", "i", 3.14, 2, 6]
ans = "".join(str(ch) for ch in my_list)
print(ans)
