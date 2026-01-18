from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from auth.routes.auth import router as auth_router

api = NinjaAPI(
    title="Catequese Backend API",
    version="1.0.0",
    docs_url="/docs"
)

api.add_router("/auth/", auth_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
