# Questions

## What's `stdint.h`?

A header file including declarations for integer types of specific widths.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

Declares and integer of a set size e.g. uint8_t will be 8 bits 'wide'.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

1,4,8,2.

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

This word or words specify a file type and will tell the computer how to interperate the binary from the given file.

## What's the difference between `bfSize` and `biSize`?

bfSize is the size of the file as a whole include the header files. biSize is the size of only the image (the rgbtriple and any padding).

## What does it mean if `biHeight` is negative?

The image is 'top down'. This means that the first bytes of data stored into memory will be the bottow row of pixels in the image.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBit Count specifies the number of bits in each pixel.

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

Output will return NULL if the file cannot be found this then will force the program to terminate to prevent the pointer being directed to incorrect memory.

## Why is the third argument to `fread` always `1` in our code?

One RGBtriple is being processed one at a time.

## What value does line 65 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

1? as padding is used in order to create a structure which can be stored with a multiple of 4.

## What does `fseek` do?

Performs a search within a file (aka go to). It is used in this case to skip over padding to rgbtriple pixels.

## What is `SEEK_CUR`?

Seek current moves to the given location in a file in this case a specified pixel within the image. I believe its use is to skip the padding in this case.

## Whodunit?

It was proffesor plum with the candlestick in the library!
