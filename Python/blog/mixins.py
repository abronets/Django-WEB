from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class AddUserToFormMixin(LoginRequiredMixin):
    def form_valid(self, form):
        new_form = form.save(commit=False)
        new_form.author = self.request.user
        new_form.save()
        return HttpResponseRedirect(self.success_url)