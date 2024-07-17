from typing import Any
from django.views import View
from globals.request_manager import Action
from globals.decorators import login_required
from django.shortcuts import redirect, render
from frontend.settings import MAIN_URL
from django.contrib import messages

class upload_view (View) : 

    @login_required
    def get (self, request, **data) :
        return render(request, 'upload.html')


    @login_required
    def post (self, request, **other) : 
        headers = other['headers']
        data = request.POST

        action = Action(
            url=MAIN_URL + '/medicine/create/',
            headers=headers,
            data=data,
        )

        action.files = request.FILES


        action.post()

        if action.is_valid:
            return redirect('home')
        
        print(action.json_data())
        messages.error(request, 'an error accoured')
        return redirect('upload')