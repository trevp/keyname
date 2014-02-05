
OPENSSL_INCLUDE = ~/tools/openssl-1.0.1f/include/
OPENSSL_LIB = ~/tools/openssl-1.0.1f/libcrypto.a
keyname: keyname.c
	gcc -O4 -I $(OPENSSL_INCLUDE) $(OPENSSL_LIB) keyname.c -o keyname

test:
	python ./keyname_script.py 