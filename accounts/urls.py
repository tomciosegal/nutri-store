from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, contact, about,delivery
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^contact/', contact, name= "contact"),
    url(r'^about/', about, name= "about"),
    url(r'delivery/', delivery, name='delivery')
]