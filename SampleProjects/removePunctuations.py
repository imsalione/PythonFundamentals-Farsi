punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

no_punc = ""

for char in my_str:
    if char not in punctuations:
        no_punc = no_punc + char
        
print(no_punc)