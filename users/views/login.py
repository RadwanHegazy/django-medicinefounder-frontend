from django.views.generic import TemplateView
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.shortcuts import redirect
from django.contrib import messages


class login_view (TemplateView) : 
    template_name = 'login.html'

    def post(self, request) : 
        data = {
            'email' : request.POST.get('email',''),
            'password' : request.POST.get('password',''),
        }
        action = Action(
            url=MAIN_URL + '/user/auth/login/',
            data=data
        )
        
        action.post()
        res = action.json_data()
        
        if action.is_valid:
            user = res['access_token']
            response = redirect('home')
            response.set_cookie('user', user)
            return response
        
        messages.error(request, 'invalid email or password')
        return redirect('login')