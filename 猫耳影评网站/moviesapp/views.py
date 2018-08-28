from django.shortcuts import render
from django.http import JsonResponse
from . import models
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
import logging
logger = logging.getLogger('moviesapp')


def master(request):
    """主页"""
    movies = models.MoviesInfo.objects.all()
    page = int(request.GET.get('page',1))
    per_page = 12
    paginator = Paginator(movies,per_page)
    try:
        show_movies = paginator.page(page)
    except (EmptyPage,InvalidPage,PageNotAnInteger) as ex:
        show_movies = paginator.page(1)
    kwags = {
        'movies': show_movies,
    }
    return render(request,'master.html',kwags)


def comment(request,id):
    """影评列表"""
    movie = models.MoviesInfo.objects.get(id=id)
    reviews = models.Reviews.objects.filter(movie_char=movie.name)
    # reviews = models.Reviews.objects.get(id=34)
    kwags = {
        'movie':movie,
        'reviews':reviews,
    }
    return render(request,'comment.html',kwags)


def reviews(request,id):
    """影评文章"""
    article = models.Reviews.objects.get(id=id)
    movie = models.MoviesInfo.objects.get(name=article.movie_char)
    print(movie)
    kwags = {
        'article': article,
        'movie':movie
    }
    return render(request,'reviews.html',kwags)


from django .core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
def search(request):
    """搜索页"""
    keywords = ""
    if request.method == 'GET':
        keywords = request.GET.get('keywords','')
    elif request.method == 'POST':
        keywords = request.POST.get('keywords','')
    movies = models.MoviesInfo.objects.filter(name__icontains=keywords)
    movies_num = len(movies)
    kwgs = {
        'movies':movies,
        'movies_num':movies_num
    }
    return render(request, 'search.html',kwgs)


class Commit(LoginRequiredMixin,View):
    """提交"""
    def get(self,request):
        return render(request, 'commit.html')
    def post(self,request):
        movie_name = request.POST.get('movie_name','')
        review_name = request.POST.get('review_name','')
        content = request.POST.get('content','')
        if models.Reviews.objects.filter(movie_char__icontains=movie_name):
            movies_name = models.Reviews.objects.filter(movie_char__icontains=movie_name)[0].movie_char
            models.Reviews.objects.create(auth=request.user,name=review_name,movie_char=movies_name,content=content)
            ret = {"status": 200, "msg": "错误"}
        else:
            models.Reviews.objects.create(name=review_name, movie_char=movie_name, content=content)
            ret = {"status": 200, "msg": "错误"}
            print('电影表中没有该电影，请管理员添加该电影基本信息！')
        return JsonResponse(ret)


def category(request,keywords):
    """分类"""
    movies = models.MoviesInfo.objects.filter(tag_char__contains=keywords)
    kwags = {
        'movies':movies
    }
    return render(request,'category.html',kwags)


def high_score(request):
    """高分经典"""
    movies = models.MoviesInfo.objects.filter(score__gte=9)
    kwags = {
        'movies':movies
    }
    return render(request,'category.html',kwags)

def about(request):
    return render(request,'about.html')



