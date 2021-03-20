"""定义 learning_logs 的URL模式"""

from django.urls import path
from . import views

app_name = 'learnings_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index')
]
