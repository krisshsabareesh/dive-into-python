`NODEJS`

var codes = {}
function frequency(str) {

  freqs = {}
  console.log('Running...Frequency')
  console.log('Frequency')
  for( ch in str) {
    if(freqs[str[ch]] == undefined) {
      freqs[str[ch]] = 1
    }
    else {
      freqs[str[ch]]++
    }
  }
  console.log(freqs)
  return(freqs)
}


function sortFreq(freqs) {
  tuples = []
  for( key in freqs) { 
    tuples.push([freqs[key], key])
  }
  console.log(tuples.sort()) 
  t = tuples.sort()
  return(t)
}


function buildTree(tuples) {

  while(tuples.length > 1) {
    leastTwo  = tuples.slice(0,2)             
    theRest = tuples.slice(2,tuples.length)
    combFreq = leastTwo[0][0] + leastTwo[1][0]
    tuples = theRest + [(combFreq, leastTwo)]
    tuples.sort()
  }
  console.log(tuples)
  return(tuples[0])
}


function trimTree(tree) {

  p = tree[1]
  if( typeof p == typeof 'str') 
    return p
  else
    return(trimTree(p[0]), trimTree(p[1]))
}


function assignCodes(node, pat) {

  if( typeof node == 'str') { 
    codes[node] = pat
  }
  else { 
    assignCodes(node[0], pat+"0")
    assignCodes(node[1],pat+"1") 
  }
}


function encode (str) {

    var output = ""
    for(ch in str) 
      output += codes[ch]
    return(output)
}


function decode (tree, str) {

    var output = ""
    var p = tree
    for( bit in str) {
        if( bit == '0') 
          p = p[0]     
        else
          p = p[1]     
        if( typeof p == 'str') {
            output += p              
            p = tree  
        }
    }               
    return(output)
}



var freqs = frequency('aaababacadaeef');
console.log('After Frequency : ' + freqs)
var tuples = sortFreq(freqs)
console.log('After sorting Frequency : ' + tuples)
var tree = buildTree(tuples)
console.log('After Building Tree : ' + tree)
var ttree = trimTree(tree)
