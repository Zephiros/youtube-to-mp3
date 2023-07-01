EXEMPLO PARA BAIXAR VÍDEO:
python3 main.py https://www.youtube.com/watch?v=zmx1pSxfG6s -ss 00:28:38 -t 00:47:00 -o output.mp4

EXEMPLO PARA CONVERTER PARA MP3:
ffmpeg -i output.mp4 -vn -ar 44100 -ac 2 -ab 320k -f mp3 output.mp3

