
import sys
import hashlib
import time

start_time = time.process_time()
target_hash = 'd54cc1fe76f5186380a0939d2fc1723c44e8a5f7'
rainbow_table = dict()

substitution = {
  'a': '@A',
  'b': '8B',
  'c': 'C',
  'd': 'D',
  'e': '3E',
  'f': 'F',
  'g': '96G',
  'h': 'H',
  'i': '1!I',
  'j': 'J',
  'k': 'K',
  'l': '1L',
  'm': 'M',
  'n': 'N',
  'o': '0O',
  'p': 'P',
  'q': 'Q',
  'r': 'R',
  's': '$5S',
  't': '7T',
  'u': 'U',
  'v': 'V',
  'w': 'W',
  'x': 'X',
  'y': 'Y',
  'z': '2Z'
}

# rainbow_table_file = open('rainbow_table.txt','x')

def try_all_substitutions(str, pos):
  # base case
  if pos == len(str): 
    hash = hashlib.sha1(str.encode()).hexdigest()
    rainbow_table[str] = hash
    # rainbow_table_file.write(str + ', ' + hash + '\n')
    if hash == target_hash:
      print('Original value is', str)
      print('Hash is', hash)    
    return

  try_all_substitutions(str, pos+1)
  if str[pos] in substitution.keys():
    for sub in substitution[str[pos]]:
      try_all_substitutions(str[:pos] + sub + str[pos+1:], pos+1)
  

with open('dictionary.txt') as f:
  entries = [line[:-1] for line in f]
  for entry in entries:
    try_all_substitutions(entry, 0)

print("The size of the rainbow table is {} bytes".format(sys.getsizeof(rainbow_table)))
# rainbow_table_file.close()
print("--- %.2f seconds ---" % (time.process_time() - start_time))