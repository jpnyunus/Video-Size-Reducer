import os
from moviepy import VideoFileClip

def compress_video(input_path, output_path, target_size_mb):
    # Byte cinsinden hedef boyut
    target_size_bytes = target_size_mb * 1024 * 1024
    
    # Video çözünürlüğünü ve bitrate'i otomatik ayarlamak için moviepy
    video = VideoFileClip(input_path)  # Değişkeni string yerine doğrudan kullan
    
    # Mevcut video boyutunu kontrol et
    current_size = os.path.getsize(input_path)
    print(f"Current size: {current_size / (1024 * 1024):.2f} MB")
    
    # Eğer video zaten istenen boyutun altındaysa, yeniden işleme gerek yok
    if current_size <= target_size_bytes:
        print("Video zaten hedef boyutun altında!")
        video.close()
        return
    
    # Bitrate hesaplama
    duration = video.duration  # saniye cinsinden uzunluk
    target_bitrate = (target_size_bytes * 8) / duration  # bit/s
    
    # Sıkıştırma işlemi
    print(f"Target bitrate: {target_bitrate / 2500:.2f} kbps")
    video.write_videofile(output_path, bitrate=f"{int(target_bitrate)}")
    print("Video sıkıştırma tamamlandı.")
    video.close()

# Girdi ve çıktı dosyaları
input_video = r"C:\Users\user\Desktop\test.mp4"  # Tam dosya yolunu belirt
output_video = r"C:\Users\user\Desktop\test_compressed.mp4"  # Sıkıştırılmış dosyanın yolu

compress_video(input_video, output_video, target_size_mb=9)