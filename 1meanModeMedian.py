a = input("Enter the values for mean mode median : ")
b = a.split(" ")

mean = 0
mode = 0
median = 0

for i in b:
    mean += int(i)
mean /=len(b)


d={}

for i in b:
    if(i not in d.keys()):
        d[i]=1
    else:
        d[i]+=1

print(max(d))

# mode
        

print(mean)