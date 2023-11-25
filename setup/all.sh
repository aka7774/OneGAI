#!/usr/bin/bash

workdir=`pwd`

for sh in `find setup/ -type f -name *.sh`;
do
	chmod +x $sh
	cd $workdir; . $sh
done

for sh in `find install/ -type f -name *.sh`;
do
	chmod +x $sh
	cd $workdir; . $sh
done
