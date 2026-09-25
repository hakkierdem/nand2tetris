// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

(RESET)
@SCREEN
D=A

@address
M=D

(LOOP)

@KBD
D=A

@address
D=D-M

@RESET
D;JEQ

@KBD
D=M

@WHITE
D;JEQ

@BLACK
0;JMP

(WHITE)

@address
A=M
M=0

@address
M=M+1

@LOOP
0;JMP

(BLACK)

@address
A=M
M=-1

@address
M=M+1

@LOOP
0;JMP