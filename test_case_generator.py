"""
Tweets Preprocessor Test Case Generator
"""

class TestCasesGenerator:
	"""define test case generator class"""

	clean = [
		{
			'case':'RT @BBMAs: Who is most excited to see at the #BBMAs? Everybody. And honestly same. https://t.co/76BFUvHIlD',
			'expected':'who is most excited to see at the  everybody and honestly same'
		}
	]


	tokenize = [
		{
			'case': 'who is  most excited to see at the  everybody and honestly same',
			'expected': ['who', 'is', 'most', 'excited', 'to', 'see', 'at',
			 'the', 'everybody', 'and', 'honestly', 'same']
		}
	]

	index = [
		{
			'case': ['who', 'is', 'most', 'excited', 'to', 'see', 
			'at', 'the', 'everybody', 'and', 'honestly', 'same'],
			'expected': [127, 32, 449, 870, 16, 163, 
			66, 13, 897, 26, 1647, 450]
		}
	]

	padding = [
		{
			'case': [127, 32, 449, 870, 16, 163, 66, 13, 897, 26, 1647, 450],
			'expected': [127, 32, 449, 870, 16, 163, 66, 13, 897, 26, 1647, 450, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		}
		]
