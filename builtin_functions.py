# abs(x): Retorna o valor absoluto de um número.
print(abs(-5))  # 5

# aiter(iterable): Retorna um iterador para o objeto iterável ("lista percorrível").
a = [1, 2, 3]
it = aiter(a)
print(next(it))  # 1
print(next(it))  # 2

# all(iterable): Retorna True se TODOS os elementos do iterável forem verdadeiros.
print(all([True, 1, "Olá"]))  # True
print(all([True, 0, "Olá"]))  # False - O 0 é considerado falso

# anext(iterator[, default]): Retorna o próximo item do iterador.
# Diferente do next(), pode definir um valor (int, str, ...) se o próximo valor não existir
a = [1, 2, 3]
it = iter(a)
print(anext(it))  # 1
print(anext(it))  # 2

# any(iterable): Retorna True se pelo menos UM elemento do iterável for verdadeiro.
print(any([True, 0, ""]))  # True
print(any([False, 0, ""]))  # False

# ascii(object): Retorna uma string representando o objeto com caracteres ASCII.
print(ascii('café'))  # "'caf\\xe9'"

# bin(x): Converte um inteiro para uma string binária.
print(bin(10))  # '0b1010'

# bool(x): Converte um valor para um booleano (True ou False).
print(bool("Olá"))  # True
print(bool(""))  # False

# breakpoint(): Permite inserir um breakpoint para depuração.
# (Comentado para evitar interrupções)
# for i in range(5):
#     breakpoint()
#     print(i)

# bytearray([source[, encoding[, errors]]]): Cria um objeto bytearray.
print(bytearray([1, 2, 3]))  # bytearray(b'\x01\x02\x03')

# bytes([source[, encoding[, errors]]]): Cria um objeto bytes.
print(bytes([1, 2, 3]))  # b'\x01\x02\x03'

# callable(object): Retorna True se o objeto for chamável (como uma função).
def my_function():
    return True
print(callable(my_function))  # True

# chr(i): Retorna o caractere Unicode correspondente ao inteiro i.
print(chr(97))  # 'a'

# classmethod(function): Declara um método de classe.
class MyClass:
    @classmethod
    def my_method(cls):
        print("Método de classe")
MyClass.my_method()  # Saída: Método de classe

# compile(source, filename, mode, flags=0, dont_inherit=0, optimize=-1):
# Compila uma string em um objeto de código.
code = compile('print("Olá")', 'test.py', 'exec')
exec(code)  # Saída: Olá

# complex([real[, imag]]): Cria um número complexo.
print(complex(1, 2))  # (1+2j)

# delattr(object, name): Exclui um atributo de um objeto.
class MyClass:
    x = 5
obj = MyClass()
delattr(obj, 'x')
# print(obj.x)  # Irá gerar um erro, pois o atributo 'x' foi excluído

# dict(**kwarg): Cria um dicionário.
print(dict(nome="João", idade=30))  # {'nome': 'João', 'idade': 30}

# dir([object]): Lista os nomes no escopo atual ou os atributos de um objeto.
print(dir())  # Exibe uma lista de nomes no escopo atual

# divmod(a, b): Retorna o quociente e o resto da divisão de a por b.
print(divmod(10, 3))  # (3, 1)

# enumerate(iterable, start=0): Retorna tuplas (índice, valor)
# para cada item em um iterável.
for i, v in enumerate(["a", "b", "c"]):
    print(i, v)  # Saída: 0 a, 1 b, 2 c

# eval(expression[, globals[, locals]]):
# Executa uma string como uma expressão Python.
print(eval("1 + 2"))  # 3

# exec(object[, globals[, locals]]):
# Executa um objeto (como um objeto de código) como código Python.
exec('print("Olá")')  # Saída: Olá

# filter(function, iterable): Constrói um iterador a partir dos elementos
# de iterable para os quais function retorna True.
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))  # [2, 4]

# float([x]): Converte um número ou string para um número de ponto flutuante.
print(float("3.14"))  # 3.14

# format(value[, format_spec]): Formata um valor usando um especificador de formato.
print(format(1000, ',d'))  # '1,000'

# frozenset([iterable]): Cria um conjunto imutável.
print(frozenset([1, 2, 3]))  # frozenset({1, 2, 3})

# getattr(object, name[, default]): Retorna o valor do atributo nomeado
# de um objeto.
class MyClass:
    x = 5
obj = MyClass()
print(getattr(obj, 'x'))  # 5

# globals(): Retorna um dicionário representando a tabela de símbolos global atual.
print(globals())  # Exibe o dicionário global

# hasattr(object, name): Retorna True se o objeto tiver o atributo nomeado.
class MyClass:
    x = 5
obj = MyClass()
print(hasattr(obj, 'x'))  # True

# hash(object): Retorna o valor hash do objeto.
print(hash("Olá"))  # Valor hash da string "Olá"

# help([object]): Invoca o sistema de ajuda integrado.
# help(print)  # Descomente para visualizar a ajuda da função 'print'

# hex(x): Converte um inteiro para uma string hexadecimal.
print(hex(255))  # '0xff'

# id(object): Retorna a "identidade" de um objeto.
print(id("Olá"))  # Valor da identidade da string "Olá"

# input([prompt]): Lê uma linha de entrada.
# nome = input("Digite seu nome: ")  # Descomente para testar

# int([x]): Converte um número ou string para um inteiro.
print(int("10"))  # 10

# isinstance(object, classinfo):
# Retorna True se o objeto for uma instância de classinfo.
print(isinstance("Olá", str))  # True

# issubclass(class, classinfo):
# Retorna True se class for uma subclasse de classinfo.
class MinhaClasse(object):
    pass
print(issubclass(MinhaClasse, object))  # True

# iter(object[, sentinel]): Retorna um iterador para o objeto.
it = iter([1, 2, 3])
print(next(it))  # 1

# len(s): Retorna o comprimento (o número de itens) de um objeto.
print(len("Olá"))  # 3

# list([iterable]): Cria uma lista.
print(list(range(1, 4)))  # [1, 2, 3]

# locals(): Retorna um dicionário representando
# a tabela de símbolos local atual.
print(locals())  # Exibe o dicionário local

# map(function, iterable, ...): Aplica function a cada item de iterable
# e retorna um iterador.
print(list(map(lambda x: x * 2, [1, 2, 3])))  # [2, 4, 6]

# max(iterable, *[, key, default]) or max(arg1, arg2, *args[, key]):
# Retorna o maior item em um iterável ou o maior de dois ou mais argumentos.
print(max([1, 2, 3]))  # 3

# memoryview(obj): Cria um objeto memoryview a partir de um objeto
# que suporta o protocolo buffer.
data = b'abc'
view = memoryview(data)
print(view[0])  # 97

# min(iterable, *[, key, default]) or min(arg1, arg2, *args[, key]):
# Retorna o menor item em um iterável ou o menor de dois ou mais argumentos.
print(min([1, 2, 3]))  # 1

# next(iterator[, default]): Retorna o próximo item de um iterador.
it = iter([1, 2, 3])
print(next(it))  # 1

# object(): Retorna um novo objeto sem características.
obj = object()

# oct(x): Converte um inteiro para uma string octal.
print(oct(10))  # '0o12'

# open(file, mode='r', buffering=-1, encoding=None, errors=None,
# newline=None, closefd=True, opener=None):
# Abre um arquivo e retorna um objeto de arquivo.
with open('meu_arquivo.txt', 'w') as f:
    f.write('Olá, mundo!')

# ord(c): Dada uma string representando um caractere Unicode,
# retorna um inteiro representando o código do caractere.
print(ord('a'))  # 97

# pow(x, y[, z]): Retorna x elevado à potência y;
# se z está presente, retorna x elevado à potência y, módulo z.
print(pow(2, 3))  # 8

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
# Imprime objetos na saída padrão.
print("Olá", "mundo")  # Saída: Olá mundo

# property(fget=None, fset=None, fdel=None, doc=None):
# Cria uma propriedade para uma classe.
class MyClass:
    def __init__(self):
        self._x = 0
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
obj = MyClass()
obj.x = 10
print(obj.x)  # 10

# range(stop) or range(start, stop[, step]): Retorna uma sequência de números.
print(list(range(1, 5)))  # [1, 2, 3, 4]

# repr(object): Retorna uma string contendo
# uma representação imprimível de um objeto.
print(repr("Olá"))  # "'Olá'"

# reversed(seq): Retorna um iterador reverso.
print(list(reversed([1, 2, 3])))  # [3, 2, 1]

# round(number[, ndigits]): Retorna o número arredondado
# para ndigits após a vírgula decimal.
print(round(3.14159, 2))  # 3.14

# set([iterable]): Cria um conjunto.
print(set([1, 2, 3, 1, 2]))  # {1, 2, 3}

# setattr(object, name, value): Define o valor do atributo
# nomeado de um objeto.
class MyClass:
    pass
obj = MyClass()
setattr(obj, 'x', 5)
print(obj.x)  # 5

# slice(stop) or slice(start, stop[, step]): Retorna um objeto slice.
my_list = [1, 2, 3, 4, 5]
my_slice = slice(1, 4, 2)
print(my_list[my_slice])  # [2, 4]

# sorted(iterable, *, key=None, reverse=False):
# Retorna uma nova lista classificada a partir dos itens do iterável.
print(sorted([3, 1, 4, 2]))  # [1, 2, 3, 4]

# staticmethod(function): Declara um método estático.
class MyClass:
    @staticmethod
    def my_method():
        print("Método estático")
MyClass.my_method()  # Saída: Método estático

# str(object=''): Retorna uma string contendo uma representação
# legível por humanos de um objeto.
print(str(10))  # '10'

# sum(iterable, /, start=0): Soma os itens de um iterável
# de da esquerda para a direita e retorna a soma total.
print(sum([1, 2, 3]))  # 6

# super([type[, object-or-type]]): Retorna um objeto proxy que delega
# chamadas de método para uma classe pai ou irmão.
class Pai:
    def metodo(self):
        print("Método da classe Pai")
class Filho(Pai):
    def metodo(self):
        super().metodo()
        print("Método da classe Filho")
obj = Filho()
obj.metodo()  # Saída: Método da classe Pai, Método da classe Filho

# tuple([iterable]): Cria uma tupla.
print(tuple([1, 2, 3]))  # (1, 2, 3)

# type(object) or type(name, bases, dict): Retorna o tipo de um objeto.
print(type("Olá"))  # <class 'str'>

# vars([object]): Retorna o atributo __dict__ de um objeto.
class MyClass:
    x = 5
obj = MyClass()
print(vars(obj))  # {'x': 5}

# zip(*iterables): Cria um iterador que agrega elementos
# de cada um dos iteráveis.
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))  # [(1, 'a'), (2, 'b'), (3, 'c')]