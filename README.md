# ffmpeg-wav-to-mp3-Helper
wav파일에서 mp3로 변환하는 ffmpeg명령어를 실행하는 프로그램  
wav파일을 320kbps mp3파일로 변환합니다.

# 사용법
1. 프로그램과 같은 폴더에 'ffmpeg.exe' 파일을 둔다.
2. 프로그램과 같은 폴더에 변환할 wav 파일을 둔다.
3. 이 프로그램을 실행시킨다.

# 실제 실행되는 명령어
```shell
ffmpeg -i "filename.wav" -codec:a libmp3lame -b:a 320k "filename.mp3"
```