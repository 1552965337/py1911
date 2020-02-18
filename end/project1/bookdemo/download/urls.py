# author sqz
# date 2020/2/17 17:41
# file_name urls
from django.conf.urls import url
from django.http import FileResponse

def load(request,filename):
    return FileResponse(open(filename+".txt","rb"),content_type="application/msword",filename=filename+".txt",as_attachment=True)

app_name='download'
urlpatterns=[
    url(r'^(\w+)/$',load)
]