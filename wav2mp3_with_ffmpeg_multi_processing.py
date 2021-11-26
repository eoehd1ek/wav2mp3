from multiprocessing import *
import os


process_size = 4

wav = ".wav"
mp3 = ".mp3"


def execute_command(queue):
    while(not queue.empty()):
        command = queue.get()
        os.system(command)


def main():
    freeze_support()    # pyinstaller exe 생성 시 프로그램이 재실행 되는 것을 방지

    path = os.getcwd()  # 현재 경로 획득
    file_list = os.listdir(path)  # 파일이름 리스트로 획득

    queue = Queue()
    for file in file_list:
        splited_name = file.split('.')
        # wav 확장자인 경우 queue에 명령어 추가
        if(splited_name[-1] == "wav" or splited_name[-1] == "WAV"):
            filename_for_transform = file[0: len(file) - 4]
            command = f"ffmpeg -i \"{filename_for_transform + wav}\" -codec:a libmp3lame -b:a 320k \"{filename_for_transform + mp3}\""
            queue.put(command)

    # 멀티 프로세싱 코드 작성
    if(not queue.empty()):
        procs = []
        for _ in range(process_size):
            p = Process(target=execute_command, args=(queue,))
            procs.append(p)
            p.start()

        for proc in procs:
            proc.join()

        print("모든 프로세스가 join 되었습니다.")
    else:
        print("변경할 wav 확장자 파일을 찾지 못했습니다.")

    os.system("pause")


if __name__ == "__main__":
    main()
