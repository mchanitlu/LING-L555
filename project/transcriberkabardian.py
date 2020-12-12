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
    dtemp = {'А':'a','а':'a','Э':'a','э':'a','Б':'b','б':'b','В':'v','в':'v','Г':'ɣ','г':'ɣ','Гу':'ɡ(w)','гу':'ɡ(w)','Гъ':'ʁ','гъ':'ʁ','Гъу':'ʁ(w)','гъу':'ʁ(w)','Д':'d','д':'d','Дж':'d͡ʒ','дж':'d͡ʒ','Дз':'d͡z','дз':'d͡z','Е':'ja','е':'ja','Ё':'jo','ё':'jo','Ж':'ʒ','ж':'ʒ','Жь':'ʑ','жь':'ʑ','З':'z','з':'z','И':'jə','и':'jə','Й':'j','й':'j','К':'k','к':'k','Ку':'k(w)','ку':'k(w)','Къ':'q','къ':'q','Къу':'q(w)','къу':'q(w)','Кхъ':'q͡χ','кхъ':'q͡χ','Кхъу':'q͡χ(w)','кхъу':'q͡χ(w)','Кӏ':'t͡ʃʼ','кӏ':'t͡ʃʼ','Кӏу':'k(w)ʼ','ху':'x(w)','Хъ':'χ','хъ':'χ','Хъу':'χ(w)','Хь':'ħ','Л':'ɮ','л':'ɮ','Лъ':'ɬ','лъ':'ɬ','Лӏ':'ɬ‘','лӏ':'ɬ‘','М':'m','м':'m','Н':'n','н':'n','О':'aw','о':'aw','П':'p','п':'p','Пӏ':'p‘','пӏ':'p‘','Р':'r','р':'r','С':'s','с':'s','Т':'t','т':'t','Тӏ':'t’','тӏ':'t‘','У':'w','у':'w','Ф':'f','ф':'f','Фӏ':'f’','фӏ':'f’','Х':'x','х':'x','Ху':'x(w)','Хь':'ħ','хь':'ħ','Ц':'t͡s','ц':'t͡s','Цӏ':'t͡s‘','цӏ':'t͡s‘','Ч':'t͡ʃ','ч':'t͡ʃ','Чӏ':'t͡ʃ’','чӏ':'t͡ʃ’','Ш':'ʃ','ш':'ʃ','Щ':'ɕ','щ':'ɕ','Щӏ':'ɕʼ','щӏ':'ɕʼ','Ъ':'(ɣ)','ъ':'(ɣ)','Ы':'ə','ы':'ə','Ь':'(j)','ь':'(j)','Ю':'ju','ю':'ju','Я':'jaː','я':'jaː','ӏ':'ʔ','ӏу':'ʔ(w)','хъу':'χ(w)'}
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

