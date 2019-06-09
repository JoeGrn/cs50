// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[N];


// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int length = strlen(word);
    char lower[length + 1];
    for (int i = 0; i < length; i++)
    {
        lower[i] = tolower(word[i]);
    }

    lower[length] = '\0';

    int index = hash(lower);

    node* head = hashtable[index];

    node *cursor = head;

    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }

        cursor = cursor->next;

    }
    return false;
}

int nowords = 0;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
        {
            word[strlen(word)] = '\0';

            node *new_node = malloc(sizeof(node));

            if (new_node == NULL)
            {
                unload();
                return false;
            }

        strcpy(new_node->word, word);

        int index = 0;
        index = hash(word);

        new_node->next = hashtable[index];
        hashtable[index] = new_node;

        nowords++;
        }


    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return nowords;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{

    for (int i = 0; i < N; i++)
    {
        node *cursor = hashtable[i];

        while (cursor != NULL)
        {
            node *temp = cursor;

            cursor = cursor->next;

            free(temp);
        }

    }

    return true;

}
