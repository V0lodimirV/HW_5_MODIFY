def dec(func):
  def wrapper(a,b):
    res = func(a,b)
    f = open('результат вызова функции','a')
    f.write('результат работы функции'+" "+ str(res) + '\n')
    f.close()
    print('результат работы функции',res)
    return func(a,b)
  return wrapper



@dec  # декорирование функции
def func(a,b):
  return (a+b)


func(1,2)
