/**
 * Graphics
 **/

drawdot (5, 5, 255) %drawdot (x1,y1,c1)
drawbox (10, 10, 20, 20, 255) %drawbox (x1,y1,x2,y2,c1)
drawfillbox (10, 30, 20, 60, 10) %drawfillbox (x1,y1,x2,y2,c1)

drawoval (50, 50, 10, 20, 10) %drawfilloval (x,y,xRadius,yRadius,c1)
drawfilloval (50, 50, 5, 10, 255) %drawfilloval (x,y,xRadius,yRadius,c1)


var x : array 1 .. 5 of int := init (10, 50, 75, 80, 100)
var y : array 1 .. 5 of int := init (80, 150, 70, 80, 100)
drawpolygon (x, y, 5, 10) %drawpolygon(xArray,yArray,numberOfSides,c1)

