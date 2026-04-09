https://clang.llvm.org/docs/AddressSanitizer.html
⁨Aaron⁩ started
screenshare
Quint
Is everyone using C? Or did some people deviate and use other languages?
⁨Aaron⁩’s
screensharehas stopped
Yigal
Is everyone using C? Or did some people deviate and use other languages?
Samir did some Rust stuff. I did some Go stuff. But I think we both stopped doing that because it became too complicated for reasons
Aaron
I did a partial Lua implementation in parallel with the Java version.
Samir
I did do the Haskell version too but I didn't bother with classes, because there was too much mutation and it seemed horrifying. I think Raphael did it though.
Raphael
Is everyone using C? Or did some people deviate and use other languages?
https://github.com/raphaelmeyer/crafting-interpreters/
Yigal
ooooooh, Ada 😍
Quint
Wow, a lot of different languages!
Quint
I'll probably try to go through the book on my own in Zig.
Yigal
Yes, Zig sounds very applicable for the second part
Aaron
struct Obj {
  bool isMarked :  1;
  ObjType type : 3;
  struct Obj* next;
};
- 	strb	wzr, [x1, #16]
+ 	and	w8, w8, #0xfe
+ 	strb	w8, [x1]
Richard
https://www.baeldung.com/jvm-garbage-collectors
Aaron
Contrast this with Go's "escape analysis" that will decide at compile time what can be allocated on the stack.
Samir
https://github.com/munificent/lisp2-gc