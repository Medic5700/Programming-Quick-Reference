$temp = 0
try{
    $temp = 2/0
}
catch{
    echo "Error 0: attempt to divide by zero"
}

try{
    #some commands have a "-erroraction" that needs to be set in order to catch it, or handle errors in general
    $temp = Test-Connection "www.google.com" -count 1 -TimeToLive 1 -ErrorAction stop #note: timetolive set to 1, almost gurenteeing it fails
    echo "Error 1: no error"
}
catch{
    echo "Error 1: error exicuting command"
}
