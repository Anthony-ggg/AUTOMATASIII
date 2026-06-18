package com.automatas.model;

public class ParseRequest {
    private String input;

    public ParseRequest() {}

    public ParseRequest(String input) {
        this.input = input;
    }

    public String getInput() { return input; }
    public void setInput(String input) { this.input = input; }
}
