from django.urls import path
from .views import news_list, news_detail, HomePageView #, UzbekistanPageview,JamiyatPageview, SportPageview, IqtisodiyotPageview, Fan_texnikaPageview, ContactPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('Sport/', SportNewsView.as_view(template_name='news/Sport.html), name='Sport'),
    # path('iqtisodiyot/', IqtisodiyotPageview, name='iqtisodiyot'),
    # path('jamiyat/', JamiyatPageview, name='jamiyat'),
    # path('fan_texnika', Fan_texnikaPageview, name='fan_texnika'),
    path("news/", news_list, name='news_all'),
    # path('uzbekistan/', UzbekistanPageview, name='uzbekistan'),
    path("news/<slug:news>", news_detail, name='news_detail_page'),
    # path('contact/', ContactPageView.as_view(), name='contact-us'),
]
