import re, operator
from scipy.stats import mode

class textfile:
  
  def __init__(self, filename):
    self.filein = open("files/" + filename, 'r')
    data = self.filein.read()
    self.words = self._getwords(data)
    self.sortedwords = sorted(self.words.iteritems(), key=operator.itemgetter(1), reverse=True)
    self.averagechar = self._averagelenchar(data)
    self.sentences = map(lambda x: x.split(" "), map(lambda x: x.lstrip().rstrip(), data.split('.')))
    self.averagelength = self._averagelensen(self.sentences)
    self.modesen = self._modesentences(self.sentences)
    self.link = False
    self.partner = None

    #self.filein.close()

  def _getwords(self, filein):
    words = dict()
    for w in re.findall(r"\w+", filein):
      if w in words:
        words[w] += 1
      else:
        words[w] = 1
    return words

  def _averagelenchar(self, filein):
    sentencepiles = ''.join(filein.split()).split('.')
    total = 0
    for senpile in sentencepiles:
      total += len(senpile)
    return total/float(len(sentencepiles))

  def _averagelensen(self, sentencepiles):
    total = 0
    for sentence in sentencepiles:
      total += len(sentence)
    return total/float(len(sentencepiles))

  def _modesentences(self, sentencepiles):
    return tuple(map(lambda x: int(x[0]), mode(map(lambda x: len(x), sentencepiles))))
