
# Generate odd numbers util x
x=int(input("Enter a number: "))
output=[2*i+1 for i in range(x)]
print(",".join(map(str,output)))