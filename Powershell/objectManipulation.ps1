$data = ls

echo "get-member==============================================================="
$data | get-member #lists all the attributes of object(s) that it's passed

echo "select==================================================================="
$data | select Mode, Length, Name | get-member #"select" selects which attributes you want to keep/pass through

echo "add elements 1==========================================================="
$data | select Mode, Name, @{N="LengthKB";E={($_.length)/1024}}
#the @{N="NameOfNewAttribute";E={}} adds a new attribute called N, set to E (the $_ allows you to access the object being passed through, for processing something)
#ex: creates a new attribute "LengthKB" that is the size of the file in kilobytes

echo "create an object========================================================="
$temp = New-Object System.Object
$temp | Add-Member -type NoteProperty -name AttributeName -value ("some value") #the verbose way
$temp | Add-Member NoteProperty "Second Attribute" 5
echo $temp

