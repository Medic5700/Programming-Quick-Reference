<#
Author: Medic5700

A simple program that displays the powers of 2.
#>

#uses the Math function Pow (since ** or ^ doesn't do it)
for ($i = 1;$i -le 20;$i++){
    ("2`^" + $i + "`t=`t" + ([Math]::Pow(2,$i)))
}