from django.shortcuts import render
from django.views import View

from adminka.model.news import News


class NewsView(View):
    def get(self, request):
        news_list = News.objects.all()
        return render(request, 'main/news.html', {'news_list': news_list})


class NewsSingleView(View):
	def get(self, request, slug):
		news = News.objects.get(slug=slug)
		return render(request, 'main/news_view.html', {'news': news})