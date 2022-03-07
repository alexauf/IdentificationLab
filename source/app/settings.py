import os

IS_PRODUCTION = os.environ.get('IS_PRODUCTION')
PRODUCTION = False

if PRODUCTION:
    from .conf.production.settings import *
else:
    from .conf.development.settings import *
