#!/usr/bin/env python3
"""
lorem-2.py
Generates nonsense Hungarian sentences with proper articles (névelők) and prints the requested number of sentences.
"""
import random
import sys

PROMPT = "Hány mondatot akarsz? "

# Larger database of Hungarian words with simple rules for definite/indefinite articles
NOUNS = [
    'bagoly', 'paprika', 'erdő', 'papucs', 'villanykacsa', 'tornádó', 'kürtőskalács',
    'torta', 'fánk', 'hidrogén', 'buborék', 'szendvics', 'tükör', 'szék', 'asztal',
    'bicikli', 'macska', 'kutya', 'telefon', 'szivárvány', 'cseresznye', 'szőlő',
    'zebra', 'póló', 'kalap', 'cipő', 'szomszéd', 'robogó', 'porszívó'
]
ADJECTIVES = [
    'kockás', 'sárga', 'csintalan', 'békés', 'zajos', 'szomorú', 'vidám', 'ragacsos',
    'cukros', 'fűszeres', 'parázsló', 'színes', 'hűvös', 'furfangos', 'szagos'
]
VERBS = [
    'fut', 'táncol', 'suttog', 'sikolyog', 'szalad', 'pattog', 'kecmereg', 'szendereg',
    'forog', 'dübörög', 'mormol', 'csoszog', 'teker', 'gurul'
]
OBJECTS = [
    'szandál', 'kalap', 'kürtő', 'csoki', 'szendvics', 'paplan', 'csiga', 'hinta',
    'lámpa', 'sátor', 'festék', 'ceruza'
]
ADVERBS = [
    'furcsán', 'halkan', 'vidáman', 'búsan', 'pörgősen', 'lassan', 'hangosan', 'büszkén'
]
PLACES = [
    'szigeten', 'erdőben', 'utcán', 'piacon', 'múzeumban', 'kávéházban', 'szobában'
]

# Simple heuristic for Hungarian indefinite article: use 'a' or 'az' before vowel-starting words
VOWELS = set('aáeéiíoóöőuúüű')

def article_for(word):
    if not word:
        return 'a'
    return 'az' if word[0].lower() in VOWELS else 'a'

TEMPLATE_PATTERNS = [
    # Each pattern will produce a grammatically simple Hungarian phrase with articles
    # e.g., "A kockás bagoly fut az erdőben."
    ['ADJ', 'NOUN', 'VERB', 'PLACE'],
    ['NOUN', 'VERB', 'OBJECT'],
    ['ADJ', 'NOUN', 'ADV', 'VERB', 'OBJECT', 'PLACE'],
    ['NOUN', 'ADV', 'VERB', 'OBJECT'],
    ['ADJ', 'NOUN', 'VERB']
]


def make_sentence():
    pattern = random.choice(TEMPLATE_PATTERNS)
    parts = []
    for token in pattern:
        if token == 'NOUN':
            w = random.choice(NOUNS)
            parts.append((article_for(w), w))
        elif token == 'ADJ':
            adj = random.choice(ADJECTIVES)
            # attach adjective to next noun later
            parts.append(('ADJ', adj))
        elif token == 'VERB':
            parts.append(('VERB', random.choice(VERBS)))
        elif token == 'OBJECT':
            obj = random.choice(OBJECTS)
            parts.append((article_for(obj), obj))
        elif token == 'ADV':
            parts.append(('ADV', random.choice(ADVERBS)))
        elif token == 'PLACE':
            parts.append(('PLACE', random.choice(PLACES)))

    # Build sentence with basic Hungarian order and spacing
    output_words = []
    i = 0
    while i < len(parts):
        p = parts[i]
        if p[0] == 'ADJ':
            # Next should be a noun (article before adjective+noun)
            adj = p[1]
            if i + 1 < len(parts) and isinstance(parts[i+1], tuple) and parts[i+1][0] in ('a', 'az'):
                art, noun = parts[i+1]
                output_words.append(art)
                output_words.append(adj)
                output_words.append(noun)
                i += 2
            else:
                # fallback: just adjective
                output_words.append(adj)
        elif p[0] in ('a', 'az'):
            art, noun = p
            output_words.append(art)
            output_words.append(noun)
        elif p[0] == 'VERB':
            output_words.append(p[1])
        elif p[0] == 'ADV':
            output_words.append(p[1])
        elif p[0] == 'PLACE':
            output_words.append(p[1])
        else:
            # unknown structure, append raw
            output_words.append(str(p))
        i += 1

    if not output_words:
        sentence = 'Semmi.'
    else:
        # Capitalize first word and end with period
        output_words[0] = output_words[0].capitalize()
        sentence = ' '.join(output_words) + '.'
    return sentence


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
