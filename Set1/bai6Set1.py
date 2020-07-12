import cryptoModule as cryp

message = "lethanhtuandeptrai"
key = "deo"
decr = cryp.repeatXor(message,key)[2:]
print(decr)
for i in range(2,40):
    print()