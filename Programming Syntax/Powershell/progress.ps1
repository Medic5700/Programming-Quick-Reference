for ($i=0;$i -le 10;$i++){
    write-progress -activity ("Some Activity: "+$currentVC) -status "An Opperation" -currentoperation "Current Operation: $i" -percentcomplete ($i*10)
    echo "output that isn't affected by the write-progress commandlet"
    sleep(1);
}
