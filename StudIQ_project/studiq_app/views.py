from django.shortcuts import render 
from studiq_app.forms import UserForm, UserProfileInfoForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_protect


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth.decorators import login_required

from .models import Videoing
from .models import Videoing2

# mtk kelas 4
from .models import Video1mtkkls4
from .models import Video2mtkkls4
from .models import Video3mtkkls4
from .models import Video4mtkkls4

from jwt import PyJWTError

# Create your views here.
@login_required  # Pastikan hanya user yang sudah login yang bisa mengakses halaman ini
def profil(request):
    user = request.user  # Ambil data pengguna yang sedang login
    context = {
        'name': user.get_full_name(),  # Mengambil nama lengkap pengguna
        'email': user.email,  # Mengambil email pengguna
        'password': user.password,  # Mengambil password pengguna (tidak disarankan ditampilkan)
    }
    return render(request, 'profil.html', context)

def index(request):
    return render(request, "index.html")

def daftar_kelas(request):
    return render(request, "daftar_kelas.html")

def daftar_materi(request):
    return render(request, "daftar_materi.html")

def tentang_kami(request):
    return render(request, "tentang_kami.html")

def FAQs(request):
    return render(request, "FAQs.html")

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def pengaturan(request):
    return render(request, 'pengaturan.html')

def materi2(request):
    return render(request, 'materi2.html')

def belajar(request):
    return render(request, 'belajar.html')

def video(request):
    return render(request, 'video.html')

def materi_view(request, kelas, mapel):
    template_map = {
        '4SD': {
            'IPA': 'daftar_kelas.html',
            'MM': 'mtk_4/materi1_mtk_kls4.html',
            'ING': 'english_4/materi1-ing.html',
        },
        '5SD': {
            'IPA': 'ipa_5/ipa5_1.html',
            'MM': 'mtk_5/materi-mtk.html',
            'ING': 'english_5/materi3-ing.html',
        },
        '6SD': {
            'IPA': 'ipa_6/materi-ipa.html',
            'MM': 'mtk_6/materi3-mtk.html',
            'ING': 'english_6/materi5-ing.html',
        }
    }

    template_name = template_map.get(kelas, {}).get(mapel)

    if template_name:
        return render(request, template_name)
    else:
        return render(request, 'not_found.html')

@csrf_protect
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Menggunakan login dari django.contrib.auth
            return redirect('studiq_app:daftar_materi')  # Ganti 'dashboard' dengan URL tujuan setelah login
        else:
            messages.error(request, 'Username atau password salah!')
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)  # Logout pengguna
    return redirect('studiq_app:index')  # Redirect ke halaman index setelah logout

# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method == 'POST':
        # Ambil data dari form
        username = request.POST['username']
        email = request.POST['email']  # Jika ini adalah email, ubah nama field
        password = request.POST['password']

        # Validasi sederhana (bisa diperluas sesuai kebutuhan)
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username sudah digunakan.')
            return redirect('studiq_app:register')
        
        # Buat akun pengguna
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Beri pesan sukses dan alihkan ke halaman login
        messages.success(request, 'Pendaftaran berhasil. Silakan login.')
        return redirect('studiq_app:login')
    return render(request, 'register.html')



# TAMBAHAN DARI YANG LAIN

def materi1ing(request):
    return render(request, 'english_4/materi1-ing.html')

def materi2ing(request):
    return render(request, 'english_4/materi2-ing.html')

def belajaring(request):
    return render(request, 'english_4/belajar-ing.html')

def belajar2ing(request):
    return render(request, 'english_4/belajar2-ing.html')

def ipa4_1(request):
    return render(request, 'ipa_4/ipa4_1.html')

def materiipa4_11(request):
    return render(request, 'ipa_4/materiipa4_1.1.html')

def materiipa4_12(request):
    return render(request, 'ipa_4/materiipa4_1.2.html')

def materiipa4_13(request):
    return render(request, 'ipa_4/materiipa4_1.3.html')

def ipa4_2(request):
    return render(request, 'ipa_4/ipa4_2.html')

def materiipa4_21(request):
    return render(request, 'ipa_4/materiipa4_2.1.html')

def materiipa4_22(request):
    return render(request, 'ipa_4/materiipa4_2.2.html')

def materiipa4_23(request):
    return render(request, 'ipa_4/materiipa4_2.3.html')

def ipa5_1(request):
    return render(request, 'ipa_5/ipa5_1.html')

def mtk_5(request):
    return render(request, 'mtk_5/belajar2-mtk.html')

def materiipa5_11(request):
    return render(request, 'ipa_5/materiipa5_1.1.html')

def materiipa5_12(request):
    return render(request, 'ipa_5/materiipa5_1.2.html')

def materiipa5_13(request):
    return render(request, 'ipa_5/materiipa5_1.3.html')

def materiipa6_1(request):
    return render(request, 'ipa_6/materi-ipa.html')

def materiipa6_2(request):
    return render(request, 'ipa_6/materi2-ipa.html')

def belajar_ipa(request):
    return render(request, 'ipa_6/belajar-ipa.html')

def belajar2_ipa(request):
    return render(request, 'ipa_6/belajar2-ipa.html')


# def belajarmtk4_1(request):
#     return render(request, 'mtk_4/belajar_mtk_kls4_1.html')

# def belajarmtk4_2(request):
#     return render(request, 'mtk_4/belajar_mtk_kls4_2.html')


# def materi1mtkkls4(request):
#     return render(request, 'mtk_4/materi1_mtk_kls4.html')

# def materi2mtkkls4(request):
#     return render(request, 'mtk_4/materi2_mtk_kls4.html')

# def materi3mtkkls4(request):
#     return render(request, 'mtk_4/materi3_mtk_kls4.html')

# def materi4mtkkls4(request):
#     return render(request, 'mtk_4/materi4_mtk_kls4.html')

def materimtk4_1(request):
    return render(request, 'mtk_4/materi1_mtk_kls4.html')

def materimtk4_2(request):
    return render(request, 'mtk_4/materi2_mtk_kls4.html')

def materimtk4_3(request):
    return render(request, 'mtk_4/materi3_mtk_kls4.html')

def materimtk4_4(request):
    return render(request, 'mtk_4/materi4_mtk_kls4.html')

def belajar_mtk(request):
    return render(request, 'mtk_5/belajar-mtk.html')

def materimtk5_1(request):
    return render(request, 'mtk_5/materi-mtk.html')

def materimtk5_2(request):
    return render(request, 'mtk_5/materi2-mtk.html')

def materimtk6_1(request):
    return render(request, 'mtk_6/materi3-mtk.html')

def materimtk6_2(request):
    return render(request, 'mtk_6/materi4-mtk.html')

def belajarmtk3_6(request):
    return render(request, 'mtk_6/belajar3-mtk.html')

def belajarmtk4_6(request):
    return render(request, 'mtk_6/belajar4-mtk.html')

# View untuk Video Mapel IPA Kelas 4
def videoipa(request, order):
    # Ambil video berdasarkan `order`
    videoipa = Videoipa.objects.get(order=order)

    prev_video = Videoipa.objects.filter(order__lt=order, order__gte=1, order__lte=3).last()
    next_video = Videoipa.objects.filter(order__gt=order, order__gte=1, order__lte=3).first()

    context = {
        'videoipa': videoipa,
        'prev_video': prev_video,
        'next_video': next_video,
    }
    
    return render(request, 'ipa_4/videoipa4_1.html', context)

def video2ipa(request, order):
    # Ambil video berdasarkan `order`
    videoipa = Videoipa.objects.get(order=order)

    prev_video = Videoipa.objects.filter(order__lt=order, order__gte=4, order__lte=6).last()
    next_video = Videoipa.objects.filter(order__gt=order, order__gte=4, order__lte=6).first()

    context = {
        'videoipa': videoipa,
        'prev_video': prev_video,
        'next_video': next_video,
    }
    
    return render(request, 'ipa_4/videoipa4_2.html', context)

# View untuk Video Mapel IPA Kelas 5
def videoipa5(request, order):
    # Ambil video berdasarkan `order`
    videoipa2 = Videoipa2.objects.get(order=order)

    prev_video = Videoipa2.objects.filter(order__lt=order, order__gte=1, order__lte=3).last()
    next_video = Videoipa2.objects.filter(order__gt=order, order__gte=1, order__lte=3).first()

    context = {
        'videoipa2': videoipa2,
        'prev_video': prev_video,
        'next_video': next_video,
    }
    
    return render(request, 'ipa_5/videoipa5_1.html', context)

# View untuk Materi Mapel IPA Kelas 4
def materiipa4(request, order):
    # Ambil video berdasarkan `order`
    materiipa = Materiipa4.objects.get(order=order)

    prev_materi = Materiipa4.objects.filter(order__lt=order, order__gte=1, order__lte=3).last()
    next_materi = Materiipa4.objects.filter(order__gt=order, order__gte=1, order__lte=3).first()

    context = {
        'materiipa': materiipa,
        'prev_video': prev_materi,
        'next_video': next_materi,
    }
    
    return render(request, 'ipa_4/materiipa4_1.html', context)

def videoing(request, order):
    # Ambil video berdasarkan `order`
    videoing = Videoing.objects.get(order=order)

    # Batasi prev_video dan next_video hanya untuk order 1-6
    prev_video = Videoing.objects.filter(order__lt=order, order__gte=1, order__lte=6).last()
    next_video = Videoing.objects.filter(order__gt=order, order__gte=1, order__lte=6).first()

    context = {
        'videoing': videoing,
        'prev_video': prev_video,
        'next_video': next_video,
    }
    
    return render(request, 'english_4/video-ing.html', context)

def video2ing(request, order):
    # Ambil video berdasarkan `order`
    videoing = Videoing.objects.get(order=order)

    # Batasi prev_video dan next_video hanya untuk order 7-12
    prev_video = Videoing.objects.filter(order__lt=order, order__gte=7, order__lte=12).last()
    next_video = Videoing.objects.filter(order__gt=order, order__gte=7, order__lte=12).first()

    context = {
        'videoing': videoing,
        'prev_video': prev_video,
        'next_video': next_video,
    }
    
    return render(request, 'english_4/video2-ing.html', context)

def materi3ing(request):
    return render(request, 'english_5/materi3-ing.html')

def materi4ing(request):
    return render(request, 'english_5/materi4-ing.html')

def belajar3ing(request):
    return render(request, 'english_5/belajar3-ing.html')

def belajar4ing(request):
    return render(request, 'english_5/belajar4-ing.html')

def belajar5ing(request):
    return render(request, 'english_6/belajar5-ing.html')

def belajar6ing(request):
    return render(request, 'english_6/belajar6-ing.html')

def materi5ing(request):
    return render(request, 'english_6/materi5-ing.html')

def materi6ing(request):
    return render(request, 'english_6/materi6-ing.html')

def video3ing(request, order):
    # Ambil video berdasarkan `order`
    videoing2 = Videoing2.objects.get(order=order)

    # Batasi prev_video dan next_video hanya untuk order 1-6
    prev_video = Videoing2.objects.filter(order__lt=order, order__gte=1, order__lte=5).last()
    next_video = Videoing2.objects.filter(order__gt=order, order__gte=1, order__lte=5).first()

    context = {
        'videoing2': videoing2,
        'prev_video': prev_video,
        'next_video': next_video,
    }
    
    return render(request, 'english_5/video3-ing.html', context)

def video4ing(request, order):
    # Ambil video berdasarkan `order`
    videoing2 = Videoing2.objects.get(order=order)

    # Batasi prev_video dan next_video hanya untuk order 1-6
    prev_video = Videoing2.objects.filter(order__lt=order, order__gte=6, order__lte=10).last()
    next_video = Videoing2.objects.filter(order__gt=order, order__gte=6, order__lte=10).first()

    context = {
        'videoing2': videoing2,
        'prev_video': prev_video,
        'next_video': next_video,
    }
    
    return render(request, 'english_5/video4-ing.html', context)

#VIEWS UNTUK VIDEO MTK KELAS 4 (BELUM MASUK DATABASE)

# VIDEO MATEMATIKA KELAS 4
def video1mtkkls4(request, order):
    # Ambil video berdasarkan `order`
    video1mtkkls4 = Video1mtkkls4.objects.get(order=order)

    # Batasi prev_video dan next_video hanya untuk order 1-4
    prev_video = Video1mtkkls4.objects.filter(order__lt=order, order__gte=1, order__lte=4).last()
    next_video = Video1mtkkls4.objects.filter(order__gt=order, order__gte=1, order__lte=4).first()

    context = {
        'video1mtkkls4': video1mtkkls4,
        'prev_video': prev_video,
        'next_video': next_video,
    }
    
    return render(request, 'mtk_4/video1_mtk_kls4.html', context)

def video2mtkkls4(request, order):
    # Ambil video berdasarkan `order`
    video2mtkkls4 = Video2mtkkls4.objects.get(order=order)

    # Batasi prev_video dan next_video hanya untuk order 1-4
    prev_video = Video2mtkkls4.objects.filter(order__lt=order, order__gte=1, order__lte=4).last()
    next_video = Video2mtkkls4.objects.filter(order__gt=order, order__gte=1, order__lte=4).first()

    context = {
        'video2mtkkls4': video2mtkkls4,
        'prev_video': prev_video,
        'next_video': next_video,
    }
    
    return render(request, 'mtk_4/video2_mtk_kls4.html', context)

def video3mtkkls4(request, order):
    # Ambil video berdasarkan `order`
    video3mtkkls4 = Video3mtkkls4.objects.get(order=order)

    # Batasi prev_video dan next_video hanya untuk order 1-4
    prev_video = Video3mtkkls4.objects.filter(order__lt=order, order__gte=1, order__lte=4).last()
    next_video = Video3mtkkls4.objects.filter(order__gt=order, order__gte=1, order__lte=4).first()

    context = {
        'video3mtkkls4': video3mtkkls4,
        'prev_video': prev_video,
        'next_video': next_video,
    }
    
    return render(request, 'mtk_4/video3_mtk_kls4.html', context)

def video4mtkkls4(request, order):
    # Ambil video berdasarkan `order`
    video4mtkkls4 = Video4mtkkls4.objects.get(order=order)

    # Batasi prev_video dan next_video hanya untuk order 1-4
    prev_video = Video4mtkkls4.objects.filter(order__lt=order, order__gte=1, order__lte=4).last()
    next_video = Video4mtkkls4.objects.filter(order__gt=order, order__gte=1, order__lte=4).first()

    context = {
        'video4mtkkls4': video4mtkkls4,
        'prev_video': prev_video,
        'next_video': next_video,
    }
    
    return render(request, 'mtk_4/video4_mtk_kls4.html', context)





