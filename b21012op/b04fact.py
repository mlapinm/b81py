if __name__ == "__main__":
  import unittest

def factorize(x):
    """ 
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass
    return
    if type(x) == str or type(x) == float:
      raise TypeError
    if x < 0:
      raise ValueError
    if x == 0 or x == 1:
      return (x, )
    res = []
    b = x
    a = 2
    while a < b:
      k = b // a
      if k * a == b:
        b = k
        res += [a]
      a += 1 
    res += [b]

    return tuple(res)


class TestFactorize(unittest.TestCase):

  def test_wrong_types_raise_exception(self):
    sequence = ['string',  1.5]
    for e in sequence:
      with self.subTest(x=e):
        self.assertRaises(TypeError, factorize, e)

  def test_negative(self):
    sequence = [-1,  -10,  -100]
    for e in sequence:
      with self.subTest(x=e):
        self.assertRaises(ValueError, factorize, e)

  def test_zero_and_one_cases(self):
    sequence = [0, 1]
    for e in sequence:
      with self.subTest(x=e):
        self.assertEqual((e,), factorize(e))

  def test_simple_numbers(self):
    sequence = [(3, (3, )), (13, (13, )), (29, (29, ))]
    for e in sequence:
      with self.subTest(x=e):
        self.assertEqual(factorize(e[0]), e[1])

  def test_two_simple_multipliers(self):
    sequence = [(6, (2, 3)),   (26, (2, 13)),   (121, (11, 11))]
    for e in sequence:
      with self.subTest(x=e):
        self.assertEqual(factorize(e[0]), e[1])

  def test_many_multipliers(self):
    sequence = [(1001, (7, 11, 13)), (9699690, (2, 3, 5, 7, 11, 13, 17, 19))]
    for e in sequence:
      with self.subTest(x=e):
        self.assertEqual(factorize(e[0]), e[1])


if __name__ == "__main__":
  unittest.main()
