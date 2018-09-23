from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html', {"football": "the best"})


def barcelona(request):
    return HttpResponse("<h1>Forca Barca<h1>")


def count(request):
    text = request.GET['fulltext']
    wordlist = text.split()
    worddictionary = {}

    for words in wordlist:
        if words in worddictionary:
            worddictionary[words] += 1
        else:
            worddictionary[words] = 1

    sorted_words = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': text, 'count': len(wordlist), 'sorted_words': sorted_words})
