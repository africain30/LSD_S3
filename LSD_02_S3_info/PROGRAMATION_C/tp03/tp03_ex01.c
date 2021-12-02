#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>
#define N 3

double PolyLagrange( double X[N],double x, int i)
{
	double L=1;
	int j=0;
	while(j<N)
	{
		if(i!=j)
			L=L*(x-X[j])/(X[i]-X[j]);
		j++;
	}
	return L;
}

double f(double x)
{
	return (exp(x));
}



  
double InterpLagrange(double X[N],double x,double(*f)(double))
{
	double P=0;
	int j=0;
	while(j<N)
	{
		P=P+f(X[j])*PolyLagrange(X,x,j);
		j++;
	}
	return P;
}


void Representation(double(*f)(double),double a,double b,int n,int p)
{
	double * X =(double *)(malloc(sizeof(double)*n));
	int j=0;
	double x;
	double y;
	while(j<n+1)
	{
		X[j]= a + ((b-a)*j)/n;
		j++;
	}
	j=0;
	while(j<p+1)
	{
		x= a + ((b-a)*j)/p;
		y=InterpLagrange(X,x,f);
		printf("%f		%f\n ", x,y);
		j++;
	}
}

int main()
{
	double X[]={-1,0,3};
	double i=0;
	double x=2.0;
	double c =PolyLagrange(X,x,i);
	printf("%f\n",c);
	Representation(f,-10,10,10,30);
	return 0;
}
