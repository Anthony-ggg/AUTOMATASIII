package com.automatas.controller;

import com.automatas.model.ParseRequest;
import com.automatas.model.ParseResponse;
import com.automatas.model.TokenDTO;
import com.automatas.service.LexicalAnalyzerService;

import java.util.List;

public class AnalyzerController {

    private final LexicalAnalyzerService lexicalAnalyzerService;

    public AnalyzerController() {
        this.lexicalAnalyzerService = new LexicalAnalyzerService();
    }

    public AnalyzerController(LexicalAnalyzerService lexicalAnalyzerService) {
        this.lexicalAnalyzerService = lexicalAnalyzerService;
    }

    public ParseResponse analyze(ParseRequest request) {
        return lexicalAnalyzerService.analyze(request);
    }

    public ParseResponse analyze(String input) {
        return lexicalAnalyzerService.analyze(input);
    }

    public List<TokenDTO> getTokens(String input) {
        return lexicalAnalyzerService.getTokens(input);
    }
}
