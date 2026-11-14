number=int(input("Enter a number: "))
position=0
if number<=0:
    print("Please enter a positive number.")
else:
    print("Binary number: ", bin(number)[2:])
    while(number & 1)==0:
        number=number>>1
        position +=1
    print("First set bit position: ", position)
