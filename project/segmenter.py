import sys


def segmenter(text):
    text = text.replace("\n", " ")
    punc = ['.', '?', '!']
    for c in punc:
        text = text.replace(c + " ", c + "\n")
    return text


if __name__ == "__main__":
    text = sys.stdin.read()
    text = segmenter(text)
    print(text)
