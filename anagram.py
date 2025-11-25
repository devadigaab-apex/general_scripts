from collections import defaultdict
anagram_map=defaultdict(list)
words =input("Enter words to test for anagram: ").split()

for i in words:
    signature=tuple(sorted(i))
    anagram_map[signature].append(i)

print (list(anagram_map.values()))
