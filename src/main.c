#include "cfilelib.h"

int main(void)
{
    double pi = 3.14545174837;
    int x = 250;
    FILE* fp = FileOpen("test.bin","w+b");
    WriteDouble(pi,fp);
    FileSeek(fp,0,SEEK_SET);
    double val = ReadDobule(fp);
    printf("%4.20f\n",val);
    FileClose(fp);
    return 0;
}