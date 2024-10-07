from django.urls import path
from .views import news_list, news_detail, HomePageView, UzbekistanPageview,JamiyatPageview, SportPageview, IqtisodiyotPageview, Fan_texnikaPageview


urlpatterns = [
    path('', HomePageView, name="homepage"),
    path('sport/', SportPageview, name='sport'),
    path('iqtisodiyot/', IqtisodiyotPageview, name='iqtisodiyot'),
    path('jamiyat/', JamiyatPageview, name='jamiyat'),
    path('fan_texnika', Fan_texnikaPageview, name='fan_texnika'),
    path("news/", news_list, name='news_all'),
    path('uzbekistan/', UzbekistanPageview, name='uzbekistan'),
    path("news/<int:id>", news_detail, name='news_detail_page'),
]
