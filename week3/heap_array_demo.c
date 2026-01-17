#include<stdio.h>
#include<stdlib.h>


int main(){
    int num;
    printf("enter the limit of the array:\n");
    scanf("%d",&num);

    int *arr=(int*)malloc(num*sizeof(int));

    printf("enter the elements of the array:\n");
    for(int i=0;i<num;i++){
        scanf("%d",arr+i);
    }

    printf("the elements of the array:\n");
    for(int i=0;i<num;i++){
        printf("%d\n",*(arr+i));
    }

    free(arr);
    arr=NULL;


    return 0;
}