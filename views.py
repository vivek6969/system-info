from django.shortcuts import render
import platform

def index(request):
    z = platform.processor()
    z2 = platform.machine()
    z3 = platform.version()
    z4 = platform.release()
    z5 = platform.node()
    z6 = platform.system()
    z7 = platform.platform()



    return render(request, 'index.html',{'p':z,'m':z2,'v':z3,'r':z4,'n':z5,'s':z6,'p2':z7})
