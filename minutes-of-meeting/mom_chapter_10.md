🎉
Aaron
Comma!
Aaron
Yep!
Aaron
a = b, c, d; assert(a == d);
Nivath
😮
Aaron
The solution for comma, BTW, is to use assignment() for the function arguments instead of expression().
Samir Talwar
fun one() {
  print 1
  return 1
}

fun two() {
  print 2
  return 2
}

fun plus(a, b) {
  return a + b
}

plus(one(), two())
Aaron
I would prefer if he'd used two functions for these two cases, rather than relying on the programmer to notice whether there was or was not a throw...
Aaron
1 to: 20 do: [:each | [block value: each)] fork]
Aaron
CLOS :-)
Samir Talwar
From Chapter 12:
> 

Multimethods are the approach you’re least likely to be familiar with. I’d love to talk more about them—I designed a hobby language around them once and they are super rad—but there are only so many pages I can fit in. If you’d like to learn more, take a look at CLOS (the object system in Common Lisp), Dylan, Julia, or Raku.
Andreas
Julia does it really  good!
Basil
I now need to read it, there is a proposal from 2007 for multi-method in C++:
https://www.stroustrup.com/multimethods.pdf
