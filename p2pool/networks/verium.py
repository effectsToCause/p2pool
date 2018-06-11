from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['verium']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'e037d5b8c6923610'.decode('hex')
PREFIX = 'e05775b8c6a6331d'.decode('hex')
P2P_PORT = 36999
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 8336
BOOTSTRAP_ADDRS = 'emea.supernode.vericonomy.com amer.supernode.vericonomy.com apac.supernode.vericonomy.com'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-verium'
VERSION_CHECK = lambda v: None if 80001 <= v else 'Verium version too old. Upgrade to 1.0.1 or newer!'
VERSION_WARNING = lambda v: None
MINIMUM_PROTOCOL_VERSION = 1700
NEW_MINIMUM_PROTOCOL_VERSION = 1700
