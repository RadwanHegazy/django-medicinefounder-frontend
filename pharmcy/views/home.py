from typing import Any
from django.views.generic import TemplateView
from globals.request_manager import Action
from frontend.settings import MAIN_URL


class home_view (TemplateView) : 
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = {}
        
        search = self.request.GET.get('search', None)
        url = MAIN_URL + '/medicine/get/'

        if search :
            url += '?search=' + search

        action = Action(
            url=url,
        )

        action.get()

        data['object_list'] = action.json_data()
        
        return data