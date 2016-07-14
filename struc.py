from struct import *

packed_data=pack('iiffc',3,4,5.44,6.5,'c')
print(packed_data)			#convert in bytes

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('c'))
print(calcsize('iiffc'))

unpacked_data=unpack('iiffc',packed_data)
print(unpacked_data)

