#include<stdlib.h>
#include<stdio.h>

void check_msb(int num)
{
	int j = num>>31;
	if(j^num == 0)
		printf("this number is  set\n");
	else
		printf("this number is not set\n");
}

void print_bits(unsigned char byte)
{
	for(int i=0; i<8;i++)
	{
		if(byte & (1<<7))
			printf("1");
		else
			printf("0"); 
		byte = byte <<1;
	}		
}

int main()
{
	int i=2;
	check_msb(i);
	print_bits(i);
	return 0;
}
