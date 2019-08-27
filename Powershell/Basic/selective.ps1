<# basics
-eq - equal to
-lt - less then
-gt - greater then
-ge - greater then or equal to
-le - less than of equal to
-ne - not equal to
! - not
-not - not
-and - and
-or - or
-xor - xor
-contains
-notcontains
#>

<#
-match - matches a regular expression
-cmatch - matches a regular expression case sensitive
#>

for ($i = 0;$i -lt 10; $i++){
    if ($i -eq 0){
        echo "if statment 0 option 0"
    }
    elseif ($i -eq 1){
        echo "if statment 0 option 1"
    }
    else{
        echo "if statment 0 option 2"
    }
}

for ($i = 0; $i -lt 4; $i++){
    switch ($i){
        (2-2) {echo "if statment 1 option 0"}
        1 {echo "if statment 1 option 1"}
        default {echo "if statment 1 option 2"}
    }
}

#other...?

#where goes through each element passed in, and passes it along if the element passes a condition
(0,1,2,3,4,5,6,7,8,9) | where { $_ -eq 2 } | echo #note: you can put anything in that where clause, as long as a $true or $false gets passed back
