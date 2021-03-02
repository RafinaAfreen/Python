import re

#patterns = ['term1','term2']

text = 'this is a strimg with term1, not the other!'

#for pattern in patterns:
#    print("I'm Searching for: "+pattern)

#    if re.search(pattern,text):
#        print("MATCH!")
#    else:
#        print("no Match!")

match = re.search('term1',text)

print(match.start())


split_term = '@'

email = 'user@gmail.com'

print(re.split(split_term,email))

#match
print(re.findall('match','test phrase match in match middle'))


def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

#test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sdddddd'
test_phrase = 'This is a string! but is has puntuation. How can we remove it  123  #hashtag?'

#[[A-Z]+]
#[r'\d+']
#[r'\D+']
#[r'\s+']
#[r'\S+']
#[r'\w+']
#[r'\W+']
test_patterns = ['[^!.?]+']


multi_re_find(test_patterns,test_phrase)
