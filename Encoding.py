a = 'AJEET'#initializing a string
d = b'AJEET'#intializing a byte object

b = a.encode("ASCII")#using eencode to encode a string using ASCII mapping

if(d==b):#checking if a is converted to byte or not
    print("Encoding is Successful")
else:
    print("Encoding is not Successful")
