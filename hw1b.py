

# כמה חברים הגיעו לדני
friends = int(input("enter the number of friends who came to danny house: "))

# כמה משולשי פיצה הוזמנו
slices = int(input("the number of pizza slices orderd: "))

# חישוב מספר משולשים פר חבר slice per friend
spf = slices // friends
# חישוב משולשים אקסטרה
leftover = slices % friends


print(f"every guest got = {spf} slices of pizza")
print(f"there are = {leftover} slices left")

