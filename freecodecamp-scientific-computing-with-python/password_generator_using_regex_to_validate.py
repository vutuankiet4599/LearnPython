from string import ascii_letters, digits, punctuation
from re import findall
from secrets import choice

def password_generator(length=8, nums_count=1, special_chars_count=1, uppercase_count=1, lowercase_count=1):
    all_characters = ascii_letters + digits + punctuation

    while True:
        password = ''
        for _ in range(length):
            password += choice(all_characters)
        
        constraints = [
            (nums_count, r'[0-9]'),
            (uppercase_count, r'[A-Z]'),
            (lowercase_count, r'[a-z]'),
            (special_chars_count, fr'[{punctuation}]')
        ]

        if all(
            constraint <= len(findall(pattern, password))
            for constraint, pattern in constraints
        ):
            return password

if __name__ == '__main__':
    print(f'Generated password: {password_generator()}')