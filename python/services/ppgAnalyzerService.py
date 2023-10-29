from spectrum import pyule
from scipy.signal import butter, filtfilt, find_peaks
from scipy.interpolate import interp1d
from scipy.integrate import trapz
from numpy import diff, cumsum, arange, max, asarray

class PPGAnalyzerService:
    
    TAG = __name__
    cutoff = [0.05, 4]
    order = 3

    def get_filter_params(self, fs: float, btype: str = 'bandpass'):
        return butter(self.order, [2*self.cutoff[0]/fs, 2*self.cutoff[1]/fs], btype=btype)
    
    def filter(self, sig: list[float], fs: float):
        b, a = self.get_filter_params(fs)
        return filtfilt(b, a, sig, axis = 0)

    def _find_peaks(self, sig: list[float], fs: float):
        pks = find_peaks(sig, threshold = 0, distance = 0.7*fs)
        return pks[0]

    def _compute_rr(self, pks: list[float], fs: float, interp: bool = True):
        rr = diff(pks) / fs
        t_rr = cumsum(rr)
        t_rr -= t_rr[0]
        if interp:
            fs = 4
            fxx = interp1d(t_rr, rr, 'cubic')
            t_i = arange(t_rr[0], max(t_rr), 1/fs)
            rr_i = fxx(t_i)
            return t_i, rr_i
        return t_rr, rr
    
    def compute_hfnu(self, sig: list[float], fs: float):
        bp = self.filter(sig, fs)
        pks = self._find_peaks(bp, fs)
        _, rr = self._compute_rr(pks, fs, True)
        rr = rr - rr.mean() 
        ar = pyule(data=rr, order=16, NFFT=4096, sampling=4, scale_by_freq=False)
        ar()
        fx = asarray(ar.frequencies())
        px = asarray(ar.psd)

        cond_lf =  (fx > 0.04) & (fx <= 0.15)
        cond_hf = (fx > 0.15) & (fx <= 0.4)

        lf = trapz(px[cond_lf], fx[cond_lf])
        hf = trapz(px[cond_hf], fx[cond_hf])
        return hf / (lf + hf)



