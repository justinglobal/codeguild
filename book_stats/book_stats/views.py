'''
book_stats views
'''
from django.http import HttpResponse

from .logic import find_word_freq

import datetime

def count(request):
    w = request.GET['w']
    word_freq = find_word_freq(w)
    output = 'word: ' , w , '\n| ' , 'count: ' , word_freq
    output2 = '<html><body><h1>Word: ' , w , '</h1><br><h1>Count: ' , word_freq , '</h1></body></html>'
    return HttpResponse(output2, status=200)

def bookpage(request):
    test = 'Awesome'
    html = '<html><body><h1>' , test , ' This worked!' , '</h1><section><form><input type=text value="type here player"><button name="button" onclick="alert(\'Good job, gangster!\')">submit</button></form></section></body></html>'
    # html = '<html><body><h1>' , test , ' This worked!' , '</h1><section><form><input type=button value="click here" onclick="alert(\'Good job!\')"></form></section></body></html>'
    return HttpResponse(html)


    # html = '<html><body><h1>' , test , ' This worked!' , '</h1></body></html>'

def current_datetime(request):
    now = datetime.datetime.now()
    why_not = 'time to smoke a bowl'
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
