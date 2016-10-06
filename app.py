

from flask.helpers import get_debug_flag

from poetics.app import create_app
from poetics.settings import DevConfig, ProdConfig


CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)
