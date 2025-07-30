from django.shortcuts import render
from .forms import QrCodeForm
import qrcode


def generate_qr_code(request):
    if request.method == 'post':
        form = QrCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data('restaurant_name')
            url = form.cleaned_data('url')

            # Generating QR Code
            qr = qrcode.make(url)
            print(qr)
    else:
        form = QrCodeForm()
        context = {
            'form': form,
        }
        return render(request, 'generate_qr_code.html', context)