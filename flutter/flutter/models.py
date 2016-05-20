from django.db import models

import datetime

class Flut(models.Model):

    user_name = models.TextField()
    text_of_flut = models.TextField()
    time_stamp = models.DateTimeField()

    def __str__(self):
        return '{} - {} - {}'.format(self.user_name , self.text_of_flut, self.time_stamp)

    def __repr__(self):
        return 'Flut(user_name={!r}, text_of_flut={!r}, time_stamp={!r})'.format(
            self.user_name,
            self.text_of_flut,
            self.time_stamp,
        )
