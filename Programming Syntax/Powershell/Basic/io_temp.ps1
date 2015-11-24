#console input and output
$num1 = 5
echo "output $num1 to the console"

#write to a file
$text = "testtest"
$text | set-content "bin\test.txt"
$text | add-content "bin\test.txt"
$text | out-file "bin\test.txt"
$text > "bin\test.txt"
$text >> "bin\test.txt"
$text | export-csv -path "bin\test.csv" -notypeinformation #doesn't work so well on a plain string since the only attribute is length... which will explain the output being confusing

#read from a file
get-content "bin\test.txt" | echo
import-csv "bin\test.csv" | echo
