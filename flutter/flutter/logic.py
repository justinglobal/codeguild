from . import models

import datetime

def get_all_fluts():
    return models.Flut.objects.all()

# def create_and_save_new_user(user_name):
#     filter:
#         user_name = models.UserName(
#             user_name=user_name,
#         )
#         user_name.save()
#     else:
#         pass

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
