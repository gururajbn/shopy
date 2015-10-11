from django.db import models

# Create your models here.

ethnicity_choices=(
	('Asian','0'),
	('Indian','1'),
    ('African Americans','2'),
    ('Asian Americans','3'),
    ('European','4'),
    ('British','5'),
    ('Jewish','6'),
    ('Latino','7'),
    ('Native American','8'),
    ('Arabic','9'),
	)

class member(models.Model):
	pnum= models.PositiveSmallIntegerField(blank=True, null=True)
	caption= models.TextField(null=True)
	ethnicity= models.CharField(null=True,max_length=20)
	weight= models.FloatField(blank=True, null=True)
	height= models.PositiveSmallIntegerField(blank=True, null=True)
	is_veg= models.BooleanField(default=True)
	drink= models.BooleanField(default=False)
	dob = models.DateField(null=True)

	class Meta:
		ordering= ['pnum']

	def __unicode__(self):
		return "%s,%s" % (self.pnum,self.caption)