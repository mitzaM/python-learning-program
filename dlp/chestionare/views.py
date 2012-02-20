from models import Quest, Page, Response
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
	request.session['total_score'] = 0
	request.session['current_page'] = str(1)
	return render_to_response('quest.html', {
				'questionnaire': q,
				'page_list': page_list
				})

def page(request, quest_id, page_id):
	current_page = request.session['current_page']
	if page_id != current_page:
		return HttpResponseRedirect(reverse('dlp.chestionare.views.page', args=(quest_id, current_page)))

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
	score = request.session['total_score']
	result_list = q.result_set.all();
	if result_list.count() > 0:
		result = result_list[0]
	else:
		result = ""
	for i in range(result_list.count() - 1):
		if score >= result_list[i].limit:
			result = result_list[i+1]
	return render_to_response('result.html', {
				'questionnaire': q,
				'result': result,
				'score': score
				})

def answer(request, quest_id, page_id):
	p = get_object_or_404(Page, order = page_id, quest = quest_id)
	page_count = Quest.objects.get(pk = quest_id).page_set.count()
	question_count, next = p.question_set.count(), p.order + 1
	#ret = ""
	total_score = request.session.get('total_score', 0)
	#ret += "<p>Total score: " + str(total_score) + "</p>"
	for question in p.question_set.all():
		responseId = request.POST['question' + str(question.id)]
		total_score += Response.objects.get(pk = responseId).score
	#ret += "<p>" + str(total_score) + "</p>"
	request.session['total_score'] = total_score
	#return HttpResponse(ret)
	if next > page_count:
		request.session['current_page'] = str(0)
		return HttpResponseRedirect(reverse('dlp.chestionare.views.results', args=(quest_id)))
	else:
		request.session['current_page'] = str(next)
		return HttpResponseRedirect(reverse('dlp.chestionare.views.page', args=(quest_id, next)))
