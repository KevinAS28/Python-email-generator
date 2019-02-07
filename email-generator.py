#!/usr/bin/python3
#by Kevin A.S
#try my another code: email-filter.py (to filter the ouput. COOL!)
import random, string
import sys
abjad = list(string.ascii_letters) + list(string.digits)	
#for i in list(string.punctuation)):
# abjad += i
kata = ""
smtp = ["gmail", "yahoo", "hotmail", "protonmail", "kevin"]
if True:
 for a in  range(50):
  for c in range(random.randint(4, 9)):
   kata += random.choice(abjad)
  if random.randint(0, 1):
   kata += "@"
  if random.randint(0, 1):
   kata += random.choice(smtp)
  else:
   for d in range(4):
    kata += random.choice(abjad)
  if random.randint(0, 1):
   kata += "."
  if random.randint(0, 1):
   kata += "com"
  else:
   for i in range(3):
    kata += random.choice(abjad)
  kata += "\n" 

print(kata)

