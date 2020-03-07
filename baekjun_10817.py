a,b,c = input().split()
a,b,c = int(a),int(b),int(c)

if a==b and b==c and a==c :
    print(a)
elif a==b and b!=c:
    print(a)
elif a==c and c!=b:
    print(a)
elif b==c and c!=a:
    print(b)
else:
    if a>b and a>c :
        if b>c :
            print(b)
        elif c>b:
            print(c)
        else:
            print(b)

    if b>a and b>c:
        if a>c :
            print(a)
        elif c>a :
            print(c)
        else:
            print(a)

    if c>a and c>b:
        if a>b:
            print(a)
        elif b>a:
            print(b)
        else:
            print(b)