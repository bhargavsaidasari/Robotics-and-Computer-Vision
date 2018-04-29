function [C, R] = LinearPnP(X, x, K)
%% LinearPnP
% Getting pose from 2D-3D correspondences
% Inputs:
%     X - size (N x 3) matrix of 3D points
%     x - size (N x 2) matrix of 2D points whose rows correspond with X
%     K - size (3 x 3) camera calibration (intrinsics) matrix
% Outputs:
%     C - size (3 x 1) pose transation
%     R - size (3 x 1) pose rotation
%
% IMPORTANT NOTE: While theoretically you can use the x directly when solving
% for the P = [R t] matrix then use the K matrix to correct the error, this is
% more numeically unstable, and thus it is better to calibrate the x values
% before the computation of P then extract R and t directly
%Calibrate x values
pr=[1 0 0;0 1 0];
[N,~]=size(x);
x=(pr*(K\[x';ones(1,N)]))';
A=zeros(2*N,12);

for i=1:N
    A(i*2-1,1:4)= zeros(1,4);
    A(i*2-1,5:8)= -1*[X(i,:) 1];
    A(i*2-1,9:12)= x(i,2)*[X(i,:) 1];
     A(i*2,1:4) = [X(i,:) 1];
    A(i*2,5:8) = zeros(1,4);
    A(i*2,9:12)= -1*x(i,1)*[X(i,:) 1];
end

[~,~,V]=svd(A);

p = V(:,12);

P = [transpose(p(1:4,:)) ; transpose(p(5:8,:)) ; transpose(p(9:12,:))];

R_b = P(1:3,1:3);

[U2,S2,V2] = svd(R_b);

if det(U2*(V2.'))>0
    R =  U2*transpose(V2);
    t = P(:,4)/S2(1,1);
    C = -1* R.' * t;
end

if det(U2*(V2.'))<0
    R = -1* U2* transpose(V2);
    t = -1* P(:,4)/S2(1,1);
    C = -1* R.' * t;
end

end






