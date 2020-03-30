#day1(table of number)

n=int(input("Enter the number of multiplication table"))
for i in range(1,11):
    print(n ,"*" ,i, "=",n*i)

#day2(star pattern)

for i in range(1,11):
	for j in range(i+1):
		print("*",end="")
	print()

            #day3(chef)
# print("required water 200ml")
print("we have 300ml cup and 500ml cup")
bigcup=500
smallcup=300
requiredcup=bigcup-smallcup
print("now we have",requiredcup,"ml water" )


        #3DAY4(hot dog)

i=0
for j in range(8,401,8):
    i=i+1
print("required packet",i)



