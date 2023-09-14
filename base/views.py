from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random,time,json

from .models import RoomMember

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def getToken(request):
    appId = 'a5905ed6c9b249b1a336a313a09e24f2'
    appCertificate = '83364e28547b43edaad7954fc0f186f1'
    channelName = request.GET.get('channel')
    uid = random.randint(1,230)
    expirationTimeInSeconds = 3600*24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId,appCertificate,channelName,uid,role,privilegeExpiredTs)
    return JsonResponse({'token':token,'uid':uid},safe=False)

def lobby(request):
    return render(request,'base/lobby.html')

def room(request):
    return render(request,'base/room.html')

@csrf_exempt  
def createMember(request):
    data = json.loads(request.body)

    member, created = RoomMember.objects.get_or_create(
        name = data['name'],
        uid = data['UID'],
        room_name = data['room_name']
    )
    return JsonResponse({'name': data['name']},safe=False)

def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')
    member = RoomMember.objects.get(
        uid = uid,
        room_name = room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name},safe=False)

@csrf_exempt  
def deleteMember(request):
    data = json.loads(request.body)

    member = RoomMember.objects.get(
        name = data['name'],
        uid = data['UID'],
        room_name = data['room_name'],
    )
    member.delete()
    return JsonResponse('Member was deleted',safe=False)

