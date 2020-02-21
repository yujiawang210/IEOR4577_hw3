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
            'expected': ['who', 'is', 'most', 'excited', 'to', 'see', 'at', 'the', 'everybody', 'and', 'honestly', 'same']
        }
    ]

    index = [
        {
            'case': ['who', 'is', 'most', 'excited', 'to', 'see', 'at', 'the', 'everybody', 'and', 'honestly', 'same'],
            'expected': [128, 33, 450, 871, 17, 164, 67, 14, 898, 27, 1648, 451]
        }
    ]

    padding = [
        {
            'case': [128, 33, 450, 871, 17, 164, 67, 14, 898, 27, 1648, 451],
            'expected': [128, 33, 450, 871, 17, 164, 67, 14, 898, 27, 1648, 451, 0, 0, 0, 0, 0, 0, 0, 0]
        }
        ]

    preprocessing = [
        {
            'case': 'RT @BBMAs: Who is most excited to see at the #BBMAs? Everybody. And honestly same. https://t.co/76BFUvHIlD',
            'expected': [128, 33, 450, 871, 17, 164, 67, 14, 898, 27, 1648, 451, 0, 0, 0, 0, 0, 0, 0, 0]
        }
    ]
