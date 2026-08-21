def calculate_marks(maths, english, hindi, computer, history=0):
    print(f"maths={maths}")
    print(f"english={english}")
    print(f"hindi={hindi}")
    print(f"computer={computer}")
    print(f"history={history}")
    total_marks = maths + english + hindi + computer + history
    print(f"the total marks scored{total_marks}")


calculate_marks(english=20, hindi=50, maths=70, computer=40)
