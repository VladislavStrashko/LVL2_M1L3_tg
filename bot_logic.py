import random

def gen_pass(pass_length):
    
    elements = "+-/*!&$#?=@<>123456789"

    return ''.join(random.choice(elements) for _ in range(pass_length))

def coin_flip():

    return random.choice(['Орел', 'Решка'])

def random_emoji():

    emojis = ['😀',  '🎉', '🚀', '🔥', '👍']

    return random.choice(emojis)
