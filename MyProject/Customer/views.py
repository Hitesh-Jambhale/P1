from django.shortcuts import render,redirect
from .models import Customer
from .forms import CustomerForm
from AddressApp.models import PermanentAddress


def create_customer_view(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect("/dapp/address/cAddress/%i" % customer.id)
    template_name = 'DashboardApp/personaldetail.html'
    context = {'form':form}
    return render(request,template_name,context)

def show_customer_view(request):
    customer = Customer.objects.all()
    template_name = 'DashboardApp/showCustomer.html'
    context = {'customer':customer}
    return render(request,template_name,context)


