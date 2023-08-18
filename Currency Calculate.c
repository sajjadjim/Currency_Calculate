#include<stdio.h>
int main()
{
    
    int n;
    int a,b,c,d,e,f,g;
    printf(" \"Enter BDT any amount currency for calculation\"\n");
    scanf("%d", &n);
    printf("Amount of Money=%dTaka\n",n);

    a = n/100;
    n = n-(a*100);

    b = n/50;
    n = n-(b*50);

    c = n/20;
    n = n-(c*20);

    d = n/10;
    n = n-(d*10);

    e = n/5;
    n = n-(e*5);

    f = n/2;
    n = n-(f*2);

    g = n/1;

    printf("%d note(s) Taka 100\n",a);
    printf("%d note(s) Taka 50\n",b);
    printf("%d note(s) Taka 20\n",c);
    printf("%d note(s) Taka 10\n",d);
    printf("%d note(s) Taka 5\n",e);
    printf("%d note(s) Taka 2\n",f);
    printf("%d note(s) Taka 1\n",g);
    return 0;

}
