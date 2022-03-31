from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import ast
from datetime import datetime

# Teachers sign-up section 

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('unsername')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            User.objects.filter(email = email).first()
            messages.info(request, "There is another account with same username or email")
            return redirect('signup')
        except:
            teachers = User.objects.create_user(username, email, password)
            teachers.save()
            messages.info(request, "You have signed up successfully")
            return redirect('signin')

    else:
        return render(request, 'teachers/signup.html')


# Teachers sign-in section


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('checkUsername')
        password = request.POST.get('checkPassword') 
        user = authenticate(username=username, password=password)
        try:
            User.objects.get(username = username)
            login(request, user)
            return redirect(f'/dashboard/{username}')            
        except:
            messages.info(request, "Username or Password was wrong")
            return redirect('signin')   
    else:    
        return render(request, 'teachers/signin.html')


# Teachers sign-out section

def signout(request):
    logout(request)
    messages.info(request, "You have successfully signed-out ")
    return redirect('signin')


# Teachers Dashboard


def dashboard(request, username):
    try:
        statusCounter = ClassForm.objects.get(user = username)
        statusCounter.returned = 0
        statusCounter.not_returned = 0
        allperiod1_objects = period1.objects.filter(Teacher = username)
        allperiod2_objects = period2.objects.filter(Teacher = username)
        allperiod3_objects = period3.objects.filter(Teacher = username)
        allperiod4_objects = period4.objects.filter(Teacher = username)
        for each in allperiod1_objects:
            allperiod1_dict = ast.literal_eval(each.EachPersonData)
            if allperiod1_dict['Status']:
                statusCounter.returned = int(statusCounter.returned+1)
            else:
                statusCounter.not_returned = int(statusCounter.not_returned+1)
        for each in allperiod2_objects:
            allperiod2_dict = ast.literal_eval(each.EachPersonData)
            if allperiod2_dict['Status']:
                statusCounter.returned = int(statusCounter.returned+1)
            else:
                statusCounter.not_returned = int(statusCounter.not_returned+1)
        for each in allperiod3_objects:
            allperiod3_dict = ast.literal_eval(each.EachPersonData)
            if allperiod3_dict['Status']:
                statusCounter.returned = int(statusCounter.returned+1)
            else:
                statusCounter.not_returned = int(statusCounter.not_returned+1)
        for each in allperiod4_objects:
            allperiod4_dict = ast.literal_eval(each.EachPersonData)
            if allperiod4_dict['Status']:
                statusCounter.returned = int(statusCounter.returned+1)
            else:
                statusCounter.not_returned = int(statusCounter.not_returned+1)
        statusCounter.save()
        returned = statusCounter.returned
        not_returned = statusCounter.not_returned
        teacherData = User.objects.get(username = username)

        contextDashboard = {'username':teacherData.username, 'email':teacherData.email, 'returned':returned, 'not_returned':not_returned}
        return render(request, 'teachers/dashboard.html', contextDashboard)
    except:

        returned = '0'
        not_returned = '0'
        teacherData = User.objects.get(username = username)
        contextDashboard = {'username':teacherData.username, 'email':teacherData.email, 'returned':returned, 'not_returned':not_returned}
        return render(request, 'teachers/dashboard.html', contextDashboard)
# Creating new form for students


def createNewForm(request, username):
    if request.method == 'POST':
        allDataRecived = {}
        for i in range(1, 51):
            input = str(request.POST.get(f'input{i}'))
            if str(input) == "None":
                break
            else:
                allDataRecived[input] = []
                for j in range(1, 21):
                    option = request.POST.get(f'input{i}-Option{j}')
                    if str(option) == "None":
                        break                    
                    if len(str(option)) != 0 or option != 0:
                        allDataRecived.setdefault(input, []).extend([option])
                    else:
                        break
        try:
            ClassForm.objects.get(user = username)
            ClassForm.objects.update(forms = str(allDataRecived))
            period1.objects.all().delete()
            period2.objects.all().delete()
            period3.objects.all().delete()
            period4.objects.all().delete()
            return redirect(f'/dashboard/{username}/sign-out-form')
        except:
            print(str(allDataRecived))
            ClassForm.objects.create(user = username , forms = str(allDataRecived))
            return redirect(f'/dashboard/{username}/sign-out-form')
    else:
        return render(request, 'teachers/createNewForm.html', {'username':username})


# The actual student side Form


def form_signout_equipments(request, username):
    if request.method == 'POST':
        period = int(request.POST.get('period'))
        nameOfSubmissioner = request.POST.get('nameOfSubmissioner')
        groupMemebers = request.POST.get('groupMembers')
        Identifier = nameOfSubmissioner
        allDataRecived = {'Name':Identifier , 'Group Memebers':groupMemebers}
        information_object = ClassForm.objects.get(user = username)
        information_form_str = information_object.forms
        usernameIs = username
        information_form_dict = ast.literal_eval(information_form_str)
        for each in information_form_dict:
            value = str(request.POST.get(each))
            allDataRecived[each]= value if len(value)!=0 or value == "None" else "-"
        now = datetime.now()
        signedOutTime = now.strftime("%B %d - %H:%M:%S")
        allDataRecived['Checked out'] = signedOutTime
        allDataRecived['Checked in'] = ""
        allDataRecived['Status'] = False
        context = {'username':username}
        if period == 1:
            period1.objects.create(Student = Identifier ,Teacher = usernameIs, EachPersonData = str(allDataRecived), signedOutTime = signedOutTime, signedInTime = "", Status = False)
            return render(request, 'students/signedIn.html')
        elif period == 2:
            period2.objects.create(Student = Identifier ,Teacher = usernameIs, EachPersonData = str(allDataRecived), signedOutTime = signedOutTime, signedInTime = "", Status = False)
            return render(request, 'students/signedIn.html')            
        elif period == 3:
            period3.objects.create(Student = Identifier ,Teacher = usernameIs, EachPersonData = str(allDataRecived), signedOutTime = signedOutTime, signedInTime = "", Status = False)
            return render(request, 'students/signedIn.html')
        elif period == 4:
            period4.objects.create(Student = Identifier ,Teacher = usernameIs, EachPersonData = str(allDataRecived), signedOutTime = signedOutTime, signedInTime = "", Status = False)
            return render(request, 'students/signedIn.html')
        else:
            return render(request, 'teachers/error.html')
    else:
        try:
            information3 = ClassForm.objects.get(user = username)
            information2 = information3.forms
            information = information2
            finalInformation = ast.literal_eval(information)
            return render(request, 'students/signOutEqp.html', {'form':finalInformation})
        except:
            messages.info(request, "There is no form available, please create new one")
            return redirect(f'/dashboard/{username}')


# Students sign-out form


def form_signin_equipments(request, username):
    if request.method == 'POST':
        recivedName = request.POST.get('checkNameOfSubmissioner')
        recivedPeriod = request.POST.get('recivedPeriod')
        now = datetime.now()
        signedInTime = now.strftime("%B %d - %H:%M:%S")
        context = {'username':username}

        if recivedPeriod == '1':
            try:
                student = period1.objects.get(Student = recivedName)
                if student.Status == "False":
                    dictionry = ast.literal_eval(student.EachPersonData)
                    dictionry['Status'] = True
                    dictionry['Checked in'] = signedInTime
                    student.Status = True
                    student.signedInTime = signedInTime
                    student.EachPersonData = dictionry
                    student.save()
                    return render(request, 'students/signedOut.html')
                else:
                    messages.info(request, "You have signed out equipments once")
                    return render(request, 'students/signInEqp.html')
            except:
                messages.info(request, "You haven't signed out anything under this name")
                return render(request, 'students/signInEqp.html')


        if recivedPeriod == '2':
            try:
                student = period2.objects.get(Student = recivedName)
                if student.Status == "False":
                    dictionry = ast.literal_eval(student.EachPersonData)
                    dictionry['Status'] = True
                    dictionry['Checked in'] = signedInTime
                    student.Status = True
                    student.signedInTime = signedInTime
                    student.EachPersonData = dictionry
                    student.save()
                    return render(request, 'students/signedOut.html')
                else:
                    messages.info(request, "You have signed out equipments once")
                    return render(request, 'students/signInEqp.html')
            except:
                messages.info(request, "You haven't signed out anything under this name")
                return render(request, 'students/signInEqp.html')

        if recivedPeriod == '3':
            try:
                student = period3.objects.get(Student = recivedName)
                if student.Status == "False":
                    dictionry = ast.literal_eval(student.EachPersonData)
                    dictionry['Status'] = True
                    dictionry['Checked in'] = signedInTime
                    student.Status = True
                    student.signedInTime = signedInTime
                    student.EachPersonData = dictionry
                    student.save()
                    return render(request, 'students/signedOut.html')
                else:
                    messages.info(request, "You have signed out equipments once")
                    return render(request, 'students/signInEqp.html')
            except:
                messages.info(request, "You haven't signed out anything under this name")
                return render(request, 'students/signInEqp.html')

        if recivedPeriod == '4':
            try:
                student = period4.objects.get(Student = recivedName)
                if student.Status == "False":
                    dictionry = ast.literal_eval(student.EachPersonData)
                    dictionry['Status'] = True
                    dictionry['Checked in'] = signedInTime
                    student.Status = True
                    student.signedInTime = signedInTime
                    student.EachPersonData = dictionry
                    student.save()
                    return render(request, 'students/signedOut.html')
                else:
                    messages.info(request, "You have signed out equipments once")
                    return render(request, 'students/signInEqp.html')
            except:
                messages.info(request, "You haven't signed out anything under this name")
                return render(request, 'students/signInEqp.html')

    return render(request, 'students/signInEqp.html')



def period_one(request, username):
    all_period1_obejcts = period1.objects.filter(Teacher = username)
    result = []
    for each in all_period1_obejcts:
        each_period1_dict = ast.literal_eval(each.EachPersonData)
        result.append(each_period1_dict)
    return render(request, 'periods/period1.html', {'result':result})

def period_two(request, username):
    all_period2_obejcts = period2.objects.filter(Teacher = username)
    result = []
    for each in all_period2_obejcts:
        print('ok')
        each_period2_dict = ast.literal_eval(each.EachPersonData)
        print(each_period2_dict)
        result.append(each_period2_dict)    
    return render(request, 'periods/period2.html', {'result':result})

def period_three(request, username):
    all_period3_obejcts = period3.objects.filter(Teacher = username)
    result = []
    for each in all_period3_obejcts:
        each_period3_dict = ast.literal_eval(each.EachPersonData)
        result.append(each_period3_dict) 
    return render(request, 'periods/period3.html', {'result':result})

def period_four(request, username):
    all_period4_obejcts = period4.objects.filter(Teacher = username)
    result = []
    for each in all_period4_obejcts:
        each_period4_dict = ast.literal_eval(each.EachPersonData)
        result.append(each_period4_dict)
    return render(request, 'periods/period4.html', {'result':result})
