from django.shortcuts import render

# Create your views here.
def js_test(request):
    name = '황성민'
    phone = '001'
    address = '분당'
    
    context = { 
        'name' : name,
        'phone' : phone,
        'address' : address
    }
    return render(request, 'JS_TEST.html', context)