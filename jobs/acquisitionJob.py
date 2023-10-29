import sys
from struct import pack
from serial import Serial, SerialException
from multiprocessing import Queue
from jobs.interfaces import IJob

class AcquisitionJob(IJob):

    TAG = __name__


    def run(self, rq: Queue, port: str, fs: float):
        
        # port opening
        try:
            ser = Serial(port, 112800)
            ser.flushInput()
            print(f"{self.TAG}: {port} port opening, done.")
        except SerialException as e:
            print(f'{self.TAG}: {e}')
            sys.exit()
    
         # sensors settings 
        ser.write(pack('BBBB', 0x08 , 0x04, 0x01, 0x00))  
        ddata = ""
        ack = pack('B', 0xff)
        while ddata != ack:
            ddata = ser.read(1)   
        print(f'{self.TAG}: sensor setting, done.')

        # Enable internal expansion board
        ser.write(pack('BB', 0x5E, 0x01))
        ddata = ""
        ack = pack('B', 0xff)
        while ddata != ack:
            ddata = ser.read(1)
        print(f'{self.TAG}: enable internal expansion board power, done.')

        # sampling frequency
        clock_wait = int((2 << 14) / fs)
        ser.write(pack('<BH', 0x05, clock_wait))
        ddata = ""
        ack = pack('B', 0xff)
        while ddata != ack:
            ddata = ser.read(1)
        print(f'{self.TAG}: sampling frequency ({fs}Hz) set.')

        # acquisition loop
        while 1:
            try:
                data = ser.read(size=8)
                rq.put(data)
            except KeyboardInterrupt:
                print(f'{self.TAG}: All done')
                sys.exit()
            except Exception:
                sys.exit()


