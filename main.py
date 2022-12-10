import random
import copy

class Replace:
    def __init__(self, chance=100, choice=()):
        self.chance = chance
        self.choice = choice

    def is_good(self):
        return random.randint(0, 100) <= self.chance

    def any(self):
        return random.choice(self.choice)


REPLACES = {
    ',': Replace(50, [', бля,', ', нахуй,', ', сука,', ', ебать,', ', пидоры,', ', блять,']),
    '.': Replace(33, ['. Вот такой пиздец.', '. Вот такая хрень.', '. Дохуя истина.', '. Ахуеть!']),
    '!': Replace(50, ['! Вот такой пиздец.', '! Вот такая хрень.', '! Дохуя истина.', '. Ахуеть!']),
    '?': Replace(20, ['? Ты ахуел?', '? Рил такой пиздец?']),
    ' ': Replace(15, [', нахуй, ', ', бля, ', ', сука, ', ', пидоры, ', ', eбать, ', ', блять, '])
}


def modify(txt, chances=None):
    if chances is None:
        chances = {}
    repl = copy.deepcopy(REPLACES)
    for s in chances.keys():
        if s in repl:
            repl[s].chance = chances[s]
    res = ''

    for ch in txt:
        if ch in REPLACES and REPLACES[ch].is_good():
            res += REPLACES[ch].any()
        else:
            res += ch

    res = res.replace(',,', ',').replace('  ', ' ').replace('.,', '.')\
             .replace(',.', '.').replace(':,', ':').replace('!,', '!')\
             .replace(',!', '!').replace('?,', '?').replace(',?', '?')

    return res


if __name__ == '__main__':
    text = open('zadacha.txt').read()

    with open('zadacha_proceeed.txt', 'w') as f:
        f.write(modify(text))
