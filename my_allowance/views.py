from django.shortcuts import render

#Main Site
def home(request):
	return render(request, 'my_allowance/index.html', {})

def about(request):
	return render(request, 'my_allowance/about.html', {})

def privacy_policy(request):
	return render(request, 'my_allowance/privacy_policy.html', {})

def contact(request):
	return render(request, 'my_allowance/contact.html', {})

def who_we_are(request):
	return render(request, 'my_allowance/who_we_are.html', {})

def earn(request):
	return render(request, 'my_allowance/earn.html', {})



#Dashboard
def dashboard(request):
	return render(request, 'my_allowance/dashboard/home.html', {})

def add_child(request):
	return render(request, 'my_allowance/dashboard/add_child.html', {})

def pay_history(request):
	return render(request, 'my_allowance/dashboard/pay_history.html', {})

def pay_methods(request):
	return render(request, 'my_allowance/dashboard/pay_methods.html', {})

def notifications(request):
	return render(request, 'my_allowance/dashboard/notifications.html', {})

def refer(request):
	return render(request, 'my_allowance/dashboard/refer.html', {})

def settings(request):
	return render(request, 'my_allowance/dashboard/settings.html', {})



# Settings
def account(request):
	from .forms import Account
	if request.method == 'POST':
		form = Account(request.POST)
		if form.is_valid():
			pass  # does nothing, just trigger the validation
	else:
		form = Account()
	return render(request, 'my_allowance/dashboard/settings/account.html', {'form': form})


def password(request):
	return render(request, 'my_allowance/dashboard/settings/password.html', {})

def not_preferences(request):
	return render(request, 'my_allowance/dashboard/settings/notifications.html', {})
