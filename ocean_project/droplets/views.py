from django.views.generic import TemplateView

class GetDroplets(TemplateView):
    template_name = 'droplets.html'
    def get_context_data(self, *args, **kwargs):
        pass