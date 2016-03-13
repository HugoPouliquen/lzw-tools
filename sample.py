import cli
import compress_funcs

args = cli.parser.parse_args()
if args.text:
    print(compress_funcs.compress(args.string))
