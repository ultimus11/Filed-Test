from django.db import models
from django.core import checks, exceptions, validators

#Custom Model field
'''
As recommended for podcasts there needs a list field which accepts 10 elements.
where each element has max size 100.
I am not aware of any such list field where max size for element could be specified.

Hence I created A custom model field which supports such list although there are some
listfield available with postgrey and mongo but the problem with them is they dont accept anything for max element size.

In the below field 10 comma seperated elements are allowed with max 100 character length each

'''
class ParticipantField(models.Field):
    description = "A list of 10 participants max element size 100"

    def __init__(self, *args, **kwargs):
        kwargs['blank'] = True
        super().__init__(*args, **kwargs)
    def get_internal_type(self):
        return "CharField"
    #def get_db_prep_value(self,value):
    def get_prep_value(self,value):
        value = super().get_prep_value(value)
        if value is None:
            return value
        newval = value.split(",")
        if len(newval)>10:
            raise Exception('Maximum 10 participents can be added')
        for element in newval:
            if len(element)>100:
                raise Exception('maximum length of participent name must be 100')
        return value
    # def to_python(self, value):
    #     if value is None:
    #         return value
    #     return value

# Create your models here.
#songs
class song(models.Model):
    audioFileType = models.CharField(max_length=100, null=False, blank=False)
    NameOfTheSong = models.CharField(max_length=100, null=False, blank=False)
    DurationInNoOfSeconds = models.PositiveIntegerField(blank=False)
    UploadedTime = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.NameOfTheSong

#podcast
class podcast(models.Model):
    audioFileType = models.CharField(max_length=100, null=False, blank=False)
    NameOfThePodcast = models.CharField(max_length=100, null=False, blank=False)
    DurationInNoOfSeconds = models.PositiveIntegerField(blank=False)
    UploadedTime = models.DateTimeField(auto_now=True, blank=False)
    Host = models.CharField(max_length=100, null=False, blank=False)
    participents = ParticipantField()

    def __str__(self):
        return self.NameOfThePodcast

#audiobook
class audiobook(models.Model):
    audioFileType = models.CharField(max_length=100, null=False, blank=False)
    TitleOfTheAudiobook = models.CharField(max_length=100, null=False, blank=False)
    AutherOfTheTitle = models.CharField(max_length=100, null=False, blank=False)
    Narrator = models.CharField(max_length=100, null=False, blank=False)
    DurationInNoOfSeconds = models.PositiveIntegerField(blank=False)
    UploadedTime = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.TitleOfTheAudiobook
