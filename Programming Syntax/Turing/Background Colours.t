import GUI
View.Set ("graphics:800;450,nobuttonbar,title:Background Colours")
var font1:=Font.New("times new roman:10")

for c : 0 .. 100
    colorback (c)
    put c, "   " ..
    delay (5)
end for
put ""
for c : 101 .. 255
    colorback (c)
    put c, "       " ..
    delay (5)
end for
colorback (0)
put ""
put "This is background colours from 0-255! " ..
put "Press any key to exit ..."
var ch : char := getchar
