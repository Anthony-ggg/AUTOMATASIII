package com.automatas.model;

public class LexicalError {
    private String message;
    private int line;
    private int column;

    public LexicalError() {}

    public LexicalError(String message, int line, int column) {
        this.message = message;
        this.line = line;
        this.column = column;
    }

    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }

    public int getLine() { return line; }
    public void setLine(int line) { this.line = line; }

    public int getColumn() { return column; }
    public void setColumn(int column) { this.column = column; }
}
