import codecs
def asciiToHex(message):
    encoded = ""
    for char in message:
        encoded += hex(ord(char))[2:]
    return encoded
def hexToAscii(encoded):
    message = ""
    for i in range(0,len(encoded),2):
        character = encoded[i:i+2]
        message += chr(int('0x'+character,16))
    return message

def asciiToBase64(message):
    '''
    b1: chuyển ascii sang binary
    b2: tách 6 bytes binary trên , chuyển sang hex
    b3: dò trong charset sẽ thành 1 kí tự mới
    b4: cộng kí tự mới vào chuỗi encoded
    '''
    charset="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    encoded = ""
    sizeOfmessage = len(message)
    hexOfmessage = int(asciiToHex(message),16)
    # binaryOfmessage = format(hexOfmessage,"0>"+str(sizeOfmessage*8)+"b")
    binaryOfmessage = str(bin(hexOfmessage)[2:].zfill(sizeOfmessage*8))
    while(len(binaryOfmessage)%6):
        binaryOfmessage += '0'
    for i in range(0,len(binaryOfmessage),6):
        encoded += charset[int(binaryOfmessage[i:i+6],2)]
    return encoded

def hex2base64(hexString):
    return codecs.encode((codecs.decode(hexString,'hex')),'base64').decode()

print(hex2base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))

# print (stringToHex('tuan'))
# print (hexToString('7475616e'))
# hexnum = 1234
# print (hexnum)
# print(format(hexnum,"0>40b"))
# print(bin(hexnum)[2:].zfill(40))
# asciiToBase64('tuan')
# print(asciiToBase64(hexToAscii('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')))
# print(asciiToHex('1c0111001f010100061a024b53535009181c'))
# print(hexToAscii('61'))