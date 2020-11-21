from .base_settings import *
from .prod_settings import *

try:
    from .local_settings import *
except ImportError:
    pass


