# RSA
is one of the first public-key cryptosystems and is widely used for secure data transmission.

————By Wikipedia

# Usage
### encode or decode the file (run.py)
```
python3 run.py -f 32 README.md rm.encode.md rm.decode.md
```
next printing
```
{ 4168463629687917583 3704611002826026679 12940768536243160463 }
$ py: Encrypted file =>
$ py.RSA: Save as to: rm.encode.md
$ py: Decrypted file =>
$ py.RSA: Save as to: rm.decode.md
```
> RSA OBJ: { public_key, private_key, modulus}
> <br>(#but in fact it isn't)
### resolve string or string array
```
python3 run.py -t Life is short, you need Python
```

# todo
暂时这样吧，能使(本来吧只是想写个给区块链数据加密的玩具...)

# Tip
> 没试过究竟能防多大强度的破解，生产环境请一定要用128位以上，放心很快

如果有什么好建议及时联系哦.
