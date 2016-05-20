from . import models

import datetime

def get_last_ten():
    return models.Flut.objects.all().order_by('time_stamp').reverse()[:10]

def get_all_fluts():
    return models.Flut.objects.all().order_by('time_stamp').reverse()


def create_and_save_new_flut(user_name, text_of_flut):

    time_raw = datetime.datetime.now()
    time_stamp = time_raw.isoformat()

    new_flut = models.Flut(
        user_name=user_name,
        text_of_flut=text_of_flut,
        time_stamp=time_stamp
        )
    print(new_flut)
    new_flut.save()
    return time_stamp

def get_all_fluts_by_text_query(query_to_search):
    return models.Flut.objects.filter(text_of_flut__icontains=query_to_search)

def get_all_fluts_by_user(user_name):
    return models.Flut.objects.filter(user_name=user_name).order_by('time_stamp').reverse()
