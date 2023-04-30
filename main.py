from multiprocessing import *
import os


process_size = 8
input_extension = "wav"
output_extension = "mp3"


def execute_command(queue):
    while (not queue.empty()):
        command = queue.get()
        os.system(command)


def is_audio_file(path: str) -> bool:
    return path[-len(input_extension):] == input_extension


def get_audio_file_list() -> list[str]:
    file_list = os.listdir(os.getcwd())
    audio_file_list = list(filter(is_audio_file, file_list))
    return audio_file_list


def get_result_file_path(path: str) -> str:
    return path[:(len(path) - len(input_extension))] + output_extension


def get_ffmpeg_command(path: str) -> str:
    return f"ffmpeg -i \"{path}\" -codec:a libmp3lame -b:a 320k \"{get_result_file_path(path)}\""


def main():
    freeze_support()
    command_queue = Queue()
    commands = list(map(get_ffmpeg_command, get_audio_file_list()))
    for command in commands:
        command_queue.put(command)

    if (not command_queue.empty()):
        procs = []
        for _ in range(process_size):
            p = Process(target=execute_command, args=(command_queue,))
            procs.append(p)
            p.start()
        for proc in procs:
            proc.join()
        print("모든 프로세스가 join 되었습니다.(작업이 완료되었습니다.)")
    else:
        print("변경할 wav 확장자 파일을 찾지 못했습니다.")
    os.system("pause")


if __name__ == "__main__":
    main()
