from django.shortcuts import render, HttpResponse
from .forms import ContactForm, ContactForm_Adam
import xlsxwriter
import dropbox

class TransferData: #létrehozom a TransferData osztályt
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to): #upload_file függvény létrehozása
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
                
def main():
    access_token = 'gAn1wHVkcYAAAAAAAAAAFskV2ZAJvluOD3PWg3JPO3nY_xU-Hm5uWBgiMTfsMT-Y'
    transferData = TransferData(access_token)
 
    file_from = 'D:/Dokumentumok/Biznisz/Code/Site/butor_sablon/butor_data_Adam.xlsx' # This is name of the file to be uploaded
    file_to = '/butor_data_Adam.xlsx'  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.
 
    # API v2
    transferData.upload_file(file_from, file_to)

def home_page(request):
    return render(request, 'home_page.html')

def velemeny(request):
    return render(request, 'velemeny.html')

def kapcsolat(request):
    return render(request, 'kapcsolat.html')

def about(request):
    return render(request, 'about.html')

def parameterek(request):
        if request.method == "GET":
            form_Adam = ContactForm_Adam()
        else:
            form_Adam = ContactForm_Adam(request.POST)
            if form_Adam.is_valid():                     # a ContactForm osztály minden eleme ki legyen töltve !!!!
                dim1 = form_Adam.cleaned_data["dim1"]
                dim2 = form_Adam.cleaned_data["dim2"]
                dim3 = form_Adam.cleaned_data["dim3"]
                dim4 = form_Adam.cleaned_data["dim4"]
                dim5 = form_Adam.cleaned_data["dim5"]
                dim6 = form_Adam.cleaned_data["dim6"]
                message = form_Adam.cleaned_data["message"]
                
                butor_1_Adam = xlsxwriter.Workbook('butor_data_Adam.xlsx')
                worksheet = butor_1_Adam.add_worksheet()
                worksheet.write(0, 0, dim1)
                worksheet.write(1, 0, dim2)
                worksheet.write(2, 0, dim3)
                worksheet.write(3, 0, dim4)
                worksheet.write(4, 0, dim5)
                worksheet.write(5, 0, dim6)
                butor_1_Adam.close()
                main()

            #return redirect("home")
        context = {"form": form_Adam}
        return render(request, 'parameterek.html', context)

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
            worksheet.write(0, 0, dim1)
            worksheet.write(1, 0, dim2)
            worksheet.write(2, 0, dim3)
            worksheet.write(3, 0, message)
            butor_1.close()

        #return redirect("home")
    context = {"form": form}
    return render(request, 'contact_user.html', context)

def stilus_proba(request):
    return render(request, 'stilus_proba.html')


