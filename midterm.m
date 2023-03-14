clc , clear

% length of arms
l1 = 7;
l2 = 13;

% Path
X = [0 1 2 3 4 5 6 7 8 9 10 11 12 13];
Y = [20 15 12.5 12 12.5 12.6 12.7 12.8 12.7 12.6 12.5 12 12.5 12];

% Path Plot
scatter(X,Y)

% End-Effector Position
x = 1;
y = 15;

% Inverse Kinematics
l3 = ((x^2) + (y^2));

theta2 = pi - acos(((l3) - (l1^2) - (l2^2)) / (l1*l2*(-2)));
theta1 = atan(x/y) - atan((l2*sin(theta2))/(l1 + l2*cos(theta2)));

theta1 = rad2deg(theta1);
theta2 = rad2deg(theta2);
x0 = 0;
y0 = 0;
x1 = x0 + l1*cosd(theta1);
y1 = y0 + l1*sind(theta1);
x2 = x1 + l2*cosd(theta2+theta1);
y2 = y1 + l2*sind(theta2+theta1);

hold on
plot([y0 y1],[x0 x1])
plot([y1 y2],[x1 x2])
hold off
