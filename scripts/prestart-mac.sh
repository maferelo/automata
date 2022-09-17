#!/bin/bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install --cask docker visual-studio-code

code --install-extension ms-vscode-remote.remote-containers

code .
