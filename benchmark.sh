# Usage: ./benchmark.sh [dataDir] [solDir] [algo} [timeLimit]
# where algo can be one of these:
#   --enum
#   --gradient
#   --meta1
#   --meta2
# and timeLimit is in seconds.


#if size of argv less than 4 or more than 4, then print the help message and exit
if [ $# -lt 4 ] || [ $# -gt 4 ]; then
    echo "Usage: ./benchmark.sh [dataDir] [solDir] [algo] [timeLimit]"
    echo "where algo can be one of these:"
    echo "  --enum"
    echo "  --gradient"
    echo "  --meta1"
    echo "  --meta2"
    echo "and timeLimit is in seconds."
    exit 1
fi

echo Experimental Campaign:
echo Data directory: $1
echo Output directory: $2
echo Algorithm: $3
echo Time limit: $4

algoDir = "${3#*--}"

mkdir -p $2  # create the output directory if it does not already exist
cd $2 && mkdir -p $algoDir
echo `date` > $2/$algoDir/date.txt

for instance in `ls $1` ; do  # for each instance in directory $1
    echo Resolution of $instance
    python3 src/main.py $1/$instance $3 -t $4 >> $2/$algoDir/log_${instance}.txt  # writing console output to a log file
done

grep Result $2/$algoDir/*.txt >> $2/$algoDir/results.csv  # lines containing the word "Result" will be concatenated in the results.csv file

exit 0