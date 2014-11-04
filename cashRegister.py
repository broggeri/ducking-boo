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
    return raw_input()

def main():
    db = json.load(open('database.json'))
    synonyms = json.load(open('synonyms.json'))

    cart = dict();

    total = 0
    while True:
        fruit = input_fruit()
        if fruit in synonyms:
            fruit = synonyms[fruit]
        if fruit in cart:
            cart[fruit] += 1
        else:
            cart[fruit] = 0

        if fruit in db:
            total += db[fruit][cart[fruit] % len(db[fruit])]*100
        print total

if __name__ == '__main__':
    main()
