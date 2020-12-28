
from django.shortcuts import render 

def home(request):
    return render(request,"index.html")

def calculator(request):
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")
    operation = request.GET.get("operation")    
    result = {"total": "",
              "num1": num1, 
              "num2": num2, 
              "operation": operation,
               "equal" :"=",
               "except": ""}
    print(operation)
    try:
        if operation == "+":
            total = int(num1) + int(num2)
            result["total"] = total
            
        elif operation == "-":
                total = int(num1) - int(num2)
                result["total"] = total
            
        elif operation == "x":
                total = int(num1) * int(num2)
                result["total"] = total
            
            
        elif operation == "/":
                total = int(num1) / int(num2)
                result["total"] = total
            
    except Exception as e:
        result["except"] = e 

        
    return render(request , "index.html",result)
    
