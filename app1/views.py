from django.shortcuts import render

from app1.models import HOD,Facality

def details(request):
    hod_count=list(HOD.objects.all())
    faculity_count=list(Facality.objects.all())

    hods=len(hod_count)
    facalites=len(faculity_count)
    total_staf=hods+facalites

    context={
        "hod_count": hods,
        "faculty_count": facalites,
        "total_count": total_staf,
    }
    return render(request,'front/home.html',context)


   
