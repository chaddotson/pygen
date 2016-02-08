from mock import patch
from unittest import TestCase


from pygen.data_generators import SineWaveGenerator, CosineWaveGenerator, noisify_data_generator


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


class TestNoisifyDataGenerator(TestCase):
    @patch("pygen.data_generators.normalvariate")
    def test_can_noisify_with_normal_random_generator(self, normalvariate):

        normalvariate.return_value = 3.0

        gen = noisify_data_generator(SineWaveGenerator(1, 2), 2, 0.25)

        self.assertAlmostEquals(gen.generate(0.125), 3)

    @patch("pygen.data_generators.normalvariate")
    def test_can_noisify_calls_normal_random_generator_with_mean_and_std_dev(self, normalvariate):

        gen = noisify_data_generator(SineWaveGenerator(1, 2), 2, 0.25)
        gen.generate(0.125)

        normalvariate.assert_called_with(2, 0.25)

