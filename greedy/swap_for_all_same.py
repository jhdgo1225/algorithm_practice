s = input()
new = ''
compare = s[0]

for i in s:
    if i != compare:
        new += compare
        compare = i
new += compare

cnt = new.count

print(min(cnt("0"), cnt("1")))