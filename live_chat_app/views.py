from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .forms import UserForm,LoginForm,post_comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Comment
from .long_word import kelime_sil



def ana_sayfa(request):
    

    return render(request,"live_chat_app/main.html")


def log_in(request):
    request.session['login_redirect'] = request.META.get('HTTP_REFERER', '/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # user = authenticate(email=form['email'].data, password=form['password'].data)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            

        else:
            pass
        
        next_page = request.GET.get('next')
        return redirect(next_page)

    else:
        form = LoginForm()
    user = request.user
    return render(request, 'live_chat_app/log_in.html', {'form': form,"user":user})

    

@login_required
def log_out(request):
    logout(request)
    return redirect("ana_sayfa")


def sign_up(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user=User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            login(request, user)
            return redirect("ana_sayfa")
    else:
        form = UserForm()
    return render(request, 'live_chat_app/sign_up.html', {'form': form})


@login_required
def chat(request):
    
    if request.method == 'POST':
        form = post_comment(request.POST)
        if form.is_valid():
            text=  kelime_sil(form.cleaned_data['text'])
            if text =='':
                pass
            else:
                user = request.user
                new_comment = Comment(user=user, text=text)  
                new_comment.save()



            return redirect("chat")
    else:
        user = request.user
        comment_list=Comment.objects.all()
        comment_list=comment_list[::-1]
        return render(request, 'live_chat_app/chat.html', {'list':comment_list,"user":user})

  



  