#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc,char *argv[])
{
    //check correct usage
    if (argc != 2)
    {
        printf("Usage: Recovers JPEG. \n");
        return 1;
    }

    //pointer to file
    FILE *in_file = fopen(argv[1], "r");

    //create out file pointer
    FILE *out_file = NULL;

    //if file isn't present return error
    if (in_file == NULL)
    {
        printf("File Not Found");
        return 2;
    }

    //create arrays for file name and buffer
    char filename[8];
    unsigned char buffer[512];

    //initialised states
    int counter = 0;
    bool check = false;

    //read file
    while(fread(buffer,512, 1, in_file) == 1)
    {
        //check file is JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (check == true)
            {
                fclose(out_file);
            }
            else
            {
                check = true;
            }

            //write to file
            sprintf(filename, "%03i.jpg", counter);
            out_file = fopen(filename, "w");
            counter++;
        }

        if (check == true)
        {
            fwrite(&buffer, 512, 1 , out_file);
        }
    }

    //close files
    fclose(in_file);
    fclose(out_file);

    //complete
    return 0;

}