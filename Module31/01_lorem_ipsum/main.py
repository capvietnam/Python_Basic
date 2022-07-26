from re import findall

text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""

symbol_4_patern = r'\b\w{4}\b'

full_search = findall(symbol_4_patern, text)
print(full_search)
