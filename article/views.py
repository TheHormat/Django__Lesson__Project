from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages


# Create your views here.
def home__view(request):
    return render(request, "index.html")


def about__view(request):
    return render(request, "about.html")


def contact__view(request):
    return render(request, "contact.html")


def articles__view(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles": articles})


def article__detail__view(request, id):
    article = Article.objects.filter(id = id).first()
    # print(article)
    return render(request, "article-detail.html", {"article": article})


def addarticle__view(request):
    form = ArticleForm(request.POST or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        # save() -> hemise commiti True olaraq qebul edir.
        messages.success(request, "Məqaləniz uğurla əlavə olundu...")
        return redirect("dashboard")

    context = {"form": form}
    return render(request, "addarticle.html", context)


def dashboard__view(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, "dashboard.html", {"articles": articles})
