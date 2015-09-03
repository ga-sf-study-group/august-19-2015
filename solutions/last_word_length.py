import sys
from string import rfind

if __name__ == '__main__':
  if len(sys.argv) > 1:
    s = sys.argv[1]
    s = s.strip(' ')
    if len(s) == 0:
      print 'no word in string'
    elif rfind(s, ' ') == -1:
      print 'length of last word: ', len(s)
    else:
      print 'length of last word: ', len(s) - rfind(s, ' ') - 1
  else:
    print 'input a word'
    print 'run the program as:'
    print 'python last_word_length.py " xyz abcdefg "'
