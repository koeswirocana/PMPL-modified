from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/')

	comments = 'yey, waktunya berlibur'

	if Item.objects.count() > 0:
		comments = 'sibuk tapi santai'

	if Item.objects.count() >= 5:
		comments = 'oh tidak'

	items = Item.objects.all()
	return render(request, 'home.html', {'items': items, 'comments': comments})
