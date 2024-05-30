import random

def gen_pass(pass_length):
    elements = "abcdefghijklmnñopqrstuvwxyz+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):    
        password += random.choice(elements)

    return password
def flip_coin():
    coin = ["cara","crus"]
    flip = random.randint(0, 1)

    return coin[flip]
