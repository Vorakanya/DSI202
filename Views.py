from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def promotion(request):
    return render(request, 'promotion.html')

def store(request):
    return render(request, 'store.html')

def mitr(request):
    return render(request, 'mitr.html')

def hanuman(request):
    return render(request, 'hanuman.html')

def kraithong(request):
    return render(request, 'kraithong.html')

def nagas(request):
    return render(request, 'nagas.html')

def erawan(request):
    return render(request, 'erawan.html')

def tossakan(request):
    return render(request, 'tossakan.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')
