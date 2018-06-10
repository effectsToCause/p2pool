import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '70352205'.decode('hex')
P2P_PORT = 36988
ADDRESS_VERSION = 70
RPC_PORT = 33987
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue('veriumaddress' in (yield bitcoind.rpc_help()) and not (yield bitcoind.rpc_getinfo())['testnet']))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//210000
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'VRM'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Verium') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Verium/') if platform.system() == 'Darwin' else os.path.expanduser('~/.verium'), 'verium.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/vrm/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/vrm/address.dws?'
TX_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/vrm/tx.dws?'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.1e8
