import argparse

parser = argparse.ArgumentParser(description='Compress LZW tool')
parser.add_argument('-t', '--text', help='compress string', action="store_true")
parser.add_argument("string", help="compress string")
# parser.add_argument('-f', '--file', help='compress file.txt', action="store_true")
# parser.add_argument('-i', '--image', help='compress image.jpg', action="store_true")
