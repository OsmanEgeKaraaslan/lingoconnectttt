from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Quiz,question
def home(request):

  return render(request,"home.html")

def Quizes(request):
   quizlist=Quiz.objects.all()
   return render(request,"quizes.html",{"quizlist":quizlist})

def quiz(request,quiz_id):

    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request,"Quiz.html",{"quiz":quiz})
def submit_quiz(request, quiz_id):
    fail=0

    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, pk=quiz_id)



        answer_id = request.POST.get('question_{}'.format(quiz.q1.id))
        if answer_id==quiz.q1.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q1.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
        else:
            obj_to_update = question.objects.get(id=quiz.q1.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            fail+=1
        answer_id = request.POST.get('question_{}'.format(quiz.q2.id))
        if answer_id==quiz.q2.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q2.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
        else:
            obj_to_update = question.objects.get(id=quiz.q2.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            fail+=1
        answer_id = request.POST.get('question_{}'.format(quiz.q3.id))
        if answer_id==quiz.q3.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q3.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
        else:
            obj_to_update = question.objects.get(id=quiz.q3.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            fail+=1
        answer_id = request.POST.get('question_{}'.format(quiz.q4.id))
        if answer_id==quiz.q4.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q4.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
        else:
            obj_to_update = question.objects.get(id=quiz.q4.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
        answer_id = request.POST.get('question_{}'.format(quiz.q5.id))
        fail+=1
        if answer_id==quiz.q5.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q5.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
        else:
            obj_to_update = question.objects.get(id=quiz.q5.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
        answer_id = request.POST.get('question_{}'.format(quiz.q6.id))
        fail+=1
        if answer_id==quiz.q6.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q6.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
        else:
            obj_to_update = question.objects.get(id=quiz.q6.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            fail+=1
        answer_id = request.POST.get('question_{}'.format(quiz.q7.id))
        if answer_id==quiz.q7.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q7.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
        else:
            obj_to_update = question.objects.get(id=quiz.q7.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            fail+=1
        answer_id = request.POST.get('question_{}'.format(quiz.q8.id))
        if answer_id==quiz.q8.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q8.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
        else:
            obj_to_update = question.objects.get(id=quiz.q8.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            fail+=1
        answer_id = request.POST.get('question_{}'.format(quiz.q9.id))
        if answer_id==quiz.q9.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q9.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
        else:
            obj_to_update = question.objects.get(id=quiz.q9.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            fail+=1
        answer_id = request.POST.get('question_{}'.format(quiz.q10.id))
        if answer_id==quiz.q10.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q10.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
        else:
            obj_to_update = question.objects.get(id=quiz.q10.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            fail+=1

    score=10-fail
    return render(request, 'submit_quiz.html', {'quiz': quiz},score)
