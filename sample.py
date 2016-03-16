import cli
import compress_funcs

args = cli.parser.parse_args()

if args.text:
    print(compress_funcs.compress(args.string))
elif args.file:
    # print("Your content compressed in : ", compress_funcs.input(args.string))
    compress_funcs.input(args.string)
