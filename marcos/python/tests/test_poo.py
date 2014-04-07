
# Unit testing in python

import unittest
import poo

class TestPoint(unittest.TestCase):
	def setUp(self):
		#print("SetUp!")
		self.p0 = poo.Punto.getOrg()
		self.p02 = poo.Punto(0,0)
		self.p1 = poo.Punto(1,1)
		self.p2 = poo.Punto(2,2)

	def tearDown(self):
		self.p0 = None
		#print("tearDown!")

	def testEq(self):
		self.assertEqual(self.p02, self.p0)
		self.assertTrue(not(self.p1 == self.p0))
		self.assertEqual(self.p0, self.p0)

	def testNEq(self):
		self.assertTrue(self.p1 != self.p0)
		self.assertTrue(not(self.p1 == self.p0))
		self.assertTrue(not(self.p0 != self.p0))

	def testGt(self):
		self.assertTrue(self.p2 > self.p1)

	def testGt(self):
		self.assertTrue(self.p2 > self.p1)

	def testOrg(self):
		self.assertTrue(self.p0.x == 0 and self.p0.y == 0)

	def testGetX(self):
		self.p0.getX() == self.p0.x

	def testGetY(self):
		self.p0.getY() == self.p0.y



unittest.main()
