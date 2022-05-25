from time import sleep

def run():  
  for element in FibonacciIterator(10):
    print(element)
    sleep(0.5)


class FibonacciIterator:
  def __init__(self, steps) -> None:
      self.steps = steps


  def __iter__(self):
    self.n1 = 0
    self.n2 = 1
    self.counter = 0
    return self


  def __next__(self):
    if self.counter < self.steps:
      if self.counter == 0:
        self.counter += 1
        return self.n1

      elif self.counter == 1:
        self.counter += 1
        return self.n2

      else:
        self.counter += 1
        self.aux = self.n1 + self.n2
        self.n1, self.n2 = self.n2, self.aux
        return self.aux
        
    else:
      raise StopIteration


if __name__ == '__main__':
  run()
