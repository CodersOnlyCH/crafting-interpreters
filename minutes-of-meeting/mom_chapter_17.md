Amdrew⁩ started
screenshare
Yigal
👍
⁨Amdrew⁩’s
screensharehas stopped
Christian
How do you read the function ppointer type def?
Amdrew
typedef void (*ParseFn)();
Nivath
👏
Aaron
https://journal.stuffwithstuff.com/2011/03/19/pratt-parsers-expression-parsing-made-easy/
Aaron
+ static void ternary() {
+   TokenType operatorType = parser.previous.type;  
+   ParseRule* rule = getRule(operatorType);
+   parsePrecedence((Precedence)(rule->precedence + 1));
+   consume(TOKEN_COLON, "Expect ':' in ternary expression.");
+   parsePrecedence((Precedence)(rule->precedence + 1));  
+ }
Christian Egli
https://www.cs.tufts.edu/~nr/cs257/archive/ralf-hinze/CAM-basics.pdf
Nivath
@Samir Talwar More night time reading matrerial https://www.oreilly.com/library/view/dancing-with-qubits/9781838827366/