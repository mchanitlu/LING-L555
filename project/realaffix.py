import sys


def check_have(content, root):
    ret = []
    for r in root:
        if content.find(r) >= 0:
            ret.append(r)
    return ret


def show_word(word, root):
    ret = []
    length = 6
    for i in range(len(word)):
        length = min(6, len(word) - i)
        while length > 0:
            part = word[i:i + length]
            if part in root:
                ret.append((part, 1))
                break
            length = length - 1
        if length <= 0:
            ret.append((word[i], 0))
    for w in ret:
        if w[1] == 0:
            print(w[0], end="")
        else:
            print('\033[1;32m%s\033[0m' % (w[0]), end="")

    return ret


if __name__ == "__main__":
    root = {}
    wc = 0
    text = sys.stdin.readlines()
    for line in text:
        line = line.strip()
        # empty line
        if len(line) <= 0 or line[0] == "#":
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        word = parts[1]
        # short word or long word
        if len(word) <= 2 or len(word) > 10:
            continue
        wc = wc + 1
        length = 2
        while length < len(word):
            for i in range(len(word) - length):
                root[word[i:i + length]] = root.get(word[i:i + length], 0) + 1
            length = length + 1

    ret = [[k, v / wc] for k, v in root.items()]
    ret.sort(key=lambda v: v[1], reverse=True)
    # delete low frequent words
    end = len(ret)
    for i in range(end):
        if ret[i][1] < 0.02:
            end = i
            break
    ret = ret[:end]
    # print(ret)

    select_root = [i[0] for i in ret]
    print(select_root)

    true_root = ['ащ', 'гъащ', 'нщ', 'нущ', 'т', 'рт', 'ат', 'гъат', 'нт', 'нут', 'мэ', 'ми', 'къэ', 'рэ', 'рэ', 'мрэ',
                 'мри', 'и', 'мкӏи', 'гъэ', 'гъакӏэ', 'гъэ，рэ，ри，гъэ', 'гъах', 'ж', 'и', 'къым', 'мэ', 'ми', 'н', 'еи',
                 'хы', 'рей', 'рт', 'т', 'тэмэ', 'тэми', 'фы', 'пэ', 'кӏэ', 'лӏ', 'ӏуэ', 'къуэ', 'хэ', 'хэ', 'ххэ',
                 'хь', 'щэрэ', '-м', 'м', '-р', 'р', '-хэ-р', 'мкӏэ', 'ыу', 'уэ', 'эa', 'э', '-рэ', 'н', 'къым', '-мы-',
                 'си', 'уи', 'и', 'ди', 'фи', 'я', 'ӏуэ', 'щэ', 'дэд', 'кӏей', 'ншэ', 'фӏэ', 'гъэ，дэ', 'зэ', 'з', 'здэ',
                 'къэ', 'ӏэщӏэ', 'нэ', 'фӏэ', 'ху', 'блэ', 'пхы', 'пыры', 'кӏэлъ']

    for line in text:
        line = line.strip()
        # empty line
        if len(line) <= 0:
            continue
        if line[0] == "#":
            print(line)
            if line.find("# text = ") >= 0:
                sentence = line[9:]
                select_have = check_have(sentence, select_root)
                true_have = check_have(sentence, true_root)
                intersection = select_have and true_have
                print("intersection:", intersection)
                if len(select_have) != 0:
                    print("precise:", len(intersection) / len(select_have))
                print("selected - true:", list(set(select_have) - set(true_have)))
                # print("recall:")
                print("true - selected:", list(set(true_have) - set(select_have)))
                # print("")
                print()
        else:
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            word = parts[1]
            print("%s\t" % (parts[0]), end="")
            show_word(word, true_root)
            print("\t-" * 8)

        # parts = line.split("\t")
        # if len(parts) < 2:
        #     continue
        # word = parts[1]
