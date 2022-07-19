#c opy the text and replace the ans then restart if erro
from tqdm import tqdm
from pwn import *
import string

data = [];
ws = remote("mercury.picoctf.net", 2431);
def test(t):
    ws.recvuntil("encrypted:")
    ws.sendline(t);
    ws.recvline()
    ws.recvline()
    return int(ws.recvline().decode())

length = 48;
charBase = string.ascii_letters + string.digits + "_}";
ans = "picoCTF{sheriff_you_solved";

for i in tqdm(range(50),ascii=True,desc="\n" + ans):
    for c in tqdm(charBase):
        if test(ans+c)==length:
            ans+=c;
            print(ans);
            break;
