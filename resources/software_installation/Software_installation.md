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

## Nix installation

As per 2025-01-23 the latest release of Nixpkgs/NixOS is 24.11.

### Without Flakes

Put the following code into a file called `shell.nix`. Then afterwards run `nix-shell` in the same directory and you get shell where the tools are available to you.

```nix
{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/refs/heads/nixos-24.11.zip") {} }:

pkgs.mkShell {
  packages = [
    pkgs.entr
    pkgs.gcc14
    pkgs.gnumake
    pkgs.jdk23
  ];
}
```

### With Flakes

Create a directory and run `git init` in it. Then create a file called `flake.nix` with the following content in that directory.

```nix
{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-24.11";
  };
  outputs =
    { ... }@inputs:
    let
      system = "x86_64-linux"; # change this if you are on a different architecture
      pkgs = inputs.nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [
          pkgs.entr
          pkgs.gcc14
          pkgs.gnumake
          pkgs.jdk23
        ];
      };
    };
}
```

## Tooling

### Emacs

- Tree-sitter support for Lox
  - https://github.com/nverno/lox-ts-mode
- Major Mode for Lox
  - https://github.com/timmyjose-projects/lox-mode
- Both are in Nixpkgs
  - https://search.nixos.org/packages?channel=unstable&from=0&size=50&sort=relevance&type=packages&query=emacsPackages.lox
