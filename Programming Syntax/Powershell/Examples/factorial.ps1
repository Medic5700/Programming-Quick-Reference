Function factorial ($t1){
    if ($t1 -gt 1){
        return $t1*(factorial($t1-1))
    }
    else{
        return 1
    }
}

for ($i=0;$i -le 10;$i++){
    echo ("$i!`t= " + (factorial($i)))
}