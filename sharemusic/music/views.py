from django.shortcuts import render,redirect
from .forms import MusicForm
from .models import PublicPrivate,Protected,EmailAllowed
from users.models import CustomUser
# Create your views here.
def MusicDetails(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MusicForm(request.POST,request.FILES)
            if form.is_valid():
                type_of = form.cleaned_data["upload_file_as"]
                file = form.cleaned_data["file"]
                shared_emails = []
                check_users = []
                if type_of == "protected":
                    shared_emails = form.cleaned_data["share_with_emails"].split(',')
                    shared_emails_instance = []
                    file_record = Protected(file=file,user = request.user)
                    file_record.save()
                    for email in shared_emails:
                        try:
                            CustomUser.objects.get(email = email)
                        except:
                            check_users.append(email)

                        if email == request.user.email:
                            continue
                        try:
                            EmailAllowed.object.get(email = email)
                            file_record.emails.add(EmailAllowed.object.get(email = email))
                        except:
                            e = EmailAllowed(email = email)
                            e.save()
                            file_record.allowed_emails.add(e)
                else:
                    file_record = PublicPrivate(type_of=type_of,file=file,user=request.user)
                    file_record.save()
                msg = ""
                if len(check_users) != 0:
                    # print(len(check_users))
                    msg = "Users with these emails are not registered!!!"

                return render(request, 'musicform.html', {'form': form,"msg":msg, "emails":check_users})
            else:
                return render(request, 'musicform.html', {'form': form})
                
        else:
            form = MusicForm()

        return render(request, 'musicform.html', {'form': form})
    else:
        return redirect('home')



