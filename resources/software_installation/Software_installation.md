# Software installation

We have agreed as a group on the following versions:

- Java JDK 23
- C23

## macos installation

### java

```bash
brew install openjdk@23
```

> Note all the small print at the end of the install, you will need to do some symlinks, some PATH manipulations and some environment variable setups afterwards

```bash
sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc
export CPPFLAGS="-I/opt/homebrew/opt/openjdk/include"
```

### dart 2.19 (for makeing of Robert's clox/jlox)

```bash
brew tap dart-lang/dart
brew install dart-lang/dart/dart@2.19
export PATH=$(brew --prefix dart-lang/dart/dart@2.19)/bin:$PATH
dart --version
Dart SDK version: 2.19.6 (stable) (Tue Mar 28 13:41:04 2023 +0000) on "macos_arm64"
make clean
make get
```