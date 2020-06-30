from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = (request.GET.get('text', 'default'))
    removep = (request.GET.get('removepunc', 'off'))
    capital = (request.GET.get('allcaps', 'off'))
    spaceremove = (request.GET.get('removespace', 'off'))
    newlineremove = (request.GET.get('removenewline', 'off'))
    charcount = (request.GET.get('countchar', 'off'))

    if removep == "on":
        punctuations = ''' !*()[]'";:,<.>/? '''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:  
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)


    if (capital == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Capitalized text', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    if (spaceremove == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
        

    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed+char

        params = {'purpose': 'remove extra line', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)


    if (charcount == "on"):
        analyzed = ""

        count=0
        for char in djtext:
            count +=1
            analyzed=count

        params = {'purpose': 'count char', 'analyzed_text': analyzed}
        #djtext = analyzed
        #return render(request, 'analyze.html', params)
        
    if (removep != "on" and capital != "on" and spaceremove != "on" and newlineremove != "on" and charcount != "on"):
        return HttpResponse("Error")
    
    
    return render(request,'analyze.html',params)
  


