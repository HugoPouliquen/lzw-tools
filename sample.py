import cli
from utils.compression import compress
from utils.file_manager import file_treat

args = cli.parser.parse_args()

if args.text:
    print(compress(args.string))
elif args.file:
    print("Your content has compressed in:", file_treat(args.string))
