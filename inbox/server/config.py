from ConfigParser import SafeConfigParser, NoSectionError

import logging as log

try:
    server_type = open('/etc/inbox/server_type', 'r').read().strip()
except IOError:
    server_type = 'development'

def is_prod():
    return server_type == 'production'

config = dict(server_type=server_type)

def load_config(filename='config.cfg'):
    global config
    try:
        parser=SafeConfigParser()
        parser.read([filename])
        config.update(dict((k.upper(), v) for k, v in parser.items('inboxserver')))
        log.info('Loaded configuration from {0}'.format(filename))
    except NoSectionError:
        log.error("Couldn't load configuration from {0}".format(filename))
