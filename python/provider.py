from multiprocessing import Queue
from jobs import AcquisitionJob, DecoderJob, CoreJob
from test.mockedJob import MockedJob
from json import load

config = load(open('config.json'))


_rq = Queue()
_wq = Queue()
_acquisition_task = AcquisitionJob()
_decoder_task = DecoderJob()
_core_task = CoreJob(config.get('UnityAppHost'), config.get('UnityAppPort'))


_mocked_task = MockedJob(_rq)


def acquire(rq: Queue, port: str, fs: float):
    _acquisition_task.run(rq, port, fs)

def decode(rq: Queue, wq: Queue):
    _decoder_task.run(rq=rq, wq=wq)

def core(q: Queue, mapping: str, fu: float, fs: float):
    _core_task.run(q, mapping, fu, fs)

def mock_random_data(rq: Queue):
    _mocked_task.run(rq=rq)