# lzw-tools
[![Circle CI](https://circleci.com/gh/HugoPouliquen/lzw-tools.svg?style=shield)](https://circleci.com/gh/HugoPouliquen/lzw-tools)

LZW tools for compress &amp; uncompress

Build in Python 3

# Resources
[Lempel-Ziv-Welch](https://fr.wikipedia.org/wiki/Lempel-Ziv-Welch)

# Run
- Compress text
```bash
[lzw-tools] $ python3 sample.py -t TOBEORNOTTOBEORTOBEORNOT
# OUTPUT => ['T', 'O', 'B', 'E', 'O', 'R', 'N', 'O', 'T', 256, 258, 260, 265, 259, 261]
```

# Tests
```bash
[lzw-tools] $ python3 -m compress_test
# OUTPUT =>
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
#OK
```
