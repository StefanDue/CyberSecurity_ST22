import operator as op
import binascii
import codecs as ccs


TEXT1 = "44415349535445494E4C414E47455254455854"
CIPHER2 = "F82FFF2EEE32EC3BEE34EE35E639F928EE24FF"
CIPHER1 = "EF3DF835F828EE35E530EA32EC39F928EE24FF"

if __name__ == "__main__":
    # Test what TEXT1 is as plain text
    text1 = bytes.fromhex(TEXT1)
    plaintext1 = text1.decode("ASCII")
    print("Text1: " + plaintext1 + "    (ASCII)")

    # Convert HEX to INT
    text1 = int(TEXT1, base=16)
    cipher1 = int(CIPHER1, base=16)
    cipher2 = int(CIPHER2, base=16)

    # Calculate key with XOR
    key = (op.xor(text1,cipher1))

    # Decrypt cipher 2
    text2 = op.xor(cipher2,key)
    plaintext2 = binascii.unhexlify('%x' % text2)
    print("Text2: " + plaintext2.decode("ASCII") + "    (ASCII)")
    plaintext2_hex = hex(int(text2))[2:]
    print("Cipher2: " + CIPHER2 + "    (HEX)")
    print("Text2  : " + plaintext2_hex + "    (HEX)")

    
    