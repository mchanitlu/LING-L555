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
	dtemp = {'a': 'a', 'b': 'b', 'v': 'b', 'c': 'k','que':'kue','qui':'kui', 'ch' : 'tʃ','qua':'kwa','quo':'kwo','küe':'kwe','küi':'kwe','d':'d','e':'e','f':'f','g':'g','gua':'gwa','guo':'gwo','güe':'gwe','güi':'gwi','i':'i','h':'h','i':'i','l':'l','ʎ':'ll','m':'m','n':'n','ɲ':'ny','o':'o','p':'p','r':'ɾ','rr':'r',' r':'r', 's':'s','t':'t','u':'u','ix':'jʃ','y':'j','za':'θ','zo':'θ','zu':'θ','ce':'θ','ci':'θ'}
	for k,v in dtemp.items():
		ipa[k] = v
	for line in sys.stdin.readlines():
		line = line.strip('\n')
        # if there is no tab character, skip the line
		if '\t' not in line:
			print(line)
			continue
        # make a list of the cells in the row
		row = line.split('\t')# if there are not 10 cells, skip the line
		if len(row) != 10:
			print(line)
			continue
        # the form is the value of the second cell
		form = row[1]
		form_ipa = ss(form, ipa)
		print("%s\t%s\t_\t_\t_\t_\t_\t_\t_\t_\tIPA=%s" % (row[0], form, form_ipa)	
	
