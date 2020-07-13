from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = (request.POST.get('text', 'default'))

    # check checkboxe values
    removep = (request.POST.get('removepunc', 'off'))
    capital = (request.POST.get('allcaps', 'off'))
    spaceremove = (request.POST.get('removespace', 'off'))
    newlineremove = (request.POST.get('removenewline', 'off'))
    charcount = (request.POST.get('countchar', 'off'))

    # check which checkbox is on
    if removep == "on":
        punctuations = ''' !()-[]{};:'"\,<>./?@#$%^&*_~ '''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (capital == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Capitalized text', 'analyzed_text': analyzed}
        djtext = analyzed

    if (spaceremove == "on"):
        analyzed = ""
        analyzed = " ".join(djtext.split())

        params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed+char

        params = {'purpose': 'remove extra line', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == "on"):
        analyzed = ""
        count = 0
        for char in djtext:
            count += 1
            analyzed = count

        params = {'purpose': 'count char', 'analyzed_text': analyzed}
        djtext = analyzed


    # if none of the checkboxes are on then return error
    if (removep != "on" and capital != "on" and spaceremove != "on" and newlineremove != "on" and charcount != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
