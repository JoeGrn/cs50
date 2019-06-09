
#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)

{

    float change;

//ask user how much change is needed

    do
    {
        printf("Please enter the ammount of change required:");
        change = get_float();
    }

    while (change < 0.0);

//calculates change due based upon input

    int input = round(change * 100);
    int quaters = input / 25;
    int dimes = (input % 25) / 10;
    int nickles = (input % 25 % 10) / 5;
    int pennies = (input % 5) / 1;

//calculates minimum coins needed and outputs to user

    int total = quaters + dimes + nickles + pennies;
    printf ("%d\n", total);

}