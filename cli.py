import argparse
from utils.compression import compress
from utils.compression import file_compression
from utils.decompression import decompress
from utils.decompression import file_decompression

"""
This is the simple cli. To understand read the argparse doc
htp://www.......
"""

parser = argparse.ArgumentParser(description='Compress LZW tool')

subparsers = parser.add_subparsers()
subparsers.required = True
subparsers.dest = 'command'
subparser = subparsers.add_parser('compress', help='run compression')
subparser.add_argument('-f', '--file', help='compress file.txt', action='store_true')
subparser.add_argument('string', help='to compress')

subparser = subparsers.add_parser('decompress', help='run decompression')
subparser.add_argument('-f', '--file', help='decompress file.lzw', action='store_true')
subparser.add_argument("string", help="to compress")

args = parser.parse_args()
if args.command == 'compress':
    if args.text:
        print(compress(args.string))
    elif args.file:
        print('Your content has compressed in:', file_compression(args.string))
elif args.command == 'decompress':
    if args.text:
        print(decompress(args.string))
    elif args.file:
        print('Your content is in:', file_decompression(args.string))
