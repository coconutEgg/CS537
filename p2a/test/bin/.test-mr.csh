#! /bin/csh -f

set TEST_HOME = /afs/cs.wisc.edu/p/course/cs537-remzi/tests
set source_file = mapreduce.c,wordcount.c
set binary_file = mr
set bin_dir = /afs/cs.wisc.edu/p/course/cs537-remzi/tests/bin
set test_dir = /afs/cs.wisc.edu/p/course/cs537-remzi/tests/tests-mr
${bin_dir}/generic-tester-multi.py $argv[*] -s $source_file -b $binary_file -t $test_dir


