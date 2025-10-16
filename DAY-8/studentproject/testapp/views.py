from django.shortcuts import render

# Create your views here.
def student_data(request):
    student_profile = {
        #key : value
        'name':'pikachu',
        'age':'10',
        'cousre':'pokemon training'
    }
    return render(request, 'testapp/index.html',context=student_profile)