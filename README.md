# BetterPacmanLook
An improved version of the common `pacman -S`.
## Installation
I know that this is probably one of the worst solutions and i will be working on a better one.
### But for now
1. Clone the repo
2. Paste this into your `.zshrc` or `.bashrc` but *change the path*
```
pmlook() {
    if [ $# -ne 1 ];
    then
        pacman -Ss "$1" | python ~/path/of/main.py "$2"
    else	
        pacman -Ss "$1" | python ~/path/of/main.py
    fi
}
```
## Testing
```
cd BetterPacmanLook
cat test.txt | python main.py
```
The result should be something like this:
![Example.png]