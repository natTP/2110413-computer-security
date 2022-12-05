text = "PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE."
 
char_freq = dict()

for c in text: 
  if c not in ' .':
    if c in  char_freq.keys():
      char_freq[c] += 1
    else: 
      char_freq[c] = 1

for char in char_freq.items():
  print(char[0], char[1])