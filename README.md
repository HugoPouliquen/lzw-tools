# lzw-tools
[![Circle CI](https://circleci.com/gh/HugoPouliquen/lzw-tools.svg?style=shield)](https://circleci.com/gh/HugoPouliquen/lzw-tools)

LZW tools for compress &amp; uncompress

Build in Python 3

# Resources
[Lempel-Ziv-Welch](https://fr.wikipedia.org/wiki/Lempel-Ziv-Welch)

# Run with cli-menu
In `sample.py` **UNCOMENT** `import menu_cli` & **COMENT** `import cli`
```bash
[lzw-tools] $ python3 sample.py
```

# Run with cli
In `sample.py` **UNCOMENT**  `import cli` & **COMENT** `import menu_cli`
- Compress text
```bash
[lzw-tools] $ python3 sample.py -t TOBEORNOTTOBEORTOBEORNOT
# OUTPUT => ['T', 'O', 'B', 'E', 'O', 'R', 'N', 'O', 'T', 256, 258, 260, 265, 259, 261]
```
- Compress file.txt
```bash
[lzw-tools] $ python3 sample.py -f file.txt
# OUTPUT => Your content has compressed in: file.lzw
```

# Tests
```bash
[lzw-tools] $ python3 -m tests.pretty_test
[lzw-tools] $ python3 -m tests.compress_test
# OUTPUT =>
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
#OK
```
