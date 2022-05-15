for i in * 
do
base=${i%_veets}
echo "mv ${i} ${base}_veets" 
mv ${i} ${base}_veets
done
  