from flask import _request_ctx_stack, current_app
from werkzeug.local import LocalProxy

from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from ..helpers import ModelMixin
from .flask_oss import FlaskOSS
from .oauth import OAuthApi
from flask_socketio import SocketIO

logger = LocalProxy(lambda: current_app.logger)
current_user = LocalProxy(lambda: getattr(_request_ctx_stack.top, 'user', None))

db = SQLAlchemy(model_class=ModelMixin)

redis_store = FlaskRedis(decode_responses=True, decode_components=True)
oss = FlaskOSS()
oauth_client = OAuthApi()
socketIO = SocketIO