# BetterPacmanLook
An improved version of the common `pacman -S`.
## Installation
I know that this is probably one of the worst solutions and i will be working on a better one.
### But for now
1. Clone the repo
2. Paste this into your `.zshrc` or `.bashrc` but ==change the path==
    ```pmlook() {
        echo pmlook pipes pm -Ss into ~/desktop/Python/Better \pmlook/main.py
        if [ $# -ne 1 ];
        then
            echo lol
            pacman -Ss "$1" | python ~/path/of/main.py "$2"
        else	
            pacman -Ss "$1" | python ~/path/of/main.py
        fi
    }```
