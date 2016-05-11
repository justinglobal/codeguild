"""
jokes views.py
"""

from django.http import HttpResponse
from django.shortcuts import render

from . import logic

def render_page(request):
    """Renders the HTML for some random page."""
    return HttpResponse('<html><body><h1>This will be HTML.</h1></body></html>')

def render_form_page(request):
    """Renders the HTML from Template file form_page"""
    context = {'name': 'justin'}
    # context = {'name': request.GET['name']}
    return render(request, 'jokes/form_page.html' , context)

def render_ack(request):
    """Accepts a POST of a joke and renders the ack page."""
    comment_text = request.POST['comment_text']

    logic.save_comment(comment_text)

    context = {
        'comment_text': comment_text,
    }
    return render(request, 'jokes/ack.html', context)

def render_index(request):
    """Renders the listing of previous jokes page.
    """
    comments = logic.get_all_comments()

    context = {
        'comments': comments,
    }
    return render(request, 'jokes/index.html', context)

# def render_greeting(request):
#     context = {'name': request.GET['name']}
#     return render(request, 'DJANGO_APP_NAME/greet.html', context)
