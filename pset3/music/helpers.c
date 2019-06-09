// Helper functions for music

#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    //checks note leength based upon note being of 1/X value
    if (fraction[0] == '1')
    {
        if(fraction[2] == '8')
        {
            return 1;
        }
        else if (fraction[2] == '4')
        {
            return 2;
        }
        else if (fraction[2] == '2')
        {
            return 4;
        }
        else if(fraction[2] == '1')
        {
            return 8;
        }

    }
    //triplet note conditons
    else if (fraction[0] == '3' && fraction[2] == '8')
    {
        return 3;
    }
    else
    {
        return 0;
    }

    return 0;

}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{

    //last character in string determines octave
    int octave = note[strlen(note) - 1] - '0';


    //determine frequency of note
    double frequency = 0.0;


    //note to frequency conditions
    if (note[0] == 'A')
    {
        frequency = 440;
    }
    else if (note[0] == 'B')
    {
        frequency = 440.0 * (pow(2.0, (2.0/12.0)));
    }
    else if (note[0] == 'C')
    {
        frequency = 440.0 / (pow(2.0, (9.0 / 12.0)));
    }
    else if (note[0] == 'D')
    {
        frequency = 440.0 / (pow(2.0, (7.0 / 12.0)));
    }
    else if (note[0] == 'E')
    {
        frequency = 440.0 / (pow(2.0, (5.0 / 12.0)));
    }
    else if (note[0] == 'F')
    {
        frequency = 440.0 / (pow(2.0, (4.0 / 12.0)));
    }
    else if (note[0] == 'G')
    {
        frequency = 440.0 / (pow(2.0, (2.0 / 12.0)));
    }


    //conditions to dictate octave played
    if (octave > 4)
    {
        for (int i = 0; i < octave - 4; i++)
        {
            frequency *= 2.0;
        }
    }
    else if (octave < 4)
    {
        for (int i = 0; i < 4 - octave; i++)
        {
            frequency /= 2.0;
        }
    }

    //operation to create flats and sharps when applicable

    if (note[1] == 'b')
    {
        frequency /= (pow(2.0, (1.0 / 12.0)));
    }
    else if (note[1] == '#')
    {
        frequency *= (pow(2.0, (1.0 / 12.0)));
    }

    // Convert double back to int

    int result = round(frequency);
    return result;
}

// Determines whether a string represents a rest

bool is_rest(string s)
{
    if (s[0] == '\0')
    {
        return true;
    }
   else
   {
       return false;
   }
}
