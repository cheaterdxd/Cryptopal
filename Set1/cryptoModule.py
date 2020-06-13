 #!/usr/bin/python
 # -*- coding: utf-8 -*-
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

def paddingBytes(plain,len):
    hexString = b1.asciiToHex(plain)
    return hexString.rjust(len-len(hexString),"00")

def fixedXorAsciiString(string1, string2):
    hexString1 = asciiToHex(string1)
    hexString2 = asciiToHex(string2)
    return fixedXorHexString(hexString1,hexString2)

def fixedXorHexString(string1, string2):
    return hex(int(string1,16)^int(string2,16))

def single_byte_xor(hexString, singleHexChar):
    hexXorString = ""
    for c in range(0, len(hexString),2):
        hexXorString += hex(int(singleHexChar,16)^int(hexString[c:c+2],16))[2:]
    return hexXorString

def single_byte_xor_ver2(hexString,single_byte_xor):
    # assert (len(hexString)%2 == 1)
    byteString = binascii.unhexlify(hexString)
    output = b""
    for byte in byteString:
        output += bytes([byte ^ single_byte_xor])
    return output

def paddingBytes(plain,lenOfOutput):
    hexString = asciiToHex(plain)
    return hexString.rjust(lenOfOutput*2,"0")

def xorUnfixedString(string1,string2):
    if(len(string1) > len(string2)):
        string2 = paddingBytes(string2,len(string1))
        string1 = asciiToHex(string1)
    else:
        string1 = paddingBytes(string1,len(string2))
        string2 = asciiToHex(string2)
    return fixedXorHexString(string1,string2)

def generateKey(key,outLen):
    return (round(outLen/len(key)+1)*key)[:outLen]

def repeatXor(plain,key):
    #padding the key
    key= generateKey(key,len(plain))
    return fixedXorAsciiString(plain,key)