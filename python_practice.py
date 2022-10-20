counties = ("Arapahoe","Denver","Jefferson")

if 'Arapahoe'in counties and 'El Paso' not in counties:
    print('only Arapahoe is in the list of counties')
else:
    print('Arapahoe is in the list of counties and El Paso is not in the list of counties')

for county in counties:
    print (county)

for i in range(len(counties)):
    print (counties[i])