from django.urls import path

from .views import index, detail, results, vote, IndexView, DetailView, ResultsView

app_name = 'polls'

# print("polls입니다")


urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/results/', results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),

    path('cbv/', IndexView.as_view(), name='cbv-index'),
    path('cbv/<int:pk>/', DetailView.as_view(), name='cbv-detail'),
    path('cbv/<int:pk>/', ResultsView.as_view(), name='cbv-detail')
]
