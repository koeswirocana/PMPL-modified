from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return HttpResponse('<html><title>Testing Site</title><head>koeswirocana site is here<br></head><body>Nama: I Wayan Kuswirocana<br>NPM: 1206208510</body></html>')
