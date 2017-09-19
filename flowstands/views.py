# -*- coding: utf-8 -*-

from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flowstand, Manufactor, Customer, NationalStandard
from datetime import date, timedelta
from django.core.urlresolvers import reverse
from django.contrib import messages

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit

from .util import paginate, get_current_region
from .util import search

import sendgrid
from sendgrid.helpers.mail import *
from flowstanddb.settings import ADMIN_EMAIL, SENDGRID_API_KEY


##########################################################################

# Flow standards Views

def flowstands_list(request):
    flowstands = Flowstand.objects.all()
    # кількість еталонів у базі
    count = len(flowstands)
    # визначення поточного регіону
    current_region = get_current_region(request)
    if current_region:
        flowstands = Flowstand.objects.filter(region=current_region)
    else:
        flowstands = Flowstand.objects.all()

    search_terms = ('name',)
    q = request.GET.get('q', '')
    if len(q) >= 3:
        results = search(q, flowstands, search_terms)
        if results:
            flowstands = results.get('objects')

    today = date.today()
    context = paginate(flowstands, 15, request, {}, var_name='flowstands')
    context['q'] = q
    context['count'] = count
    context['today'] = today

    return render(request, 'flowstands/flowstands_list.html', context)


########################################################################
# Flowstand Detail Views

def flowstand_view(request, pk):
    flowstand = Flowstand.objects.get(id=pk)
    today = date.today()
    # calculation of certificate expiration date
    delta = timedelta(days=365)
    expir_date = flowstand.date_calibr + delta
    diff = (today - flowstand.date_calibr).days
    diff = 365 - int(diff)

    return render(request, 'flowstands/flowstand_view.html', {
        'flowstand': flowstand,
        'today': today,
        'expir_date': expir_date,
        'diff': diff
    }
                  )

##########################################################################
# Customers Views

def customers_list(request):
    current_region = get_current_region(request)
    if current_region:
        customers = Customer.objects.filter(region=current_region)
    else:
        customers = Customer.objects.all()
    context = paginate(customers, 10, request, {}, var_name='customers')

    return render(request, 'flowstands/customers_list.html', context)

#############################################################
# Manufactors Views

def manufactors_list(request):
    manufactors = Manufactor.objects.all()
    context = paginate(manufactors, 15, request, {}, var_name='manufactors')
    return render(request, 'flowstands/manufactors_list.html', context)


# National Standards list #################################################
def national_standards(request):
    nat_standards = NationalStandard.objects.all()
    return render(request, 'flowstands/nat_standards.html', {'nat_standards': nat_standards})


# View of selected National Standard
def national_standard(request, pk):
    nat_standard = NationalStandard.objects.get(id=pk)
    return render(request, 'flowstands/nat_standard.html', {'nat_standard': nat_standard})


# Contact Admin ###################
class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact')

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-4 control-label'
        self.helper.field_class = 'col-sm-8'
        self.helper.layout = Layout(
            'from_email',
            'subject',
            'message',
            Div(
                Div(
                    Submit('send_button', u'Надіслати'),
                    css_class='col-sm-offset-4 col-sm-12'
                ),
                css_class='form-group'
            )
        )

    from_email = forms.EmailField(
        label=u'Ваш Е-мейл')
    subject = forms.CharField(
        label=u'Заголовок',
        max_length=128)
    message = forms.CharField(
        label=u'Текст повідомлення',
        max_length=2560,
        widget=forms.Textarea)


def contact_admin(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            content = Content("text/plain", message)
            from_email = Email(form.cleaned_data['from_email'])
            to_email = Email(ADMIN_EMAIL)

            try:
                mail = Mail(from_email, subject, to_email, content)
                response = sg.client.mail.send.post(request_body=mail.get())
            except Exception:
                message = u'Під час відправки листа виникла помилка'
                messages.warning(request, message)
            else:
                message = u'Повідомлення успішно надіслане!'
                messages.success(request, message)
                return HttpResponseRedirect(reverse('contact'))
    else:
        form = ContactForm()
    return render(request, 'contact_admin/form.html', {'form': form})
