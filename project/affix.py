import sys

if __name__ == "__main__":
    root = {}

    for line in sys.stdin.readlines():
        line = line.strip()
        # empty line
        if len(line) <= 0 or line[0] == "#":
            continue
        parts = line.split("\t")
        word = parts[1]
        # short word or long word
        if len(word) <= 2 or len(word) > 10:
            continue

        length = 2
        while length < len(word):
            for i in range(len(word) - length):
                root[word[i:i + length]] = root.get(word[i:i + length], 0) + 1
            length = length + 1

    ret = sorted(root.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

    # delete low frequent words
    end = len(ret)
    for i in range(end):
        if ret[i][1] <= 40:
            end = i
            break
    ret = ret[:end]

    print(ret)
