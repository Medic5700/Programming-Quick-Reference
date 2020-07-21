#primitives
$var_int = [int] 10
$var_float = [float] 20.5
$var_string = [string] "string"
$var_bool = [bool] $false # $true

$temp = [string]$var_int #casting

#arrays
$var_array = @("a","b","c","d","e")
$var_array = $var_array + "f" #this allows for simple appending to an array
for ($i=0; $i -lt 6; $i++){
    echo $var_array[$i]
}


# http://technet.microsoft.com/en-us/library/ee692803.aspx
$var_hashtable = @{"a" = 1;"b" = 2} #create a hash table
$var_hashtable.Add("c",3) #add entry
$var_hashtable.remove("a")
#accessing a hash table
echo $var_hashtable["b"]
$var_hashtable.GetEnumerator() | foreach {
    echo $_
}
echo $var_hashtable.ContainsKey("b")
echo $var_hashtable.ContainsValue(2)
