import sys


def get_voice(word, ipa):
    ret = ""
    # for c in word:
    #     if c in ipa:
    #         ret = ret + ipa[c]
    #     else:
    #         ret = ret + c

    i = 0
    while i < len(word):
        if i + 1 < len(word):
            # print(type(i))
            c = word[i:i + 2]
            if c in ipa:
                ret = ret + ipa[c]
                i = i + 2
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
    dtemp = {'v':'b','que':'kue','qui':'kui','ch': 'tʃ','qu':'k','qü':'kw','gua':'gwa','güi':'gwi','güe':'gwi','ll':'ʎ','ny':'ɲ','rr':'rr','r':'ɾ','ix':'jʃ','y': 'j', 'za': 'θa', 'zo': 'θo', 'zu': 'θu', 'ce': 'θe', 'ci': 'θi'}
    for k, v in dtemp.items():
        ipa[k] = v
    for line in sys.stdin.readlines():
        # strip any excess newlines
        line = line.strip('\n')
        # if there is no tab character, skip the line
        if '\t' not in line:
            print(line)
            continue
        # make a list of the cells in the row
        row = line.split('\t')
        # if there are not 10 cells, skip the line
        if len(row) != 10:
            print(line)
            continue
        # the form is the value of the second cell
        form = row[1]
        form_ipa = get_voice(form, ipa)
        print("%s\t%s\t_\t_\t_\t_\t_\t_\t_\t_\tIPA=%s" % (row[0], form, form_ipa))

