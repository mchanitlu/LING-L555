import sys
import itertools
text = sys.stdin.read()	
z = text.splitlines()
def newlist(z):
	res = []
	for el in z:
		sub = el.split("!@#$%^&*")
		res.append(sub)
	res = [ele for ele in res if ele != [' ']] 
	res = [ele for ele in res if ele != ['']]  
	return(res) 
w = newlist(z)
#for i in range(len(w)):
#	print("%d\t%s"%(i+1,w[i]))
a = "ID\tFROM\tLEMMA\tUPOS\tXPOS\tFEATS\tHEAD\tDEPREL\tDEPS\tMISC"
flat_list = []
for sublist in w:
	for item in sublist:
		punc = item.replace('"','\n"\n')
		punc = punc.replace(') ','\n)\n')
		punc = punc.replace(' (','\n(\n')
		punc = punc.replace(',','\n,\n')
		punc = punc.replace('.','\n.\n')
		ok = punc.split()
		flat_list.append(ok)
flatten = lambda w: [item for sublist in w for item in sublist]
a = "ID\tFROM\tLEMMA\tUPOS\tXPOS\tFEATS\tHEAD\tDEPREL\tDEPS\tMISC"
punct:[',',')','(','"','.']
for i in range(len(flat_list)):
	print('# sent_id = %s' % (i+1))
	nano = ' '.join(flat_list[i])
	print("# text = " + str(nano))
	flat_list[i] = list(filter(lambda item: item.strip(), flat_list[i]))
	#x = ['ID','FROM','LEMMA','UPOS','XPOS','FEATS','HEAD','DEPREL','DEPS','MISC']
	for c in range(len(flat_list[i])):
		u = flat_list[i]
		print("%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_\t"%(c+1,u[c]))
	print('\t')
			
		
