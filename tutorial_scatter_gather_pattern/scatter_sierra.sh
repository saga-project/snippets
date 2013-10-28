#!/bin/bash

module load python/2.7

curl --insecure -s https://raw.github.com/pypa/virtualenv/master/virtualenv.py | python - /tmp/sagaenv
. /tmp/sagaenv/bin/activate

python insertion_sort.py -i Data2.txt -o Sorted_Data2.txt$@
