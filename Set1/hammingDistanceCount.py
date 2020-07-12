import cryptoModule as cryp

string1 = str(input("string 1: "))
string2 = str(input("string 2: "))
distance = cryp.hammingDistanceCount(string1,string2)
print(distance)