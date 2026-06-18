package com.automatas.service;

import java.util.LinkedList;
import java.util.Queue;

import com.automatas.lexer.Lexer;
import com.automatas.parser.sym;

import java_cup.runtime.Scanner;
import java_cup.runtime.Symbol;

public class TokenInjector implements Scanner {

    private final Lexer lexer;
    private Symbol lastRealToken;
    private final Queue<Symbol> buffer = new LinkedList<>();

    public TokenInjector(Lexer lexer) {
        this.lexer = lexer;
    }

    @Override
    public Symbol next_token() throws Exception {
        if (!buffer.isEmpty()) {
            Symbol buffered = buffer.poll();
            if (buffered.sym != sym.EOF) {
                lastRealToken = buffered;
            }
            return buffered;
        }

        Symbol token = lexer.next_token();
        if (token == null || token.sym == sym.EOF) {
            lastRealToken = token;
            return token;
        }

        if (lastRealToken != null && lastRealToken.left == token.left) {
            boolean thisIsIdentifierOrLParen = token.sym == sym.IDENTIFIER || token.sym == sym.LPAREN;
            boolean thisIsNumber = token.sym == sym.NUMBER;
            boolean lastWasNumberOrRParen = lastRealToken.sym == sym.NUMBER || lastRealToken.sym == sym.RPAREN;
            boolean lastWasIdentifier = lastRealToken.sym == sym.IDENTIFIER;

            if ((lastWasNumberOrRParen && thisIsIdentifierOrLParen) ||
                (lastWasIdentifier && (thisIsIdentifierOrLParen || thisIsNumber))) {
                buffer.add(token);
                Symbol injected = new Symbol(sym.TIMES, lastRealToken.left, lastRealToken.right, null);
                return injected;
            }
        }

        lastRealToken = token;
        return token;
    }
}
