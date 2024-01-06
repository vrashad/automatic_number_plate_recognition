# Avtomatik olaraq şəkildəki avtomobil nömrə nişanının oxunması
[OpenCV](https://opencv.org/) və [EasyOCR](https://github.com/JaidedAI/EasyOCR) vasitəsilə, şəkildəki avtomobil nömrə nişanının oxunması

Bu proyektin məqsədi, Computer Vision və OCR vasitəsilə, avtomatik olaraq, şəkildəki avtomobilin nömrə nişanını oxumaqdır

## İstifadə qaydası:

İlk olaraq lazım olan paketləri yükləyirik

```bash
pip install -r requirements.txt
```

Sonra nömrə nişanını oxumaq istədiyimiz avtomobilin şəklini hazırlayırıq və scripti icra edirik
Məndə faylın adı **car1.jpg** kimi təyin edilib. Siz faylın adını, öz faylınızın adına uyğun olaraq təyin etməlisiniz
Burada dövrü for operatoru vasitəsilə bir yox, istədiyiniz sayda şəkilləri bu qayda ilə emal edə bilərsiniz


İlk olaraq şəkil faylını Image, Grayscale, Blur rejimində oxuyuruq
<img src="https://i.postimg.cc/d00Mzh42/1.png">

