#!/usr/bin/bash

echo -n 'Reblacking python files: '
find . -name \*.py -exec black --quiet {} \;
if [ $? == 0 ]; then
	echo 'OK'
else
	echo 'FAILED'
	exit 1
fi

echo -n 'Running unit tests: '
pytest --quiet
if [ $? == 0 ]; then
	echo 'OK'
else
	echo 'FAILED'
	exit 1
fi

echo -n 'Updating attribute documentation: '
python sole_attributes.py > docs/attributes.md
if [ $? == 0 ]; then
	echo 'OK'
else
	echo 'FAILED'
	exit 1
fi

echo -n 'Creating HTML documentation: '
for i in `find . -name \*.md`; do
	markdown_py $i -x extra -x toc -x nl2br -f `echo $i | sed 's/\.md$/.html/'`
done
if [ $? == 0 ]; then
	echo 'OK'
else
	echo 'FAILED'
	exit 1
fi
