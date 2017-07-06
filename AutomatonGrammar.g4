grammar AutomatonGrammar; // Definimos uma gramática chamada Hello
r : 'hello' ID ; // encontramos a palavra chave ‘hello’ seguida de um identificador
ID : [a-z]+ ; // encontramos identificadores de letra minúscula
WS : [ \t\r\n]+ -> skip;
