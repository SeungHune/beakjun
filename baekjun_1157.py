import collections

text = input().upper()
counter = collections.Counter(text)
# print(counter)
# print(counter.values())
# print(counter.keys())
# print(counter.most_common(2)[1])
# print(counter.most_common(2)[1][1])

if len(text) == 1:
    print(text)

else:
    if counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
        print("?")
    else:
        print(counter.most_common(1)[0][0])
