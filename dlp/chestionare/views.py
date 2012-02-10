from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello world")

def test(request, test_id):
	return HttpResponse("This is test %s." % test_id)

def page(request, test_id, page_id):
	return HttpResponse("This is page %s of test %s." % (page_id, test_id))

def results(request, test_id):
	return HttpResponse("This is the result for %s." % test_id)
