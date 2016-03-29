# lzw-tools
[![Circle CI](https://circleci.com/gh/HugoPouliquen/lzw-tools.svg?style=shield)](https://circleci.com/gh/HugoPouliquen/lzw-tools)
[![Code Climate](https://codeclimate.com/github/HugoPouliquen/lzw-tools/badges/gpa.svg)](https://codeclimate.com/github/HugoPouliquen/lzw-tools)

LZW tools to compress &amp; decompress

Build in **Python 3**

## Resources
[Lempel-Ziv-Welch](https://fr.wikipedia.org/wiki/Lempel-Ziv-Welch)

## Todo:
- Compression
    - [x] Build Ascii byte list
    - [x] Read file in byte array
    - [x] Compress file
    - [x] Write compressed result in file.lzw
    - [ ] Compressed file size is less than base file size
    - [ ] Insert file extension in compressed file
    - [x] CLI/menu-CLI
- Decompression
    - [x] Build Ascii byte list
    - [x] Read file in byte array
    - [x] Decompress file
    - [x] Write decompressed result in original file
    - [x] Decompressed file size is equal to original file
    - [ ] Decompressed file content is the same as the original file content
    - [ ] Extract file extension from compressed file
    - [x] CLI/menu-CLI
- Tests
    - [x] Ascii byte list
    - [ ] Compression
    - [ ] Decompression
    - [x] Automatically build tests : CirleCi
    - [x] Code quality : CodeClimate

## Usage

### With menu

![CLI-menu](img/menu_preview.png?raw=true)

```bash
[lzw-tools] $ python3 sample.py
```

### Without menu

To simply use the CLI :
- In `sample.py` file **uncomment**  `import cli` and  **comment** `# import menu_cli`
```bash
[lzw-tools] $ python3 sample.py compress -f file.txt
# OUTPUT => Your content is now compressed and is available in: file.lzw
[lzw-tools] $ python3 sample.py decompress -f file.lzw
# OUTPUT => Your content is now decompressed and is available in: file.txt
```

## Tests
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

## Demo
![S](img/animation.gif?raw=true)

For example, [GIF images](https://en.wikipedia.org/wiki/GIF) are compressed using the Lempel–Ziv–Welch (LZW) lossless data compression technique.
