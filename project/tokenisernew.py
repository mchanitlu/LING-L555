import sys
import segmenter
import string
from typing import List


def tokenize(text: str) -> str:
    ret = []
    sentences = text.split("\n")
    for s in sentences:
        ret.extend(tokenize_sentence(s))
    return "\n".join(ret)


def tokenize_sentence(sentence: str) -> str:
    ret = []
    ws = sentence.split()
    for w in ws:
        ret.extend(tokenize_part(w))
    return ret


def tokenize_part(part: str) -> str:
    ret = []
    temp = get_punc(part)
    if len(temp) < 1:
        return ret
    ret.extend(temp[:-1])
    part = temp[-1]
    if r"'" in part:
        p = part.split("'")
        ret.append(p[0] + r"'")
        part = p[1]
    part = part[::-1]
    temp = get_punc(part, True)
    temp.reverse()
    # print(temp)
    ret.extend(temp)
    return ret


def get_punc(part: str, reversed: bool = False) -> List:
    ret = []
    for i in range(len(part)):
        c = part[i]
        if c in string.punctuation:
            ret.append(c)
        else:
            s = part[i:]
            if reversed is True:
                s = s[::-1]
            ret.append(s)
            break
    return ret


if __name__ == "__main__":
    text = sys.stdin.read()
    sentences = text.split("\n")
    index = 1

    for i in range(len(sentences)):
        s = sentences[i].strip()
        if len(s) <= 0:
            continue
        print("# sent_id =", index)
        index = index + 1
        print("# text =", s)
        part = tokenize_sentence(s)
        # print word
        for j in range(len(part)):
            print("%d\t%s" % (j + 1, part[j]), end="")
            print("\t-" * 8)
        print()
