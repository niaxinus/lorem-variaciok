#!/usr/bin/env python3
"""
lorem-1.py
Generates nonsense Hungarian sentences starting with "lorem ipsum:" and prints the requested number of sentences.
"""
import random
import sys

PROMPT = "Hány mondatot akarsz? "

# Larger database of Hungarian words (nouns, verbs, adjectives, adverbs, objects)
WORDS = {
    'nouns': [
        'bagoly', 'paprika', 'erdő', 'papucs', 'villanykacsa', 'torna', 'kürtőskalács',
        'torta', 'fánk', 'hidrogén', 'buborék', 'szendvics', 'tükör', 'szék', 'asztal',
        'bicikli', 'macska', 'kutya', 'telefon', 'szivárvány', 'cseresznye', 'szőlő',
        'zebra', 'póló', 'kalap', 'cipő', 'szomszéd', 'robogó', 'porszívó'
    ],
    'adjectives': [
        'kockás', 'sárga', 'csintalan', 'békés', 'zajos', 'szomorú', 'vidám', 'ragacsos',
        'cukros', 'fűszeres', 'parázsló', 'színes', 'hűvös', 'furfangos', 'szagos'
    ],
    'verbs': [
        'fut', 'táncol', 'suttog', 'sikolyog', 'szalad', 'pattog', 'kecmereg', 'szendereg',
        'forog', 'kecseg', 'dübörög', 'mormol', 'csoszog', 'teker', 'gurul'
    ],
    'objects': [
        'szandál', 'kalap', 'kürtő', 'csoki', 'szendvics', 'paplan', 'csiga', 'hinta',
        'lámpa', 'sátor', 'hobbi', 'festék', 'ceruza'
    ],
    'adverbs': [
        'furcsán', 'halkan', 'vidáman', 'búsan', 'pörgősen', 'lassan', 'hangosan', 'büszkén'
    ],
    'places': [
        'szigeten', 'erdőben', 'utcán', 'piacon', 'múzeumban', 'kávéházban', 'oltárral', 'szobában'
    ]
}

TEMPLATE_PATTERNS = [
    # Patterns are lists of parts of speech to join
    ['adjectives', 'nouns', 'verbs', 'places'],
    ['nouns', 'verbs', 'objects'],
    ['adjectives', 'nouns', 'adverbs', 'verbs', 'objects', 'places'],
    ['nouns', 'adverbs', 'verbs', 'objects'],
    ['adjectives', 'nouns', 'verbs'],
]

def make_sentence():
    pattern = random.choice(TEMPLATE_PATTERNS)
    words = []
    for part in pattern:
        pool = WORDS.get(part, [])
        if not pool:
            continue
        w = random.choice(pool)
        words.append(w)
    # Capitalize first word and end with a period
    if not words:
        return 'lorem ipsum: ...'
    words[0] = words[0].capitalize()
    sentence = ' '.join(words) + '.'
    return 'lorem ipsum: ' + sentence.lower()


def main():
    try:
        n = input(PROMPT)
    except (EOFError, KeyboardInterrupt):
        print('\nKilépés.')
        sys.exit(0)
    n = n.strip()
    if not n:
        count = 1
    else:
        try:
            count = int(n)
            if count < 1:
                count = 1
        except ValueError:
            count = 1

    for _ in range(count):
        print(make_sentence())

if __name__ == '__main__':
    main()
