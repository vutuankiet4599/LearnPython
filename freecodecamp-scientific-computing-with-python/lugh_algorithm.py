def verify_card_number(card_number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    even_digits = card_number_reversed[1::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    return (sum_of_odd_digits + sum_of_even_digits) % 10 == 0

def main():
    card_number = '4111-1112-4432-1223'
    card_translation_table = str.maketrans({'-': '', ' ': ''})
    card_translated = card_number.translate(card_translation_table)
    
    if verify_card_number(card_translated):
        print('VALID!')
    else:
        print('INVALID!')

main()