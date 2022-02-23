import unittest

class TestFibonacci(unittest.TestCase):
  def test_simple(self):
    self.assertEqual(5, fib(5))

  def test_wrong_types_raise_exception(self):
    aa = ['str', 0.1, -1]
    for e in aa:
      with self.subTest(i=e):
        self.assertRaises(TypeError, fib, e)



def fib(n: int) -> int:
  if type(n) == str or type(n) == float or n < 0:
    raise TypeError
  f = [0, 1] + [0] * (n - 1)
  for i in range(2, n+1):
    f[i] = f[i-2] + f[i-1]
  return f[n]

def factorize(x):
  l = []
  for i in range(1, x+1):
    if x // i * i == x:
      l += [i]
  return l


if __name__ == "__main__":
  unittest.main()

  items = []
  for i in range(6):
    items += [fib(i)] 
  # print(items)
  # print(factorize(28))
