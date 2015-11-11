from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
	# comments = 'yey, waktunya berlibur'

	# if Item.objects.count() > 0:
	#	comments = 'sibuk tapi santai'

	# if Item.objects.count() >= 5:
	#	comments = 'oh tidak'

	# items = Item.objects.all()
	# return render(request, 'home.html', {'comments': comments})
	return render(request, 'home.html')

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'], list=list_)
		return redirect('/lists/%d/' % (list_.id,))
	comment = 'yey, waktunya berlibur'
	count = Item.objects.filter(list_id=list_.id).count()

	if (count > 0) and (count < 5):
		comment = 'sibuk tapi santai'
	else:
		comment = 'oh tidak'
	#items = Item.objects.filter(list=list_)
	#return render(request, 'list.html', {'items': items})
	return render(request, 'list.html', {'list': list_, 'comment': comment})

def new_list(request):
	list_ = List.objects.create()
	item = Item(text=request.POST['item_text'], list=list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {"error": error})
	return redirect('/lists/%d/' % (list_.id,))

# def add_item(request, list_id):
#	list_ = List.objects.get(id=list_id)
#	Item.objects.create(text=request.POST['item_text'], list=list_)
#	return redirect('/lists/%d/' % (list_.id,))

def blog_page(request):
	return render(request, 'index.html')
