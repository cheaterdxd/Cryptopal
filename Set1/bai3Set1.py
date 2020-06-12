# single byte xor
# import bai1Set1
import binascii
import codecs

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

# for i in range(256):
#     print(i)
#     sa = single_byte_xor('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736',hex(i)[2:])
    # print(sa)
    # print(bai1Set1.hexToAscii(sa))
    # print(binascii.unhexlify(sa)) # 1 cách để convert hex sang char
# print(codecs.decode('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736','hex'))
# print(single_byte_xor_ver2('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736',61))
