 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import numbers
import cryptoModule as cryp


input1 = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"
print(cryp.repeatXor(input1,key))
