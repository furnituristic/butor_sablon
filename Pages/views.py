from django.shortcuts import render, HttpResponse
from .forms import ContactForm
import xlsxwriter

def home_page(request):
    return render(request, 'home_page.html')

def velemeny(request):
    return render(request, 'velemeny.html')

def kapcsolat(request):
    return render(request, 'kapcsolat.html')

def about(request):
    return render(request, 'about.html')

def contact_user(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():                     # a ContactForm osztály minden eleme ki legyen töltve !!!!
            dim1 = form.cleaned_data["dim1"]
            dim2 = form.cleaned_data["dim2"]
            dim3 = form.cleaned_data["dim3"]
            message = form.cleaned_data["message"]

            butor_1 = xlsxwriter.Workbook('butor_data.xlsx')
            worksheet = butor_1.add_worksheet()
            worksheet.write(0,0, dim1)
            worksheet.write(1,0, dim2)
            worksheet.write(2,0, dim3)
            butor_1.close()

        #return redirect("home")
    context = {"form": form}
    return render(request, 'contact_user.html', context)


