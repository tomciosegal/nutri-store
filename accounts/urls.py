from accounts import url_reset
from accounts.views import (
    about,
    contact,
    delivery,
    login,
    logout,
    registration,
    return_policy,
    user_profile,
    subscribe_mail
)
from django.conf.urls import include, url

urlpatterns = [
    url(r"^logout/", logout, name="logout"),
    url(r"^login/", login, name="login"),
    url(r"^register/", registration, name="registration"),
    url(r"^profile/", user_profile, name="profile"),
    url(r"^password-reset/", include(url_reset)),
    url(r"^contact/", contact, name="contact"),
    url(r"^about/", about, name="about"),
    url(r"delivery/", delivery, name="delivery"),
    url(r"return-policy/", return_policy, name="return-policy"),
    url(r"(?P<user_id>[0-9]+)/subscribe", subscribe_mail, name="subscribe_mail")
]
