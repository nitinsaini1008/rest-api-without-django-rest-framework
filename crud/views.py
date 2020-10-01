from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import About
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import form_about
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name='dispatch')
class myclass(View):
	def get(self,request,id,*args,**kwargs):
		emp=About.objects.get(id=id)
		data=serialize('json',[emp,])
		d=json.loads(data)
		ans=[]
		for i in d:
			t=i['fields']
			ans.append(t)
		ans=json.dumps(ans)
		return HttpResponse(ans,content_type='application/json')
	def put(self,request,id,*args,**kwargs):
		try:
			emp=About.objects.get(id=id)
			data=request.body
			try:
				upd=json.loads(data)
				main_data={'name':emp.name,'sub':emp.sub,'num':emp.num}
				main_data.update(upd)
				f=form_about(main_data,instance=emp)
				if f.is_valid():
					f.save(commit=True)
					return HttpResponse(json.dumps({'msg':'saved successfully'}),content_type='application/json')
				if f.errors:
					data=json.dumps(f.errors)
					return HttpResponse(data,content_type='application/json',status=404)
			except:
				ans=json.dumps({'msg':'data formate is invalid'})
				return HttpResponse(ans,content_type='application/json',status=404)
		except:
			ans=json.dumps({'msg':'id if invalid'})
			return HttpResponse(ans,content_type='application/json',status=404)
	def delete(self,request,id,*args,**kwargs):
		try:
			emp=About.objects.get(id=id)
			a,b=emp.delete()
			if a==1:
				return HttpResponse(json.dumps({'msg':'deleted successfully'}),content_type='application/json')
			else:
				return HttpResponse(json.dumps({'msg':'unable to delete'}),content_type='application/json')
		except:
			ans=json.dumps({'msg':'id if invalid'})
			return HttpResponse(ans,content_type='application/json',status=404)
@method_decorator(csrf_exempt,name='dispatch')
class my_class_2(View):
	def get(self,request,*args,**kwargs):
		emp=About.objects.all()
		data=serialize('json',emp)
		d=json.loads(data)
		ans=[]
		for i in d:
			t=i['fields']
			ans.append(t)
		ans=json.dumps(ans)
		return HttpResponse(ans,content_type='application/json')
	def post(self,request,*args,**kwargs):
		data=request.body
		try:
			json_data=json.loads(data)
			f=form_about(json_data)
			if f.is_valid():
				f.save(commit=True)
				return HttpResponse(json.dumps({'msg':'saved successfully'}),content_type='application/json')
			if f.errors:
				data=json.dumps(f.errors)
				return HttpResponse(data,content_type='application/json')
		except:
			json_data=json.dumps({'msg':'entervalid data'})
		return HttpResponse(json_data,content_type='application/json')

