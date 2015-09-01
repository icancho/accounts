from django.shortcuts import render
from app.models import *


def data_accounts(request):
	data_list = ExpensesRegistry.objects.all()
	template = 'home.html'

	return render(request, template, {
		'data_list': data_list,

	})

