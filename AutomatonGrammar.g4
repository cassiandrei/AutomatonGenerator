grammar AutomatonGrammar; 
s : 'A' alfabeto| 'Q' estados| 'T' transicoes | 'I' inicio | 'F' final ;
alfabeto : '={' alf '}';
alf : (LETRA',' | NUM',')* | LETRA | NUM;
LETRA : 'a'..'z';
NUM : '0' .. '1';

estados : '={'estado'}';
estado :  (EST',')+ | EST;
EST : 'q'NUM;

transicoes : '{'trans'}';
trans : '('EST','LETRA')='EST',' | '('EST','LETRA')='EST;

inicio : EST;

final : '{'EST'}';

WS : [ \t\r\n]+ -> skip;
