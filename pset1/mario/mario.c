
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;

//promt height  for pyramid from user
    do
    {
        printf("Specify Pryamid Height:");
        height = get_int();
    }

    while (height < 0 || height > 23);

//for loop to build the pyramid

    for (int row = 0; row < height; row++)
    {
        for (int spaces = height - row; spaces > 1; spaces--)
        {
            printf(" ");
        }
        for (int hashes = 0; hashes < row + 2; hashes++)
        {
            printf("#");
        }

        printf("\n");

    }
}