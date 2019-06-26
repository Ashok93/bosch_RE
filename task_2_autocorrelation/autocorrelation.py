import numpy as np
import time

def autocorr_sample(signal):
	start_time = time.time()
	n = len(signal)
	mean = sum(signal)/n
	var = sum([(s - mean)**2 for s in signal]) / n
	signal = [s - mean for s in signal]

	auto_correlation = []
	
	for i in range(n):
		c = 0
		for j in range(10):
			c += signal[j-i] * signal[j]

		c = c / (var*(n-i))
		auto_correlation.append(c)

	print("--- classical corr: %s seconds ---" % (time.time() - start_time))
	print(len(auto_correlation))
	return auto_correlation

def autocorr_sample_full(signal):
	start_time = time.time()
	n = len(signal)
	mean = sum(signal)/n
	var = sum([(s - mean)**2 for s in signal]) / n
	signal = [s - mean for s in signal]

	auto_correlation = []
	
	for i in range(n):
		c = 0
		for j in range(i, n):

			c += signal[j-i] * signal[j]

		c = c / (var*(n-i))
		auto_correlation.append(c)

	print("--- classical corr: %s seconds ---" % (time.time() - start_time))
	print(len(auto_correlation))
	return auto_correlation

def autocorr_numpy(signal):
	start_time = time.time()
	n = len(signal)
	variance = signal.var()
	signal = signal - signal.mean()
	r = np.correlate(signal, signal, mode = 'full')[-n:]
	auto_correlation = r/(variance*(np.arange(n, 0, -1)))

	print("--- classical numpy corr: %s seconds ---" % (time.time() - start_time))
	return auto_correlation

def autocorr_fft(x):
	start_time = time.time()
	r2=np.fft.ifft(np.abs(np.fft.fft(x))**2).real
	c=(r2/x.shape-np.mean(x)**2)/np.std(x)**2
	print("--- FFT corr: %s seconds ---" % (time.time() - start_time))
	return c[:len(x)//2]

if __name__ == "__main__":
	arr = np.random.randn(200)
	print("For sample signal size {}".format(len(arr)))
	print(autocorr_sample(arr))
	print(autocorr_sample_full(arr))
	print(autocorr_numpy(arr))
	autocorr_fft(arr)
	a = np.array([1,1,1,1,1,1,1,1,1,1])
	c = 0
	for i in range(100):
		for j in range(10):
			c += 1
	print(c)
