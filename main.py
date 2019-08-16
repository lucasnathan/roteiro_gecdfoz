def main():
  print('por favor digite o número correspondente a sua operação:')
  print('1 - adicao')
  print('2 - subtracao')
  print('3 - divisao')
  print('4 - multiplicacao')
  operacao = int(input())
  if operacao == 1:
    print('adicao')
  elif operacao == 2:
    print('subtracao')
  elif operacao == 3:
    print('divisao')
  elif operacao == 4:
    print('multiplicacao')
  else:
    print('operacao não implementada')

if __name__ == "__main__":
  main()