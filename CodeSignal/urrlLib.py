import urllib.request, urllib.parse,urllib.error
counts=dict()
fhand = urllib.request.urlopen('https://www.uniprot.org/uniprot/Q02388.txt')
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
    print(counts)