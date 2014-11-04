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
    return [fruit.strip() for fruit in raw_input().split(',')]

def main():
    db = json.load(open('database.json'))

    total = 0
    while True:
        for fruit in input_fruit():
            if fruit in db:
                total += db[fruit]*100
        print total

if __name__ == '__main__':
    main()
