# Generated from AutomatonGrammar.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("X\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\5\2\37\n\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4")
        buf.write(")\n\4\f\4\16\4,\13\4\3\4\3\4\5\4\60\n\4\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\6\68\n\6\r\6\16\69\3\6\5\6=\n\6\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\5\bP\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\2\2\13\2\4\6\b")
        buf.write("\n\f\16\20\22\2\2\2Y\2\36\3\2\2\2\4 \3\2\2\2\6/\3\2\2")
        buf.write("\2\b\61\3\2\2\2\n<\3\2\2\2\f>\3\2\2\2\16O\3\2\2\2\20Q")
        buf.write("\3\2\2\2\22S\3\2\2\2\24\25\7\3\2\2\25\37\5\4\3\2\26\27")
        buf.write("\7\4\2\2\27\37\5\b\5\2\30\31\7\5\2\2\31\37\5\f\7\2\32")
        buf.write("\33\7\6\2\2\33\37\5\20\t\2\34\35\7\7\2\2\35\37\5\22\n")
        buf.write("\2\36\24\3\2\2\2\36\26\3\2\2\2\36\30\3\2\2\2\36\32\3\2")
        buf.write("\2\2\36\34\3\2\2\2\37\3\3\2\2\2 !\7\b\2\2!\"\5\6\4\2\"")
        buf.write("#\7\t\2\2#\5\3\2\2\2$%\7\16\2\2%)\7\n\2\2&\'\7\17\2\2")
        buf.write("\')\7\n\2\2($\3\2\2\2(&\3\2\2\2),\3\2\2\2*(\3\2\2\2*+")
        buf.write("\3\2\2\2+\60\3\2\2\2,*\3\2\2\2-\60\7\16\2\2.\60\7\17\2")
        buf.write("\2/*\3\2\2\2/-\3\2\2\2/.\3\2\2\2\60\7\3\2\2\2\61\62\7")
        buf.write("\b\2\2\62\63\5\n\6\2\63\64\7\t\2\2\64\t\3\2\2\2\65\66")
        buf.write("\7\20\2\2\668\7\n\2\2\67\65\3\2\2\289\3\2\2\29\67\3\2")
        buf.write("\2\29:\3\2\2\2:=\3\2\2\2;=\7\20\2\2<\67\3\2\2\2<;\3\2")
        buf.write("\2\2=\13\3\2\2\2>?\7\13\2\2?@\5\16\b\2@A\7\t\2\2A\r\3")
        buf.write("\2\2\2BC\7\f\2\2CD\7\20\2\2DE\7\n\2\2EF\7\16\2\2FG\7\r")
        buf.write("\2\2GH\7\20\2\2HP\7\n\2\2IJ\7\f\2\2JK\7\20\2\2KL\7\n\2")
        buf.write("\2LM\7\16\2\2MN\7\r\2\2NP\7\20\2\2OB\3\2\2\2OI\3\2\2\2")
        buf.write("P\17\3\2\2\2QR\7\20\2\2R\21\3\2\2\2ST\7\13\2\2TU\7\20")
        buf.write("\2\2UV\7\t\2\2V\23\3\2\2\2\t\36(*/9<O")
        return buf.getvalue()


class AutomatonGrammarParser ( Parser ):

    grammarFileName = "AutomatonGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'A'", "'Q'", "'T'", "'I'", "'F'", "'={'", 
                     "'}'", "','", "'{'", "'('", "')='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LETRA", "NUM", "EST", "WS" ]

    RULE_s = 0
    RULE_alfabeto = 1
    RULE_alf = 2
    RULE_estados = 3
    RULE_estado = 4
    RULE_transicoes = 5
    RULE_trans = 6
    RULE_inicio = 7
    RULE_final = 8

    ruleNames =  [ "s", "alfabeto", "alf", "estados", "estado", "transicoes", 
                   "trans", "inicio", "final" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    LETRA=12
    NUM=13
    EST=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alfabeto(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.AlfabetoContext,0)


        def estados(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.EstadosContext,0)


        def transicoes(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.TransicoesContext,0)


        def inicio(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.InicioContext,0)


        def final(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.FinalContext,0)


        def getRuleIndex(self):
            return AutomatonGrammarParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = AutomatonGrammarParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AutomatonGrammarParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(AutomatonGrammarParser.T__0)
                self.state = 19
                self.alfabeto()
                pass
            elif token in [AutomatonGrammarParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(AutomatonGrammarParser.T__1)
                self.state = 21
                self.estados()
                pass
            elif token in [AutomatonGrammarParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.match(AutomatonGrammarParser.T__2)
                self.state = 23
                self.transicoes()
                pass
            elif token in [AutomatonGrammarParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.match(AutomatonGrammarParser.T__3)
                self.state = 25
                self.inicio()
                pass
            elif token in [AutomatonGrammarParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.match(AutomatonGrammarParser.T__4)
                self.state = 27
                self.final()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlfabetoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alf(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.AlfContext,0)


        def getRuleIndex(self):
            return AutomatonGrammarParser.RULE_alfabeto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlfabeto" ):
                listener.enterAlfabeto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlfabeto" ):
                listener.exitAlfabeto(self)




    def alfabeto(self):

        localctx = AutomatonGrammarParser.AlfabetoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_alfabeto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(AutomatonGrammarParser.T__5)
            self.state = 31
            self.alf()
            self.state = 32
            self.match(AutomatonGrammarParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETRA(self, i:int=None):
            if i is None:
                return self.getTokens(AutomatonGrammarParser.LETRA)
            else:
                return self.getToken(AutomatonGrammarParser.LETRA, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(AutomatonGrammarParser.NUM)
            else:
                return self.getToken(AutomatonGrammarParser.NUM, i)

        def getRuleIndex(self):
            return AutomatonGrammarParser.RULE_alf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlf" ):
                listener.enterAlf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlf" ):
                listener.exitAlf(self)




    def alf(self):

        localctx = AutomatonGrammarParser.AlfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_alf)
        self._la = 0 # Token type
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==AutomatonGrammarParser.LETRA or _la==AutomatonGrammarParser.NUM:
                    self.state = 38
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [AutomatonGrammarParser.LETRA]:
                        self.state = 34
                        self.match(AutomatonGrammarParser.LETRA)
                        self.state = 35
                        self.match(AutomatonGrammarParser.T__7)
                        pass
                    elif token in [AutomatonGrammarParser.NUM]:
                        self.state = 36
                        self.match(AutomatonGrammarParser.NUM)
                        self.state = 37
                        self.match(AutomatonGrammarParser.T__7)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 42
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(AutomatonGrammarParser.LETRA)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.match(AutomatonGrammarParser.NUM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EstadosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def estado(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.EstadoContext,0)


        def getRuleIndex(self):
            return AutomatonGrammarParser.RULE_estados

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstados" ):
                listener.enterEstados(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstados" ):
                listener.exitEstados(self)




    def estados(self):

        localctx = AutomatonGrammarParser.EstadosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_estados)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(AutomatonGrammarParser.T__5)
            self.state = 48
            self.estado()
            self.state = 49
            self.match(AutomatonGrammarParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EstadoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EST(self, i:int=None):
            if i is None:
                return self.getTokens(AutomatonGrammarParser.EST)
            else:
                return self.getToken(AutomatonGrammarParser.EST, i)

        def getRuleIndex(self):
            return AutomatonGrammarParser.RULE_estado

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstado" ):
                listener.enterEstado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstado" ):
                listener.exitEstado(self)




    def estado(self):

        localctx = AutomatonGrammarParser.EstadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_estado)
        self._la = 0 # Token type
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 51
                    self.match(AutomatonGrammarParser.EST)
                    self.state = 52
                    self.match(AutomatonGrammarParser.T__7)
                    self.state = 55 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==AutomatonGrammarParser.EST):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.match(AutomatonGrammarParser.EST)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TransicoesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trans(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.TransContext,0)


        def getRuleIndex(self):
            return AutomatonGrammarParser.RULE_transicoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransicoes" ):
                listener.enterTransicoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransicoes" ):
                listener.exitTransicoes(self)




    def transicoes(self):

        localctx = AutomatonGrammarParser.TransicoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_transicoes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(AutomatonGrammarParser.T__8)
            self.state = 61
            self.trans()
            self.state = 62
            self.match(AutomatonGrammarParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TransContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EST(self, i:int=None):
            if i is None:
                return self.getTokens(AutomatonGrammarParser.EST)
            else:
                return self.getToken(AutomatonGrammarParser.EST, i)

        def LETRA(self):
            return self.getToken(AutomatonGrammarParser.LETRA, 0)

        def getRuleIndex(self):
            return AutomatonGrammarParser.RULE_trans

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrans" ):
                listener.enterTrans(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrans" ):
                listener.exitTrans(self)




    def trans(self):

        localctx = AutomatonGrammarParser.TransContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_trans)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(AutomatonGrammarParser.T__9)
                self.state = 65
                self.match(AutomatonGrammarParser.EST)
                self.state = 66
                self.match(AutomatonGrammarParser.T__7)
                self.state = 67
                self.match(AutomatonGrammarParser.LETRA)
                self.state = 68
                self.match(AutomatonGrammarParser.T__10)
                self.state = 69
                self.match(AutomatonGrammarParser.EST)
                self.state = 70
                self.match(AutomatonGrammarParser.T__7)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(AutomatonGrammarParser.T__9)
                self.state = 72
                self.match(AutomatonGrammarParser.EST)
                self.state = 73
                self.match(AutomatonGrammarParser.T__7)
                self.state = 74
                self.match(AutomatonGrammarParser.LETRA)
                self.state = 75
                self.match(AutomatonGrammarParser.T__10)
                self.state = 76
                self.match(AutomatonGrammarParser.EST)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InicioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EST(self):
            return self.getToken(AutomatonGrammarParser.EST, 0)

        def getRuleIndex(self):
            return AutomatonGrammarParser.RULE_inicio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicio" ):
                listener.enterInicio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicio" ):
                listener.exitInicio(self)




    def inicio(self):

        localctx = AutomatonGrammarParser.InicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_inicio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(AutomatonGrammarParser.EST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FinalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EST(self):
            return self.getToken(AutomatonGrammarParser.EST, 0)

        def getRuleIndex(self):
            return AutomatonGrammarParser.RULE_final

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinal" ):
                listener.enterFinal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinal" ):
                listener.exitFinal(self)




    def final(self):

        localctx = AutomatonGrammarParser.FinalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_final)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(AutomatonGrammarParser.T__8)
            self.state = 82
            self.match(AutomatonGrammarParser.EST)
            self.state = 83
            self.match(AutomatonGrammarParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





