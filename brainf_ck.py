import click

dictionary = {
    '+': '\ttape[index]++;\n',
    '-': '\ttape[index]--;\n',
    '>': '\t++index;\n',
    '<': '\t--index;\n',
    '.': '\tprintf("%c", tape[index]);\n',
    ',': '\ttape[index] = getchar();\ngetchar();\n',
    '[': '\twhile(tape[index]) {\n',
    ']': '\t}\n'
}


@click.command()
@click.argument('source', type=click.File('r'))
@click.option('-o', nargs=1, type=click.File('w'))
def parser(source, o):
    program = ("#include <stdio.h>\n"
               "#include <stdlib.h>\n"
               "int main(){"
               "\n\t char tape [5000];\n"
               "\n\tint index = 0;;\n"
               )
    data = source.read()
    for char in data:
        if char in dictionary:
            program += dictionary[char]

    program += '\n    return 0;\n}'

    write_program(o, program)


def write_program(file_out, program_c):
    file_out.write(program_c)
    file_out.flush()


# Call parser brainfuck to C
parser()
