msg = 'This is first message'
print(msg)

msg2 = 'This is second message'
print(msg2)
msg2 = 'This is modified message'
print(msg2)

personalMessage = 'Eric'
print('Hello ' + personalMessage + ', would you like to learn some Python today?')
print('Hello {}, would you like to learn some Python today?'.format(personalMessage))
print("Hello %s, would you like to learn some Python today?" % personalMessage)

personName = 'Muhammad azeem'
print('This is upper case:',personName.upper())
print('This is lower case:',personName.lower())
print('This is title case:',personName.title())

print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')

famous_person = 'Albert Einstein'
message = famous_person + ' once said, “A person who never made a mistake never tried anything new.”'
print(message)


strippingNames = '   \tAlbert\nEinstein   '
print(strippingNames)
print(strippingNames.lstrip())
print(strippingNames.rstrip())
print(strippingNames.strip())


x = 5
y = 10
z = 15
print(x + y + z)


a = 'a'
b = 'b'
print(a,b)
c = b
b = a
a = c
print(a,b)

a = 'a'
b = 'b'
print(a,b)
a, b = b, a
print(a,b)


color = 'White'
print(color)
color2 = 'White'
print(color2)


pet_name = 'Buddy'
pet_name = 'Max'
print(pet_name)


variableName = "Sunshine"
print(variableName)
# print(Variableame)

score = 100
print(score)
score = 101
print(score)


city = 'Lahore'
print(city)

text = "python programming"
print(text.title())

text = 'This is MIXED cases string'
print(text.lower())

text = 'This is MIXED cases string'
print(text.upper())

temperature = 25
print("The current temperature is [%d] degrees." % temperature)

poem = '''Poem first line
poem second line
poem third line'''
print(poem)