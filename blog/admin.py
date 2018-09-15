from django.contrib import admin
from .models import Post, PostTest

admin.site.register(Post) # 모델등록
admin.site.register(PostTest) # 모델등록
