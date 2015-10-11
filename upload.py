import csv
from app.models import member


ethnicity_choices={
	0:'Asian',
	1:'Indian',
    2:'African Americans',
    3:'Asian Americans',
    4:'European',
    5:'British',
    6:'Jewish',
    7:'Latino',
    8:'Native American',
    9:'Arabic',
	}

def upload():
	f= open("dump-1k.csv",'r')
	reader= csv.reader(f)
	for row in reader:
		try:
			pnum= row[0]
			dob= row[1]
			caption= row[2]
			ethnicity= ethnicity_choices[int(row[3])]
			weight= int(row[4])/1000
			height= int(row[5])
			is_veg= bool(row[6])
			drink= bool(row[7])
			mem= member(
				pnum=int(pnum),
				dob=dob,
				caption=caption,
				ethnicity=ethnicity,
				is_veg=is_veg,
				drink=drink,
				height=height,
				weight=weight
				)
			mem.save()
			print row

		except:
			 print "error with",row
	f.close()		 

upload()

