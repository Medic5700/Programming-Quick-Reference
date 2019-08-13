%import GUI
import GUI
%"position:50;50," detemins where the window will open, relitive to bottom left
%"graphics:200;50" determines size of window
%"nobutonbar" makes buttons at top disaper
%title:___ gives title to run window
View.Set ("position:250;250,graphics:600;400,nobuttonbar,title:GUI Training,")
%------------------------------------------------------------------------------

%color sets colour of text (0-255)
color (48)
%colorback sets colour of background (0-255)
colorback (255)
%clears the screen so backgroung is all the same colour
cls
%------------------------------------------------------------------------------

for : 0 .. 50
    put "cool dude"
    delay (25)
end for

%Changes apperence of screen, or window settings,using it clears screen
%"text" causes a scrol bar to be active
setscreen ("text")

for : 0 .. 50
    put "cool dude"
    delay (25)
end for
%this Counter-acts "text" and sets it to graphics
setscreen ("graphics")
%------------------------------------------------------------------------------

%Allows stuff to be draw of screen
View.Set ("offscreenonly")

for x : 1 .. 500
    drawfilloval (x, 250, 50, 50, 255)
    drawfilloval (x, 250, 45, 45, 14)
end for
%This updates the screen to what has been drawn
View.Update
%this counter-acts "offscreenonly"
View.Set ("nooffscreenonly")
%this is without the drawoffscreen
delay (2000)
for x : 1 .. 500
    drawfilloval (x, 250, 50, 50, 255)
    drawfilloval (x, 250, 45, 45, 14)
end for
%------------------------------------------------------------------------------

