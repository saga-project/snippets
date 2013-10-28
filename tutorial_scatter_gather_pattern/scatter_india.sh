#!/bin/bash

curl --insecure -s https://raw.github.com/pypa/virtualenv/master/virtualenv.py | python - /tmp/sagaenv
. /tmp/sagaenv/bin/activate

python insertion_sort.py -i Data1.txt -o Sorted_Data1.txt$@
