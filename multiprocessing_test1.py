from multiprocessing import *
import os


queue_size = 4


def print_queue_data(queue):
    process_id = os.getpid()
    while(not queue.empty()):
        data = queue.get()
        print(
            f"pid = {process_id}, num = {data}, 남은 번호 = {queue.qsize()} \n")


def main():
    freeze_support()        # pyinstaller exe 생성 시 프로그램이 재실행 되는 것을 방지

    datas = [i + 1 for i in range(100)]
    queue = Queue()
    for i in datas:
        queue.put(i)

    procs = []
    for _ in range(queue_size):
        p = Process(target=print_queue_data, args=(queue,))
        procs.append(p)
        p.start()

    for proc in procs:
        proc.join()

    print(10)
    os.system("pause")


if __name__ == "__main__":
    main()
