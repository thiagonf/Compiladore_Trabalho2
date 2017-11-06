#include <stdio.h>
#include <stdlib.h>
int main(){
	 char tape [5000];

	int index = 0;
	tape[index]++;
	tape[index]++;
	++index;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	--index;
	while(tape[index]) {
	tape[index]--;
	++index;
	tape[index]++;
	--index;
	}
	++index;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	tape[index]++;
	printf("%c\n", tape[index]);

    return 0;
}