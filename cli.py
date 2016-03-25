import argparse
from utils.compression import file_compression
from utils.compression import compress
from utils.decompression import decompress
from utils.decompression import file_decompressed

parser = argparse.ArgumentParser(description='Compress LZW tool')

subparsers = parser.add_subparsers()
subparsers.required = True
subparsers.dest = 'command'
subparser = subparsers.add_parser('compress', help='run compression')
subparser.add_argument('-t', '--text', help='compress string', action='store_true')
subparser.add_argument('-f', '--file', help='compress file.txt', action='store_true')
subparser.add_argument('string', help='to compress')

subparser = subparsers.add_parser('uncompress', help='run uncompression')
subparser.add_argument('-t', '--text', help='uncompress string', action='store_true')
subparser.add_argument('-f', '--file', help='uncompress file.lzw', action='store_true')
subparser.add_argument("string", help="to compress")

args = parser.parse_args()
if args.command == 'compress':
    if args.text:
        print(compress(args.string))
    elif args.file:
        print('Your content has compressed in:', file_compression(args.string))
elif args.command == 'uncompress':
    if args.text:
        print(decompress(args.string))
    elif args.file:
        print('Your content is in:', file_decompressed(args.string))
