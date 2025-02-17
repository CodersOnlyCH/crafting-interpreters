package org.codersonly.lox.scanner;

import com.google.common.io.Resources;
import org.junit.Test;

import java.io.IOException;
import java.nio.charset.Charset;
import java.util.List;

import static org.codersonly.lox.scanner.Token.*;
import static org.junit.Assert.*;

public class ScannerTest {
   @Test
    public void testThatItScansOneSemicolon() {
        assertScansAs(";", List.of(SEMICOLON, EOF));
   }

   @Test
   public void testThatItScansBrackets() {
       assertScansAs("();", List.of(LEFT_PAREN, RIGHT_PAREN, SEMICOLON, EOF));
   }

   @Test
   public void testThatWeCanReadASampleFile() throws IOException {
       // this is how to load a file from the test resources
       var url = Resources.getResource("string-assignment.lox");
       var content = Resources.toString(url, Charset.defaultCharset());

       assertFalse("Expected file content not to be empty", content.isEmpty());
   }

   private void assertScansAs(String source, List<Token> expectedTokens) {
       Scanner scanner = new Scanner(source);
       var result = scanner.scanTokens();
       assertEquals(expectedTokens, result);
   }
}
