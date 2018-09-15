from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),  # 모든 url이 들어올때 views.py 에 정의된 함수 post_list 를 불러온다
    #   url(r'mySite^$', views.post_list, name='post_list'), http://127.0.0.1:8000/mySite 로 하려고 했는데.. 잘안된다
]
