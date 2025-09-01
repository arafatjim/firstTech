from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm
def home(request):
        my_course = {
        'id': 1,
        'name': 'Web Development',
        'instructor': 'Arafat Jim',
        'duration': '3 months',
        'topics': ['HTML', 'CSS', 'JavaScript', 'React', 'Tailwind CSS'],
        'numbers': ['5', '10', '15', '20', '25', '30', '35', '40'],
        'numbers2': [5, 10, 15, 20, 25, 30, 35, 40],
        'is_active': True,
        'students_info': [
            {
            'id': 101,
            'name': 'Rahim',
            'email': 'rahim@example.com',
            'enrolled_date': '2025-08-01'
            },
            {
            'id': 102,
            'name': 'Karim',
            'email': 'karim@example.com',
            'enrolled_date': '2025-08-03'
            },
            {
            'id': 103,
            'name': 'Jannat',
            'email': 'jannat@example.com',
            'enrolled_date': '2025-08-04'
            }
        ]
        }


        return render(request, "home.html", my_course)
def homePage(request):
          return HttpResponse("this is home page.")

def aboutUs(request):
          return render(request,"aboutUs.html")
def mainPage(request):
          return render(request,"index.html")


def club(request):
          return render(request,"club.html")


def offers(request):
          return render(request,"offer.html")
def featuredProducts(request):
          return render(request,"featuredProducts.html")

def contactUs(request):
        return render(request,"contact.html")
def events(request):
          return HttpResponse("<h2>Events</h2>"+"<p><b>Event 1:</b></p>"+"<ul><li>Item 1.Home</li><li>Item 2.Country</li></ul>")
def gallery(request):
        return HttpResponse("Gallery page.")
def contactUsDetails(request,detailsId):
        return HttpResponse('contact details id:'+str(detailsId))


def userForm(request):
        fn= UserForm()
        finalresult = 0
        data = {'form':fn}
        try:
                if request.method=='POST':
                        n1 = int(request.POST.get('num1'))
                        n2 = int(request.POST.get('num2'))
                
                
                finalresult = finalresult + n1 + n2
                data={
                        'form':fn,
                        'n1':n1,
                        'n2':n2,
                        'output':finalresult
                }
                return HttpResponseRedirect('/todays-offer/',{'output':finalresult})
                # GET mathod
                
                # if i want ot use of get mathod
                # nam1 = str(request.GET.get('text1', ''))
                # m1 = str(request.GET.get('email1', ''))
                # p1 = str(request.GET.get('password1', ''))
                # if request.method=='GET':
                #         n1 = int(request.GET.get('num1'))
                #         n2 = int(request.GET.get('num2'))
                
                
                # if i want to use POST method then you have to use csrf_token
                # or else it will give error (403 forbidden)
                # or else you can use GET method
                # or else you can disable csrf middleware from settings.py file           
                # POST method
                # finalresult = int(n1) + int(n2)
                
                
        except :
                pass
        # return render(request, "userForm.html", {'output': finalresult})
        return render(request, "userForm.html", data)
def signUpPage(request):
    finallSubmission = {}
    try:
        if request.method == 'POST':
            fullName = str(request.POST.get('fullname', ''))
            userName = str(request.POST.get('useremail', ''))
            userPhone = str(request.POST.get('phone', ''))
            userDepartment = str(request.POST.get('department', ''))
            userSkills = str(request.POST.get('skills', ''))
            userReason = str(request.POST.get('reason', ''))
            finallSubmission = {
                'fullName': fullName,
                'userName': userName,
                'userPhone': userPhone,
                'userDepartment': userDepartment,
                'skills': userSkills,
                'reason': userReason
            }
            return HttpResponseRedirect('/welcome-text/')
    except :
        pass
    return render(request, "signup.html", finallSubmission)
        
def welcomeText(request):
        if request.method == 'POST':
                output=request.POST.get('output','')
                
        return render(request,"welcomeBanner.html",);
# def sumbmitForm(request):
#         finalresult = 0
#         data = {}
#         try:
#                 if request.method=='POST':
#                         n1 = int(request.POST.get('num1'))
#                         n2 = int(request.POST.get('num2'))
                
                
#                         finalresult = n1 + n2
#                         data={
#                                 'n1':n1,
#                                 'n2':n2,
#                                 'output':finalresult
#                         }
#                         return HttpResponse("This is sumbmit form page. " +str(finalresult))
#         except:
#                 pass
        
def sumbmitForm(request):
    if request.method == 'POST':
        try:
            n1 = int(request.POST.get('num1', 0))
            n2 = int(request.POST.get('num2', 0))
            finalresult = n1 + n2
            return HttpResponse(f"The sum of {n1} and {n2} is {finalresult}.")
        except ValueError:
            # If user enters non-integer values
            return HttpResponse("Invalid input. Please enter numbers only.")
    else:
        # For GET requests, render a simple form
        return render(request, 'submitForm.html')
def calculator(request):
        result = None
        error = None
        if request.method == 'POST':
                try:
                        n1 = int(request.POST.get('num1', 0))
                        n2 = int(request.POST.get('num2', 0))
                        operator = request.POST.get('operator', '+')
                        if operator == '+':
                                result = n1 + n2
                        elif operator == '-':
                                result = n1 - n2
                        elif operator == '*':
                                result = n1 * n2
                        elif operator == '/':
                                if n2 == 0:
                                        error = "Cannot divide by zero"
                                else:
                                        result = n1 / n2
                        else:
                                error = "Invalid operator"
                except ValueError:
                        error = "Invalid input. Please enter numbers only."
        return render(request, "calculator.html", {'result': result, 'error': error})
def calculator2(request):
    r = 0
    if request.method == 'POST':
        try:
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            op = request.POST.get('operator')

            if op == "+":
                r = n1 + n2
            elif op == "-":
                r = n1 - n2
            elif op == "*":
                r = n1 * n2
            elif op == "/":
                try:
                    r = n1 / n2
                except ZeroDivisionError:
                    r = "Cannot divide by zero"
        except ValueError:
            r = "Invalid input"
    return render(request, "calculator2.html", {'r': r})
