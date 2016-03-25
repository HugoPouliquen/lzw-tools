# lzw-tools
[![Circle CI](https://circleci.com/gh/HugoPouliquen/lzw-tools.svg?style=shield)](https://circleci.com/gh/HugoPouliquen/lzw-tools)
[![Code Climate](https://codeclimate.com/github/HugoPouliquen/lzw-tools/badges/gpa.svg)](https://codeclimate.com/github/HugoPouliquen/lzw-tools)

LZW tools for compress &amp; decompress

Build in Python 3

# Resources
[Lempel-Ziv-Welch](https://fr.wikipedia.org/wiki/Lempel-Ziv-Welch)

# Todo:
- Compression
    - [x] Build Ascii byte list
    - [x] Open file in byte
    - [x] Compress file
    - [x] Write compressed content in file.lzw
    - [ ] File compressed size less than base size
    - [ ] Insert extension information in compressed file
- Decompression
    - [x] Build Ascii byte list
    - [x] Open file in byte
    - [x] Decompress file
    - [x] Write decompressed content in original file
    - [x] File decompressed size is equal to original file
    - [ ] File decompressed content is equal to original content
    - [ ] Get extension information in compressed file
- Tests
    - [x] Ascii byte list
    - [ ] Compression
    - [ ] Decompression
    - [x] Automatically build tests : CirleCi
    - [x] Code quality : CodeClimate

# Run with cli-menu
```bash
[lzw-tools] $ python3 sample.py
```
- Menu

    ![](img/menu_preview.png?raw=true)

- File browser

    ![](img/browser_preview.png?raw=true)

# Run with cli

If you want run simple cli, follow this instructions :
- In `sample.py` **uncomment**  `import cli` and  **comment** `# import menu_cli`
```bash
[lzw-tools] $ python3 sample.py compress -f file.txt
# OUTPUT => Your content has compressed in: file.lzw
[lzw-tools] $ python3 sample.py decompress -f file.lzw
# OUTPUT => Your content is in: file.txt
```

# Tests
```bash
[lzw-tools] $ python3 -m tests.make_list_test
```

## Contributing
1. Fork it
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Ensure unit tests
5. Push to the branch (git push origin my-new-feature)
6. Create new Pull Request
