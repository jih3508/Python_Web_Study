from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from django.http import HttpResponseNotAllowed
from .form import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import  login_required

# Create your views here.

def index(request):
    page =request.GET.get('page', '1') # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj} # question_list는 페이징 객체(page_obj)
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect("pybo:detail", question_id = question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question' : question, 'form' : form}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(requset):
    if requset.method == "POST":
        form = QuestionForm(requset.POST)
        if form.is_valid():
            question = form.save(commit=False) # 임시 저장하여 question 객체르 리턴받는다.
            question.author = requset.user # author 속성에 로그인 계정 저장
            question.create_date = timezone.now() # 실제 저장을 위해 작성일시를 설정한다.
            question.save() # 데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    return render(requset, 'pybo/question_form.html', {'form' : form})