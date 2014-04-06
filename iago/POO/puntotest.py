import unittest
import punto

class TestPunto(unittest.TestCase):
    def setUp(self):
        self.p0 = punto.Punto.getOrg()
        self.p02 = punto.Punto(0, 0)
        self.p1 = punto.Punto(0, 1)
        
    def tearDown(self):
        self.p0 = None
        
    def testOrg(self):
        self.p0 = punto.Punto.getOrg()
        self.assertTrue(self.p0.x == 0 and self.p0.y == 0)
        self.assertEqual(punto.Punto(0,0),self.p0)
        
    def testGetX(self):
        self.p0.getX() == self.p0.x
        
    def testGetY(self):
         self.p0.getY() == self.p0.y
    
    def testEq(self):
        self.assertEqual(self.p0,self.p02)
        self.assertEqual(self.p0,self.p0)
        self.assertTrue(self.p0 != self.p1)
    
    def testNeq(self):
        self.assertTrue(self.p1 != self.p0)
        self.assertTrue(not(self.p1 == self.p0))
    
    def testGt(self):
        self.assertTrue(self.p1 > self.p0)
    
    def testLt(self):
        self.assertTrue(self.p0 < self.p1)

if __name__=="__main__":
    unittest.main()
    