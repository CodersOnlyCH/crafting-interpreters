package org.codersonly.lox.scanner;

import com.google.common.collect.Lists;

import java.util.List;

public class Scanner {
    private final String source;

    public Scanner(String source) {
        this.source = source;
    }

    public List<Token> scanTokens() {
        return Lists.newArrayList(Token.SEMICOLON, Token.EOF);
    }
}
