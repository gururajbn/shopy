from app.serializers import MemberSerializer
from app.models import member
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from json import dumps
# Create your views here.

@api_view(['GET'])
def search(request):
	query= request.GET['query']
	members= member.objects.filter(caption=query)[:10]
	serializers=  MemberSerializer(members,many=True)
	return Response(serializers.data)

@api_view(['GET'])
def count(request):
	memcount= member.objects.all().count()
	return HttpResponse(dumps({ "count":memcount}),content_type="application/json")

@api_view(['GET'])
def ethnicity(request):
	ethnicity= request.GET['ethnicity']
	members= member.objects.filter(ethnicity=ethnicity)[:10]
	serializers=  MemberSerializer(members,many=True)
	return Response(serializers.data)
