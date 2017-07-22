from sage.all import *
from ..matsumoto_imai import *
import time

class Sflashv1(MatsumotoImai):

	def __init__(self):
		i,j = var('i', 'j')
		super(Sflashv1, self).__init__(2**7, 37, 11, 2**258+sum(sum(2**j,j,154*i+76,154*i+152),i,0,17))
		x = var('x')
		self.Fqn = self.Fq.extension(x**37+x**12+x**10+x**2+1, 'W')

	def genAff(self, n):
		AG = AffineGroup(n, GF(2))
		return AG.random_element()

	def getExpTable(self):
		return [[0,8,9,14,16,17,18,27,30,31,33,34],[11,14,24,25,26,27,29,30,31,32,36],[9,14,15,22,23,27,28,29,31],[5,11,14,24,25,26,27,29,31,36],[8,18,19,21,22,26,27,28,30],[5,12,14,24,25,27,28,29,33],[10,17,18,22,23,28,29,32,34,35],[12,14,18,19,23,25,27,28,29,30,32,33],[1,9,16,17,21,22,26,27,31,33,34],[12,15,18,19,23,24,25,26,27,28,30,31,32,33],[8,9,10,14,15,17,18,23,24,27,28,29,31,32,33,34],[6,11,12,14,15,24,28,29,31,36],[14,15,19,20],[5,6,11,13,14,15,24,27,28,30,31,34,36],[8,11,21,22,23,24,26,27,28,29,33,35,36],[5,12,13,14,15,19,20,25,26,27,30,31,34],[2,27,29],[12,13,14,16,18,20,23,24,26,30,31,34],[9,11,21,22,24,25,26,27,29,30,34],[7,12,13,15,16,18,19,23,24,25,29,30,32],[15,16,20,21],[6,7,12,14,15,16,25,28,29,31,32,35],[9,12,22,23,24,25,27,28,29,30,34,36],[6,13,14,15,16,20,21,26,27,28,31,32,35],[3,28,30],[13,14,15,17,19,21,24,25,27,31,32,35],[10,12,22,23,25,26,27,28,30,31,35],[8,13,14,16,17,19,20,24,25,26,30,31,33],[16,17,21,22],[7,8,13,15,16,17,26,29,30,32,33,36],[10,13,23,24,25,26,28,29,30,31,35],[7,14,15,16,17,21,22,27,28,29,32,33,36],[4,29,31],[14,15,16,18,20,22,25,26,28,32,33,36],[11,13,23,24,26,27,28,29,31,32,36],[9,14,15,17,18,20,21,25,26,27,31,32,34],[17,18,22,23]]

	def Fmap(self, TX):
		W = self.PFqn.extension(self.Fqn.modulus()).gen()
		Xn = vector(self.PFqn.gens())
		Wn = vector(map(lambda x: W**x, range(self.n)))
		QTX = []
		powtab = self.getExpTable()
		for i in range(self.n):
			QTX.append(sum(map(lambda j: TX[j], powtab[i])))
		return vector(((vector(QTX) * Wn) * (vector(TX) * Wn)).lift().coefficients())

	def genP(self):
		super(Sflashv1, self).genP()
		self.P = self.P[0:26]