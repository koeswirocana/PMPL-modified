from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
<<<<<<< HEAD
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
=======
	return HttpResponse('<html><title>Testing Site</title><head>koeswirocana site is here<br></head><body>Nama: I Wayan Kuswirocana<br>NPM: 1206208510</body></html>')
>>>>>>> 570d05fdaa9eaa99579689008602ff15b5b6e5e0
