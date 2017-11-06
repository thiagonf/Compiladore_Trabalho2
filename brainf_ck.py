import click


@click.command()
@click.argument('code_file', type=click.File('r'))
@click.option('-o', nargs=1, type=click.File('w'))
def parser(code_file, o):
    progam_c = """
#include<stdio.h>
#include <stdlib.h>

int main(){
       char *tape = malloc(sizeof(char)*20000);
       char *ptr =  &tape[0];
"""
    parsedic = {">": "  ++ptr; \n",
                "<": "  --ptr; \n",
                "+": "  ++(*ptr); \n",
                "-": "  --(*ptr); \n",
                ".": """    printf("%c \\n",(*ptr)); \n""",
                ",": """    scanf("%c",ptr); \n""",
                "[": """  while(*ptr) { \n""",
                "]": " \n}\n"}

    source_code = code_file.read()
    for data in source_code:
        if data in parsedic:
            progam_c = progam_c + parsedic[data]
    progam_c = progam_c + " return 0; \n} "

    write_program(o, progam_c)


def write_program(file_out, program_c):
    file_out.write(program_c)
    file_out.flush()


if __name__ == "__main__":
    op = parser()
