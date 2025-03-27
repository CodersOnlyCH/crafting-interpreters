@Samir Talwar Do you have a working dev container for Haskell?
Samir Talwar
I use Nix so no, sorry.
Samir Talwar

Primitive.java, in case anyone's interested:
https://codeberg.org/ooble/crafting-interpreters/src/branch/main/java/src/main/java/com/craftinginterpreters/lox/Primitive.java
Paul

Primitive.java, in case anyone's interested:
https://codeberg.org/ooble/crafting-interpreters/src/branch/main/java/src/main/java/com/craftinginterpreters/lox/Primitive.java

Nice
Paul

@Samir Talwar Have you a resource I could read to get started for Nix and Haskell?
Samir Talwar

Shells in Nix:
https://functional.computer/blog/throwaway-development-environments-with-nix

Building programs with Nix:
https://nixos.wiki/wiki/Haskell

⁨Amdrew⁩ started
screenshare
Dominik
👍
⁨Amdrew⁩’s
screensharehas stopped
Corinna (She/Her)
👍
Basil
Alternatively, you can make everything a string and end up in CMake
Patrick
:D

Samir Talwar
😂
Paul
Alternatively, you can make everything a string and end up in CMake
😂
Samir Talwar

Bash:
```
$ if [[ 11 < 9 ]]; then echo true; else echo false; fi
true
$ if [[ 11 -lt 9 ]]; then echo true; else echo false; fi
false
```

Samir Talwar
https://en.wikipedia.org/wiki/IEEE_754#Design_rationale

Dumitru
0.1 + 0.2 = 0.30000000000000004

Samir Talwar
A friend of mine did his PhD on how exactly to define a "real" number, and what it means to have an "exact" one: https://etheses.bham.ac.uk//id/eprint/10411/

Spoiler: it's really complicated.

Andreas
👏

Christian
https://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science)#Covariant_arrays_in_Java_and_C.23

Chat
