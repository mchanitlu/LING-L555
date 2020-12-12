import sys

"""
分句子
"""
punctuation = ['.', '!', '?']


def segment(text: str) -> str:
    ret = text
    for c in punctuation:
        ret = ret.replace(c + " ", c + "\n")
    return ret


if __name__ == "__main__":
    text = sys.stdin.read()
    new_text = segment(text)
    print(new_text)
