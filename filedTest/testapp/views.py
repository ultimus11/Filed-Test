from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SongSerializer
from .serializers import PodcastSerializer
from .serializers import AudiobookSerializer
from .models import song
from .models import podcast
from .models import audiobook
from django.http import HttpResponse
class GETAPIView(APIView):
    '''
    below validateFileTypes method checks whether requested URL is valid 
    and contains required data for CURD operations
    this also perform input validation on id and filetype passed in url
    following the SOLID principles validation is seperately used in every class
    as there it might need some further class specific operations needed in future
    '''
    def validateFileTypes(self,Url):
        fileType=""
        id1=0
        fileTypes=["song","podcast","audiobook"]
        BreakUrlToList = Url.split('/')
        print(BreakUrlToList,"break url to list")
        try:
            if BreakUrlToList[3]:
                fileType=str(BreakUrlToList[3])
            if BreakUrlToList[4]:
                id1=str(BreakUrlToList[4])
        except:
            pass
        if id1!=0 and id1!='':
            try:
                id1=int(id1)
            except:
                id1=-1
        if id1=='':
            id1=0
        if fileType not in fileTypes:
            filetype="invalid_filetype"
            #Check whether file type is correct
        return fileType,id1
    '''
    This is all in one get method for filetypes
    this is used to get list of data as well as id specific data
    the format given is test is applied here for get api routs
    which is <filetype>/<AudioFileId>
    here <AudioFileId> parameter is not json as recommended in test
    hence url manipulation is used here although json is widely used in production environment
    This url manupulation applies for all the CURD operation instances
    '''
    def get(self, request, *args, **kwargs):
        Error=False
        print(str(request.path),"here the request")
        fileType,id1 = self.validateFileTypes(request.path)
        print(fileType,id1,"heres the url params")
        if fileType=='song':
            if id1==0:
                Audio = song.objects.all()
                serializer = SongSerializer(Audio, many=True)
            else:
                try:
                    if id1!=-1:
                        Audio = song.objects.get(id=id1)
                        print("song id is",Audio)
                        serializer = SongSerializer(Audio)
                    if id1==-1:
                        Error=True
                except:
                    Error=True
        elif fileType=='podcast':
            if id1==0:
                Audio = podcast.objects.all()
                serializer = PodcastSerializer(Audio, many=True)
            else:
                try:
                    if id1!=-1:
                        Audio = podcast.objects.get(id=id1)
                        serializer = PodcastSerializer(Audio)
                    if id1==-1:
                        Error=True
                except:
                    Error=True
        elif fileType=='audiobook':
            if id1==0:
                Audio = audiobook.objects.all()
                serializer = AudiobookSerializer(Audio, many=True)
            else:
                try:
                    if id1!=-1:
                        Audio = audiobook.objects.get(id=id1)
                        serializer = AudiobookSerializer(Audio)
                    if id1==-1:
                        Error=True
                except:
                    Error=True
        else:
            Error=True
        if Error==False:
            print(serializer.data,"serializer data")
            return Response(serializer.data)
        elif Error==True:
            data={' The request is invalid':'400 bad request'}
            return HttpResponse(data,content_type='application/json',status=400)
class CREATEAPIView(APIView):
    def validateFileTypes(self,Url):
        fileType=""
        id1=0
        fileTypes=["song","podcast","audiobook"]
        BreakUrlToList = Url.split('/')
        print(BreakUrlToList,"break url to list")
        try:
            if BreakUrlToList[3]:
                fileType=str(BreakUrlToList[3])
            if BreakUrlToList[4]:
                id1=str(BreakUrlToList[4])
        except:
            pass
        if id1!=0 and id1!='':
            try:
                id1=int(id1)
            except:
                id1=-1
        if id1=='':
            id1=0
        if fileType not in fileTypes:
            filetype="invalid_filetype"
            #Check whether file type is correct
        return fileType,id1
    def post(self, request, *args, **kwargs):
        Error=False
        audio_data = request.data
        fileType,id1 = self.validateFileTypes(request.path)
        print(fileType,id1,"heres the url params")
        if fileType=='song':
            new_audio = song.objects.create(audioFileType=audio_data["audioFileType"], NameOfTheSong=audio_data["NameOfTheSong"], DurationInNoOfSeconds=audio_data[
                        "DurationInNoOfSeconds"])

            new_audio.save()
            serializer = SongSerializer(new_audio)
        if fileType=='podcast':
            new_audio = podcast.objects.create(audioFileType=audio_data["audioFileType"], NameOfThePodcast=audio_data["NameOfThePodcast"], DurationInNoOfSeconds=audio_data[
                        "DurationInNoOfSeconds"], Host=audio_data["Host"], participents=audio_data["participents"])

            new_audio.save()
            serializer = PodcastSerializer(new_audio)
        if fileType=='audiobook':
            new_audio = audiobook.objects.create(audioFileType=audio_data["audioFileType"], TitleOfTheAudiobook=audio_data["TitleOfTheAudiobook"], AutherOfTheTitle=audio_data["AutherOfTheTitle"], 
                        Narrator=audio_data["Narrator"], DurationInNoOfSeconds=audio_data["DurationInNoOfSeconds"])

            new_audio.save()
            serializer = AudiobookSerializer(new_audio)
        else:
            Error=True
        if Error==False:
            print(serializer.data,"serializer data")
            return Response(serializer.data)
        elif Error==True:
            data={' The request is invalid':'400 bad request'}
            return HttpResponse(data,content_type='application/json',status=400)
class UPDATEAPIView(APIView):
    def validateFileTypes(self,Url):
        fileType=""
        id1=0
        fileTypes=["song","podcast","audiobook"]
        BreakUrlToList = Url.split('/')
        print(BreakUrlToList,"break url to list")
        try:
            if BreakUrlToList[3]:
                fileType=str(BreakUrlToList[3])
            if BreakUrlToList[4]:
                id1=str(BreakUrlToList[4])
        except:
            pass
        if id1!=0 and id1!='':
            try:
                id1=int(id1)
            except:
                id1=-1
        if id1=='':
            id1=0
        if fileType not in fileTypes:
            filetype="invalid_filetype"
            #Check whether file type is correct
        return fileType,id1
    def put(self, request, *args, **kwargs):
        Error=False
        print(str(request.path),"here the request")
        fileType,id1 = self.validateFileTypes(request.path)
        print(fileType,id1,"heres the url params")
        if fileType=="audiobook" and id1!=-1 and id1!=0:
            try:
                audio = audiobook.objects.get(id=id1)
            except:
                Error=True
            serializer = AudiobookSerializer(instance=audio, data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                Error=True
        if fileType=="song" and id1!=-1 and id1!=0:
            try:
                audio = song.objects.get(id=id1)
            except:
                Error=True
            serializer = SongSerializer(instance=audio, data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                Error=True
        if fileType=="podcast" and id1!=-1 and id1!=0:
            try:
                audio = podcast.objects.get(id=id1)
            except:
                Error=True
            serializer = PodcastSerializer(instance=audio, data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                Error=True
        if Error==False:
            return Response(serializer.data)
        elif Error==True:
            data={' The request is invalid':'400 bad request'}
            return HttpResponse(data,content_type='application/json',status=400)
class DELETEAPIView(APIView):
    def validateFileTypes(self,Url):
        fileType=""
        id1=0
        fileTypes=["song","podcast","audiobook"]
        BreakUrlToList = Url.split('/')
        print(BreakUrlToList,"break url to list")
        try:
            if BreakUrlToList[3]:
                fileType=str(BreakUrlToList[3])
            if BreakUrlToList[4]:
                id1=str(BreakUrlToList[4])
        except:
            pass
        if id1!=0 and id1!='':
            try:
                id1=int(id1)
            except:
                id1=-1
        if id1=='':
            id1=0
        if fileType not in fileTypes:
            filetype="invalid_filetype"
            #Check whether file type is correct
        return fileType,id1
    def get(self, request, *args, **kwargs):
        Error=False
        print(str(request.path),"here the request")
        fileType,id1 = self.validateFileTypes(request.path)
        print(fileType,id1,"heres the url params")
        if fileType=="audiobook" and id1!=-1 and id1!=0:
            try:
                audio = audiobook.objects.get(id=id1)
                audio.delete()
            except:
                Error=True
        elif fileType=="song" and id1!=-1 and id1!=0:
            try:
                audio = song.objects.get(id=id1)
                audio.delete()
            except:
                Error=True
        elif fileType=="podcast" and id1!=-1 and id1!=0:
            try:
                audio = podcast.objects.get(id=id1)
                audio.delete()
            except:
                Error=True
        else:
            Error=True
        if Error==False:
            return Response({"message": "{} with id {} has been deleted. Action is sccessful 200 OK".format(fileType,id1)})
        else:
            return Response({"message": "Request is invalid 400"})