# function that Generate Authorization/verification code for user-account.

def verification_code():
    import random
    import string

    characters = string.digits
    code = ''.join(random.choice(characters) for i in range(5))
    print (f'verification_code is : {code}')


verification_code()
