grammar AutomatonGrammar; 
s : 'A' alfabeto 'Q' estados 'T' transicoes 'I' inicio 'F' final EOF;

alfabeto : '={' alf '}';
alf : letra ',' alf | num ',' alf | letra | num ;
letra : TOKENALF;
TOKENALF: 'a'..'z' | 'A'..'Z';
num : TOKENNUM;
TOKENNUM: '0'..'9';

estados : '={'estado'}';
estado :  est',' estado | est;
est : 'q'num;

transicoes : '={'trans'}';
trans : '('est','letra')='est',' trans | '('est','letra')='est;

inicio : '='est;
final : '={'estado'}';
WS : [ \t\r\n]+ -> skip;