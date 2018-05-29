#!/bin/bash

cd "node_modules/vux/src/components"

find ./ -name *.vue | xargs sed -i 's/$t//g'

echo "End."