disp('hello world')

%import an image
A = importdata('test.png');
image(A); %this image would be shown, except the next show image overwrites the display for it?

B = A + 250;
image(B); %display this image (surpress does not surpress showing it)

%some string stuff?
C = 'Hello World';
C = [C, ' it is a new day'];
C

%2D plots
x = 0:pi/100:2*pi;
y = sin(x);
plot(x,y)
hold on %allows surperimposing multiple functions to the same plot
y2 = cos(x);
plot(x,y2,'r--')
%note: to label it, the labels must go AFTER the plotting
xlabel('x');
ylabel('sin(x)');
title('Plot of the sine function');
legend('sin','cos');

