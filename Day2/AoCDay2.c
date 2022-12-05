#include <stdio.h> // define the header file  
#include <stdlib.h>
#include <string.h>
# define LINE_LENGTH 1000

int Compare(char left, char right)
{
    int temp,rock,paper,sis,A,B,C = 0;

    if (right == 'X')
    {
        rock = 1;
    }
    if (right == 'Y')
    {
        paper = 1;
    }
    if (right == 'Z')
    {
        sis = 1;
    }
    if (left == 'A')
    {
        A = 1;
    }
    if (left == 'B')
    {
        B = 1;
    }
    if (left == 'C')
    {
        C = 1;
    }

    printf("I need this to make it work idk why %d ",C);

    if (A == 1)
    {
        if (rock == 1)
        {
            temp = 4;
            return temp;
        }
        if (paper == 1)
        {
            temp = 8;
            return temp;
        }
        if (sis == 1)
        {
            temp = 3;
            return temp;
        }
    }
    if (B == 1)
    {
        if (rock == 1)
        {
            temp = 1;
            return temp;
        }
        if (paper == 1)
        {
            temp = 5;
            return temp;
        }
        if (sis == 1)
        {
            temp = 9;
            return temp;
        }
    }
    if (C == 1)
    {  
        if (rock == 1)
        {
            temp = 7;
            return temp;
        }
        if (paper == 1)
        {
            temp = 2;
            return temp;
        }
        if (sis == 1)
        {
            temp = 6;
            return temp;
        }
    } 
}

int main()   // define the main function  
{  
    FILE *inptr;
    char line [LINE_LENGTH];
    char str1;
    char str2;
    int ans;
    int sum;

    sum = 0;
    inptr = fopen("C:\\Users\\Matthew.Eckert\\Desktop\\AoC\\Day2\\input.txt","r");
    if(inptr == NULL)
       {return 1;}

    while(fgets(line, LINE_LENGTH, inptr))
    {
        str1 = line[0];
        str2 = line[2];
        ans = Compare(str1,str2);
        printf("Round %c %c : %d \n", str1,str2,ans);
        sum += ans;
    }  

    fclose(inptr);
    printf("%d", sum);
}