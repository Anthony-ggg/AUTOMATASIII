package com.automatas;

import java.util.List;

import com.automatas.controller.AnalyzerController;
import com.automatas.model.ParseResponse;
import com.automatas.model.TokenDTO;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class Main {

    private static final Gson gson = new GsonBuilder().setPrettyPrinting().create();

    public static void main(String[] args) {
        AnalyzerController controller = new AnalyzerController();

        if (args.length > 0) {
            String input = String.join(" ", args);
            processInput(controller, input);
            return;
        }

        String defaultInput = "x + y = 30\nx - y = 6\n2x = 36\nx = 18";

        System.out.println("=== Lexical Analyzer with JFlex + CUP ===");
        System.out.println("Analyzing equations from the problem:\n");
        System.out.println(defaultInput);
        System.out.println("\n--- Token Analysis ---\n");

        List<TokenDTO> tokens = controller.getTokens(defaultInput);
        printTokens(tokens);

        System.out.println("\n--- Syntax Analysis ---\n");
        ParseResponse response = controller.analyze(defaultInput);
        System.out.println("Success: " + response.isSuccess());
        System.out.println("Message: " + response.getMessage());
        System.out.println("\nParsed Result (JSON):");
        System.out.println(gson.toJson(response.getParsedResult()));
    }

    private static void processInput(AnalyzerController controller, String input) {
        System.out.println(gson.toJson(controller.analyze(input)));
    }

    private static void printTokens(List<TokenDTO> tokens) {
        System.out.printf("%-15s %-15s %-8s %-8s%n", "TYPE", "LEXEME", "LINE", "COLUMN");
        System.out.println("--------------------------------------------------");
        for (TokenDTO token : tokens) {
            System.out.printf("%-15s %-15s %-8d %-8d%n",
                token.getType(), token.getLexeme(), token.getLine(), token.getColumn());
        }
    }
}
