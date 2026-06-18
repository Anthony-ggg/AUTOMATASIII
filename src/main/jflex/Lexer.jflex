package com.automatas.lexer;

import java_cup.runtime.*;
import com.automatas.parser.sym;

%%

%public
%class Lexer
%cup
%line
%column
%unicode

%{
    private Symbol symbol(int type) {
        return new Symbol(type, yyline + 1, yycolumn + 1);
    }

    private Symbol symbol(int type, Object value) {
        return new Symbol(type, yyline + 1, yycolumn + 1, value);
    }
%}

LineTerminator = \r|\n|\r\n
WhiteSpace = {LineTerminator} | [ \t\f]
Identifier = [a-zA-Z_][a-zA-Z0-9_]*
Number = [0-9]+

%%

<YYINITIAL> {
    "+"            { return symbol(sym.PLUS); }
    "-"            { return symbol(sym.MINUS); }
    "="            { return symbol(sym.EQUALS); }
    "*"            { return symbol(sym.TIMES); }
    "/"            { return symbol(sym.DIVIDE); }
    "("            { return symbol(sym.LPAREN); }
    ")"            { return symbol(sym.RPAREN); }
    {Identifier}   { return symbol(sym.IDENTIFIER, yytext()); }
    {Number}       { return symbol(sym.NUMBER, Integer.parseInt(yytext())); }
    {WhiteSpace}   { }
}

[^]              { throw new Error("Illegal character <" + yytext() + "> at line " + (yyline + 1) + ", column " + (yycolumn + 1)); }
