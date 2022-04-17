# Usage: ./benchmark.sh [dataDir] [solDir] [algo] [timeLimit] [k] [sizeNeighborhood]
# where algo can be one of these:
#   --enum
#   --gradient
#   --meta1
#   --meta2
# timeLimit is the time limit in seconds,
# k is the number of partitions (default: 2),
# and sizeNeighborhood is the size of the neighborhood,
# only for the meta-heuristics (default: all the neighborhoods).


#if size of argv less than 4 or more than 5, then print the help message and exit
if [ $# -lt 4 ] || [ $# -gt 6 ]; then
    echo "Usage: ./benchmark.sh [dataDir] [solDir] [algo] [timeLimit] [k] [sizeNeighborhood]"
    echo "where algo can be one of these: "
    echo "  --enum"
    echo "  --gradient"
    echo "  --meta1"
    echo "  --meta2"
    echo "timeLimit is the time limit in seconds,"
    echo "k is the number of partitions (default: 2),"
    echo "and sizeNeighborhood is the size of the neighborhood,"
    echo "only for the meta-heuristics (default: all the neighborhoods)."
    exit 1
fi

echo Experimental Campaign:
echo Data directory: $1
echo Output directory: $2
echo Algorithm: $3
echo Time limit: $4

if [ $# -eq 5 ]; then
    echo Number of partitions: $5
fi

if [ $# -eq 6 ]; then
    echo Number of partitions: $5
    echo Neighborhood size: $6
fi

algoDir="${3#*--}"
mkdir -p $2  # create the output directory if it does not already exist
cd $2 && mkdir -p $algoDir
echo `date` > $algoDir/date.txt
cd ..

if [ $# -eq 5 ]; then # if the number of partitions is specified
    for instance in `ls $1` ; do  # for each instance in directory $1
        echo Resolution of $instance
        python3 src/main.py $1/$instance $3 -t $4 -c $5 >> $2/$algoDir/log_${instance} # writing console output to a log file
    done
    elif [ $# -eq 6 ]; then # if the neighborhood size is specified
    for instance in `ls $1` ; do
        echo Resolution of $instance
        python3 src/main.py $1/$instance $3 -t $4 -c $5 -s $6 >> $2/$algoDir/log_${instance}
    done
else # if no parameters are specified
    for instance in `ls $1` ; do  # for each instance in directory $1
        echo Resolution of $instance
        python3 src/main.py $1/$instance $3 -t $4 >> $2/$algoDir/log_${instance} # writing console output to a log file
    done
fi

grep Result $2/$algoDir/*.txt >> $2/$algoDir/results.csv  # lines containing the word "Result" will be concatenated in the results.csv file

exit 0