# -*- coding: utf-8 -*-

"""doctopt wallet inspect tools

Usage:
  catwallet <datapath>

Options:
  -h --help                                             Show this screen.
  --version                                             Show version.

"""

import include
import settings
import logging
import pprint
from contrib.core import HornNode
from docopt import docopt

logger = logging.getLogger('default')

if __name__ == '__main__':
    arguments = docopt(__doc__, version='catwallet 1.0')
    datapath = arguments['<datapath>']
    spv = HornNode(app_name='pytxhorn_catwallet',
                   testnet=True,
                   peer_goal=10,
                   broadcast_peer_goal=10,
                   sync_block_start=0,
                   listen=('127.0.0.1', 15000),
                   app_datapath=datapath,
                )

    wallet = spv.wallet
    wallet_temp_info = wallet.get_temp_collections()

    pp = pprint.PrettyPrinter(indent=4)
    wallet_temp_info = "\r\n{}".format(pp.pformat(wallet_temp_info))
    logger.info(wallet_temp_info)
