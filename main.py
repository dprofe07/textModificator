import random

replaces = {
    ',': {'chance': (1, 2, [1]), 'choice': [', бля,', ', нахуй,', ', сука,', ', ебать,', ', пидоры,', ', блять,']},
    '.': {'chance': (1, 3, [1]), 'choice': ['. Вот такой пиздец.', '. Вот такая хрень.', '. Дохуя истина.', '. Ахуеть!']},
    '!': {'chance': (1, 4, [1, 2]), 'choice': ['! Вот такой пиздец.', '! Вот такая хрень.', '! Дохуя истина.', '. Ахуеть!']},
    '?': {'chance': [1, 5, [1]], 'choice': ['? Ты ахуел?', '? Рил такой пиздец?']},
    ' ': {'chance': [1, 10, [1]], 'choice': [', нахуй, ', ', бля, ', ', сука, ', ', пидоры, ', ', eбать, ', ', блять, ']}
}


def modify(txt):
    res = ''

    for ch in txt:
        if ch in replaces and random.randint(*replaces[ch]['chance'][:2]) in replaces[ch]['chance'][2]:
            res += random.choice(replaces[ch]['choice'])
        else:
            res += ch

    res = res.replace(',,', ',').replace('  ', ' ').replace('.,', '.')\
             .replace(',.', '.').replace(':,', ':').replace('!,', '!')\
             .replace(',!', '!').replace('?,', '?').replace(',?', '?')

    return res


text = open('zadacha.txt').read()

with open('zadacha_proceeed.txt', 'w') as f:
    f.write(modify(text))
