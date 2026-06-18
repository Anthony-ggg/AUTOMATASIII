package com.automatas.model;

import java.util.List;

public class ParseResponse {
    private boolean success;
    private String message;
    private List<TokenDTO> tokens;
    private Object parsedResult;

    public ParseResponse() {}

    public ParseResponse(boolean success, String message, List<TokenDTO> tokens, Object parsedResult) {
        this.success = success;
        this.message = message;
        this.tokens = tokens;
        this.parsedResult = parsedResult;
    }

    public boolean isSuccess() { return success; }
    public void setSuccess(boolean success) { this.success = success; }

    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }

    public List<TokenDTO> getTokens() { return tokens; }
    public void setTokens(List<TokenDTO> tokens) { this.tokens = tokens; }

    public Object getParsedResult() { return parsedResult; }
    public void setParsedResult(Object parsedResult) { this.parsedResult = parsedResult; }
}
