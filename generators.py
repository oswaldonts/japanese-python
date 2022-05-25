from time import sleep

def run():
  for element in fibonacci_generator(10):
    print(element)
    sleep(0.5)


def fibonacci_generator(steps):
  n1 = 0
  n2 = 1
  counter = 0

  while counter < steps:
    if counter == 0:
      counter += 1
      yield n1

    elif counter == 1:
      counter += 1
      yield n2
      
    else:
      aux = n1 + n2
      counter += 1
      n1, n2 = n2, aux
      yield aux


if __name__ == '__main__':
  run()
