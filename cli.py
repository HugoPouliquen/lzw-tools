import argparse
from utils.file_manager import file_treat
from utils.compression import compress

parser = argparse.ArgumentParser(description='Compress LZW tool')
parser.add_argument(
    '-t', '--text', help='compress string', action="store_true"
)
parser.add_argument(
    '-f', '--file', help='compress file.txt', action="store_true"
)
parser.add_argument("string", help="to compress")


args = parser.parse_args()
if args.text:
    print(compress(args.string))
elif args.file:
    print("Your content has compressed in:", file_treat(args.string))
