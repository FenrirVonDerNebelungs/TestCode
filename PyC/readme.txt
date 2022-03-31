g++ -c -fPIC testPYC0.cpp -o testPYC.o #-c compile and assemble without link, -fPIC is position (in memory) independent code need when making a shared library 
#g++ -shared -Wl,-soname,testPYC.so -o testPYC.so testPYC.o #-shared is shared library, -Wl pas comma-seperated opitons, -soname some desination of the name of the so file -o precedes the output file
try this first
g++ -shared -o testPYC.so testPYC.o
