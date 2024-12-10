from django.shortcuts import render,redirect
from django.http import HttpResponseForbidden

class RoleBaseAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        if not request.user.is_authenticated:
            if request.path.startswith('/pembeli/') or request.path.startswith('/penjual/'):
                return redirect('login')
            # elif request.path.startswith('/admin/'):
            #     return HttpResponseForbidden("Anda Tidak Punya Akses Untuk Mengakses Halaman Ini!")
            
        else:
            if request.path.startswith('/auth/') and request.user.role != 'buyer':
                return redirect('seller_dashboard')
            elif request.path.startswith('/auth/') and request.user.role != 'seller':
                return redirect('home')
            elif request.path.startswith('/pembeli/') and request.user.role != 'buyer':
                return redirect('seller_dashboard')
            elif request.path.startswith('/penjual/') and request.user.role != 'seller':
                return redirect('home')
            elif request.path.startswith('/admin/') and request.user.role != 'admin':
                return HttpResponseForbidden("Anda Tidak Punya Akses Untuk Mengakses Halaman Ini!")
        
        return self.get_response(request)