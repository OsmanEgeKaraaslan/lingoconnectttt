from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .forms import RegistrationForm
# Create your views here.
from .models import Quiz,question,UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, pk=quiz_id)



        answer_id1 = request.POST.get('question_{}'.format(quiz.q1.id))
        if answer_id1==quiz.q1.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q1.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
              obj_to_update.save()
        else:
            obj_to_update = question.objects.get(id=quiz.q1.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            obj_to_update.save()
            fail+=1
        answer_id2 = request.POST.get('question_{}'.format(quiz.q2.id))
        if answer_id2==quiz.q2.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q2.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
              obj_to_update.save()
        else:
            obj_to_update = question.objects.get(id=quiz.q2.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            obj_to_update.total_number=obj_to_update.total_number+1
            obj_to_update.save()
            fail+=1
        answer_id3 = request.POST.get('question_{}'.format(quiz.q3.id))
        if answer_id3==quiz.q3.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q3.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
              obj_to_update.save()
        else:
            obj_to_update = question.objects.get(id=quiz.q3.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            obj_to_update.total_number=obj_to_update.total_number+1
            obj_to_update.save()
            fail+=1
        answer_id4 = request.POST.get('question_{}'.format(quiz.q4.id))
        if answer_id4==quiz.q4.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q4.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
              obj_to_update.save()
        else:
            obj_to_update = question.objects.get(id=quiz.q4.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            obj_to_update.total_number=obj_to_update.total_number+1
            obj_to_update.save()
            fail+=1
        answer_id5 = request.POST.get('question_{}'.format(quiz.q5.id))


        if answer_id5==quiz.q5.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q5.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
              obj_to_update.save()
        else:
            obj_to_update = question.objects.get(id=quiz.q5.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            obj_to_update.total_number=obj_to_update.total_number+1
            obj_to_update.save()
            fail+=1

        answer_id6 = request.POST.get('question_{}'.format(quiz.q6.id))


        if answer_id6==quiz.q6.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q6.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
              obj_to_update.save()
        else:
            obj_to_update = question.objects.get(id=quiz.q6.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            obj_to_update.total_number=obj_to_update.total_number+1
            obj_to_update.save()
            fail+=1
        answer_id7 = request.POST.get('question_{}'.format(quiz.q7.id))
        if answer_id7==quiz.q7.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q7.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
              obj_to_update.save()
        else:
            obj_to_update = question.objects.get(id=quiz.q7.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            obj_to_update.total_number=obj_to_update.total_number+1
            obj_to_update.save()
            fail+=1
        answer_id8 = request.POST.get('question_{}'.format(quiz.q8.id))
        if answer_id8==quiz.q8.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q8.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
              obj_to_update.save()
        else:
            obj_to_update = question.objects.get(id=quiz.q8.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            obj_to_update.total_number=obj_to_update.total_number+1
            obj_to_update.save()
            fail+=1
        answer_id9 = request.POST.get('question_{}'.format(quiz.q9.id))
        if answer_id9==quiz.q9.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q9.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
              obj_to_update.save()
        else:
            obj_to_update = question.objects.get(id=quiz.q9.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            obj_to_update.total_number=obj_to_update.total_number+1
            obj_to_update.save()
            fail+=1
        answer_id10 = request.POST.get('question_{}'.format(quiz.q10.id))
        if answer_id10==quiz.q10.correct_answer:
              obj_to_update = question.objects.get(id=quiz.q10.id)
              obj_to_update.number_of_passes=obj_to_update.number_of_passes+1
              obj_to_update.total_number=obj_to_update.total_number+1
              obj_to_update.save()
        else:
            obj_to_update = question.objects.get(id=quiz.q10.id)
            obj_to_update.number_of_fails=obj_to_update.number_of_fails+1
            obj_to_update.total_number=obj_to_update.total_number+1
            obj_to_update.save()
            fail+=1

    score=10-fail
    user_profile = request.user.userprofile
    user_profile.finished_quizzes.add(quiz)

    x=10-fail

    user_profile.update_correct_answers(num_correct=x)
    user_profile.update_false_answers(num_correct=x)

    return render(request, 'submit_quiz.html', {'quiz': quiz,"score":score,"answer_id1":answer_id1,"answer_id2":answer_id2,"answer_id3":answer_id3,"answer_id4":answer_id4,"answer_id5":answer_id5,"answer_id6":answer_id6,"answer_id7":answer_id7,"answer_id8":answer_id8,"answer_id9":answer_id9,"answer_id10":answer_id10})
def register(request):
    global form
    if request.method == 'POST':
        try:

            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()

                # Create UserProfile associated with the new user
                user_profile=UserProfile.objects.create(user=user)
                user_profile.save()
                # Additional logic as needed
                return redirect('login')
            else:
                print(form.errors)
        except Exception as e:
            print(f"Exception: {e}")
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def user_profile(request):
    current_user = request.user

    try:
        profile_instance = UserProfile.objects.get(user=current_user)
    except UserProfile.DoesNotExist:
        return "Please log in"  # Return a string indicating that the user should log in

    # Rest of your view logic...


    # Retrieve information about completed quizzes
    completed_quizzes = profile_instance.finished_quizzes.all()

    context = {
        'user_profile': profile_instance,
        'completed_quizzes': completed_quizzes,
    }

    return render(request, 'user_profile.html', context)
