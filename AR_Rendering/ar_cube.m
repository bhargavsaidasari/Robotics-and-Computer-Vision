function [proj_points, t, R] = ar_cube(H,render_points,K)
%% ar_cube
% Estimate your position and orientation with respect to a set of 4 points on the ground
% Inputs:
%    H - the computed homography from the corners in the image
%    render_points - size (N x 3) matrix of world points to project
%    K - size (3 x 3) calibration matrix for the camera
% Outputs: 
%    proj_points - size (N x 2) matrix of the projected points in pixel
%      coordinates
%    t - size (3 x 1) vector of the translation of the transformation
%    R - size (3 x 3) matrix of the rotation of the transformation
% Written by Stephen Phillips for the Coursera Robotics:Perception course

% YOUR CODE HERE: Extract the pose from the homography

% YOUR CODE HERE: Project the points using the pose
if H(3,3)<0
    H=-H;
end
h1=H(:,1);
h2=H(:,2);
h3=cross(h1,h2);
H1=[h1 h2 h3];
[U,~,V]=svd(H1);
R=U*[1 0 0;0 1 0;0 0 sign(det(U*V'))]*V';
t=H(:,3)/norm(h1);
render_points=[render_points ones(size(render_points,1),1)];
size(render_points)
proj_points=K*[R t]*render_points';
proj_points=proj_points./proj_points(3,:);
proj_points=proj_points(1:2,:);
proj_points=proj_points';
end