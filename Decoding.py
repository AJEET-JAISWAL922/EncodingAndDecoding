a = 'AJEET'#initializing a string
d = b'AJEET'#intializing a byte object

b = d.decode("ASCII")#using eencode to encode a string using ASCII mapping

if(a==b):#checking if a is converted to byte or not
    print("Decoding is Successful")
else:
    print("Decoding is not Successful")

g = True
print(~g)