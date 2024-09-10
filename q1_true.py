# MAKE ALL OF THIS CONDITION TRUE

a = 1
b = 1
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 1
b = 2
c = 1
d = 2
if a + b and c + d:
    print(f"was True for {1} {2} {1} {2}")
else:
    print(f"was False for {1} {2} {1} {2}")

a = 2
b = 1
c = 2
d = 1
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 2
b = 1
c = 2
d = 1
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 1
c = 1
d = 2
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 2
c = 3
d = 4
if True and a + b + c + d:
    print(f"was True for {1} {2} {3} {4}")
else:
    print(f"was False for {1} {2} {3} {4}")

a = 1
b = 2
if 1 != 2:
    print(f"was True for {1} {2}")
else:
    print(f"was False for {1} {2}")

a = 0
b = 1
c = 1
if a != b and a <= c or a <= b or True:
    print(f"was True for {0} {1} {1}")
else:
    print(f"was False for {0} {1} {1}")

a = 1
b = 2
c = 3
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 0
b = 0
c = 2
d = 2
if a % b == 0 and c % d == 1:
    print(f"was True for {0} {0} {2} {2}")
else:
    print(f"was False for {0} {0} {2} {2}")