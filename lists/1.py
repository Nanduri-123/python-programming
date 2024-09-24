heros=['spider man','thor','hulk','iron man','captain america']
print("Total length of list : ",len(heros))

heros.append('black panther')
print("List after adding 'black panther' :", heros)

heros.remove('black panther')
heros.insert(heros.index('hulk') + 1, 'black panther')
print("List after adding 'black panther' after 'hulk':", heros)

heros[1:3] = ['doctor strange']
print("List after replacing 'thor' and 'hulk':", heros)

heros.sort()
print("Sorted List:", heros)

