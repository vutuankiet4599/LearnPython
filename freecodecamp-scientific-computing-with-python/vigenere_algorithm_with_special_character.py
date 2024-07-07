alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY'
special_characters = '!@#$%^&*()-_=+[]{}:;"\'<>,. ?/\\'

custom_key = 'mykey'

def convert_string_to_integer(text):
    return sum(ord(char) for char in text)

def algorithm(message, key, direction=1):
    if not key.isalpha():
        return ''
    
    key_index = 0
    final_message = ''
    offset_special_characters = convert_string_to_integer(custom_key)

    for char in message:
        if char in special_characters:
            index = special_characters.index(char)
            new_index = (index + offset_special_characters*direction) % len(special_characters)
            final_message += special_characters[new_index]
        elif not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message


def encrypt(message, key):
    return algorithm(message, key)

def decrypt(message, key):
    return algorithm(message, key, -1)


encryption = encrypt('Hello world!#', custom_key)
decryption = decrypt(encryption, custom_key)

print(f'Encryption: {encryption}')
print(f'Decryption: {decryption}')