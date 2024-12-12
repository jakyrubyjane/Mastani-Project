from django.shortcuts import render, redirect
from .models import literasi
from .forms import ContactMessageForm
# Create your views here.

def index(request):
    return render (request, "Home/index.html", {'active_page': 'home'})

def literasi_view(request):
    data_literasi = literasi.objects.all()
    context = {
        'data_literasi':data_literasi,
        'active_page':'literasi'
    }
    
    return render (request, 'Home/literasi.html', context)

def pemasaran_view(request):
    return render (request, "Home/pemasaran.html", {'active_page':'pemasaran'})

def about_view(request):
    return render (request, "Home/about.html", {'active_page':'about'})
from django.core.mail import send_mail

def contactus_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            # Simpan form ke database
            form.save()
            # Kirim pesan sukses ke template
            return render(request, 'Home/contactus.html', {'form': form, 'success_message': 'pertanyaan atau masukan berhasil dikirim!'})
    else:
        form = ContactMessageForm()
    
    return render(request, 'Home/contactus.html', {'form': form})
def privacy_view(request):
    return render (request, "Home/privacy_policy.html", {'active_page':'privacy_policy'})

def cart_view(request):
    # Mengambil data dari session jika menggunakan session untuk menyimpan keranjang
    cart = request.session.get('cart', [])

    # Menghitung total harga
    total_price = sum(item['price'] * item.get('quantity', 1) for item in cart)
    
    # Mengirimkan data keranjang ke template cart.html
    return render(request, 'Home/cart.html', {'cart': cart, 'total_price': total_price})