#!/usr/bin/env sh

set -e
set -x

RED="\e[31m\e[47m"
GREEN='\033[0;32m'
CYAN='\033[0;36m'
GREY="\e[37m"
NC='\033[0m' # No Color

here=$(dirname $(realpath $0))
sourcedir=$here/source
builddir=$here/build

rm -rf $builddir
VERSION=`cat $sourcedir/VERSION`
PRODUCT="aie-st-app"

target_no_version=$PRODUCT.tex
target=$PRODUCT-$VERSION.tex

sphinx-build -b latex $sourcedir $builddir
test -f $builddir/$target_no_version
mv $builddir/$target_no_version $builddir/$target
test -f $builddir/$target

sha1file=$sourcedir/git_sha1

git log | head -n 1 | sed "s/commit *" > $sha1file \
  || printf "sorry, this release document was not generated from a git repo, cannot get sha1" > $sha1file


(
  cd $builddir
  count=0
  while true ; do
    let count+=1
    pdflatex $target
    logfile=$builddir/$(basename $target .tex).log
    test -f $logfile
    rerun=`cat $logfile | grep "Rerun to get" | wc -l`
    if test $rerun -eq 0 ;  then
      break
    fi
    echo "need to rerun after $count runs"
  done
  echo "$count runs"
)
pdf_file=$builddir/$PRODUCT-$VERSION.pdf
test -n $pdf_file
printf "you generated the delivery sheet : \n${GREEN}${pdf_file}${NC}\n"
echo DONE
