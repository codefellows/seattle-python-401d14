
def encrypt(plain, key):
    """
    plain is a string on integers
    key = an integer shift
    return: string of shifted integers
    """

    encrypted_pin = ""

    for char in plain:
        num = int(char)

        shifted_num = (num + key) % 10

        encrypted_pin += str(shifted_num)

    return encrypted_pin

def decrypt(encoded, key):
    return encrypt(encoded, -key)



if __name__ == "__main__":

    assert encrypt('12345', 1) == '23456'
    assert encrypt('23456',-1) == '12345'

    assert encrypt('12345',5) == '67890'
    assert encrypt('12345',9) == '01234'
    assert encrypt('12345',21) == '23456'
    assert encrypt('12345',-1) == '01234'


    key = 5
    plain = '12345'


    encrypted = encrypt(plain,key)
    decrypted = decrypt(encrypted, key)
    assert decrypted == plain


    print('#'*20)
    print("All Good")
    print('#'*20)



cat is hungry but the dog is lazy is named Ramona and she says 'slsdfd'
xyd as asdfry asd hdl dls ds dsxt fd rudhd xhsdkl dhd Snx xhdy 'dhxndh'



