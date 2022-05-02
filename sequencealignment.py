"""
This library will contain methods for alignment of protein
and DNA sequences. These will be utilized in another file.
"""

#Makes a matrix
def buildmatrix(height, width):
	matrix = []
	line = []
	[line.append(0) for i in range(width)]
	[matrix.append(line) for i in range(height)]
	return matrix

#Returns array of fragments from a string given
#an array of index tuple pairs
def extractsequences(sequence, indeces):
	seqarray = []
	[seqarray.append(sequence[start:end]) for start, end in indeces]
	return seqarray

#Function Tester
def functiontester():
	newmatrix = buildmatrix(10, 10)
	print('A 10 X 10 matrix:', newmatrix)
	samplesequenceone = 'ATGCTGATGTCATTTTGGTCTATCGTG'
	samplespliceindeces = [(0, 6), (10, 15)]
	print('Sample Sequence:', samplesequenceone)
	print('What the splices should be:', samplesequenceone[0:6], samplesequenceone[10:15])
	samplesplices = extractsequences(samplesequenceone, samplespliceindeces)
	print('What the function extracted:', samplesplices)

functiontester()
