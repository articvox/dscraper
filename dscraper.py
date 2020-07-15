import logging

from twitter.service import TwitterService
from util.argparse import get_argument_parser
from dbot import DBot
from history.history import delete_all_history
from twitter.defaultservice import DefaultTwitterService
from twitter.mock import MockTwitterService

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s: %(message)s'
    )
    args = get_argument_parser().parse_args()

    default_service: TwitterService = DefaultTwitterService(args.truncate)

    if args.reset is True:
        delete_all_history()
        logging.info('Post history reset')
    if args.delete is True:
        default_service.delete_all()

    DBot(MockTwitterService() if args.debug else
         default_service, args.limit).run()
