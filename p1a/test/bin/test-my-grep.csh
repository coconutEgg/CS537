#! /bin/csh -f
set TEST_HOME = /afs/cs.wisc.edu/p/course/cs537-remzi/tests
set source_file = my-grep.c
set binary_file = my-grep
set bin_dir = /afs/cs.wisc.edu/p/course/cs537-remzi/tests/bin
set test_dir = /afs/cs.wisc.edu/p/course/cs537-remzi/tests/tests-my-grep
${bin_dir}/generic-tester.py -s $source_file -b $binary_file -t $test_dir $argv[*]
