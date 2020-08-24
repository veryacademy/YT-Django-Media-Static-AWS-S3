from demo.forms import Upload
from django.views.generic.edit import FormView
from .models import Post


class Upload(FormView):
    template_name = 'index.html'
    form_class = Upload
    success_url = '/'

    def form_valid(self, form):
        form.save()
        print(form.cleaned_data)
        return super().form_valid(form)
