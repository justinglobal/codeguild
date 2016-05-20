from django.shortcuts import render

from . import logic

def render_index(request):
    all_fluts = logic.get_all_fluts()

    template_args = {
        'all_fluts': all_fluts,
    }
    return render(request, 'flutter/index.html', template_args)

def render_post_page(request):
    return render(request, 'flutter/post.html', {})

def render_post_ack(request):

    user_name = request.POST['user_name']
    text_of_flut = request.POST['text_of_flut']
    # time_stamp = request.POST['time_stamp']

    time_stamp = logic.create_and_save_new_flut(user_name, text_of_flut)
    # time_stamp = logic.

    template_args = {
        'user_name': user_name,
        'text_of_flut': text_of_flut,
        'time_stamp': time_stamp,
    }

    return render(request, 'flutter/ack.html', template_args)
