#!/bin/end python
#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      r.bauvin
#
# Created:     04/11/2014
# Copyright:   (c) r.bauvin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import json

def input_fruit():
    try:
        return raw_input()
    except EOFError, e:
        return None

def main():
    db = json.load(open('database.json'))
    synonyms = json.load(open('synonyms.json'))

    cart = dict();

    total = 0
    fruitNr = 0

    while True:
        fruit = input_fruit()

        if fruit is None:
            break

        fruitNr += 1

        if fruit not in db and fruit in synonyms:
            fruit = synonyms[fruit]
        if fruit in cart:
            cart[fruit] += 1
        else:
            cart[fruit] = 0

        if fruit in db:
            total += int(db[fruit][cart[fruit] % len(db[fruit])]*100)
            if fruitNr % 5 == 0:
                total -= 200
        print total

if __name__ == '__main__':
    main()
