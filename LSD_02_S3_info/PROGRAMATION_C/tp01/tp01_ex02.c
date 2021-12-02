#include <stdlib.h>
#include <stdio.h>
int **dummy( int **x , int n)
{
	int **y ;
	int i ;
	int j ;
	i = 0;
	y = ( int **) malloc ( sizeof ( int *) *(n +1) ) ;
	while ( i <n)
	{
		y [ i ] = ( int *) malloc ( sizeof ( int ) *n ) ;
		j = 0;
		while( j <n)
		{
			y [ i ] [ j ] = j ;
			j++;
		}
		i ++;
	}
	y [ n ] = (x [ 0 ]) ;
	return(y ) ;
}


int main ()
{
	int n ;
	int **x ;
	int i ;
	int j ;
	n = 10;
	i = 0;
	x = ( int **)malloc(sizeof(int *) *(n) ) ;
	while ( i <n)
	{
		x [ i ] = (int *)malloc(sizeof( int ) *n ) ;
		j = 0;
		while( j <n)
		{
			x [ i ] [ j ] = j ;
			j++;
		}
		i ++;
	}
	int ** temp =x;
	i=0;
	
	x = dummy(x , n ) ;
	while ( i <n)
	{
		free(temp[i]);
		i++;
	}
	free(temp);

	i = 0;
	while ( i <n)
	{
		j = 0;
		while ( j <n)
		{
			printf( "%d" , x [ i ] [ j ] ) ;
			j++;
		}
		printf( "\n" ) ;
		i ++;
	}
	i=0;
	while ( i <n)
	{
		free(x[i]);
		i++;
	}
	free(x);
	
}
