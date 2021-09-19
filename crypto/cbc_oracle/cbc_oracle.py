from pwn import *
from base64 import b64encode, b64decode

target = remote("challs.hackademint.org", 2008)
c = b64decode(b'4Ipgzg64vNPsPRcGcO+MElyU1Uo9sLyUGBE9xpo7yhg=')
print(c)
c1, c2 = c[:16], c[16:]

p2 = bytearray(16)

for i in range(256):
    d = bytearray(c1)
    d[-1] = i
    d += c2
    target.sendline(b64encode(d))
    s = target.recvline()
    if not b'Erreur' in s:
        print(s)
        r = i
    if b'invalide' in s:
        print(str(i) + " /// " + d)

print(r)

p2[-1] = int.from_bytes(xor(b'\x01', bytes([c1[-1]]), bytes([r])), 'little')
print(p2)
   
for k in range(2, 17):
    print(str(k)+':')
    t = bytearray(c1)
    for i in range(1,k):
        t[-i] = int.from_bytes(xor(bytes([k]), bytes([c1[-i]]), bytes([p2[-i]])), 'little')
    for i in range(256):
        d = t[:]
        d[-k] = i
        d += c2
        target.sendline(b64encode(d))
        s = target.recvline()
        if not b'Erreur' in s:
            print(s)
            r = i
        if b'invalide' in s:
            print(len(t))
            print()



    print(r)
    p2[-k] = int.from_bytes(xor(bytes([k]), bytes([c1[-k]]), bytes([r])), 'little')
    print(p2)

