from app.serializers import MemberSerializer
from app.models import member
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.db.models import Avg
from json import dumps
# Create your views here.

@api_view(['GET'])
def search(request):
	query= request.GET['query']
	members= member.objects.filter(caption__search=query)[:10]
	serializers=  MemberSerializer(members,many=True)
	return Response(serializers.data)

@api_view(['GET'])
def count(request):
	memcount= member.objects.all().count()
	return HttpResponse(dumps({ "count":memcount}),content_type="application/json")

@api_view(['GET'])
def ethnicity(request):
	ethnicity= request.GET['ethnicity']
	avg_weight= member.objects.filter(ethnicity=ethnicity).aggregate(Avg('weight'))
	avg_height= member.objects.filter(ethnicity=ethnicity).aggregate(Avg('height'))
	return HttpResponse(dumps({
		"ethnicity":ethnicity,
		"mean_weight":avg_weight["weight__avg"],
		"mean_height":avg_height["height__avg"]
		}),content_type="application/json")

@api_view(['GET'])
def social(request):
	choice={
	'yes':True,
	'no': False,
	'y':True,
	'n': False,
	'': False,
	'': False,
	}
	vegetarian= request.GET['vegetarian'].lower()
	drink= request.GET['drink'].lower()
	try:
		members= member.objects.filter(is_veg=choice[vegetarian],drink=choice[drink])[:10]
		serializers= MemberSerializer(members,many=True)
		return Response(serializers.data)
	except:
		return HttpResponse(dumps({
			"message":"BAD_REQUEST, use YES/NO"
			}),content_type="application/json")