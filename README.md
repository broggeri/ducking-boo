1ST SESSION
===========
STORY 1
-------
you will have databases such as "apples - 1€" (description, price)
you will get inputs such as "apples"
if you do find it in your database, you have to print the total cents of cumulated products
example: "apples" ==> output: 100
then "apples" again, ==> output: 200
if you have bananas - 1.5€ in your database, and as input, you get "bananas" (in addition to the previous commands), then output ==> 350
then if you have "oranges" and it doesn't appear in your database, you have output ==> 350
cause oranges = 0
your database is for now:
- apples - 1€
- bananas - 1.5€
- cherries 0.75€

(!) accept only one word per line

STORY 2
-------
every two cherries you save 20 cents

STORY 3
-------
if you allow CSV formats each line starts over (example: apples, apples ==> 200 NEW LINE: apples, bananas ==> 250)

2ND SESSION
============
STORY 4
-------
- Erase story 2: every two cherries, we save 30 cents instead of 20 cents
- Erase story 3: no CSV supported
- bananas: every 2 bananas, 1 discount (2nd is free)
- each line doesn't start over


STORY 5
-------
- two cherries --> 20 cents discounts (ONLY if all story 4 is done, otherwise, stay on story 4 expectations on cherries)
- internationalization: support several words for the same product
- example: 
  - pommes = apples
  - mele = apples

==> ENDS AT 4.35pm

3RD SESSION
============
STORY 6
-------
- different local discounts
  - 3 pommes = 2€ (price)
  - 2 mele = 1.5 € (price)


STORY 7
-------
- ADDING NEW DISCOUNT RULES TO PREVIOUS ONES
  - 2 mele = 1€ (price)
  - 4 apples: -1€ (discount)
  - 5 fruits (whatever which ones): -2€ (discount)
  - Do CSV, no restart when creating a new line
  - (!) discounts are applied IN ADDITION to previous ones (examples: 2 cherries + 2 bananas + 1 apple = 75 + 75 -30 +150 (+150 - 150) -200
  - prices are > 0
