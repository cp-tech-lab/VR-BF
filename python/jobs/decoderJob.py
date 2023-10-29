from jobs.interfaces import IJob
from multiprocessing import Queue
from struct import unpack


range_map = {0: 40.2, 1: 287.0, 2: 1000.0, 3: 3300.0}

class DecoderJob(IJob):

    TAG = __name__

    def run(self, rq: Queue, wq: Queue):
        try:
            while 1:
                if rq.empty():
                    continue
                data = rq.get()
                (ppg_raw, gsr_raw) = unpack('HH', data[4:8])
                rf = range_map.get(((gsr_raw >> 14) & 0xff))
                gsr_volts = (gsr_raw & 0x3fff) * (3.0/4095.0)
                if not rf:
                    continue
                gsr_ohm = rf/( (gsr_volts /0.5) - 1.0)
                ppg_mv = ppg_raw * (3000.0/4095.0)
                wq.put((1/gsr_ohm, ppg_mv))
        except KeyboardInterrupt:
            print(f'{self.TAG}: All done')


