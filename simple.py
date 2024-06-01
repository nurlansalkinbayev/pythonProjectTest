import re
import random

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa 

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
567-473*2344

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start A sentence and then bring it to an end'

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)
# Создание списка чисел из заданного интервала с указанным количеством
deck = list(range(1000, 9999))
hand = random.sample(deck, k=28)
# Сумма чисел в списке
hand_sum = sum(hand)
print(hand)
print(hand_sum)
