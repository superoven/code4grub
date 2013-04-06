from textfile import textfile
import operator

def compscore(text1, text2):
  diffmode = text1.modesen[0] - text2.modesen[0]
  difflenchar = text1.averagechar - text2.averagechar
  difflensen = text1.averagelength - text2.averagelength

  modescore = -10*diffmode*diffmode + 1000
  lenscore = -2*difflenchar*difflenchar + 2000
  lensenscore = -20*difflensen*difflensen + 2000
  commonscore = compdict(text1, text2)

  return commonscore + modescore + lenscore + lensenscore

def compdict(text1, text2):
  wordst1 = set(map(lambda x: x[0], text1.sortedwords))
  wordst2 = set(map(lambda x: x[0], text2.sortedwords))
  temptotal = 0
  for word in (wordst1 & wordst2):
    diffword = text1.words[word] - text1.words[word]
    temptotal += -1*diffword*diffword + 10
  return (len(wordst1 & wordst2) * 50) + temptotal

files = []
for i in xrange(30):
  files.append(textfile(str(i+1) + ".txt"))

pairs = []

for j in xrange(30):
  pairlist = []
  try:
    for i in xrange(30):
      if i != j and not files[i].link and not files[j].link:
        pairlist.append(tuple([compscore(files[i], files[j]), i, j]))
    maxpair = max(pairlist, key=operator.itemgetter(0))
    files[maxpair[1]].link = True
    files[maxpair[2]].link = True
    pairs.append(maxpair[1:])
  except:
    continue

for pair in pairs:
  print "%d.txt, %d.txt" % (pair[0], pair[1])
