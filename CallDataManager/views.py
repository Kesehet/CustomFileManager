from django.shortcuts import render
#from . import filehandler as fh
# Create your views here.
from mysite.settings import GET_DATASET as DataSet
def renderPage(request):
  mlist = []
  startIndex = 0
  endIndex = len(DataSet)

   
  for i in range(startIndex,endIndex):
    mlist.append(DataSet[i])


  data = {"list":mlist}

  return render(request,'index.html',data)
  

