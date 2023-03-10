# ffmpeg_trim
使用 FFmpeg 裁剪或調整影片速率。

如果你有一部三分鐘長度的影片，然後你想要將其中的一至兩分鐘調整成三倍速，那麼你可以做這個動作:<br>
If you have a 3 minute video, and you want to 3x speed from 1 minute to 2 minutes.<br>
|0:0-1:0|1:0-2:0, speed×3|2:0-3:0|

首先這是文字檔案 https://github.com/wayne931121/ffmpeg_trim/blob/main/trim.txt
```python
string = "0:0 1:0,speed=3 2:0 3:0"
#0:0:0      ~      0:1:0    ~      0:2:0       ~     0:3:0
#0:0:0-NormalSpeed-0:1:0-SpeedUp×3-0:2:0-NormalSpeed-0:3:0
```
然後執行 Run: (預設使用 Default "trim.txt")
```cmd
C:\Users\Desktop>python ffmpeg.py
ffmpeg -i "input.mp4" -filter_complex "[0:v]trim=start=0\\:0:end=1\\:0,setpts=PTS-STARTPTS[v0];[0:v]trim=start=1\\:0:end=2\\:0,setpts=PTS-STARTPTS,setpts=PTS/3[v1];[0:v]trim=start=2\\:0:end=3\\:0,setpts=PTS-STARTPTS[v2];[0:a]atrim=start=0\\:0:end=1\\:0,asetpts=PTS-STARTPTS[a0];[0:a]atrim=start=1\\:0:end=2\\:0,asetpts=PTS-STARTPTS,atempo=3[a1];[0:a]atrim=start=2\\:0:end=3\\:0,asetpts=PTS-STARTPTS[a2];[v0][v1][v2]concat=n=3:v=1:a=0[out_v];[a0][a1][a2]concat=n=3:v=0:a=1[out_a]" -map [out_v] -map [out_a] -c:v h264 -c:a aac "output.mp4"
```
接著 And then:
```cmd
C:\Users\Desktop>ffmpeg -i "input.mp4" -filter_complex "[0:v]trim=start=0\\:0:end=1\\:0,setpts=PTS-STARTPTS[v0];[0:v]trim=start=1\\:0:end=2\\:0,setpts=PTS-STARTPTS,setpts=PTS/3[v1];[0:v]trim=start=2\\:0:end=3\\:0,setpts=PTS-STARTPTS[v2];[0:a]atrim=start=0\\:0:end=1\\:0,asetpts=PTS-STARTPTS[a0];[0:a]atrim=start=1\\:0:end=2\\:0,asetpts=PTS-STARTPTS,atempo=3[a1];[0:a]atrim=start=2\\:0:end=3\\:0,asetpts=PTS-STARTPTS[a2];[v0][v1][v2]concat=n=3:v=1:a=0[out_v];[a0][a1][a2]concat=n=3:v=0:a=1[out_a]" -map [out_v] -map [out_a] -c:v h264 -c:a aac "output.mp4"
ffmpeg version N-102564-g2261cc6d8a Copyright (c) 2000-2021 the FFmpeg developers
  built with gcc 10-win32 (GCC) 20210408
  configuration: --prefix=/ffbuild/prefix --pkg-config-flags=--static --pkg-config=pkg-config --cross-prefix=x86_64-w64-mingw32- --arch=x86_64 --target-os=mingw32 --enable-gpl --enable-version3 --disable-debug --disable-w32threads --enable-pthreads --enable-iconv --enable-libxml2 --enable-zlib --enable-libfreetype --enable-libfribidi --enable-gmp --enable-lzma --enable-fontconfig --enable-libvorbis --enable-opencl --enable-libvmaf --enable-vulkan --enable-amf --enable-libaom --enable-avisynth --enable-libdav1d --enable-libdavs2 --enable-ffnvcodec --enable-cuda-llvm --enable-libglslang --enable-libgme --enable-libass --enable-libbluray --enable-libmp3lame --enable-libopus --enable-libtheora --enable-libvpx --enable-libwebp --enable-lv2 --enable-libmfx --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-librav1e --enable-librubberband --enable-schannel --enable-sdl2 --enable-libsoxr --enable-libsrt --enable-libsvtav1 --enable-libtwolame --enable-libuavs3d --enable-libvidstab --enable-libx264 --enable-libx265 --enable-libxavs2 --enable-libxvid --enable-libzimg --extra-cflags=-DLIBTWOLAME_STATIC --extra-cxxflags= --extra-ldflags=-pthread --extra-ldexeflags= --extra-libs=-lgomp
  libavutil      57.  0.100 / 57.  0.100
  libavcodec     59.  1.100 / 59.  1.100
  libavformat    59.  2.100 / 59.  2.100
  libavdevice    59.  0.100 / 59.  0.100
  libavfilter     8.  0.101 /  8.  0.101
  libswscale      6.  0.100 /  6.  0.100
  libswresample   4.  0.100 /  4.  0.100
  libpostproc    56.  0.100 / 56.  0.100
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'input.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    encoder         : Lavf59.2.100
  Duration: 00:07:37.76, start: 0.000000, bitrate: 558 kb/s
  Stream #0:0(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p, 1920x1080 [SAR 1:1 DAR 16:9], 421 kb/s, 30 fps, 30 tbr, 15360 tbn (default)
    Metadata:
      handler_name    : VideoHandler
      vendor_id       : [0][0][0][0]
  Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 128 kb/s (default)
    Metadata:
      handler_name    : SoundHandler
      vendor_id       : [0][0][0][0]
...
```
簡介 Introduce:
```cmd
C:\Users\Desktop>python ffmpeg.py  -h
usage: ffmpeg.py [-h] [-file FILE] [-text TEXT] [-input INPUT] [-output OUTPUT] [-mute]

Help write triming video code in ffmpeg command by giving text file.
給定剪裁及加速時間，產生 FFmpeg 命令。

optional arguments:
  -h, --help            show this help message and exit 幫助，顯示此幫助訊息並離開。
  -file FILE, -f FILE   input text file, including triming time. 文字檔案，包含裁剪或加速時間點。
  -text TEXT, -t TEXT   input text, including triming time. 輸入裁剪或加速時間點。
  -input INPUT, -i INPUT
                        input video file. 輸入影片的檔名。
  -output OUTPUT        output video file. 處理完影片的檔名。
  -mute, -m             mute video. 靜音影片。
```
使用其他文字檔案 Use other file:
```cmd
C:\Users\Desktop>python ffmpeg.py  -f trim1.txt
ffmpeg -i "input.mp4" -filter_complex "[0:v]trim=start=0\\:0:end=1\\:0,setpts=PTS-STARTPTS[v0];[0:v]trim=start=1\\:0:end=2\\:0,setpts=PTS-STARTPTS,setpts=PTS/5[v1];[0:v]trim=start=2\\:0:end=3\\:0,setpts=PTS-STARTPTS,setpts=PTS/0.5[v2];[0:a]atrim=start=0\\:0:end=1\\:0,asetpts=PTS-STARTPTS[a0];[0:a]atrim=start=1\\:0:end=2\\:0,asetpts=PTS-STARTPTS,atempo=5[a1];[0:a]atrim=start=2\\:0:end=3\\:0,asetpts=PTS-STARTPTS,atempo=0.5[a2];[v0][v1][v2]concat=n=3:v=1:a=0[out_v];[a0][a1][a2]concat=n=3:v=0:a=1[out_a]" -map [out_v] -map [out_a] -c:v h264 -c:a aac "output.mp4"
```
其他例子 Other Example:
```cmd
python ffmpeg.py -f    trim1.txt -i movie1.mp4     -o movie2.mp4
python ffmpeg.py -file trim1.txt -input movie1.mp4 -output movie2.mp4
python ffmpeg.py -t    "0:0 1:0,speed=5 2:0,speed=0.5 3:0"
python ffmpeg.py -text "0:0 1:0,speed=5 2:0,speed=0.5 3:0"
python ffmpeg.py -mute
```
文字檔範例(UTF8編碼) Text File Example:<br>
https://github.com/wayne931121/ffmpeg_trim/blob/main/trim.txt
```txt
0:0 1:0,speed=3 2:0 3:0
```
https://github.com/wayne931121/ffmpeg_trim/blob/main/trim1.txt
```txt
0:0
1:0,speed=5 
2:0,speed=0.5
3:0
```
