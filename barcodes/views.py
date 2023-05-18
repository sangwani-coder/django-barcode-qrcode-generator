import os
from django.shortcuts import render
from io import BytesIO
from time import time

from barcode import EAN13
from barcode.writer import ImageWriter
from django.conf import settings

def generate_barcode(request):
    if request.method == 'POST':
        data = request.POST['text']

        save_path = settings.MEDIA_ROOT
        img_name = f'{str(time())}.png'
        full_path = os.path.join(save_path, img_name)
        print(full_path)

        with open(full_path, "wb") as f:
            EAN13(str(data), writer=ImageWriter()).write(f)
        #img.save(settings.MEDIA_ROOT + '/' + img_name)
        context = {
                'img_name': img_name
                }
        return render(request, 'barcode.html', context)
    return render(request, 'barcode.html')
