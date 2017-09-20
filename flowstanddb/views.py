# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, Layout

from flowstands.util import paginate


def user_list(request):
    users = User.objects.order_by('last_name')

    context = paginate(users, 5, request, {}, var_name='users')
    return render(request, 'flowstands/user_list.html', context)

class editProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(editProfileForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse('profile_edit', kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-4 control-label'
        self.helper.field_class = 'col-sm-8'
        self.helper.layout = Layout(
            'username',
            'email',
            'first_name',
            'last_name',
            Div(
                Div(
                    Submit('add_button', u'Зберегти', css_class='btn btn-primary'),
                    Submit('cancel_button', u'Скасувати', css_class='btn btn-link'),
                    css_class='col-sm-offset-4 col-sm-12'
                ),
                css_class='form-group'
            )
        )

class editProfileView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'registration/profile_edit.html'
    form_class = editProfileForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(editProfileView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('profile')

    def get_success_message(self, cleaned_data):
        return u'Користувач %(calc_last_name)s успішно збережений!' % dict(cleaned_data, calc_last_name=self.object.last_name)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, u'Редагування користувача <%s> скасовано' % request.POST['last_name'])
            return HttpResponseRedirect(reverse('profile'))
        else:
            return super(editProfileView, self).post(request, *args, **kwargs)