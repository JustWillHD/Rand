import random
def getclues():
  clues=["?","?","?","?","?"]
  return clues
  
def getword():
  words=["plate","angel","eight","thorn","phone","music"]
  secret_word=random.choice(words)
  return secret_word

def getstickmen(x):
  stickmen = [
"\
|------\n\
|    O\n\
| ---|---\n\
|   / \\ \n\
|  /   \\ \n\
|_____",

"\
|------\n\
|    O \n\
| ---|---\n\
|\n\
|\n\
|_____",

"\
|------\n\
|    O\n\
|\n\
|\n\
|\n\
|_____",

"\
|------\n\
|\n\
|\n\
|\n\
|\n\
|_____",

"\
|\n\
|\n\
|\n\
|\n\
|_____",

"\n\n\n\n______",

"\n\n\n\n\n",
] 
  return stickmen[x] 
  
def update_clue(guessed_letter,secret_word,clues):
  index=0
  while index<len(secret_word):
    if guessed_letter==secret_word[index]:  
      clues[index]=guessed_letter
    index=index+1  

def check_clues_left(clues):
  ct=0
  while ct<len(clues):
    if clues.count("?")!=0:
      return True
    else:
      return False  
