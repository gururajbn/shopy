from app.models import member
from rest_framework import serializers

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
		model = member
		fields = ('pnum', 'caption', 'ethnicity', 'weight','height','is_veg','drink','dob')



