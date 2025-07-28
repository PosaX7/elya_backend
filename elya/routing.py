# elya/routing.py

from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from quizz.consumers import QuizzConsumer  # on va créer ça juste après

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r"ws/quizz/(?P<room_name>\w+)/$", QuizzConsumer.as_asgi()),
        ])
    ),
})
