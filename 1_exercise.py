name = input('Whats your name?')

age = int(input('How old are you?'))

diff = 10 - (age % 10)
tenth = age + diff

print(name, ', in ', diff, ' years, you will be ', tenth, ' years old!')