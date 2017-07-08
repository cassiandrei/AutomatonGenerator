grammar AutomatonGrammar; 
s : 'A' A | 'Q' Q | 'T' T | 'I' I | 'F' F ;
A : '={' alf '}';
alf : (LETRA',' | NUM',')* | LETRA | NUM;
LETRA : 'a'..'z';
NUM : '0' .. '1';

Q : '={'estados'}';
estados :  (EST',')+ | EST;
EST : 'q'NUM;

T : '{'trans'}';
trans : '('EST','LETRA')='EST',' | '('EST','LETRA')='EST;

I : EST;

F : '{'EST'}';

WS : [ \t\r\n]+ -> skip;
