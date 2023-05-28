from django.shortcuts import render, redirect
from django.http import HttpResponse
from pythonteacherapp.forms import UserForm
from pythonteacherapp.forms import LoginForm
from pythonteacherapp.models import User
from pythonteacherapp.models import PreTest
from django.http import HttpResponse
from django.template.loader import render_to_string
import subprocess
import os
from django.views.decorators.csrf import csrf_exempt
from difflib import SequenceMatcher
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from django.conf import settings
import ast
import tempfile

loging_user = {}

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = UserForm()
    return render(request,'register.html',{'form':form})

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                global loging_user
                loging_user= user
                if user.password == password:
                    request.session['name'] = user.name
                    request.session['email'] = user.email
                    request.session['user_id'] = user.id
                    if user.test_marks == 0:
                        questions = PreTest.objects.all()
                        return render(request, 'index.html', {'questions': questions})
                    elif user.test_marks < 40:
                        return render(request, 'low_level/index.html', {'user': user})
                    elif user.test_marks < 75:
                        return render(request, 'medium_level/index.html', {'user': user})
                    else:
                        return render(request, 'high_level/index.html', {'user': user})
                else:
                    form = LoginForm()
                    return render(request, 'login.html', {'error_message': 'Invalid login credentials.', 'form': form})
            except User.DoesNotExist:
                form = LoginForm()
                return render(request, 'login.html', {'error_message': 'Invalid login credentials.', 'form': form})  
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def addnew(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = UserForm()
    return render(request, 'index.html',{'form':form})

def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'edit.html', {'user': user})

def updatetestmark(request):
    if request.method == 'POST':
        questions = PreTest.objects.all()
        total_marks = 20
        obtained_marks = 0
        for question in questions:
            selected_option = request.POST.get(f'question{question.id}')
            print(question.correct_answer)
            if question.correct_answer == selected_option:
                obtained_marks += 1
        # calculate percentage
        percentage = obtained_marks / total_marks * 100
        user_id = request.session.get('user_id')
        if user_id:
        # retrieve user object
            user = User.objects.get(id=user_id)
            user.test_marks = percentage
            user.save()
            if user.test_marks < 40:
                return render(request, 'low_level/index.html')
            elif user.test_marks < 75:
                return render(request, 'medium_level/index.html')
            else:
                return render(request, 'high_level/index.html')
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})
    else:
        questions = PreTest.objects.all()
        return render(request, 'index.html', {'questions': questions})
    # user = User.objects.get(id=id)
    # form = UserForm(request.POST, instance = user)
    # if form.is_valid():
    #     form.save()
    #     return redirect("/")
    # return render(request, 'edit.html', {'user': user})

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/')

# Medium Level
def chapter(request):
    number = request.GET.get('lesson')
    number = int(number) if number else None
    global loging_user
    if loging_user.test_marks < 40 :
        if number == 1:
            content = render_to_string('low_level/chapter_01/index.html')
        elif number == 2:
            content = render_to_string('low_level/lesson_02/index.html')
        elif number == 3:
            content = render_to_string('low_level/lesson_03/index.html')
        elif number == 4:
            content = render_to_string('low_level/lesson_04/index.html')
        elif number == 5:
            content = render_to_string('low_level/lesson_05/index.html')
        elif number == 6:
            content = render_to_string('low_level/lesson_06/index.html')
        elif number == 7:
            content = render_to_string('low_level/lesson_07/index.html')
        elif number == 8:
            content = render_to_string('low_level/lesson_08/index.html')
        elif number == 9:
            content = render_to_string('low_level/lesson_09/index.html')
        elif number == 10:
            content = render_to_string('low_level/lesson_10/index.html')
        elif number == 11:
            content = render_to_string('low_level/lesson_11/index.html')
        elif number == 12:
            content = render_to_string('low_level/lesson_12/index.html')
        elif number == 13:
            content = render_to_string('low_level/lesson_13/index.html')
        elif number == 14:
            content = render_to_string('low_level/lesson_14/index.html')
        elif number == None:
            content = render_to_string('low_level/welcome.html')
        else:
            content = render_to_string('low_level/welcome.html')

    elif loging_user.test_marks < 75 :
        if number == 1:
            content = render_to_string('medium_level/chapter_01/index.html')
        elif number == 2:
            content = render_to_string('medium_level/lesson_02/index.html')
        elif number == 3:
            content = render_to_string('medium_level/lesson_03/index.html')
        elif number == 4:
            content = render_to_string('medium_level/lesson_04/index.html')
        elif number == 5:
            content = render_to_string('medium_level/lesson_05/index.html')
        elif number == 6:
            content = render_to_string('medium_level/lesson_06/index.html')
        elif number == 7:
            content = render_to_string('medium_level/lesson_07/index.html')
        elif number == 8:
            content = render_to_string('medium_level/lesson_08/index.html')
        elif number == 9:
            content = render_to_string('medium_level/lesson_09/index.html')
        elif number == 10:
            content = render_to_string('medium_level/lesson_10/index.html')
        elif number == 11:
            content = render_to_string('medium_level/lesson_11/index.html')
        elif number == 12:
            content = render_to_string('medium_level/lesson_12/index.html')
        elif number == 13:
            content = render_to_string('medium_level/lesson_13/index.html')
        elif number == 14:
            content = render_to_string('medium_level/lesson_14/index.html')
        elif number == None:
            content = render_to_string('medium_level/welcome.html')
        else:
            content = render_to_string('medium_level/welcome.html')

    else:
        if number == 1:
            content = render_to_string('high_level/chapter_01/index.html')
        elif number == 2:
            content = render_to_string('high_level/lesson_02/index.html')
        elif number == 3:
            content = render_to_string('high_level/lesson_03/index.html')
        elif number == 4:
            content = render_to_string('high_level/lesson_04/index.html')
        elif number == 5:
            content = render_to_string('high_level/lesson_05/index.html')
        elif number == 6:
            content = render_to_string('high_level/lesson_06/index.html')
        elif number == 7:
            content = render_to_string('high_level/lesson_07/index.html')
        elif number == 8:
            content = render_to_string('high_level/lesson_08/index.html')
        elif number == 9:
            content = render_to_string('high_level/lesson_09/index.html')
        elif number == 10:
            content = render_to_string('high_level/lesson_10/index.html')
        elif number == 11:
            content = render_to_string('high_level/lesson_11/index.html')
        elif number == 12:
            content = render_to_string('high_level/lesson_12/index.html')
        elif number == 13:
            content = render_to_string('high_level/lesson_13/index.html')
        elif number == 14:
            content = render_to_string('high_level/lesson_14/index.html')
        elif number == None:
            content = render_to_string('high_level/welcome.html')
        else:
            content = render_to_string('high_level/welcome.html')
    return HttpResponse(content)

def execute_code(request):
    if request.method == 'POST':
        # Get the code from the request
        code = request.POST.get('code', '')
        # print(code)
        try:
            # Save the code to a temporary file
            filename = 'temp.py'
            with open(filename, 'w') as f:
                f.write(code)
            # Execute the Python code
            result = subprocess.run(['python', filename], capture_output=True, text=True)
            # print(result)
        finally:
            # Delete the temporary file
            os.remove(filename)
            # subprocess.run(['rm', filename])
        if result.stderr:
            return HttpResponse(result.stderr)
        else:
            return HttpResponse(result.stdout)

def assignment(request):
    number = request.GET.get('lesson')
    number = int(number) if number else None
    global loging_user
    if loging_user.test_marks < 40 :
        if number == 1:
            content = render_to_string('low_level/assignments/lesson_01/assignment_1.html', {'level':loging_user.assignment_progress_level})
        elif number == 2:
            content = render_to_string('low_level/assignments/lesson_02/assignment_2.html', {'level':loging_user.assignment_progress_level})
        elif number == 3:
            content = render_to_string('low_level/assignments/lesson_03/assignment_3.html', {'level':loging_user.assignment_progress_level})
        elif number == 4:
            content = render_to_string('low_level/assignments/lesson_04/assignment_4.html', {'level':loging_user.assignment_progress_level})
        elif number == 5:
            content = render_to_string('low_level/assignments/lesson_05/assignment_5.html', {'level':loging_user.assignment_progress_level})
        elif number == 6:
            content = render_to_string('low_level/assignments/lesson_06/assignment_6.html', {'level':loging_user.assignment_progress_level})
        elif number == 7:
            content = render_to_string('low_level/assignments/lesson_07/assignment_7.html', {'level':loging_user.assignment_progress_level})
        elif number == 8:
            content = render_to_string('low_level/assignments/lesson_08/assignment_8.html', {'level':loging_user.assignment_progress_level})
        elif number == 9:
            content = render_to_string('low_level/assignments/lesson_09/assignment_9.html', {'level':loging_user.assignment_progress_level})
        elif number == 10:
            content = render_to_string('low_level/assignments/lesson_10/assignment_10.html', {'level':loging_user.assignment_progress_level})
        elif number == 11:
            content = render_to_string('low_level/assignments/lesson_11/assignment_11.html', {'level':loging_user.assignment_progress_level})
        elif number == 12:
            content = render_to_string('low_level/assignments/lesson_12/assignment_12.html', {'level':loging_user.assignment_progress_level})
        elif number == 13:
            content = render_to_string('low_level/assignments/lesson_13/assignment_13.html', {'level':loging_user.assignment_progress_level})
        elif number == 14:
            content = render_to_string('low_level/assignments/lesson_14/assignment_14.html', {'level':loging_user.assignment_progress_level})
        elif number == None:
            content = render_to_string('low_level/welcome.html')
        else:
            content = render_to_string('low_level/welcome.html')

    elif loging_user.test_marks < 75 :
        if number == 1:
            content = render_to_string('medium_level/assignments/lesson_01/assignment_1.html', {'level':loging_user.assignment_progress_level})
        elif number == 2:
            content = render_to_string('medium_level/assignments/lesson_02/assignment_2.html', {'level':loging_user.assignment_progress_level})
        elif number == 3:
            content = render_to_string('medium_level/assignments/lesson_03/assignment_3.html', {'level':loging_user.assignment_progress_level})
        elif number == 4:
            content = render_to_string('medium_level/assignments/lesson_04/assignment_4.html', {'level':loging_user.assignment_progress_level})
        elif number == 5:
            content = render_to_string('medium_level/assignments/lesson_05/assignment_5.html', {'level':loging_user.assignment_progress_level})
        elif number == 6:
            content = render_to_string('medium_level/assignments/lesson_06/assignment_6.html', {'level':loging_user.assignment_progress_level})
        elif number == 7:
            content = render_to_string('medium_level/assignments/lesson_07/assignment_7.html', {'level':loging_user.assignment_progress_level})
        elif number == 8:
            content = render_to_string('medium_level/assignments/lesson_08/assignment_8.html', {'level':loging_user.assignment_progress_level})
        elif number == 9:
            content = render_to_string('medium_level/assignments/lesson_09/assignment_9.html', {'level':loging_user.assignment_progress_level})
        elif number == 10:
            content = render_to_string('medium_level/assignments/lesson_10/assignment_10.html', {'level':loging_user.assignment_progress_level})
        elif number == 11:
            content = render_to_string('medium_level/assignments/lesson_11/assignment_11.html', {'level':loging_user.assignment_progress_level})
        elif number == 12:
            content = render_to_string('medium_level/assignments/lesson_12/assignment_12.html', {'level':loging_user.assignment_progress_level})
        elif number == 13:
            content = render_to_string('medium_level/assignments/lesson_13/assignment_13.html', {'level':loging_user.assignment_progress_level})
        elif number == 14:
            content = render_to_string('medium_level/assignments/lesson_14/assignment_14.html', {'level':loging_user.assignment_progress_level})
        elif number == None:
            content = render_to_string('medium_level/welcome.html')
        else:
            content = render_to_string('medium_level/welcome.html')

    else :
        if number == 1:
            content = render_to_string('high_level/assignments/lesson_01/assignment_1.html', {'level':loging_user.assignment_progress_level})
        elif number == 2:
            content = render_to_string('high_level/assignments/lesson_02/assignment_2.html', {'level':loging_user.assignment_progress_level})
        elif number == 3:
            content = render_to_string('high_level/assignments/lesson_03/assignment_3.html', {'level':loging_user.assignment_progress_level})
        elif number == 4:
            content = render_to_string('high_level/assignments/lesson_04/assignment_4.html', {'level':loging_user.assignment_progress_level})
        elif number == 5:
            content = render_to_string('high_level/assignments/lesson_05/assignment_5.html', {'level':loging_user.assignment_progress_level})
        elif number == 6:
            content = render_to_string('high_level/assignments/lesson_06/assignment_6.html', {'level':loging_user.assignment_progress_level})
        elif number == 7:
            content = render_to_string('high_level/assignments/lesson_07/assignment_7.html', {'level':loging_user.assignment_progress_level})
        elif number == 8:
            content = render_to_string('high_level/assignments/lesson_08/assignment_8.html', {'level':loging_user.assignment_progress_level})
        elif number == 9:
            content = render_to_string('high_level/assignments/lesson_09/assignment_9.html', {'level':loging_user.assignment_progress_level})
        elif number == 10:
            content = render_to_string('high_level/assignments/lesson_10/assignment_10.html', {'level':loging_user.assignment_progress_level})
        elif number == 11:
            content = render_to_string('high_level/assignments/lesson_11/assignment_11.html', {'level':loging_user.assignment_progress_level})
        elif number == 12:
            content = render_to_string('high_level/assignments/lesson_12/assignment_12.html', {'level':loging_user.assignment_progress_level})
        elif number == 13:
            content = render_to_string('high_level/assignments/lesson_13/assignment_13.html', {'level':loging_user.assignment_progress_level})
        elif number == 14:
            content = render_to_string('high_level/assignments/lesson_14/assignment_14.html', {'level':loging_user.assignment_progress_level})
        elif number == None:
            content = render_to_string('high_level/welcome.html')
        else:
            content = render_to_string('high_level/welcome.html')
    
    return HttpResponse(content)

@csrf_exempt
def upload_file(request):
    content = ''
    global loging_user
    file_path = os.path.abspath('pythonteacherapp/templates/medium_level/assignments/lesson_01/1.py')
    if not os.path.exists(file_path):
        return HttpResponse(f"File {file_path} does not exist")
    if request.method == "POST":
        uploaded_file = request.FILES.get('file')
        file_copy = uploaded_file.file # make a copy of the file object
        result_similarity_ratio = run_the_file(file_copy, file_path)

        # uploaded_file = request.FILES.get('file')
        # result_similarity_ratio = run_the_file(uploaded_file, file_path)
        # uploaded_file_2 = request.FILES.get('file')
        remaining_time = request.POST.get('remaining_time')
        time = round((float(remaining_time)/60))
        # print(result_similarity_ratio); 
        if uploaded_file:
            with open(file_path, 'rb') as f: 
                stored_file = f.read()
            uploaded_content = uploaded_file.read()
            if len(uploaded_content) == 0:
                print("The uploaded file is empty.")
            else:
                print(uploaded_content)
                similarity_ratio = SequenceMatcher(None, stored_file, uploaded_content).ratio()
                result = round(result_similarity_ratio, 2)
                code = round(similarity_ratio, 2)
                if result == 2:
                    content = "Syntax Error - Check again the code !"
                elif result != 1:
                    content = "Check again the code and make sure that all the keywords are included!"
                else:
                    task = get_fuzzy_output(code, time)
                    # content = f"Final result : {task}"
                    if task =='again':
                        return ''
                    elif task== 'next_level':
                        loging_user.assignment_progress_level += 1
                    elif task =='next_chapter':
                        loging_user.assignment_progress_level = 1
                        loging_user.chapter_level += 1        

            # content = f"File uploaded successfully. Similarity ratio: {result}"
        else:
            content = render_to_string('medium_level/welcome.html')
        return HttpResponse(content)
    else:
        content = ''
    return HttpResponse(content)

def run_the_file(uploaded_file, file_path):
    try:
        # Run a Python file and wait for it to complete
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name
        result_of_uploaded_file = subprocess.run(['python', temp_file_path], capture_output=True, text=True, input='John\nDoe\n', check=True)
        result_of_stored_file = subprocess.run(['python', file_path], capture_output=True, text=True, input='John\nDoe\n', check=True)
        similarity_ratio_of_output = SequenceMatcher(None, result_of_uploaded_file.stdout, result_of_stored_file.stdout ).ratio()
        return similarity_ratio_of_output
    except subprocess.CalledProcessError as error:
        # Handle any errors that occurred while running the file
        return 2

def run_python_code(code):
    try:
        output = subprocess.check_output(['python', '-c', code])
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

def run_python_file(file_path):
    try:
        output = subprocess.check_output(['python', file_path])
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')
    
def handle_uploaded_file(uploaded_file):
    media_root = settings.MEDIA_ROOT
    filename = uploaded_file.name
    file_path = os.path.join(media_root, filename)
    with open(file_path, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
    return file_path

def get_fuzzy_output(calculated_marks, calculated_time):

    marks = ctrl.Antecedent(np.arange(0, 101, 1), 'marks')
    time = ctrl.Antecedent(np.arange(0, 51, 1), 'time')
    task = ctrl.Consequent(np.arange(0, 101, 1), 'task') 

    marks['low'] = fuzz.trapmf(marks.universe, [0, 40, 50])
    marks['average'] = fuzz.trapmf(marks.universe, [45, 75, 85])
    marks['high'] = fuzz.trapmf(marks.universe, [80, 100, 100])

    time['poor'] = fuzz.trapmf(time.universe, [0, 20, 25])
    time['average'] = fuzz.trapmf(time.universe, [20, 35, 40])
    time['excellent'] = fuzz.trapmf(time.universe, [35, 50, 50])

    # task.universe = range(101) 
    task['again'] = fuzz.trimf(task.universe, [0, 0, 50])
    task['next_level'] = fuzz.trimf(task.universe, [30, 50, 70])
    task['next_chapter'] = fuzz.trimf(task.universe, [50, 100, 100])

    # Create fuzzy rules
    rule1 = ctrl.Rule(marks['low'] & time['poor'], task['again'])
    rule2 = ctrl.Rule(marks['average'] & time['average'], task['next_level'])
    rule3 = ctrl.Rule(marks['high'] & time['excellent'], task['next_chapter'])

    # Create fuzzy system
    task_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    task_sim = ctrl.ControlSystemSimulation(task_ctrl)

    # Set input values
    task_sim.input['marks'] = calculated_marks
    task_sim.input['time'] = calculated_time
    print(calculated_marks)
    print(calculated_time)
    # Compute output
    task_sim.compute()

    # Get fuzzy output set
    task_output = task_sim.output['task']
    print(task_output)
    # task_output =  round(task_output)
    # task_output = np.array(task_output).ravel()
    # print(type(task_output));
    # print("task_output shape:", task_output.shape)
    # print("task universe shape:", task.universe.shape)
    # # Defuzzify to obtain crisp output value
    task_crisp = fuzz.defuzz(task.universe, task_output, 'centroid')
    print(task_crisp);
    # Map crisp output to linguistic label
    task_again_mem = fuzz.interp_membership(task.universe, task_again, task_crisp)
    task_next_level_mem = fuzz.interp_membership(task.universe, task_next_level, task_crisp)
    task_next_chapter_mem = fuzz.interp_membership(task.universe, task_next_chapter, task_crisp)

    # Print the degree of membership for each label
    print('Again:', task_again_mem)
    print('Next Level:', task_next_level_mem)
    print('Next Chapter:', task_next_chapter_mem)

    # Determine the label with the highest degree of membership
    if task_again_mem > task_next_level_mem and task_again_mem > task_next_chapter_mem:
        print('Task: Again')
    elif task_next_level_mem > task_again_mem and task_next_level_mem > task_next_chapter_mem:
        print('Task: Next Level')
    else:
        print('Task: Next Chapter')

    #return the output
    return task_crisp








# def get_fuzzy_output(calculated_marks, calculated_time):
#     # Define fuzzy sets for inputs and output
#     # marks = ctrl.Antecedent(np.arange(0, 101, 1), 'marks')
#     # time = ctrl.Antecedent(np.arange(0, 51, 1), 'time')
#     # task = ctrl.Consequent(np.arange(0, 101, 1), 'task')

#     marks = ctrl.Antecedent(np.arange(0, 101, 1), 'marks')
#     time = ctrl.Antecedent(np.arange(0, 51, 1), 'time')
#     task = ctrl.Consequent(np.arange(0, 101, 1), 'task') 

#     # # Define membership functions for marks
#     # marks['low'] = fuzz.trapmf(marks.universe, [0, 0, 40, 40])
#     # marks['average'] = fuzz.trapmf(marks.universe, [35, 35, 75, 75])
#     # marks['high'] = fuzz.trapmf(marks.universe, [70, 70, 100, 100])

#     # # Define membership functions for time
#     # time['poor'] = fuzz.trapmf(time.universe, [0, 0, 20, 20])
#     # time['average'] = fuzz.trapmf(time.universe, [15, 15, 35, 35])
#     # time['excellent'] = fuzz.trapmf(time.universe, [30, 30, 50, 50])

#     # # Define membership functions for output
#     # task['again'] = fuzz.trimf(task.universe, [0, 0, 50])
#     # task['next level'] = fuzz.trimf(task.universe, [50, 75, 100])
#     # task['next chapter'] = fuzz.trimf(task.universe, [75, 100, 100])

#     marks['low'] = fuzz.trapmf(marks.universe, [0, 0, 40, 50])
#     marks['average'] = fuzz.trapmf(marks.universe, [35, 45, 75, 85])
#     marks['high'] = fuzz.trapmf(marks.universe, [70, 80, 100, 100])

#     time['average'] = fuzz.trapmf(time.universe, [15, 20, 35, 40])
#     time['excellent'] = fuzz.trapmf(time.universe, [30, 35, 50, 50])
#     time['poor'] = fuzz.trapmf(time.universe, [0, 0, 20, 25])

#     # task.universe = range(101) 
#     task['again'] = fuzz.trimf(task.universe, [0, 0, 50])
#     task['next_level'] = fuzz.trimf(task.universe, [30, 50, 70])
#     task['next_chapter'] = fuzz.trimf(task.universe, [50, 100, 100])

#     # Visualize membership functions (optional)
#     # marks.view()
#     # time.view()
#     # task.view()

#     # # Define fuzzy rules
#     # rule1 = ctrl.Rule(marks['low'] & time['poor'], task['again'])
#     # rule2 = ctrl.Rule(marks['average'] & time['average'], task['next_level'])
#     # rule3 = ctrl.Rule(marks['high'] & time['excellent'], task['next_chapter'])
    
#     # # Create a control system
#     # task_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

#     # # Create a simulation
#     # task_sim = ctrl.ControlSystemSimulation(task_ctrl)

#     # Create fuzzy rules
#     rule1 = ctrl.Rule(marks['low'] & time['poor'], task['again'])
#     rule2 = ctrl.Rule(marks['average'] & time['average'], task['next_level'])
#     rule3 = ctrl.Rule(marks['high'] & time['excellent'], task['next_chapter'])

#     # Create fuzzy system
#     task_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
#     task_sim = ctrl.ControlSystemSimulation(task_ctrl)

#     # print(calculated_marks)
#     # print(calculated_time)

#     # # Set input values
#     # task_sim.input['marks'] = 60
#     # task_sim.input['time'] =  40

#     # # Compute output
#     # task_sim.compute()

#     # # Print output value
#     # print("Task:", task_sim.output['task'])

#     # # Visualize output (optional)
#     # # task.view(sim=task_sim)

#     # Set input values
#     task_sim.input['marks'] = 35
#     task_sim.input['time'] = 15

#     # Compute output
#     task_sim.compute()

#     # Get fuzzy output set
#     task_output = task_sim.output['task']
#     # task_output =  round(task_output)
#     print(type(task_output));
#     # Defuzzify to obtain crisp output value
#     task_crisp = fuzz.defuzz(task.universe, task_output, 'centroid')
#     print(task_crisp);
#     # Map crisp output to linguistic label
#     task_again_mem = fuzz.interp_membership(task.universe, task_again, task_crisp)
#     task_next_level_mem = fuzz.interp_membership(task.universe, task_next_level, task_crisp)
#     task_next_chapter_mem = fuzz.interp_membership(task.universe, task_next_chapter, task_crisp)

#     # Print the degree of membership for each label
#     print('Again:', task_again_mem)
#     print('Next Level:', task_next_level_mem)
#     print('Next Chapter:', task_next_chapter_mem)

#     # Determine the label with the highest degree of membership
#     if task_again_mem > task_next_level_mem and task_again_mem > task_next_chapter_mem:
#         print('Task: Again')
#     elif task_next_level_mem > task_again_mem and task_next_level_mem > task_next_chapter_mem:
#         print('Task: Next Level')
#     else:
#         print('Task: Next Chapter')

#     #return the output
#     return task_crisp



    # if request.method == 'POST' and request.FILES.get('file'):
    #     file = request.FILES['file']
    #     file_data = file.read()
    #     print(file_data);
    #     response_data = 'success'
    # else:
    #     response_data = 'No file provided'
    # return HttpResponse(response_data)
# import firebase_admin
# import pyrebase
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from firebase_admin import auth

# config = {
#     "apiKey": "AIzaSyDdhydmfc3dKQLHzm9AnY6a7cHjGbr_7pc",
#     "authDomain": "python-teacher-2595a.firebaseapp.com",
#     "projectId": "python-teacher-2595a",
#     "storageBucket": "python-teacher-2595a.appspot.com",
#     "databaseURL": "https://python-teacher-2595a-default-rtdb.firebaseio.com",
#     "messagingSenderId": "585232727948",
#     "appId": "1:585232727948:web:dbde242be498ba124de0a9",
#     "measurementId": "G-B4YNJ7QRQT"
# };
# firebase = pyrebase.initialize_app(config)
# firebase_admin.initialize_app()
# pyrebase_auth = firebase.auth()
# database = firebase.database()

# count = 1
# pre_test_marks = 0
# loging_user = {}
# id_token=""

# @csrf_exempt
# def postsignIn(request):
#     global count
#     global pre_test_marks
#     global loging_user
#     global id_token
#     email = request.POST.get('email')
#     pasw = request.POST.get('password')
#     try:
#         # if there is no error then signin the user with given email and password
#         user = pyrebase_auth.sign_in_with_email_and_password(email, pasw)
#         userId = user['localId']
#         result = database.child("student").get()
#         # print('result')
#         data = result.val()

#         # Filter the data based on the name
#         for key, student in data.items():
#             if student['id'] == userId:
#                 # print(item)
#                 break
#         count = 0
#         pre_test_marks = 0
#         loging_user = student
#         id_token = user['localId']
#     except:
#         message = "Invalid Credentials!!Please Check your Data"
#         return render(request, "login.html", {"message": message})
#     # session_id = user['idToken']
#     # request.session['uid'] = str(session_id)
#     # print(user)
#     if student['pre_test_marks'] == 0:
#         questions = database.child("pre-test").get().val()
#         # print(questions)
#         context = {
#             'student': student,
#             'questions': questions,
#             'count': count,
#         }
#         return render(request, "home.html", context=context)
#     elif student['pre_test_marks'] <= 40:
#         return render(request, "dashboard_01.html", context=student)
#     elif student['pre_test_marks'] <= 70:
#         return render(request, "dashboard_02.html", context=student)
#     else:
#         return render(request, "dashboard_03.html", context=student)


# @csrf_exempt
# def postsignUp(request):
#     global count
#     global pre_test_marks
#     global loging_user
#     email = request.POST.get('email')
#     passs = request.POST.get('password')
#     name = request.POST.get('name')
#     try:
#         # creating a user with the given email and password
#         user = pyrebase_auth.create_user_with_email_and_password(email, passs)
#         uid = user['localId']
#         user['name'] = name
#         user['pre_test_marks'] = 0
#         # print(user)
#         storeStudentData(user)
#         count = 0
#         pre_test_marks = 0
#         loging_user = user
#         id_token = user['localId']
#         # idtoken = request.session['uid']
#         # print(uid)
#     except:
#         return render(request, "register.html")
#     return render(request, "login.html")


# def login(request):
#     return render(request, 'login.html')


# def register(request):
#     return render(request, 'register.html')


# def storeStudentData(request):
#     data = {
#         'name': request['name'],
#         'email': request['email'],
#         'id': request['localId'],
#         'pre_test_marks': request['pre_test_marks']
#     }
#     details = database.child('student').push(data)
#     print(details)


# @csrf_exempt
# def pretest(request):
#     global  loging_user
#     global id_token
#     # user_info = pyrebase_auth.get_account_info(loging_user['idToken'])
#     # print(loging_user)
#     answer = request.POST.get('answer')
#     questions = database.child("pre-test").get().val()
#     # count = global count +1;
#     global count
#     global pre_test_marks
#     # print(answer, ' ', questions[count-1]["correct_answer"]);
#     try:
#         if answer == questions[count - 1]["correct_answer"]:
#             # print(pre_test_marks)
#             pre_test_marks += 1
#         if count == 3:
#             # database.child("student").order_by_child("email").equal_to(loging_user['email']).update({'pre_test_marks': pre_test_marks})
#             # ref = database.child("student").get().val()
#             # students = [student for student in ref.values() if student['email'] == loging_user['email']]
#             # print(id_token)
#             print(id_token)
#             user = auth.update_user(id_token, **{'pre_test_marks': pre_test_marks})
#             print(user)
#             # auth.update_user(user_uid, {"pre_test_marks": pre_test_marks})
#             # database.child("student").child(id_token).update({"pre_test_marks": pre_test_marks})

#             # # store marks -- > redirect to the specific dashboard
#             # print(loging_user['id'])
#             # user_ref = database.child("student").child(loging_user['email']).update({'pre_test_marks': pre_test_marks})
#         else:
#             count += 1
#             context = {
#                 'questions': questions,
#                 'count': count
#             }
#             return render(request, "home.html", context=context)
#     except Exception as e:
#         # return render(request, "register.html")
#         print(e)
#     return render(request, "login.html")
