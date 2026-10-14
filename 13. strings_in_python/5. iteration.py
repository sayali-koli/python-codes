# text = "programming"

# n = len(text)
# for i in range(0, n):
#     print(text[i])


text = "programming"
n = len(text)
total = 0
for i in range(0, n):
    if text[i] == "o" or text[i] == "O":
        total += 1
print(total)


# for char in text:
#     print(char)


# for ind, ch in enumerate(text):
#     print(f"index : {ind} and char : {ch}")
