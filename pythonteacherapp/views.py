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
                if user.password == password:
                    request.session['name'] = user.name
                    request.session['email'] = user.email
                    request.session['user_id'] = user.id
                    if user.test_marks == 0:
                        questions = PreTest.objects.all()
                        return render(request, 'index.html', {'questions': questions})
                    elif user.test_marks < 40:
                        return render(request, 'low_level/index.html')
                    elif user.test_marks < 75:
                        return render(request, 'medium_level/index.html')
                    else:
                        return render(request, 'high_level/index.html')
                else:
                    form = LoginForm()
                    return render(request, 'show.html', {'error_message': 'Invalid login credentials.', 'form': form})
            except User.DoesNotExist:
                form = LoginForm()
                return render(request, 'show.html', {'error_message': 'Invalid login credentials.', 'form': form})
      
    else:
        form = LoginForm()
    return render(request, 'show.html', {'form': form})

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
            return render(request, 'show.html', {'form': form})
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
    if number == 1:
        content = render_to_string('medium_level/assignments/lesson_01/assignment_1.html', {'level':1})
    # elif number == 2:
    #     content = render_to_string('medium_level/lesson_02/index.html')
    # elif number == 3:
    #     content = render_to_string('medium_level/lesson_03/index.html')
    # elif number == 4:
    #     content = render_to_string('medium_level/lesson_04/index.html')
    # elif number == 5:
    #     content = render_to_string('medium_level/lesson_05/index.html')
    # elif number == 6:
    #     content = render_to_string('medium_level/lesson_06/index.html')
    # elif number == 7:
    #     content = render_to_string('medium_level/lesson_07/index.html')
    # elif number == 8:
    #     content = render_to_string('medium_level/lesson_08/index.html')
    # elif number == 9:
    #     content = render_to_string('medium_level/lesson_09/index.html')
    # elif number == 10:
    #     content = render_to_string('medium_level/lesson_10/index.html')
    # elif number == 11:
    #     content = render_to_string('medium_level/lesson_11/index.html')
    # elif number == 12:
    #     content = render_to_string('medium_level/lesson_12/index.html')
    # elif number == 13:
    #     content = render_to_string('medium_level/lesson_13/index.html')
    # elif number == 14:
    #     content = render_to_string('medium_level/lesson_14/index.html')
    # elif number == None:
    #     content = render_to_string('medium_level/welcome.html')
    else:
        content = render_to_string('medium_level/welcome.html')
    
    return HttpResponse(content)

@csrf_exempt
def upload_file(request):
    file_path = os.path.abspath('pythonteacherapp/templates/medium_level/assignments/lesson_01/1.py')
    if not os.path.exists(file_path):
        return HttpResponse(f"File {file_path} does not exist")
    if request.method == "POST":
        uploaded_file = request.FILES.get('file')
        remaining_time = request.POST.get('remaining_time')
        time = remaining_time/60
        if uploaded_file:
            with open(file_path, 'rb') as f: 
                stored_file = f.read()
            uploaded_content = uploaded_file.read()
            similarity_ratio = SequenceMatcher(None, stored_file, uploaded_content).ratio()
            content = f"File uploaded successfully. Similarity ratio: {remaining_time}"
        else:
            content = render_to_string('medium_level/welcome.html')
        return HttpResponse(content)
    else:
        content = ''
    return HttpResponse(content)
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
