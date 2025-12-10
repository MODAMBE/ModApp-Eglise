import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
import eglise.routing  # 👈 Import du routing de ton app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModApp.settings')
django.setup()

# ======================================================
# 🚀 Configuration principale ASGI avec support WebSocket
# ======================================================
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(eglise.routing.websocket_urlpatterns)
        )
    ),
})
