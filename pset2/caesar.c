
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

//convert key string to int for encryption

    int key = atoi(argv[1]);

//check correct key input
    if (key < 0)
    {
        printf("not a positive value\n");
        return 1;
    }

    else
    {

//promt user for code to encrypt

    string code = get_string("Code to Encrypt:");

//because check50 wants it to say cyphertext:

    printf("ciphertext:");

//loop through given code

    for (int i = 0, n = strlen(code); i < n; i++)
    {

//check if lowercase then encrypt

        if islower(code[i])
        printf("%c", (((code[i] + key) - 97) % 26) + 97);

//check if uppercase then encrypt

        else if isupper(code[i])
        printf("%c", (((code[i] + key) - 65) % 26) + 65);

//print punctuation as is

        else
        printf("%c", code[i]);
    }
    }

printf("\n");
return 0;
}