Function fib($t1){
    if ($t1 -eq 0){ return 0 }
    elseif ($t1 -eq 1){ return 1 }
    else { return (fib($t1-1)) + (fib($t1-2)) }
}

for ($i=0;$i -le 10;$i++){
    echo ("fib($i)`t= " + (fib($i)))
}