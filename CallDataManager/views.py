from django.shortcuts import render
#from . import filehandler as fh
# Create your views here.
from os import listdir
from os.path import isfile, join

from django.contrib.staticfiles.utils import get_files
from django.contrib.staticfiles.storage import StaticFilesStorage

def renderPage(request):
  # dataset= getAllFileData()
  # print(dataset)
  
  s = StaticFilesStorage()
  
  mlist = list(get_files(s, location=''))
  print(mlist)
  data = {"list":mlist}
  return render(request,'index.html',data)
  

