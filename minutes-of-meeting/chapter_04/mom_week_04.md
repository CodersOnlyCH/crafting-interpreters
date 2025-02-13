Paul: used maven
Richard: used var/ used Java9 with modularity - free programs jlink and jpackage 250MB
Andreas: added error messages.
Paul: balance between string manipulation and trying to write the parser

Code block: nesting is hairy

gradle install
gradle init
gradle - choose library or application?

defaults from gradle init are good
Junit 4 is good enough

Chat:

Paul
Hi everyone!
Patrick
java pattern matching: https://dev.java/learn/pattern-matching/
Andreas Peter
```line 2] Error: 
"var y = 3; */"
            ^^
            Unexpected start of block comment
line 6] Error: 
"var k = z * /* this is a /* nested */ \nmultiline block comment  x;"
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
             Unterminated block comment
```
Andreas Peter
alignement doesn't work here though :(
Patrick
works well in Discord ;)
Paul
My editor of choice is vs code; is Intellj a little bloated and resource intensive?
Silvio Heuberger
it's very hard
Silvio Heuberger
My editor of choice is vs code; is Intellj a little bloated and resource intensive?
it is, but it's also really a lot more powerful than most 'simple' text editors, it's all trade-offs
Patrick
i take a good IDE any day over a simple editor
Silvio Heuberger
compare the following:

foo(
  bar,
  zap
)
Patrick
🎉
Silvio Heuberger
vs. lambda a: 
  a
  +
  20
Patrick
👋
⁨Silvio Heuberger⁩ started
screenshare
Richard
👍
⁨Silvio Heuberger⁩’s
screensharehas stopped
Chat
