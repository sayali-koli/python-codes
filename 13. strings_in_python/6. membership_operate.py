text = "programming"

# print("p" in text)
# print("z" in text)
# print("prog" in text)
# print("amms" is not text)

# total = 0
# for char in text:
#     if (
#         char == "a"
#         or char == "e"
#         or char == "i"
#         or char == "o"
#         or char == "u"
#         or char == "A"
#         or char == "E"
#         or char == "I"
#         or char == "O"
#         or char == "U"
#     ):
#         total += 1
#         print(char)
# print(total)


# ALTERNATE METHODE

total = 0
for ch in text:
    if ch in "aeiouAEIOU":
        total += 1
print(total)
