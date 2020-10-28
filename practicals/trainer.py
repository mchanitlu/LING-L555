import sys
def ss(word,ipa):
	ret = ""
	#for c in word:
	#	if c in ipa:
	#		ret = ret + ipa[c]
	#	else:
	#		ret = ret + c
	i = 0 
	while i < len(word):
		if i+1<(len(word)):
			c = word[i: i+2]
			if c in ipa:
				ret = ret + ipa[c]
				i = i+2
				continue
		c = word[i]	
		if c in ipa:
			ret = ret + ipa[c]
		else:
			ret = ret + c
		i = i + 1
		
	return ret
 
if __name__ == "__main__":
	ipa = {}
	#temp = ['i', 'u', 'e', 'o', 'a', 'm', 'n', 'ɲ', 'p', 't', 'k', 'b', 'd', 'g', 'f', 'θ', 's', 'ʃ', 'j', 'w', 'l','ʎ', 'ɾ', 'r']
	#for c in range(len(temp)):
	#	ipa[chr(ord('a')) + i] = temp[i]
	dtemp = {'a': 'a', 'b': 'b', 'v': 'b', 'c': 'k','que':'kue','qui':'kui', 'ch' : 'tʃ','qua':'kwa','quo'='kwo','küe'='kwe','küi'='kwe','d'='d','e'='e','f'='f','g'='g','gua'='gwa','guo'='gwo','güe'='gwe','güi'='gwi','i'='i','h'='h','i'='i','l'='l','ʎ'='ll','m'='m','n'='n','ɲ'='ny','o'='o','p'='p','r'='ɾ','rr'='r',' r'='r', 's'='s','t'='t','u'='u','ix'='jʃ','y'='j','za='θ','zo='θ','zu'='θ','ce'='θ','ci'='θ'}
	for k,v in dtemp.items():
		ipa[k] = v
	for line in sys.stdin.readlines():
		
	
