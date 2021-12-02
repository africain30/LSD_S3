#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

float ** sum_m( float **, float **, int  ) ;
float ** mult_m ( float **, float **, int  ) ;
float ** trans_m ( float **, int  ) ;
float ** dia_m ( float ** , int  ) ;

float ** matrix_create(int n,int m){
	float ** M;
	M=(float**)malloc(sizeof(float *)*n);
	int i=0;
	while(i<n){
		M[i] =(float*) malloc(sizeof(float)*m);
		i++;
	}
	return M;
}

void matrix_input (float**M, int n)
{
	int i=0;
	int j=0;
	while(i<n){
		while(j<n){
			scanf("%f",&M[i][j]);
			j++;
		}
		i++;
		j=0;
	}
	return ;
}

void free_matrix(float ** M,int n)
{
        int i = 0;
        while(i < n){
                free(M[i]);
                i++;
        }
        free(M);
	return;
}

void matrix_output(float** M,int n){
	for(int i = 0 ; i < n; i++){
		for(int j = 0 ; j < n ; j++){
			printf("%f  ",M[i][j]);
		}
		printf("\n");
	}
	printf("\n");
	return ;
}

float ** sum_m( float ** K, float ** L, int n ){
	float** M= matrix_create(n,n);
	for(int i = 0; i < n ; i++){
		for(int j = 0; j < n ; j++){
			M[i][j]=K[i][j]+L[i][j];
		}
	}
	return M;
}

float ** mult_m ( float **K, float **L, int n ){
	float** M= matrix_create(n,n);
	for(int i = 0; i < n ; i++){
		for(int j = 0; j < n ; j++){
			for(int h = 0 ; h < n ; h++){
				M[i][j]+=K[i][h]*L[h][j];
			} 
		}
	}
	return M;
}

float ** trans_m ( float **M, int n ){
	float** N= matrix_create(n,n);
	int i = 0;
	int j = 0;
	while(i<n){
		while(j<n){
			N[i][j]=M[j][i];
			j++;
		}
		i++;
		j=0;
	}
	return N;
}

float ** dia_m ( float **M , int n ){
	float** N= matrix_create(2,n);
	int i = 0;
	while(i<n){
		N[0][i]=M[i][i];
		i++;
	}
	i=0;
	while(i<n){
		N[1][i]=M[i][n-1-i];
		i++;
	}
	return N;
}

int main(){
	int n;
	printf("enter the dimensions of squared matrix\n");
	printf("the rows and columns : ");
	scanf("%d",&n);
	float** M = matrix_create(n);
	float** N = matrix_create(n);
	matrix_input(M,n);
	matrix_input(N,n);
	matrix_output(M,n);
	matrix_output(N,n);
	float** K=matrix_create(n);
	K=sum_m(M,N,n);
	matrix_output(K,n);
	K=mult_m(M,N,n);
	matrix_output(K,n);
	K=trans_m(K,n);
	matrix_output(K,n);
	K=dia_m(K,n);
	matrix_output(K,n);
	free_matrix(M,n);
	free_matrix(N,n);
	free_matrix(K,n);
}

