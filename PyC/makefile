LIBNAME = TPyClib.so
OBJS = tobjPYC_dum.o tobjPYC.o tobjPYCwrap.o
FLGS = -c -fPIC

$(LIBNAME) : $(OBJS)
	g++ -shared -o $(LIBNAME) $(OBJS)
tobjPYCwrap.o : tobjPYC.h
	g++ $(FLGS) tobjPYCwrap.cpp
tobjPYC.o : tobjPYC.h tobjPYC_dum.h
	g++ $(FLGS) tobjPYC.cpp
tobjPYC_dum.o : tobjPYC_dum.h
	g++ $(FLGS) tobjPYC_dum.cpp
clean :
	rm -f core $(LIBNAME) $(OBJS)