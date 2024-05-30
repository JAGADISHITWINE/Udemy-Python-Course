import unittest
import First_Test
import Testing_A_Class_Method

@unittest.skip('')
class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(First_Test.add(2,3),5)
        self.assertEqual(First_Test.add(20,3),23)
        self.assertEqual(First_Test.add(12,3),15)
    
    def test_sub(self):
        self.assertEqual(First_Test.sub(2,3),-1)
        self.assertEqual(First_Test.sub(20,3),17)
        self.assertEqual(First_Test.sub(12,3),9)
        
    def test_mul(self):
        self.assertEqual(First_Test.mul(2,3),6)
        self.assertEqual(First_Test.mul(20,3),60)
        self.assertEqual(First_Test.mul(12,3),36)
    
    def test_div(self):
        self.assertEqual(First_Test.div(21,3),7)
        self.assertEqual(First_Test.div(12,3),4)


## Setup Method & TearDown Method
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calculate = Testing_A_Class_Method.Calculate()
        
    def tearDown(self):
        print('This is a tear down method, executes after each test')
        
    def test_add(self):
        self.assertEqual(self.calculate.add(2,3),5)
        
    def test_sub(self):
        self.assertEqual(self.calculate.sub(5,3),2)
    
    def test_mul(self):
        self.assertEqual(self.calculate.mul(2,3),6)
    
    def test_div(self):
        self.assertEqual(self.calculate.div(1,2),0.5)
    

  
if __name__=='__main__':
    unittest.main()