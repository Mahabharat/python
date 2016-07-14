from struct import *
packed_data=pack('iif',4,6,9.98)
print(packed_data)

print(unpack('iif',b'\x04\x00\x00\x00\x06\x00\x00\x00\x14\xae\x1fA'))
