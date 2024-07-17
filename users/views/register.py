from django.views.generic import TemplateView
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.shortcuts import redirect
from django.contrib import messages


class register_view (TemplateView) : 
    template_name = 'register.html'

    def post(self, request) : 
        data = request.POST.copy()
        whats_app_number = f'+2{data.pop('whats_app_number')[0]}'

        print(whats_app_number, len(whats_app_number))
        action = Action(
            url=MAIN_URL + '/user/auth/register/',
            data={
                'whats_app_number' : whats_app_number,
                **data
            }
        )
        
        action.post()
        res = action.json_data()
        
        if action.is_valid:
            user = res['access_token']
            response = redirect('home')
            response.set_cookie('user', user)
            return response
        
        print(action.json_data())
        messages.error(request, 'an error accorued')
        return redirect('register')