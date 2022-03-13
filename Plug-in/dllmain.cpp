// dllmain.cpp : Defines the entry point for the DLL application.
#include "pch.h"
#include <stdint.h>
#include <stdlib.h>
#include <time.h>

#define DllExport __declspec (dllexport)

extern "C"
{
    DllExport void SeedRandomizer()
    {
        srand((unsigned int)time(0));
    }

    DllExport int DieRoll(int sides)
    {
        return (rand() % sides) + 1;
    }

    DllExport float Add(float a, float b)
    {
        return a + b;
    }

    DllExport float Random()
    {
        return (double)(rand()) / ((uint64_t)RAND_MAX + 1);
    }

    DllExport const char* HelloWorld()
    {
        return "Hello, world!";
    }
}