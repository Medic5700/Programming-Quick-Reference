
for($i = 0; $i -lt 10; $i++){
    echo "Loop 0 interation $i"
}

(0,1,2,3,4,5,6,7,8,9) | foreach {
    echo "Loop 1 interation $_" #the '$_' is the iterated object
}

$i = 0
while ($i -lt 10){
    echo "Loop 2 interation $i"
    $i++
}

$i=0
do {
    echo "Loop 3 interation $i"
    $i++
} while ($i -lt 10)

$i=0
do {
    echo "Loop 4 interation $i"
    $i++
} until ($i -eq 10)

$i = 0
while (1){
    echo "Loop 5 interation $i"
    $i++
    if ($i -eq 10){
        break;
    }
}

for($i = 0; $i -lt 10; $i++){
    echo "Loop 6 interation $i"
    if ($i -lt 9){
        continue
    }
    echo "--------Loop 6 finished"
}

#for 'where' loops, go to selective