# Generate odd Numbers until x

x=int(input("Enter a Number: "))
count=x//2+x%2
output=[2*i+1 for i in range(count)]
print(", ".join(map(str,output)))