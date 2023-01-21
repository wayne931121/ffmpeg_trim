# ffmpeg_trim
ffmpeg_trim

If you have a 3 minute video, and you want to 3x speed from 1 minute to 2 minutes.<br>
|0:0-1:0|1:0-2:0, speed×3|2:0-3:0|

https://github.com/wayne931121/ffmpeg_trim/blob/main/ffmpeg.py#L3
```python
string = "0:0 1:0,speed=3 2:0 3:0"
#ffmpeg.py line:3
#0:0:0      ~      0:1:0    ~      0:2:0       ~     0:3:0
#0:0:0-NormalSpeed-0:1:0-SpeedUp×3-0:2:0-NormalSpeed-0:3:0

all_mute=False
#ffmpeg.py line:15
```
Run:
```cmd
C:\Users\Desktop>python ffmpeg.py
ffmpeg -i "input.mp4" -filter_complex "[0:v]trim=start=0\\:0:end=1\\:0,setpts=PTS-STARTPTS[v0];[0:v]trim=start=1\\:0:end=2\\:0,setpts=PTS-STARTPTS,setpts=PTS/3[v1];[0:v]trim=start=2\\:0:end=3\\:0,setpts=PTS-STARTPTS[v2];[0:a]atrim=start=0\\:0:end=1\\:0,asetpts=PTS-STARTPTS[a0];[0:a]atrim=start=1\\:0:end=2\\:0,asetpts=PTS-STARTPTS,atempo=3[a1];[0:a]atrim=start=2\\:0:end=3\\:0,asetpts=PTS-STARTPTS[a2];[v0][v1][v2]concat=n=3:v=1:a=0[out_v];[a0][a1][a2]concat=n=3:v=0:a=1[out_a]" -map [out_v] -map [out_a] -c:v h264 -c:a aac "output.mp4"
```
And then:
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
