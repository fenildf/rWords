"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from .views.home import home_page, word_view
from .views.user import (
    login_view, register_view, logout_view,
    learning_settings_view, learning_view, learning_state_view,
    learning_state_forget_view, user_notes_view, user_notes_edit_view,
    change_password_view
)
from .views.wordbook import (
    create_wordbook_view, wordbook_view, wordbook_library_view,
    wordbook_set_learning_view
)


urlpatterns = [
    url(r'^$',                          home_page,              name='home_page'),

    url(r'^user/login/$',               login_view,             name='login'),
    url(r'^user/register/$',            register_view,          name='register'),
    url(r'^user/change/password/$',     change_password_view,   name='change_password'),
    url(r'^user/logout/$',              logout_view,            name='logout'),
    url(r'^user/learning/settings/$',   learning_settings_view, name='learning_settings'),
    url(r'^user/learning/$',            learning_view,          name='learning'),
    url(r'^user/learning/state/$',      learning_state_view,    name='learning_state'),
    url(r'^user/learning/state/forgot/(\d+)/$',
                                        learning_state_forget_view,
                                                                name='learning_state_forgot'),
    url(r'^user/notes/$',               user_notes_view,        name='user_notes'),
    url(r'^user/notes/edit/(\d+)/$',    user_notes_edit_view,   name='user_notes_edit'),

    url(r'^wordbook/new/$',             create_wordbook_view,   name='create_wordbook'),
    url(r'^wordbook/(\d+)/$',           wordbook_view,          name='wordbook'),
    url(r'^wordbook/library/(\d+)/$',   wordbook_library_view,  name='wordbook_library'),
    url(r'^wordbook/set/learning/(\d+)/$',
                                        wordbook_set_learning_view,
                                                                name='set_learning_wordbook'),
    url(r'^word/$',                     word_view,              name='word')
]
