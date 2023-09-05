# Enrico Bernz Reichow Santos, Gabriel Marques Simini, Henrique de Oliveira Godoy - BCC 2º SEMESTRE
# aqui fizemos uma função para verificar qual operação foi feita
def realizar_operacoes(operacoes, set1, set2):
  if operacoes == 'U':
    resultado = set1.union(set2)
    return f'União: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {resultado}'
  elif operacoes == 'I':
    resultado = set1.intersection(set2)
    return f'Interseção: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {resultado}'
  elif operacoes == 'D':
    resultado = set1.difference(set2)
    return f'Diferença: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {resultado}'
  elif operacoes == 'C':
    produto_cartesiano = {(x, y) for x in set1 for y in set2}
    return f'Produto Cartesiano: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {list(produto_cartesiano)}'


# função principal que lê os TXT e executa as operações certinhas
def main(input_file):
  with open(input_file, 'r') as file:
    num_operacoess = int(file.readline().strip())
    for _ in range(num_operacoess):
      operacoes = file.readline().strip()
      set1 = set(file.readline().strip().split(', ')) 
      set2 = set(file.readline().strip().split(', '))

      resultado = realizar_operacoes(operacoes, set1, set2)
      print(resultado)


if __name__ == "__main__":
  input_file = "input1.txt"  # coloque input1.txt input2.txt input3.txt pra fazer o teste com diferentes arquivos
  # sendo que o input1.txt é do exemplo que o professor Andrey passou #vai SAO PAULO
  main(input_file)
