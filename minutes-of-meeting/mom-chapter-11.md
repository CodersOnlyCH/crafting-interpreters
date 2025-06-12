fun print_foo() {
  print "foo";
}

{
  fun foo() {
    print_foo();
  }

  // we get what we expect, namely "foo"
  foo();

  fun print_foo() {
    print "bar";
  }

  // here, we still expect "foo", as we fixed this with the static
  // name resolving. Suprisingly however we get "bar"
  foo();
}
⁨Christian⁩’s
screensharehas stopped
⁨Amdrew⁩ started
screenshare
⁨Amdrew⁩’s
screensharehas stopped
Christian
are we going to look at the challenges?
Nivath
🎉
Nivath
👍