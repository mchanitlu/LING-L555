import sys

if __name__ == "__main__":
    text = sys.stdin.readlines()
    i = 0
    while i < len(text):
        line = text[i].strip()
        if line[0] == "#":
            # print id
            print(line)
            # print text
            print(text[i + 1].strip())
            i = i + 2
            tag_counter = {}
            word_counter = {}
            while i < len(text):
                line = text[i].strip()
                if len(line) <= 0 or line[0] == "#":
                    break
                row = line.split('\t')
                # print(row)
                # get tag
                tag = row[3]
                tag_counter[tag] = tag_counter.get(tag, 0) + 1
                tag_counter['all'] = tag_counter.get('all', 0) + 1
                # get word
                word = row[1]
                if word not in word_counter:
                    word_counter[word] = {}
                word_counter[word]['all'] = word_counter[word].get('all', 0) + 1
                word_counter[word][tag] = word_counter[word].get(tag, 0) + 1
                i = i + 1
            # print(tag_counter)
            # print(word_counter)
            # print result
            # print title
            i = i + 1
            print("# P\tcount\ttag\tform")
            for k, v in tag_counter.items():
                if k != 'all':
                    print("%.2f\t%d\t%s\t-" % (v / tag_counter['all'], v, k))
            for word, all_tag in word_counter.items():
                for k, v in all_tag.items():
                    if k != 'all':
                        print("%.2f\t%d\t%s\t%s" % (v / all_tag['all'], v, k, word))
            print()
