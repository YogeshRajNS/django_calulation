from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

# def home(request):
#     return redirect('add_numbers')  # Redirect to the addition page

def add_numbers(request):
    if request.method == "POST":
        num1 = request.POST.get("num1", 0)
        num2 = request.POST.get("num2", 0)
        try:
            result = int(num1) + int(num2)
        except ValueError:
            result = "Invalid input"
        return render(request, "addition_app/add.html", {"result": result})
    
    # Handle GET request or default case
    return render(request, "addition_app/add.html", {"result": None})
# def multiply_numbers(request):
#     if request.method == "POST":
#         num1 = request.POST.get("num1", 0)
#         num2 = request.POST.get("num2", 0)
#         try:
#             result = int(num1) * int(num2)
#         except ValueError:
#             result = "Invalid input"
#         return render(request, "addition_app/index.html", {"result": result})
    
#     # Handle GET request or default case
#     return render(request, "addition_app/index.html", {"result": None})
