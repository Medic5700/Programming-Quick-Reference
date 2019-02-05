import GUI
View.Set ("graphics:640;465,nobuttonbar,title:Text Colours")
colorback (10)
cls
for c : 0 .. 100
    color (c)
    put c, "   " ..
    delay (5)
end for
put ""
colorback (0)
for c : 101 .. 255
    color (c)
    put c, "       " ..
    delay (5)
end for

put ""
put "This is text colours from 0-255!" ..
put "Press any key to exit ..."
var ch : char := getchar