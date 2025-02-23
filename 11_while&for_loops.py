#while loops
x = 0
while (x<=5):
    print(x)
    x = x+1
#for loop
for x in range(5,10):
    print(x)

days = ["sun","mon", "tue","wed","thu","fri","sat", "sun"]
for d in days:
    if(d=="fri"):break #loop stops
    # if (d=="fri"):continue #stips d
    print(d)