# with open("new.txt", "w") as f:
#     f.write("hellow world!\n")
#     f.write("sayali learning python\n")


lines = [
    "sayali koli\n",
    "my father name is jagdish koli\n",
    "my father is police\n",
    "my mother name is shubhangi\n",
    "i have two sibling",
]
with open("new.txt", "w") as f:
    f.writelines(lines)
