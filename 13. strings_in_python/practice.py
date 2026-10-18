# user = input("enter name : ")
# n = len(user)
# print(user[0])
# print(user[-1])
# print(f"total length : {n}")


# user = input("enter string : ")
# print(user[::-1])
# print(user)


# user = input("enter a sentance : ")
# n = len(user)
# total = 0
# for char in user:
#     if char in "aeiouAEIOU":
#         total += 1
# print(total)


# user = input("enter name : ")
# print(user[::2])


# email = input("enter a email : ")

# if email.count("@") == 1 and email.count(".") == 1:
#     print("valid email")
# else:
#     print("invalid email")


# def to_remove(phone_num: str):
#     phone_num = phone_num.replace("-", "")
#     phone_num = phone_num.replace("+91", "")
#     print(phone_num)


# user = input("enter a number : ")
# to_remove(user)


# def count_vowel_words(sentance: str):
#     vowels = "aeiouAEIOU"
#     count = 0
#     words = sentance.split()
#     for word in words:
#         if word[0] in vowels:
#             count += 1
#     return count


# sentance = "sayali is grate coder and excellent engineer"
# print(count_vowel_words(sentance))


# name_input = "sayali,sujal,manish,anuj,teja"
# words = name_input.split(",")
# print("|".join(words))


# user = input("enter film name with .docx or .pdf only : ")

# if user.endswith(".txt") or user.endswith(".docx") or user.endswith(".pdf"):
#     print("valid film")
# else:
#     print("invalid film")


# username = input("enter username :  ")
# new_word = username.strip()
# if new_word[0].isdigit():
#     print("Invalid")
# else:
#     print("valid")


# paragrap = input("enter paragrap :  ")
# words = paragrap.split()
# print(set(words))


# def is_palindrome(text):
#     text = text.lower().replace(" ", "")
#     return text == text[::-1]


# user = input("enter word : ")
# ans = is_palindrome(user)
# print(ans)


# def word_length(sentance):
#     sentance = sentance.split()
#     n = len(sentance)
#     result = []
#     for value in sentance:
#         result.append(f"{value} : {len(value)}")
#     return " ".join(result)


# user = input("enter word : ")
# ans = word_length(user)
# print(ans)


# text = "python is fun"
# new_list = text.split()
# new_list = new_list[::-1]
# print(new_list)
# ans = " ".join(new_list)
# print(ans)


def is_captilize(sentance):
    new_list = []
    sentance = sentance.split()
    for word in sentance:
        if len(word) >= 3:
            new_list.append(word.title())
        else:
            new_list.append(word)

    return " ".join(new_list)


user = input("enter sentance : ")
ans = is_captilize(user)
print(ans)
