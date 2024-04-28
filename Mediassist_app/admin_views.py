from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from Mediassist_app.forms import LoginRegister, DonorRegister
from Mediassist_app.models import donor, users, Medicine_approval, Medicine_request, Cash_approval, Cash_request, \
    Feedback


class CompanyRegistrationView(View):

    def get(self, request):
        user = LoginRegister()
        company_form = DonorRegister()


        return render(request, 'admin/register_cmp.html', {"user": user, "company_form": company_form})

    def post(self, request):
        user = LoginRegister(request.POST)

        company_form = DonorRegister(request.POST)

        if user.is_valid() and company_form.is_valid():

            a = user.save(commit=False)
            print(a)
            a.is_donor = True
            a.save()
            user1 = company_form.save(commit=False)
            print(user1)
            user1.user = a
            user1.save()
            return redirect('admin_base')
        return render(request,'admin/register_cmp.html', {"user": user, "company_form": company_form})



def cmp_list(request):
    cmp=donor.objects.all()
    return render(request,'admin/cmp_list.html',{'cmp':cmp})


def user_list(request):
    user=users.objects.all()
    return render(request,'admin/user_list.html',{'user':user})


def requests(request):
    data = Medicine_approval.objects.all()
    return render(request, 'admin/approval.html', {'data': data})



def admin_approval(request):
    data=Medicine_approval.objects.filter(approval__status_1 = 3 )
    return render(request,'admin/approval.html',{'data':data})




def approve_donation(request, id):
    n = Medicine_request.objects.get(id=id)
    print(n)
    n.status_1 = 2

    print(n.status_1)
    n.save()

    messages.info(request, 'Donation Confirmed')
    return redirect('requests')

def reject_donation(request, id):
    n = Medicine_request.objects.get(id=id)
    n.status_1 = 3
    n.save()
    messages.info(request, 'Rejected')
    return redirect('requests')



def cash_requests(request):
    data = Cash_approval.objects.all()
    return render(request, 'admin/cash_approval.html', {'data': data})

def admin_cash_approval(request):
    data=Cash_approval.objects.filter(approval__status_12 = 3)
    return render(request,'admin/cash_approval.html',{'data':data})




def approve_cash_donation(request,id):
    n = Cash_request.objects.get(id=id)
    print(n)
    n.status_12 = 2

    n.save()
    messages.info(request, 'Donation Confirmed')
    return redirect('cash_requests')

def reject_cash_donation(request, id):
    n = Cash_request.objects.get(id=id)
    n.status_12 = 3
    n.save()
    messages.info(request, 'Rejected')
    return redirect('cash_requests')


#approve users

def users_approval(request,id):
    data = users.objects.get(id=id)
    data.verified = 1
    data.save()
    return redirect('user_list')

def users_reject(request,id):
    data = users.objects.get(id=id)
    data.verified = 2
    data.save()
    return redirect('user_list')



def feedbacks(request):
    n = Feedback.objects.all()
    return render(request,'admin/feedbacks.html',{'feedbacks':n})


def reply_feedback(request,id):
    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('feedbacks')
    return render(request, 'admin/admin_feedback.html', {'feedback': feedback})