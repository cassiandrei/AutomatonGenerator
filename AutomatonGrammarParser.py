# Generated from AutomatonGrammar.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\65\n\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5")
        buf.write("\bD\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13]\n\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\2\2\16")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\2\2\2^\2\32\3\2\2\2\4&")
        buf.write("\3\2\2\2\6\64\3\2\2\2\b\66\3\2\2\2\n8\3\2\2\2\f:\3\2\2")
        buf.write("\2\16C\3\2\2\2\20E\3\2\2\2\22H\3\2\2\2\24\\\3\2\2\2\26")
        buf.write("^\3\2\2\2\30a\3\2\2\2\32\33\7\3\2\2\33\34\5\4\3\2\34\35")
        buf.write("\7\4\2\2\35\36\5\f\7\2\36\37\7\5\2\2\37 \5\22\n\2 !\7")
        buf.write("\6\2\2!\"\5\26\f\2\"#\7\7\2\2#$\5\30\r\2$%\7\2\2\3%\3")
        buf.write("\3\2\2\2&\'\7\b\2\2\'(\5\6\4\2()\7\t\2\2)\5\3\2\2\2*+")
        buf.write("\5\b\5\2+,\7\n\2\2,-\5\6\4\2-\65\3\2\2\2./\5\n\6\2/\60")
        buf.write("\7\n\2\2\60\61\5\6\4\2\61\65\3\2\2\2\62\65\5\b\5\2\63")
        buf.write("\65\5\n\6\2\64*\3\2\2\2\64.\3\2\2\2\64\62\3\2\2\2\64\63")
        buf.write("\3\2\2\2\65\7\3\2\2\2\66\67\7\17\2\2\67\t\3\2\2\289\7")
        buf.write("\20\2\29\13\3\2\2\2:;\7\b\2\2;<\5\16\b\2<=\7\t\2\2=\r")
        buf.write("\3\2\2\2>?\5\20\t\2?@\7\n\2\2@A\5\16\b\2AD\3\2\2\2BD\5")
        buf.write("\20\t\2C>\3\2\2\2CB\3\2\2\2D\17\3\2\2\2EF\7\13\2\2FG\5")
        buf.write("\n\6\2G\21\3\2\2\2HI\7\b\2\2IJ\5\24\13\2JK\7\t\2\2K\23")
        buf.write("\3\2\2\2LM\7\f\2\2MN\5\20\t\2NO\7\n\2\2OP\5\b\5\2PQ\7")
        buf.write("\r\2\2QR\5\20\t\2RS\7\n\2\2ST\5\24\13\2T]\3\2\2\2UV\7")
        buf.write("\f\2\2VW\5\20\t\2WX\7\n\2\2XY\5\b\5\2YZ\7\r\2\2Z[\5\20")
        buf.write("\t\2[]\3\2\2\2\\L\3\2\2\2\\U\3\2\2\2]\25\3\2\2\2^_\7\16")
        buf.write("\2\2_`\5\20\t\2`\27\3\2\2\2ab\7\b\2\2bc\5\20\t\2cd\7\t")
        buf.write("\2\2d\31\3\2\2\2\5\64C\\")
        return buf.getvalue()


class AutomatonGrammarParser ( Parser ):

    grammarFileName = "AutomatonGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'A'", "'Q'", "'T'", "'I'", "'F'", "'={'", 
                     "'}'", "','", "'q'", "'('", "')='", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TOKENALF", "TOKENNUM", "WS" ]

    RULE_s = 0
    RULE_alfabeto = 1
    RULE_alf = 2
    RULE_letra = 3
    RULE_num = 4
    RULE_estados = 5
    RULE_estado = 6
    RULE_est = 7
    RULE_transicoes = 8
    RULE_trans = 9
    RULE_inicio = 10
    RULE_final = 11

    ruleNames =  [ "s", "alfabeto", "alf", "letra", "num", "estados", "estado", 
                   "est", "transicoes", "trans", "inicio", "final" ]

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
    T__11=12
    TOKENALF=13
    TOKENNUM=14
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


        def EOF(self):
            return self.getToken(AutomatonGrammarParser.EOF, 0)

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
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(AutomatonGrammarParser.T__0)
            self.state = 25
            self.alfabeto()
            self.state = 26
            self.match(AutomatonGrammarParser.T__1)
            self.state = 27
            self.estados()
            self.state = 28
            self.match(AutomatonGrammarParser.T__2)
            self.state = 29
            self.transicoes()
            self.state = 30
            self.match(AutomatonGrammarParser.T__3)
            self.state = 31
            self.inicio()
            self.state = 32
            self.match(AutomatonGrammarParser.T__4)
            self.state = 33
            self.final()
            self.state = 34
            self.match(AutomatonGrammarParser.EOF)
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
            self.state = 36
            self.match(AutomatonGrammarParser.T__5)
            self.state = 37
            self.alf()
            self.state = 38
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

        def letra(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.LetraContext,0)


        def alf(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.AlfContext,0)


        def num(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.NumContext,0)


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
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.letra()
                self.state = 41
                self.match(AutomatonGrammarParser.T__7)
                self.state = 42
                self.alf()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.num()
                self.state = 45
                self.match(AutomatonGrammarParser.T__7)
                self.state = 46
                self.alf()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.letra()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.num()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LetraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOKENALF(self):
            return self.getToken(AutomatonGrammarParser.TOKENALF, 0)

        def getRuleIndex(self):
            return AutomatonGrammarParser.RULE_letra

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetra" ):
                listener.enterLetra(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetra" ):
                listener.exitLetra(self)




    def letra(self):

        localctx = AutomatonGrammarParser.LetraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_letra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(AutomatonGrammarParser.TOKENALF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOKENNUM(self):
            return self.getToken(AutomatonGrammarParser.TOKENNUM, 0)

        def getRuleIndex(self):
            return AutomatonGrammarParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)




    def num(self):

        localctx = AutomatonGrammarParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(AutomatonGrammarParser.TOKENNUM)
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
        self.enterRule(localctx, 10, self.RULE_estados)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(AutomatonGrammarParser.T__5)
            self.state = 57
            self.estado()
            self.state = 58
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

        def est(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.EstContext,0)


        def estado(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.EstadoContext,0)


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
        self.enterRule(localctx, 12, self.RULE_estado)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.est()
                self.state = 61
                self.match(AutomatonGrammarParser.T__7)
                self.state = 62
                self.estado()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.est()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.NumContext,0)


        def getRuleIndex(self):
            return AutomatonGrammarParser.RULE_est

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEst" ):
                listener.enterEst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEst" ):
                listener.exitEst(self)




    def est(self):

        localctx = AutomatonGrammarParser.EstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_est)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(AutomatonGrammarParser.T__8)
            self.state = 68
            self.num()
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
        self.enterRule(localctx, 16, self.RULE_transicoes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(AutomatonGrammarParser.T__5)
            self.state = 71
            self.trans()
            self.state = 72
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

        def est(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutomatonGrammarParser.EstContext)
            else:
                return self.getTypedRuleContext(AutomatonGrammarParser.EstContext,i)


        def letra(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.LetraContext,0)


        def trans(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.TransContext,0)


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
        self.enterRule(localctx, 18, self.RULE_trans)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(AutomatonGrammarParser.T__9)
                self.state = 75
                self.est()
                self.state = 76
                self.match(AutomatonGrammarParser.T__7)
                self.state = 77
                self.letra()
                self.state = 78
                self.match(AutomatonGrammarParser.T__10)
                self.state = 79
                self.est()
                self.state = 80
                self.match(AutomatonGrammarParser.T__7)
                self.state = 81
                self.trans()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.match(AutomatonGrammarParser.T__9)
                self.state = 84
                self.est()
                self.state = 85
                self.match(AutomatonGrammarParser.T__7)
                self.state = 86
                self.letra()
                self.state = 87
                self.match(AutomatonGrammarParser.T__10)
                self.state = 88
                self.est()
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

        def est(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.EstContext,0)


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
        self.enterRule(localctx, 20, self.RULE_inicio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(AutomatonGrammarParser.T__11)
            self.state = 93
            self.est()
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

        def est(self):
            return self.getTypedRuleContext(AutomatonGrammarParser.EstContext,0)


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
        self.enterRule(localctx, 22, self.RULE_final)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(AutomatonGrammarParser.T__5)
            self.state = 96
            self.est()
            self.state = 97
            self.match(AutomatonGrammarParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





