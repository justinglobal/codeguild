from django.http import HttpResponse
from django.shortcuts import render

from . import logic


def render_ack(request):
    """Accepts a GET of a setup_text and punchline_text and renders the ack page."""
    # comment_text = request.GET['comment_text']
    #
    # logic.save_comment(comment_text)
    setup_text = request.GET['setup_text']
    punchline_text = request.GET['punchline_text']

    logic.save_joke(setup_text , punchline_text)

    return HttpResponse('')


def render_index(request):
    """Renders the listing of jokes page.
    Makes all_setups and all_punchlines variables from jokes_list via logic.py.
    defines context dict for rendering page.
    """
    all_setups = logic.get_all_setups()
    all_punchlines = logic.get_all_punchlines()

    context = {
        'setups': all_setups,
        'punchlines': all_punchlines
    }
    return render(request, 'jokes/ajax_index.html', context)
