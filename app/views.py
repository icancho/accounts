from django.shortcuts import render
from django.http import JsonResponse
from app.models import *


def data_accounts(request):
	data_list = ExpensesRegistry.objects.all()
	template = 'home.html'

	return render(request, template, {
		'data_list': data_list,
	})

def dates_concepts(request, pk):
	template = 'detail.html'
	date_concept = ExpensesRegistry.objects.get(pk = pk) 

	return render(request,template, {
		'expense': date_concept,
	})

def sum_expense(request, pk):
	my_expense = ExpensesRegistry.objects.get(pk = pk)
	suma = int(my_expense.expenses) + int(request.POST.get('add')) 
	my_expense.expenses = suma
	my_expense.save()
	return JsonResponse({
		'expenses_now': suma,
	}, status = 201)

