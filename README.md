# lzw-tools
[![Circle CI](https://circleci.com/gh/HugoPouliquen/lzw-tools.svg?style=shield)](https://circleci.com/gh/HugoPouliquen/lzw-tools)
[![Code Climate](https://codeclimate.com/github/HugoPouliquen/lzw-tools/badges/gpa.svg)](https://codeclimate.com/github/HugoPouliquen/lzw-tools)

LZW tools for compress &amp; decompress

Build in Python 3

# Resources
[Lempel-Ziv-Welch](https://fr.wikipedia.org/wiki/Lempel-Ziv-Welch)

# Todo:
- Compression
    - [x] Compress file
    - [ ] File compress less than base
    - [ ] Save extension in compressed file
- Decompression
    - [x] Decompress file
    - [x] File decompress size is equal to original file
    - [ ] Get extension in compressed file
- Tests
    - [ ] Compression
    - [ ] Decompression
    - [x] Automatically build tests : CirleCi
    - [x] Code quality : CodeClimate

# Run with cli-menu
```bash
[lzw-tools] $ python3 sample.py
```
![](img/preview.png?raw=true)

If you want run simple cli, follow this instructions :
- In `sample.py` **uncomment**  `import cli` and  **comment** `# import menu_cli`
```bash
[lzw-tools] $ python3 sample.py compress -t TOBEORNOTTOBEORTOBEORNOT
# OUTPUT => ['T', 'O', 'B', 'E', 'O', 'R', 'N', 'O', 'T', 256, 258, 260, 265, 259, 261]
[lzw-tools] $ python3 sample.py compress -f file.txt
# OUTPUT => Your content has compressed in: file.lzw
```

# Tests
```bash
[lzw-tools] $ python3 -m tests.compress_test
# OUTPUT =>
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
#OK
```
