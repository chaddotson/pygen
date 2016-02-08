from abc import ABCMeta, abstractmethod
from math import pi, sin, cos
from random import normalvariate, seed

two_pi = 2 * pi


class DataGenerator(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def generate(self, *args, **kwargs):
        pass


class SinusoidWaveGenerator(DataGenerator):
    def __init__(self, amplitude, frequency_in_hz, phase_in_radians=0):
        super(SinusoidWaveGenerator, self).__init__()

        self._amplitude = amplitude
        self._frequency_in_hz = frequency_in_hz
        self._phase_in_radians = phase_in_radians


class SineWaveGenerator(SinusoidWaveGenerator):
    def generate(self, time_in_seconds):
        return self._amplitude * sin(two_pi * self._frequency_in_hz * time_in_seconds) + self._phase_in_radians


class CosineWaveGenerator(SinusoidWaveGenerator):
    def generate(self, time_in_seconds):
        return self._amplitude * cos(two_pi * self._frequency_in_hz * time_in_seconds) + self._phase_in_radians


def noisify_data_generator(data_generator, noise_mean, noise_std_dev):

    saved_generate = data_generator.generate

    def noisify(time_in_seconds):
        return saved_generate(time_in_seconds) * normalvariate(noise_mean, noise_std_dev)

    data_generator.generate = noisify

    return data_generator
