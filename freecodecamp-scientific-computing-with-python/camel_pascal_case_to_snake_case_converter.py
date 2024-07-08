def convert_to_snake_case(camel_or_pascal_cased_string):
    return ''.join([
        '_' + char.lower() if char.isupper()
        else char
        for char in camel_or_pascal_cased_string
    ]).strip('_')

def main():
    print(convert_to_snake_case('IAmAtomic'))
    print(convert_to_snake_case('myBossIsDummy'))

main()