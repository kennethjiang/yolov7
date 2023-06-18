cd $1/labels
wc -l * | grep -v ' total' > ../count.out
cd ..
awk '$1 >= 3 && $1 <= 5 {print $2}' count.out | sed s/.txt/.jpg/ | shuf | head -10 > 3-5.out
awk '$1 >= 6 && $1 <= 10 {print $2}' count.out | sed s/.txt/.jpg/ | shuf | head -15 > 6-10.out
awk '$1 >= 11 && $1 <= 20 {print $2}' count.out | sed s/.txt/.jpg/ | shuf | head -30 > 11-20.out
awk '$1 >= 21 && $1 <= 200 {print $2}' count.out | sed s/.txt/.jpg/ | shuf | head -20 > 21.out
rm count.out

OUTDIR="/Users/kenneth/Downloads/newbatch2/batch3/neil@obico.io/$1"
INDIR="/Users/kenneth/Downloads/newbatch2/neil@obico.io/$1"
mkdir "$OUTDIR"
cat *.out | while IFS= read -r filename; do cp "$INDIR/$filename" "$OUTDIR"; done
cd ..
