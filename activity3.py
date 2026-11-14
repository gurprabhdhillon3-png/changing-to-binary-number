number=int(input("Enter a number: "))
total_bit=int(input("Enter the number of bit positions: "))
for pos in range(total_bit):
    mask=1<<pos
    print(pos)
    print(mask)
chec_pos=int(input("Enter position to check: "))
check_mask=1<<chec_pos
result=number & check_mask
if result!=0:
    print("Bit at position", chec_pos, "is On")
else:
    print("Bit at position", chec_pos, "is OFF")
