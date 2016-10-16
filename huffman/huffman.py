
#!Python2
##Huffman coding --- Data Compression

codes={}


def frequency(str) :                 
  """##########Calc ch freq"""
  freqs = {}
  for ch in str : 
    freqs[ch] = freqs.get(ch,0) + 1
  return freqs

def sort(freqs) :                     
  """#########Sort Freqs"""
  letters = freqs.keys()
  tuples = []
  for let in letters : 
    tuples.append((freqs[let], let))
  tuples.sort()
  return tuples

def buildTree(tuples) :                
  """########Build Tree"""
  while len(tuples) > 1:
    leastTwo  = tuple(tuples[0:2])             
    theRest = tuples[2:]
    combFreq = leastTwo[0][0] + leastTwo[1][0]
    tuples = theRest + [(combFreq, leastTwo)]
    tuples.sort()
  return tuples[0]

def trimTree(tree) : 
  """########Trim the tuples tree created using buildTree to get a nested char tree"""
  p = tree[1]
  if type(p) == type("") :
    return p
  else:
    return(trimTree(p[0]), trimTree(p[1]))

def assignCodes(node, pat = '') : 
  """According to the latest tree in trim, build using trimTree, assign codes to chars"""
  global codes
  if type(node) == type("") :
    codes[node] = pat
  else : 
    assignCodes(node[0], pat+"0") #Do left branch
    assignCodes(node[1],pat+"1") #Do right branch

def encode (str) :
    global codes
    output = ""
    for ch in str : output += codes[ch]
    return output


def decode (tree, str) :
    output = ""
    p = tree
    for bit in str :
        if bit == '0' : p = p[0]     # Head up the left branch
        else          : p = p[1]     # or up the right branch
        if type(p) == type("") :
            output += p              # found a character. Add to output
            p = tree                 # and restart for next character
    return output


print('String is -> \'aahavhvaa\'')
tree = trimTree(buildTree(sort(frequency('aahavhvaa'))))
assignCodes(tree)
print(codes)
print(decode(tree, encode('aahavhvaa')))
