from json import load
from multiprocessing import Process, Queue
from provider import acquire, decode, core


config = load(open('config.json'))


if __name__ == '__main__':

    rq = Queue()
    wq = Queue()

    acq_task = Process(target=acquire, args=(rq, config.get('port'), config.get('fs')))
    decode_task = Process(target=decode, args=(rq, wq, ))
    core_task = Process(target=core, args=(wq, config.get('mapping'), config.get('fu'), config.get('fs'), ))

    acq_task.start()
    decode_task.start()
    core_task.start()

    acq_task.join()
    decode_task.join()
    core_task.join()  