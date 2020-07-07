from argparse import ArgumentParser


def get_argument_parser() -> ArgumentParser:
    arg_parser: ArgumentParser = ArgumentParser()
    set_arguments(arg_parser)
    set_defaults(arg_parser)

    return arg_parser


def set_arguments(arg_parser):
    arg_parser.add_argument('--debug', dest='debug', action='store_true', help='run in debug mode')
    arg_parser.add_argument('--reset', dest='reset', action='store_true', help='clear internal post history on init')
    arg_parser.add_argument('--delete', dest='delete', action='store_true', help='delete all posted tweets on init')
    arg_parser.add_argument('--truncate', dest='truncate', action='store_true', help='truncate tweets over limit')


def set_defaults(arg_parser):
    arg_parser.set_defaults(debug=False)
    arg_parser.set_defaults(reset=False)
    arg_parser.set_defaults(delete=False)
    arg_parser.set_defaults(truncate=False)
