from django.shortcuts import render

from . import logic

def render_last_ten(request):
    last_ten = logic.get_last_ten()

    template_args = {
        'last_ten': last_ten,
    }
    return render(request, 'flutter/last_ten.html', template_args)

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
    time_stamp = logic.create_and_save_new_flut(user_name, text_of_flut)

    template_args = {
        'user_name': user_name,
        'text_of_flut': text_of_flut,
        'time_stamp': time_stamp,
    }

    return render(request, 'flutter/ack.html', template_args)

def render_text_of_flut_query(request):

    query_to_search = request.GET['search_query']

    query_result = logic.get_all_fluts_by_text_query(query_to_search)

    template_args = {
        'query_result': query_result,
    }
    return render(request, 'flutter/textquery.html', template_args)

def render_fluts_by_user(request, user_name):
    fluts_by_user = logic.get_all_fluts_by_user(user_name)
    print(fluts_by_user)
    template_args = {
        'fluts_by_user': fluts_by_user,
    }
    return render(request, 'flutter/user_fluts.html', template_args)
