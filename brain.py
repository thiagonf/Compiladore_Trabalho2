import sys
import os


def parse(string):
    cprog = """
#include<stdio.h>

int main(){
    static char a[30000], *ptr;
    ptr=a;
"""

    # to initialize the brainf*** environment
    parsedic = {">": "  ++ptr; \n",
                "<": "  --ptr; \n",
                "+": "  ++(*ptr); \n",
                "-": "  --(*ptr); \n",
                ".": """    printf("%c",(*ptr)); \n""",
                ",": """    scanf("%c",ptr); \n""",
                "[": """  while(*ptr) { \n""",
                "]": " \n}\n"}

    for i in string:
        if i in parsedic:
            cprog = cprog + parsedic[i]
    cprog = cprog + " return 0; \n} "
    return cprog


# To compile the program and run it
def compileandrun(code):
    a = open("out.c", 'w+')
    a.write(code)
    a.close()
    print ("compiling to c ... ")
    os.system("gcc out.c -o bf")
    print ("Output is as follows")
    os.system("./bf")


# main program
if __name__ == "__main__":
    # string=''.join(sys.argv[1:])
    string = """
    salva 2 e 3 na primeira e segunda posicoes; respectivamente
++ > +++ <

realiza a soma e salva na segunda posicao
[->+<]

desloca para o lado e incrementa 48 vezes (corresponde ao 0 em ascii)
> ++++++++++++++++++++++++++++++++++++++++++++++++

imprime o resultado
."""
    op = parse(string)
    print (op)
    compileandrun(op)
