from multiprocessing import Queue
from jobs.interfaces import IJob
from consts import MIN_HEIGHT, MAX_HEIGHT, SCL_SLOPE, HFNU_SLOPE
from services import EdaAnalyzerService, PPGAnalyzerService, UnityService
from helpers import Buffer


class CoreJob(IJob):
    
    TAG = __name__

    def __init__(self, unity_host: str, unity_port: int):
        self.eda = EdaAnalyzerService()
        self.ppg = PPGAnalyzerService()
        self.unity_service = UnityService(unity_host, unity_port)

    def run(self, q: Queue, mapping: str, fu: float, fs: float):
        idx = 0 if mapping == 'scl_d' else 1
        buf = Buffer(capacity=int(fu * fs))
        h = MIN_HEIGHT
        try:
            while 1:

                while not buf.full:
                    sample = q.get()
                    buf.append(sample[idx])
                else:
                    sample = q.get()
                    if mapping == 'scl_d':
                        scl_d = self.eda.compute_derivative(buf, fs)
                        h += scl_d * SCL_SLOPE
                    elif mapping == 'hfnu':
                        hfnu = self.ppg.compute_hfnu(buf, fs)
                        h = HFNU_SLOPE * hfnu
                    else:
                        raise Exception('Invalid mapping type.')
                    self.unity_service.send_height(self.tresholding(h))
                    buf.clear()
                    buf.append(sample[idx])
        except KeyboardInterrupt:
            print(f'{self.TAG}: All done')
            
    def tresholding(self, h: float):        
        if h > MAX_HEIGHT:
            return MAX_HEIGHT
        elif h < MIN_HEIGHT:
            return MIN_HEIGHT
        else:
            return h


