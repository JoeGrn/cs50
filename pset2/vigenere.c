
#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{

//promt user for key

    if (argc != 2)
    {
        printf("One Key Please!\n");
        return 1;
    }

    string key = argv[1];
    int length = strlen(key);
    for (int j = 0; j < length; j++)
    {
        if (!isalpha(key[j]))
        {
            printf("Invalid Key\n");
            return 1;
        }
    }



//promt user for code to encrypt

    string code = get_string("Code to Encrypt:");

//because check50 wants it to say cyphertext:

    printf("ciphertext:");

//loop through given code

    for (int i = 0, index = 0, n = strlen(code); i < n; i++)
    {
        if (isalpha(code[i]))

        {
            //check if lowercase then encrypt

            if (islower(code[i]))
            {
            printf("%c", (code[i] - 'a' + toupper (key[index]) - 'A') % 26 + 'a' );
            }

            //check if uppercase then encrypt

            else if (isupper(code[i]))
            {
            printf("%c", (code[i] - 'A' + toupper (key[index]) - 'A') % 26 + 'A' );
            }
            index = (index + 1) % length;
        }

            //print punctuation as is

            else
            printf("%c", code[i]);



    }

printf("\n");
return 0;



}