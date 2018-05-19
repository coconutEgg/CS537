import sys

f = open(sys.argv[1])
content = ''.join(f.readlines())
if "All heap blocks were freed -- no leaks are possible" in content and \
    "ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)" in content:
    exit(0)
exit(1)
