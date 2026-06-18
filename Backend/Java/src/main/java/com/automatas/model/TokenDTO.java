package com.automatas.model;

public class TokenDTO {
    private String type;
    private String lexeme;
    private int line;
    private int column;

    public TokenDTO() {}

    public TokenDTO(String type, String lexeme, int line, int column) {
        this.type = type;
        this.lexeme = lexeme;
        this.line = line;
        this.column = column;
    }

    public String getType() { return type; }
    public void setType(String type) { this.type = type; }

    public String getLexeme() { return lexeme; }
    public void setLexeme(String lexeme) { this.lexeme = lexeme; }

    public int getLine() { return line; }
    public void setLine(int line) { this.line = line; }

    public int getColumn() { return column; }
    public void setColumn(int column) { this.column = column; }
}
