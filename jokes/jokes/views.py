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
    context = {'name': 'comedian'}
    # context = {'name': request.GET['name']}
    return render(request, 'jokes/form_page.html' , context)

def render_ack(request):
    """Accepts a POST of a setup_text and punchline_text and renders the ack page."""
    setup_text = request.POST['setup_text']
    punchline_text = request.POST['punchline_text']

    logic.save_joke(setup_text , punchline_text)

    context = {
        'setup_text': setup_text,
        'punchline_text': punchline_text
    }
    return render(request, 'jokes/ack.html', context)

def render_index(request):
    """Renders the listing of previous jokes page.
    Makes all_setups and all_punchlines variables from jokes_dict via logic.py.
    defines context dict for rendering page.
    """
    all_setups = logic.get_all_setups()
    all_punchlines = logic.get_all_punchlines()

    context = {
        'setups': all_setups,
        'punchlines': all_punchlines
    }
    return render(request, 'jokes/index.html', context)

# def render_greeting(request):
#     context = {'name': request.GET['name']}
#     return render(request, 'DJANGO_APP_NAME/greet.html', context)
