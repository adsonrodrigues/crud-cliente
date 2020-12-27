from rest_framework import routers

from clientes.views import ClienteViewset

router = routers.SimpleRouter()

router.register(r'cliente', ClienteViewset)

urlpatterns = []

urlpatterns += router.urls
