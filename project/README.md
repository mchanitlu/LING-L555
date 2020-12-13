# Project
cat wiki.txt|python3 segmenternew.py|python3 tokenisernew.py|python3 affix.py   ->getnpopularity of certain combination of letters
`PROJECT DESCRIPTION HERE`
affix.py is to find out the popularity of certain combination of letters.
realaffix.py is to highlight the real affixes in Kabardian and compare the popularity of certain combination of letters with the real affixes.
head wiki.txt| python3 segmenternew.py|python3 tokenisernew.py| python3 transcriberkabardian.py |python3 realaffix.py
Since the highlight makes the conllu file messy, so I made a conllu without hightlight and tags parts of the speech.
cat wiki.txt|python3 segmenternew.py|python3 tokenisernew.py|python3 transcriberkabardian.py > partsofspeech.conllu
