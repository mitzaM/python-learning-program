from dlp.chestionare.models import Test
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
	test_list = Test.objects.all().order_by('name')
	return render_to_response('index.html',
				{'test_list': test_list})

def test(request, test_id):
	return HttpResponse("This is test %s." % test_id)

def page(request, test_id, page_id):
	return HttpResponse("This is page %s of test %s." % (page_id, test_id))

def results(request, test_id):
	return HttpResponse("This is the result for %s." % test_id)
