// Header file for input output functions
#include<iostream> 
#include <stdlib.h> 
#include <time.h>
#include <unistd.h>

using namespace std;

// main function -
// where the execution of program begins
int p_random();
int dice_random();

int main()
{
    // prints heelo world
    int i;
    int count = 0;
    //for ( i = 0 ; i < 100; i++){
	cout<<dice_random();	
//}
    return 0;
}

int p_random()
{
	int p = 40 ;// probablity of p_random returning true is 40%
	srand((unsigned)time(0));
	if (rand()%100 < p){
		return 1;
		}
	else {return 0;}
}


int dice_random()
{
 	int rand1 = p_random();
 	int rand2 = p_random();
 	int rand3 = p_random();
//   since we need to choose 6 combinations and we have 8, i wrote while loop as below to eliminate two combinations 101 and 110.
 	while (rand1 == 1 && rand2 != rand3)
	{
		int rand1 = p_random();
		int rand2 = p_random();
		int rand3 = p_random();
		cout <<"Here";
	}
	int case_int = rand1*100+rand2*10+rand3;
	cout<<case_int;
	switch(case_int)
	{
		case 000 : return 1;
		case 001 : return 2;
		case 010 : return 3;
		case 011 : return 4;
		case 100 : return 5;
		case 111 : return 6;
	}
}
