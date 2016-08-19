import sys
sys.path.insert(0, '../src/')
import index as tradutor
import unittest

class TestaOTradutor(unittest.TestCase):
	def test_deveRetornarOValorEsperadoParaHOMESWEETHOME(self):
		self.assertEqual(tradutor.traduz("1-HOME-SWEET-HOME"), '1-4663-79338-4663')

	def test_deveRetornar8(self):
		self.assertEqual(tradutor.traduz("V"), '8')

	def test_deveRetornar4(self):
		self.assertEqual(tradutor.traduz("I"), '4')

	def test_deveRetornarVivo(self):
		self.assertEqual(tradutor.traduz("VIVO"), '8486')

	def test_esperoQueABCSeja222(self):
		self.assertEqual(tradutor.traduz("ABC"), '222')

	def test_esperoQueSejaDOJOMT(self):
		self.assertEqual(tradutor.traduz("dojoMT"), '365668')

	def test_esperoQueSejahome4241(self):
		self.assertEqual(tradutor.traduz("homE4241"), "46634241")

	def test_EsperoQueAceiteEspacoAsteriscoJogoDaVelha(self):
		self.assertEqual(tradutor.traduz(" #*31E"), " #*313")

if __name__ == '__main__':
    unittest.main()