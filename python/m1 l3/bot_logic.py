import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
def flip_coin():
    flip = random.randint(1, 2)
    if flip == 1:
        return "HEADS"
    else:
        return "TAILS"