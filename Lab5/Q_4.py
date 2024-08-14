it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
length_it_companies = len(it_companies)
it_companies.add('Twitter')
it_companies.update(['Snapchat', 'TikTok', 'LinkedIn'])
it_companies.remove('Oracle')
print(f"Length of it_companies set: {length_it_companies}")
print(f"it_companies after adding 'Twitter': {it_companies}")
try:
    it_companies.remove('Oracle')  
except KeyError:
    print("'Oracle' was already removed using remove(), trying discard now...")
it_companies.discard('Oracle')  
print(f"it_companies after removing 'Oracle' again: {it_companies}")
