li = [123,453,65,96,230,786,108]
print("First 3 items: ")
print(li[:3])

a = int(len(li)/2)
#print(a)
print("Middle 3 items: ")
print(li[(a-1):(a+2)])

print("last 3 items: ")
print(li[-3:])

cp_li = li[:]
cp_li.append('happy')
print(cp_li)