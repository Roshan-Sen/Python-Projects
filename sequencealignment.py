"""
This library will contain methods for alignment of protein
and DNA sequences. These will be utilized in another file.
"""

#Returns array of fragments from a string given
#an array of index tuple pairs
def extractsequences(sequence, indeces):
	seqarray = []
	[seqarray.append(sequence[start:end]) for start, end in indeces]
	return seqarray

#Builds a matrix with the alignments, commonalities
#are labelled with a 1.
def alignmentmatrix(sequenceone, sequencetwo):
	alignments = []
	for charone in sequenceone:
		line = []
		for chartwo in sequencetwo:
			if chartwo == charone: line.append(1)
			else:                  line.append(0)
		alignments.append(line)
	return alignments

#Function Tester
def functiontester():
	print('Hello')
	samplesequenceone = 'ACGTATAT'
	samplesequencetwo = 'GCTACGT'
	print('Testing alignment between ' + samplesequenceone + ' and ' + samplesequencetwo + '.')
	samplealignmentmatrix = alignmentmatrix(samplesequenceone, samplesequencetwo)
	print('  ', end = ' ')
	for character in samplesequencetwo:
		print(character, end = '  ')
	print()
	
	for i in range(len(samplesequenceone)):
		print(samplesequenceone[i], samplealignmentmatrix[i])

functiontester()
