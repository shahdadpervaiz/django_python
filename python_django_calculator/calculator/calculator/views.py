from django.http import HttpResponse
from django.shortcuts import render 

def calculator(request):
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")
    operation = request.GET.get("operation")    

    if operation == "sum":
        total = int(num1) + int(num2)
        print(total)
        result = {"total": total}
        return render(request , "index.html", result)
    elif operation == "sub":
        total = int(num1) - int(num2)
        print(total)
        result = {"total": total}
        return render(request , "index.html", result)
    elif operation == "multiply":
        total = int(num1) * int(num2)
        print(total)
        result = {"total": total}
        return render(request , "index.html", result)
    
    elif operation == "divide":
         total = int(num1) / int(num2)
         print(total)
         result = {"total": total}
         return render(request , "index.html", result)
    return render(request , "index.html")
    
