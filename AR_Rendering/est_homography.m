function [ H ] = est_homography(video_pts, logo_pts)
% est_homography estimates the homography to transform each of the
% video_pts into the logo_pts
% Inputs:
%     video_pts: a 4x2 matrix of corner points in the video
%     logo_pts: a 4x2 matrix of logo points that correspond to video_pts
% Outputs:
%     H: a 3x3 homography matrix such that logo_pts ~ H*video_pts
% Written for the University of Pennsylvania's Robotics:Perception course

% YOUR CODE HERE

Ax1=[-video_pts(:,1) -video_pts(:,2) -ones(4,1) zeros(4,1) zeros(4,1) zeros(4,1) video_pts(:,1).*logo_pts(:,1) video_pts(:,2).*logo_pts(:,1) logo_pts(:,1) ];
Ax2=[zeros(4,1) zeros(4,1) zeros(4,1) -video_pts(:,1) -video_pts(:,2) -ones(4,1) video_pts(:,1).*logo_pts(:,2) video_pts(:,2).*logo_pts(:,2) logo_pts(:,2)]; 
[nRowsA,nCols] = size(Ax1);
nRowsB = size(Ax2,1);

AB = zeros(nRowsA+nRowsB,nCols);
AB(1:2:end,:) = Ax1;
AB(2:2:end,:) = Ax2;
[~,~,v]=svd(AB);
H=reshape(v(:,end),3,3)';





