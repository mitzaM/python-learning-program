from models import Quest, Page
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

def index(request):
	quest_list = Quest.objects.all().order_by('name')
	return render_to_response('index.html', {
				'quest_list': quest_list
				})

def quest(request, quest_id):
	q = get_object_or_404(Quest, pk = quest_id)
	page_list = q.page_set.all()
	return render_to_response('quest.html', {
				'questionnaire': q,
				'page_list': page_list
				})

def page(request, quest_id, page_id):
	p = get_object_or_404(Page, order = page_id, quest = quest_id)
	q = get_object_or_404(Quest, pk = quest_id)
	question_list = p.question_set.all()
	return render_to_response('page.html', {
				'questionnaire': q,
				'page': p,
				'question_list': question_list
				},
				context_instance = RequestContext(request))

def results(request, quest_id):
	q = get_object_or_404(Quest, pk = quest_id)
	result_list = q.result_set.all()
	return render_to_response('result.html', {
				'questionnaire': q,
				'result_list': result_list
				})

def answer(request, quest_id, page_id):
	p = get_object_or_404(Page, order = page_id, quest = quest_id)
	order = p.order + 1
	return HttpResponseRedirect(reverse('dlp.chestionare.views.page', args=(quest_id, order)))
