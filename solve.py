import subprocess

def HEX(hex1,hex2):

    bytes1 = [hex1[i:i+2] for i in range(0, len(hex1), 2)]
    bytes2 = [hex2[i:i+2] for i in range(0, len(hex2), 2)]
    xor_bytes = [format(int(b1, 16) ^ int(b2, 16), '02X') for b1, b2 in zip(bytes1, bytes2)]
    return ''.join(xor_bytes)

def check(iv):
    for i in range(256):

        iv = iv_base1 + f"{i:02x}" + iv_base2

        cmd = ["./oracle", iv, cipher]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            return iv
        else: 
            return 0

def check(iv):
    cmd = ["./oracle", iv, cipher]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode


cipher = "8B2B9DCD0A6633A612E415CE64B42CF1"
iv_origin = "CA1DB62557DDD1AD98953B7C8EB43F85"
iv_base2 = ""
D_crypt = ""
plain = ""

for j in range(0,15):

    iv_base1 = "00" * (15-j)

    for i in range(256):

        iv = iv_base1 + f"{i:02x}" + iv_base2

        if check(iv) == 0:
            iv_solve = iv[30-2*j:32]
            k = j+1
            tmp = f"{k:02x}"*k
            D_crypt = HEX(iv_solve,tmp)
            
            k += 1
            tmp = f"{k:02x}"*(k-1)
            iv_base2 = HEX(D_crypt,tmp)
            break
        else:
            continue

plain_hex = HEX("FF",iv_origin[0:2]) + HEX(D_crypt,iv_origin[2:32])
plaindata = bytes.fromhex(plain_hex) 
plaintext = plaindata.decode('ascii',errors='ignore')
print(plaintext)