import ctypes
import os


class FILE(ctypes.Structure):
    pass


class CFile:

    __cfilelib = None
    __file_stream:ctypes.POINTER(FILE) = None
    
    def __init__(self) -> None:
        libname = "./cfilelib.so"

        if (os.name == "nt"):
            libname = "./cfilelib.dll"

        self.__cfilelib = ctypes.CDLL(libname)

        self.__cfilelib.FileOpen.restype = ctypes.POINTER(FILE)
        self.__cfilelib.FileOpen.argtypes = [
            ctypes.POINTER(ctypes.c_char),
            ctypes.POINTER(ctypes.c_char)]

        self.__cfilelib.FileClose.argtypes = [
            ctypes.POINTER(FILE)
        ]

        self.__cfilelib.FileSeek.restype = ctypes.c_int
        self.__cfilelib.FileSeek.argtypes = [
            ctypes.POINTER(FILE),
            ctypes.c_long,
            ctypes.c_int
        ]

        self.__cfilelib.WriteInt.argtypes = [
            ctypes.c_int,
            ctypes.POINTER(FILE)
        ]

        self.__cfilelib.ReadInt.restype = ctypes.c_int
        self.__cfilelib.ReadInt.argtypes = [
            ctypes.POINTER(FILE)
        ]

        self.__cfilelib.WriteDouble.argtypes = [
            ctypes.c_double,
            ctypes.POINTER(FILE)
        ]

        self.__cfilelib.ReadDouble.restype = ctypes.c_double
        self.__cfilelib.ReadDouble.argtypes = [
            ctypes.POINTER(FILE)
        ]

        self.__cfilelib.WriteFloat.argtypes = [
            ctypes.c_float,
            ctypes.POINTER(FILE)
        ]

        self.__cfilelib.ReadFloat.restype = ctypes.c_float
        self.__cfilelib.ReadFloat.argtypes = [
            ctypes.POINTER(FILE)
        ]

        self.__cfilelib.WriteLong.argtypes = [
            ctypes.c_long,
            ctypes.POINTER(FILE)
        ]

        self.__cfilelib.ReadLong.restype = ctypes.c_long
        self.__cfilelib.ReadLong.argtypes = [
            ctypes.POINTER(FILE)
        ]

    def FileOpen(self, filename: str, mode: str) -> None:
        self.__file_stream = self.__cfilelib.FileOpen(filename.encode('utf8'), mode.encode('utf8'))

    def FileClose(self) -> None:
        self.__cfilelib.FileClose(self.__file_stream)

    def FileSeek(
            self,
            offset: int,
            whence: int) -> int:
        self.__cfilelib.FileSeek(self.__file_stream, offset, whence)

    def WriteInt(self, value: int) -> None:
        self.__cfilelib.WriteInt(value, self.__file_stream)

    def ReadInt(self) -> int:
        return int(self.__cfilelib.ReadInt(self.__file_stream))

    def WriteDouble(self, value: float) -> None:
        self.__cfilelib.WriteDouble(value, self.__file_stream)

    def ReadDouble(self) -> float:
        return float(self.__cfilelib.ReadDouble(self.__file_stream))

    def WriteFloat(self, value: float) -> None:
        self.__cfilelib.WriteFloat(value,self.__file_stream)

    def ReadFloat(self) -> float:
        return float(self.__cfilelib.ReadFloat(self.__file_stream))

    def WriteLong(self, value: int) -> None:
        self.__cfilelib.WriteLong(value, self.__file_stream)

    def ReadLong(self) -> int:
        return int(self.__cfilelib.ReadLong(self.__file_stream))


def main():  # For test C-functions
    pi:float = 3.140004240001
    print(f"Origin: {pi}")
    file_stream = CFile()
    file_stream.FileOpen("test.bin","wb")
    file_stream.FileClose()


if __name__ == "__main__":
    main()
