# Template for building the scanner (and parser) using java and gradle

## How do I run this?

`./gradlew build` will compile everything and run all the tests. There is one failing test, so you know where to start. :)

`./gradlew scanner:run` will run the scanner main class without any arguments

`./gradlew parser:run` will run the parser main class without any arguments

## What about running the tests every time I change a file?

You can do that using 

`./gradlew --continuous test`

## Can I do the same thing in my IDE

Yes, both big IDEs support continuous run of tests. In intellij you can find it in the panel that pops up when you first 
run the tests. It looks like a feedback loop with a 'play button' inside of it.
In eclipse there should be a plugin called 'infinitest' that does the same thing.

