grammar AutomatonGrammar; 
s : 'A'A | 'Q'Q | 'T'T | 'I'I | 'F'F;
A : '={'alf'}';
alf: (LETRA',' | NUM',')* | LETRA | NUM;
LETRA: 'a'..'z';
NUM: '0' .. '1';

Q: '={'estados'}';
estados: 'q'NUM ',' estados | 'q'NUM


WS : [ \t\r\n]+ -> skip;
