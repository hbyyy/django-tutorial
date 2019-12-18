from django.urls import path

from polls.views import index, detail, results, vote


app_name = 'polls'

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/result/', results, name='result'),
    path('<int:question_id>/vote/', vote, name='vote'),
]
