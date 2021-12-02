#include <stdlib.h>
#include <stdio.h>
#include <math.h>

float f(float);
float fp(float);
float Dichotomie(float(*f)(float),float a, float b, int n);
float Newton(float(*f)(float),float(*fp)(float), float x, int n);

float f(float x){
	return x*x-2;
}

float fp(float x){
	return 2*x;
}

float Dichotomie(float(*f)(float),float a, float b, int n){
	float k = (a+b)/2;
	for(int i =0 ; i < n; i++){
		if(f(a)*f(k)<0){
			b=k;
		}
		else{
			a=k;
		}
		k = (a+b)/2;
	}
	return k;
}

float Newton(float(*f)(float),float(*fp)(float), float x, int n){
	for(int i = 0 ; i< n; i++){
		x=x-(f(x)/fp(x));
	}
	return x;
}


float Dichotomie2(float(*f)(float),float a, float b, int e)
{
	float x0=Dichotomie(*f,a,b,1);
	float x1=Dichotomie(*f,a,b,2);
	int i=0;
	while( abs(x1-x0)>e)
	{
		x0=x1;
		x1=Dichotomie(*f,a,b,i);
		i++;
	}
	return x0;
}


int main(){
	float a = 1;
	float b = 3;
	float c = Dichotomie(&f,a,b,10);
	float d = Newton(&f,&fp,2,10);
	float e = Dichotomie2(&f,a,b,pow(10,-9));
	printf("%f\n",c);
	printf("%f\n",d);
	printf("%f\n",e);
	return 0;
}
