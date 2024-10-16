from django.urls import path
from .views import HomePageView , news_list, news_detail,  LocalNewsView, WorldNewsView,  SportNewsView, IqtisodiyotNewsView, SubjectNewsView, ContactPageView, JamiyatNewsView, NewsCreateView, NewsDeleteView, NewsUpdateView


urlpatterns = [
    path('', HomePageView.as_view(template_name='news/index.html'), name='home'),
    path('Sport/', SportNewsView.as_view(template_name='news/Sport.html'), name='Sport'),
    path('jahon/', WorldNewsView.as_view(template_name='jahon.html'), name='jahon'),
    path('iqtisodiyot/', IqtisodiyotNewsView.as_view(template_name='Iqtisodiyot.html'), name='iqtisodiyot'),
    path('jamiyat/', JamiyatNewsView.as_view(template_name='jamiyat.html'), name='jamiyat'),
    path('fan_texnika', SubjectNewsView.as_view(template_name='fan_texnika.html'), name='fan_texnika'),
    path("news/", news_list, name='news_all'),
    path('uzbekistan/', LocalNewsView.as_view(template_name='uzbekistan.html'), name='uzbekistan'),
    path("news/<slug:news>", news_detail, name='news_detail_page'),
    path('contact/', ContactPageView.as_view(), name='contact-us'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete')
]
