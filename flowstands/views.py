# -*- coding: utf-8 -*-

from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from .models import Flowstand, Manufactor, Customer, NationalStandard, Documents
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
    flowstands = Flowstand.objects.all().filter(traceability__icontains="Івано-Франківськ")
    # кількість еталонів у базі
    count = flowstands.count()
    # визначення поточного регіону
    current_region = get_current_region(request)
    if current_region:
        flowstands = flowstands.filter(region=current_region)

    sort_flag = None
    order_by = request.GET.get('order_by', '')
    if order_by == 'date_calibr':
        sort_flag = 'order_by'
        flowstands = flowstands.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            flowstands = flowstands.reverse()
            sort_flag = 'reverse'

    search_count = None
    result_text = ''
    result_text_dict = {('1',): 'еталон',
                        ('2', '3', '4'): 'еталони',
                        ('0', '5', '6', '7', '8', '9'): 'еталонів'}
    search_terms = ('name', 'customer__name')
    q = request.GET.get('q', '')
    if q:
        if len(q) >= 3:
            flowstands = search(q, flowstands, search_terms, 'date_calibr', sort_flag)
            search_count = len(flowstands)
            if len(str(search_count)) == 2 and str(search_count).startswith('1'):
                result_text = 'еталонів'
            else:
                for i in result_text_dict.keys():
                    if str(search_count)[-1] in i:
                        result_text = result_text_dict[i]
        else:
            flowstands = []

    today = date.today()
    context = paginate(flowstands, 15, request, {}, var_name='flowstands')
    context['q'] = q
    context['count'] = count
    context['today'] = today
    context['search_count'] = search_count
    context['result_text'] = result_text

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

# Normative documents
def documents(request):
    documents = Documents.objects.all()
    return render(request, 'flowstands/documents.html', {'documents': documents})