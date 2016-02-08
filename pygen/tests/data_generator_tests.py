from mock import patch
from unittest import TestCase


from pygen.data_generators import SineWaveGenerator, CosineWaveGenerator


class TestSineWaveGenerator(TestCase):


    def test_can_specify_amplitude(self):
        gen = SineWaveGenerator(2, 1)

        self.assertAlmostEquals(gen.generate(0.0), 0)
        self.assertAlmostEquals(gen.generate(0.25), 2)
        self.assertAlmostEquals(gen.generate(0.5), 0)
        self.assertAlmostEquals(gen.generate(0.75), -2)
        self.assertAlmostEquals(gen.generate(1.0), 0)

    def test_can_specify_frequency(self):
        gen = SineWaveGenerator(1, 2)

        self.assertAlmostEquals(gen.generate(0.0), 0)
        self.assertAlmostEquals(gen.generate(0.125), 1)
        self.assertAlmostEquals(gen.generate(0.25), 0)
        self.assertAlmostEquals(gen.generate(0.375), -1)
        self.assertAlmostEquals(gen.generate(0.5), 0)
        self.assertAlmostEquals(gen.generate(0.625), 1)
        self.assertAlmostEquals(gen.generate(0.75), 0)
        self.assertAlmostEquals(gen.generate(0.875), -1)
        self.assertAlmostEquals(gen.generate(1.0), 0)


class TestCosineWaveGenerator(TestCase):

    def test_can_specify_amplitude(self):
        gen = CosineWaveGenerator(2, 1)

        self.assertAlmostEquals(gen.generate(0.0), 2)
        self.assertAlmostEquals(gen.generate(0.25), 0)
        self.assertAlmostEquals(gen.generate(0.5), -2)
        self.assertAlmostEquals(gen.generate(0.75), 0)
        self.assertAlmostEquals(gen.generate(1.0), 2)

    def test_can_specify_frequency(self):
        gen = CosineWaveGenerator(1, 2)

        self.assertAlmostEquals(gen.generate(0.0), 1)
        self.assertAlmostEquals(gen.generate(0.125), 0)
        self.assertAlmostEquals(gen.generate(0.25), -1)
        self.assertAlmostEquals(gen.generate(0.375), 0)
        self.assertAlmostEquals(gen.generate(0.5), 1)
        self.assertAlmostEquals(gen.generate(0.625), 0)
        self.assertAlmostEquals(gen.generate(0.75), -1)
        self.assertAlmostEquals(gen.generate(0.875), 0)
        self.assertAlmostEquals(gen.generate(1.0), 1)