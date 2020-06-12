# fixed xor
def fixedXor(string1, string2):
    xorString = ""
    for i in range(0,len(string1)):
        xorString += hex((int(string1[i],16)^int(string2[i],16)))[2:]
    return xorString

print(fixedXor('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965'))
