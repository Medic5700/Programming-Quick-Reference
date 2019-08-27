# http://stevenmurawski.com/powershell/2011/04/using-pipeline-input
# http://www.powershellpro.com/powershell-tutorial-introduction/powershell-functions-filters/

function func0 {
    "function/procedure func0"
}
func0

function func1 ($t1){
    "function/procedure func1 - $t1"
}
func1(1)
func1 1

function func2 ($t1, $t2) {
    "function/procedure func2 - $t1 - $t2"
}
func2 1 2
func2 (1,2) #note how this results in $t1 being an structer containing 1 and 2, with $t2 being left blank