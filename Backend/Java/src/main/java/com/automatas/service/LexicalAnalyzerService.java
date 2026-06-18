package com.automatas.service;

import java.io.StringReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import com.automatas.lexer.Lexer;
import com.automatas.model.LexicalError;
import com.automatas.model.ParseRequest;
import com.automatas.model.ParseResponse;
import com.automatas.model.TokenDTO;
import com.automatas.parser.Parser;
import com.automatas.parser.sym;

import java_cup.runtime.Symbol;

public class LexicalAnalyzerService {

    private static final Map<Integer, String> TOKEN_NAMES = Map.of(
        sym.IDENTIFIER, "IDENTIFIER",
        sym.NUMBER, "NUMBER",
        sym.PLUS, "PLUS",
        sym.MINUS, "MINUS",
        sym.TIMES, "TIMES",
        sym.DIVIDE, "DIVIDE",
        sym.EQUALS, "EQUALS",
        sym.LPAREN, "LPAREN",
        sym.RPAREN, "RPAREN",
        sym.EOF, "EOF"
    );

    public ParseResponse analyze(ParseRequest request) {
        return analyze(request.getInput());
    }

    public ParseResponse analyze(String input) {
        List<TokenDTO> tokens = new ArrayList<>();
        List<LexicalError> errors = new ArrayList<>();
        Object parsedResult = null;

        try {
            Lexer lexer = new Lexer(new StringReader(input));
            Symbol token;
            while ((token = lexer.next_token()) != null && token.sym != sym.EOF) {
                String type = TOKEN_NAMES.getOrDefault(token.sym, "UNKNOWN");
                String lexeme = token.value != null ? token.value.toString() : "";
                tokens.add(new TokenDTO(type, lexeme, token.left, token.right));
            }
        } catch (Exception e) {
            errors.add(new LexicalError("Lexical error: " + e.getMessage(), 0, 0));
        }

        try {
            Lexer parserLexer = new Lexer(new StringReader(input));
            TokenInjector injector = new TokenInjector(parserLexer);
            Parser parser = new Parser(injector);
            Symbol resultSymbol = parser.parse();
            parsedResult = resultSymbol.value;
        } catch (Exception e) {
            errors.add(new LexicalError("Syntax error: " + e.getMessage(), 0, 0));
        }

        boolean success = errors.isEmpty();
        String message = success
            ? "Analysis completed successfully. " + tokens.size() + " tokens found."
            : errors.get(0).getMessage();

        ParseResponse response = new ParseResponse(success, message, tokens, parsedResult);
        return response;
    }

    public List<TokenDTO> getTokens(String input) {
        List<TokenDTO> tokens = new ArrayList<>();
        try {
            Lexer lexer = new Lexer(new StringReader(input));
            Symbol token;
            while ((token = lexer.next_token()) != null && token.sym != sym.EOF) {
                String type = TOKEN_NAMES.getOrDefault(token.sym, "UNKNOWN");
                String lexeme = token.value != null ? token.value.toString() : "";
                tokens.add(new TokenDTO(type, lexeme, token.left, token.right));
            }
        } catch (Exception e) {
            throw new RuntimeException("Lexical analysis failed: " + e.getMessage(), e);
        }
        return tokens;
    }
}
