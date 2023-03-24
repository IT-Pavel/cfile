//#pragma once

#ifndef _CFILE_H_
#define _CFILE_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdio.h>
#include <string.h>
#include <unistd.h>

    FILE *FileOpen(char *filename, char *mode);
    void FileClose(FILE *fp);
    int FileSeek(FILE *fp, long offset, int whence);
    void WriteInt(int val, FILE *fp);
    int ReadInt(FILE *fp);
    void WriteDouble(double val, FILE *fp);
    double  ReadDouble(FILE *fp);
    void WriteFloat(float val, FILE *fp);
    float  ReadFloat(FILE *fp);
    void WriteLong(long val, FILE *fp);
    long  ReadLong(FILE *fp);
    

#ifdef __cplusplus
}
#endif

#endif /*_CFILE_H_*/