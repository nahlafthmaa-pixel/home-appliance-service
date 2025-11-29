from django.shortcuts import render
from django.views import View
from .models import Collection

class Index(View):
    def get(self,request):
        all_collections = Collection.objects.all()
        context = {"object_list":all_collections}
        return render(request,'index.html',context)

