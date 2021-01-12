clear;clc;close all;

t=[-1:0.0001:1];%1 second

omega1=3;
omega2=3;
lambda1=0;
lambda2=pi/2;
phi1=omega1*t+lambda1;
phi2=omega2*t+lambda2;

X1=sin(phi1);
X2=sin(phi2);
subplot(2,1,1);
plot(t,X1);
hold on;
plot(t,X2);
hold off;
grid on;
xlabel('time');
ylabel('x1(t), x2(t)');

subplot(2,1,2);
plot(t,phi1);
hold on;
plot(t,phi2);
hold off;
grid on;
xlabel('time');
ylabel('phi1(t), phi2(t)');
tick=[-3*pi:pi/2:3*pi];
yticks([-pi pi/2 0 pi/2 pi]);
%bolding x=0,y=0
origin_x=zeros(1,length(t));
hold on;
plot (t,origin_x,'LineWidth',2);
plot (origin_x,[-6:0.0006:6],'LineWidth',2);
axis([-1 1 -6 6]);
