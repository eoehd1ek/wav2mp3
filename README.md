# wav 확장자 파일을 mp3 확장자로 변환을 도와주는 프로그램

ffmpeg.exe 프로그램을 사용하므로,  
변환할 wav 확장자 파일과 ffmpeg.exe, wav2mp3.exe 파일을 한 폴더에 두고 wav2mp3.exe를 실행하면 됩니다.

multiprocessing 라이브러리를 사용해 한 번에 최대 4개의 자식 프로세스를 생성해 파일을 변환합니다.

wav2mp3.exe는 wav2mp3_with_ffmpeg_multi_processing.py 의 코드를 pyinstaller로 exe파일화 했습니다.
