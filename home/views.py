from random import randrange
from django.shortcuts import render
from .models import News, Category
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    headline = News.objects.order_by('-add_time')
    first_news = News.objects.order_by('-add_time').first
    three_news = News.objects.order_by('-add_time')[1:2]
    three_categories = Category.objects.all()[0:9]
    return render(request, 'home/index.html', {
        'headline': headline,
        'first_news': first_news,
        'three_news': three_news,
        'three_categories': three_categories,

    })

# Deatil Page


def detail(request, id):
    headline = News.objects.order_by('-add_time')
    news = News.objects.get(pk=id)
    news.views = news.views + 1
    news.save()
    category = Category.objects.get(id=news.category.id)
    rel_news = News.objects.filter(category=category).exclude(id=id).order_by('-add_time')[:4]
    return render(request, 'home/detail.html', {
        'headline': headline,
        'news': news,
        'related_news': rel_news

    })
# esthaniye


def esthaniye(request):
    
    # Esthaniyes = Category.objects.all()[0:1] # comment this line
    Esthaniyes = Category.objects.filter(title="स्थानीय")  # use this
    # print("Result : ", Esthaniyes)
    c_1 = News.objects.filter(category__title="स्थानीय").order_by('-add_time')
    # pagination
    pagination = Paginator(c_1, 20)
    page_number = request.GET.get('page')
    newsdata_final = pagination.get_page(page_number)
    # print(c_1)

    context = {
        'Esthaniyes': Esthaniyes,
        # 'c_1': c_1,
        'c_1': newsdata_final,

    }
    return render(request, 'home/esthaniye.html', context)


# def edetail(request, id):
#     ndetail = News.objects.get(id=id)
#     context = {
#         'ndetail': ndetail
#     }
#     return render(request, 'home/detail.html', context)
# rajnitic


def rajnitic(request):
    Rajnitic = Category.objects.filter(title="राजनीति")
    R_news = News.objects.filter(
        category__title="राजनीति").order_by('-add_time')
    pagination = Paginator(R_news, 20)
    page_number = request.GET.get('page')
    newsdata_final = pagination.get_page(page_number)

    context = {
        'Rajnitic': Rajnitic,
        'R_news': newsdata_final,

    }
    return render(request, 'home/rajnitic.html', context)


# samsamyak


def samsamyak(request):
    Samsamyak = Category.objects.filter(title="समसम्यक")
    sm_news = News.objects.filter(
        category__title="समसम्यक").order_by('-add_time')
    pagination = Paginator(sm_news, 20)
    page_number = request.GET.get('page')
    newsdata_final = pagination.get_page(page_number)
    context = {
        'Samsamyak': Samsamyak,
        'sm_news': newsdata_final
    }
    return render(request, 'home/samsamyak.html', context)


# khelkud


def khelkud(request):
    Khelkud = Category.objects.filter(title="खेलकुद")
    K_news = News.objects.filter(
        category__title="खेलकुद").order_by('-add_time')
    pagination = Paginator(K_news, 20)
    page_number = request.GET.get('page')
    newsdata_final = pagination.get_page(page_number)
    context = {
        'Khelkud': Khelkud,
        'K_news': newsdata_final
    }
    return render(request, 'home/khelkud.html', context)


# antarastriye


def antarastriye(request):
    Antarastriye = Category.objects.filter(title="अन्तरास्ट्रिय")
    A_news = News.objects.filter(
        category__title="अन्तरास्ट्रिय").order_by('-add_time')
    pagination = Paginator(A_news, 20)
    page_number = request.GET.get('page')
    newsdata_final = pagination.get_page(page_number)
    context = {
        'Antarastriye': Antarastriye,
        'A_news': newsdata_final
    }
    return render(request, 'home/antarastriye.html', context)


# suchana parbidhi


def suchana(request):
    Suchana = Category.objects.filter(title="सूचना प्रबिधि")
    su_news = News.objects.filter(
        category__title="सूचना प्रबिधि").order_by('-add_time')
    pagination = Paginator(su_news, 20)
    page_number = request.GET.get('page')
    newsdata_final = pagination.get_page(page_number)
    context = {
        'Suchana': Suchana,
        'su_news': newsdata_final
    }
    return render(request, 'home/suchana.html', context)
# sowathya


def sowasthya(request):
    Sowasthya = Category.objects.filter(title="स्वास्थ्य")
    so_news = News.objects.filter(
        category__title="स्वास्थ्य").order_by('-add_time')
    pagination = Paginator(so_news, 20)
    page_number = request.GET.get('page')
    newsdata_final = pagination.get_page(page_number)
    context = {
        'Sowasthya': Sowasthya,
        'so_news': newsdata_final
    }
    return render(request, 'home/sowasthya.html', context)
# bichar


def bichar(request):
    Bichar = Category.objects.filter(title="विचार")
    bi_news = News.objects.filter(
        category__title="विचार").order_by('-add_time')
    pagination = Paginator(bi_news, 20)
    page_number = request.GET.get('page')
    newsdata_final = pagination.get_page(page_number)
    context = {
        'Bichar': Bichar,
        'bi_news': newsdata_final
    }
    return render(request, 'home/bichar.html', context)
# rochak


def rochak(request):
    Rochak = Category.objects.filter(title="रोचक")
    ro_news = News.objects.filter(
        category__title="रोचक").order_by('-add_time')
    pagination = Paginator(ro_news, 20)
    page_number = request.GET.get('page')
    newsdata_final = pagination.get_page(page_number)
    context = {
        'Rochak': Rochak,
        'ro_news': newsdata_final
    }
    return render(request, 'home/rochak.html', context)
