from time import sleep

def fibonacci_decorator(func):
  def wrapper(*args, **kwargs):
    for element in func(args[0]):
      print(element)
      sleep(0.5)
    
  return wrapper


@fibonacci_decorator
def fibonacci(steps):
  list = []
  
  n1 = 0
  n2 = 1
  counter = 0

  while counter < steps:
    if counter == 0:
      counter += 1
      list.append(n1)
    elif counter == 1:
      counter += 1
      list.append(n2)
    else:
      aux = n1 + n2
      counter += 1
      n1, n2 = n2, aux
      list.append(aux)

  return list


if __name__ == '__main__':
  fibonacci(10)
