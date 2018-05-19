
INSTALL_PATH:=~cs537-1/ta/tests/5a-new
PYTHON_PATH=python

all: runtests

runtests:
	echo "#!/bin/bash" > $@
	echo "base=$(INSTALL_PATH)" >> $@
	echo "$(PYTHON_PATH) \$$base/project5.py --test-path \$$base \$$@"\
		" | tee runtests.log" >> $@
	echo "exit \$$?" >> $@
	chmod a+x runtests
	gcc -o util/repair_check util/repair_check.c -Wall -Werror

install: runtests
	mkdir -p $(INSTALL_PATH)
	cp -r * $(INSTALL_PATH)
	afs_rseta $(INSTALL_PATH) system:anyuser read

clean:
	rm -f runtests*
	rm -f *.pyc
