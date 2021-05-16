# Filed-Test
Coding Exercise: Write a Flask / FastAPI / Django Web API that simulates the behavior of an audio file  server while using a MongoDB / SQL database. 

# Milestones Achieved 
## Starting With Models
> ParticipantField(models.Field)

```
Created Custom Model Field satisfying Podcast Participants requirement.
As recommended for podcasts there needs a list field which accepts 10 elements where each element has max size 100.
```

##### Use in model:
> participents = ParticipantField()

Other Model field achievements:
```
Datetime, cannot be in the past
string, cannot be larger than 100 characters
Duration in number of seconds – (mandatory, integer, positive)
Participants field set to optional and others to mandatory fields
```
## Only Four Endpoints : Create, Delete, Update, Get 
Following requirements are satisfied.
> Create only four endpoints (make them generic and usable for all audio file types, do not create four endpoints for each of them)
> Use SOLID principles. 
> The classes should be written in such a way that they are easy to test. 
> Use design patterns where you find it suitable

I had performed many tests with Postman also i have written few tests in python program available at `https://github.com/ultimus11/Filed-Test/blob/main/filedTest/test.py`

I had used some URL manipulations Hence I had `tested some URL injection payloads with the help of Burp Suit` for purposes like Redirections and othe cyber attacks.
Endpoints in urls.py looks like
```
urlpatterns = [
    url('GET/', GETAPIView.as_view()),
    url('CREATE/', CREATEAPIView.as_view()),
    url('UPDATE/', UPDATEAPIView.as_view()),
    url('DELETE/', DELETEAPIView.as_view()),
]
```
`The list view and the detailed list view are both handled by GET/ endpoint.`
All endpoints strictly follow given design and routs recommendations for API.
The response of these methods should be one of the following:
- Action is successful: 200 OK 
- The request is invalid: 400 bad request 
- Any error: 500 internal server error 
## Technologies Used/Implemented
- Django Web API
- MongoDB
# How to Use:
### Requirements:
- Python 3.6.5 (Others versions will also work I tested it on 3.6.5)
- Django: pip install Django
- djongo: pip install djongo
- django rest framework: pip install djangorestframework
- MongoDB (Compass optional)
- Will power & dedication to solve the erors (optional: because its easy)
### Initial Steps
- clone this repo
- open cmd/terminal in filedTest directory
- open mongoDB compass and connect
- create database named `filedDb`
- run in terminal `py manage.py makemigrations`
- run in terminal `py manage.py migrate`
- run in terminal `py manage.py createsuperuser`
- give required credentials & set strong password for superuser
- run in terminal `py manage.py runserver`
- Access browsable api via localhost
- Test api via python requests or Postman


Check on http://127.0.0.1:8000/admin/ for admin privileges
## Use Of Endpoints:
Objects:

-song
```json
{
    "id": 2,
    "audioFileType": "song",
    "NameOfTheSong": "Uptown Funk",
    "DurationInNoOfSeconds": 65,
    "UploadedTime": "2021-05-16T15:32:01.772000Z"
}
```
audiobook
```json
{
    "id": 2,
    "audioFileType": "audiobook",
    "TitleOfTheAudiobook": "Hacking planet needs to know11",
    "AutherOfTheTitle": "Sahil Panindre",
    "Narrator": "sahil",
    "DurationInNoOfSeconds": 10,
    "UploadedTime": "2021-05-16T00:00:00.431000Z"
}
```
podcast
```json
{
    "id": 2,
    "audioFileType": "podcast",
    "NameOfThePodcast": "life talk",
    "DurationInNoOfSeconds": 200,
    "UploadedTime": "2021-05-15T23:02:54.069000Z",
    "Host": "sandeep maheshwari",
    "participents": "sahil1,sahi2,sahil3,sahil4,sahil5,sahil6,sahil7,sahil8,sahil9,sahil10"
}
```


### GET:
BASE_URL='http://127.0.0.1:8000/testapp/'
ENDPOINT='GET/'
- The route “<audioFileType>/<audioFileID>” will return the specific audio file
- The route “<audioFileType>” will return all the audio files of that type
Example:
    Audio file type can be one of the following:
1. song
2. podcast
3. audiobook
    To get list of all podcasts use URL : http://127.0.0.1:8000/testapp/GET/podcast/
    
    To get detailed view of podcast use URL : http://127.0.0.1:8000/testapp/GET/podcast/2
    
    Note: `No need to pass json data integer is supported.`
    
    Same goes for other filetypes.
    
    Output:
    http://127.0.0.1:8000/testapp/GET/podcast/
    
    
```json
    [
    {
        "id": 1,
        "audioFileType": "podcast",
        "NameOfThePodcast": "Mann ki baat",
        "DurationInNoOfSeconds": 650,
        "UploadedTime": "2021-05-15T23:00:31.751000Z",
        "Host": "PM Modi",
        "participents": "sahil,viren,aditya"
    },
    {
        "id": 2,
        "audioFileType": "podcast",
        "NameOfThePodcast": "life talk",
        "DurationInNoOfSeconds": 200,
        "UploadedTime": "2021-05-15T23:02:54.069000Z",
        "Host": "sandeep maheshwari",
        "participents": "sahil1,sahi2,sahil3,sahil4,sahil5,sahil6,sahil7,sahil8,sahil9,sahil10"
    },
    {
        "id": 4,
        "audioFileType": "podcast",
        "NameOfThePodcast": "to the moon",
        "DurationInNoOfSeconds": 630,
        "UploadedTime": "2021-05-16T00:06:00.125000Z",
        "Host": "elon musk",
        "participents": ""
    }
]

```
    
with http://127.0.0.1:8000/testapp/GET/podcast/2

```json
    HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
{
    "id": 2,
    "audioFileType": "podcast",
    "NameOfThePodcast": "life talk",
    "DurationInNoOfSeconds": 200,
    "UploadedTime": "2021-05-15T23:02:54.069000Z",
    "Host": "sandeep maheshwari",
    "participents": "sahil1,sahi2,sahil3,sahil4,sahil5,sahil6,sahil7,sahil8,sahil9,sahil10"
}
```

### CREATE

BASE_URL='http://127.0.0.1:8000/testapp/'

ENDPOINT='CREATE/'

The request will have objects releted to filetypes (Already mentioned)


### UPDATE
BASE_URL='http://127.0.0.1:8000/testapp/'

ENDPOINT='UPDATE/'

The request will have objects releted to filetypes (Already mentioned)

- The route be in the format: `<audioFileType>/<audioFileID>`


### DELETE
BASE_URL='http://127.0.0.1:8000/testapp/'

ENDPOINT='DELETE/'

- The route will be in the format: `<audioFileType>/<audioFileID>`


