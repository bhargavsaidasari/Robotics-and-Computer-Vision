function X = LinearTriangulation(K, C1, R1, C2, R2, x1, x2)
%% LinearTriangulation
% Find 3D positions of the point correspondences using the relative
% position of one camera from another
% Inputs:
%     C1 - size (3 x 1) translation of the first camera pose
%     R1 - size (3 x 3) rotation of the first camera pose
%     C2 - size (3 x 1) translation of the second camera
%     R2 - size (3 x 3) rotation of the second camera pose
%     x1 - size (N x 2) matrix of points in image 1
%     x2 - size (N x 2) matrix of points in image 2, each row corresponding
%       to x1
% Outputs: 
%     X - size (N x 3) matrix whos rows represent the 3D triangulated
%       points
%Camera Matrices
P1=K*[R1 C1];
P2=K*[R2 C2];
N=size(x1,1);
X=zeros(N,3);

for i=1:size(x1,1)
    x1_current=[x1(i,:) 1]';
    x2_current=[x2(i,:) 1]';
    skew1=Vec2Skew(x1_current);
    skew2=Vec2Skew(x2_current);
    A=[skew1*K*[R1 -R1*C1];skew2*K*[R2 -R2*C2]];
    [u,d,v]=svd(A);
    X_temp=v(:,end)/v(end,end);
    X(i,:)=X_temp(1:3);
end


