from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .utils import get_mongodb
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from bson.objectid import ObjectId
from django.http import Http404
from .forms import AuthorForm, QuoteForm
from .models import Author, Quote, Tag

def main(request, page=1):
    db= get_mongodb()
    quotes = db.quotes.find()
    per_page =10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page =paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes':quotes_on_page})


def author_detail(request, author_id):
    db = get_mongodb()
    try:
        author = db.authors.find_one({"_id": ObjectId(author_id)})
    except:
        raise Http404("Author not found")
    if not author:
        raise Http404("Author not found")
    return render(request, 'quotes/author_detail.html', {'author': author})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:main') 
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})


def quotes_by_tag(request, tag):
    quotes = Quote.objects.filter(tags__name__iexact=tag)
    context = {
        'tag': tag,
        'quotes': quotes
    }
    return render(request, 'quotes/quotes_by_tag.html', context)


@login_required
def add_quote(request):
    pass
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
 
            author_name = form.cleaned_data['author']
            tag_names = form.cleaned_data['tags'].split(',')
            author, created = Author.objects.get_or_create(fullname=author_name)
            tags = [Tag.objects.get_or_create(name=tag.strip())[0] for tag in tag_names]
            quote.author = author
            quote.save()
            quote.tags.add(*tags)
            return redirect('quotes:main')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

