from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse


class AddUserToFormMixin(LoginRequiredMixin):
    def form_valid(self, form):
        if self.request.user.is_staff:
            new_form = form.save(commit=False)
            new_form.author = self.request.user
            new_form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponse('You can`t create posts' +
                                '<a href = "/"><button>Back</button></a>')