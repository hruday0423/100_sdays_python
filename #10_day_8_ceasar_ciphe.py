

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','q','x','y','z']


def ceasar_cipher(text,shift,encode_or_decode):
    output=''

    if encode_or_decode== 'decode':
        shift*=-1
    for letter in text:
        shifted_position = alphabet.index(letter) + shift
        shifted_position%= len(alphabet)
        output+=alphabet[shifted_position]
    print(f'the {encode_or_decode}d text is: {output}')
run_code= True
while run_code:
    user_text = input('enter the text: ').lower()
    step_no = int(input('enter no of steps to move: '))
    direction = input('enter encode or decode: ').lower()
    ceasar_cipher(text=user_text,shift=step_no,encode_or_decode=direction)
    run = input('enter yes to continue, no to exit:\n')
    if run=='no':
        run_code=False






