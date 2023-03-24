#include "cfilelib.h"

FILE *FileOpen(char *filename, char *mode)
{
    return fopen(filename, mode);
}

void FileClose(FILE *fp)
{
    fclose(fp);
}

int FileSeek(FILE *fp, long offset, int whence)
{
    return fseek(fp, offset, whence);
}

void WriteInt(int val, FILE *fp)
{
    putc(val, fp);
}

int ReadInt(FILE *fp)
{
    return getc(fp);
}

void WriteDouble(double val, FILE *fp)
{
    char *valPtr;
    int size = sizeof(val);
    valPtr = (char *)&val;
    for(int i=0;i<size;i++)
    {
        putc(*valPtr++,fp);
    }
}
double ReadDouble(FILE *fp)
{
    char *valPtr;
    double value;
    valPtr = (char *)&value;
    int size = sizeof(value);
    for(int i=0;i<size;i++)
    {
        *valPtr =  getc(fp);
        valPtr++;
    }
    return value;
}

void WriteFloat(float val, FILE *fp)
{
    char *valPtr;
    int size = sizeof(val);
    valPtr = (char *)&val;
    for(int i=0;i<size;i++)
    {
        putc(*valPtr++,fp);
    }
}
float ReadFloat(FILE *fp)
{
    char *valPtr;
    float value;
    valPtr = (char *)&value;
    int size = sizeof(value);
    for(int i=0;i<size;i++)
    {
        *valPtr =  getc(fp);
        valPtr++;
    }
    return value;
}

void WriteLong(long val, FILE *fp)
{
    char *valPtr;
    int size = sizeof(val);
    valPtr = (char *)&val;
    for(int i=0;i<size;i++)
    {
        putc(*valPtr++,fp);
    }
}
long ReadLong(FILE *fp)
{
    char *valPtr;
    long value;
    valPtr = (char *)&value;
    int size = sizeof(value);
    for(int i=0;i<size;i++)
    {
        *valPtr =  getc(fp);
        valPtr++;
    }
    return value;
}

// int main(void)
// {
//     double pi = 3.14;
//     int x = 250;
//     FILE* fp = FileOpen("test.bin","a+b");

//     FileClose(fp);
//     printf("%d\n",pi);
//     printf("%f\n",pi);
//     int size = sizeof(pi);
//     int sizeInt = sizeof(x);
//     printf("%d\n",size);
//     printf("%d\n",sizeInt);
//     return 0;
// }