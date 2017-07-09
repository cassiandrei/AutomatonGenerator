Trabalho: Um Interpretador para Autômatos Finitos Determinísticos                             #

Alunos: Cassiano Andrei e Vinícius Mateus Dreifke
Materia: Compiladores
Data: 09/07/2017

Implementação do trabalho feita na linguagem Python3

Bibliotecas necessárias:
- python3
- antlr4 para python

Inicialização:
Executar pelo terminal:
- python3 main.py arquivo_com_automato.txt
exemplo: python3 main.py Automato.txt

Arquivos:
- AutomatonGrammar.g4: arquivo com a linguagem do ANTLR.
- Automato.txt: exemplo de um automato para testar.
- automato.py: possui as definições de um automato, fita, estados e transições. Contém os métodos de geração de filhos e a validação da entrada do programa.
- estados.py: arquivo complementar ao automato.py, classe para atribuição dos estados que serão contidos ao automato.
- main.py: iniciação do programa, gera as gramaticas a partir do arquivo de texto carregado e cria um automato com suas propriedades.

Descrição:
O programa executa a partir do main.py gerando a gramática dada pelo arquivo passado pela linha de comando do terminal. A geração é feita a partir da lib ANTLR4.
Após ter criado a gramática, um objeto do tipo automato é criado para configurar seus estados e transições.
O programa em seguida pede para entrar com uma fita que será testada no automato criado.
O programa retorna True se a fita for aceita e False caso ao contrário.