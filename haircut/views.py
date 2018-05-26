from django.shortcuts import render

def home_page(request):

     if request.method == 'POST':
        our_type = request.POST.get("type")
        barber_name = request.POST.get("name")
        our_time = request.POST.get("time")

        context = {'type': our_type, 'name': barber_name, 'time': our_time}
        print("Here is our comment", our_type)
        
        return render(request, 'haircut/home_page.html', context)


     if request.method == 'GET':
        return render(request, 'haircut/home_page.html')