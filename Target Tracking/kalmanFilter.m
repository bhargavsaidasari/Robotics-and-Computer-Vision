function [ predictx, predicty, state, param ] = kalmanFilter( t, x, y, state, param, previous_t )
%UNTITLED Summary of this function goes here
%   Four dimensional state: position_x, position_y, velocity_x, velocity_y

    %% Place parameters like covarainces, etc. here:
    % P = eye(4)
    % R = eye(2)

    % Check if the first time running this function
    if previous_t<0
        state = [x, y, 0, 0];
        param.P = 0.1 * eye(4);
        predictx = x;
        predicty = y;
        return;
    end
    dt=t-previous_t;
    z=[x;y];
    %%
    %State Matrix
    A=[1 0 0 dt;0 1 0 dt;0 0 1 0;0 0 0 1];
    C=[1 0 0 0;0 1 0 0];
    %%
    %Covariance MArices
    covariance_state=[dt*dt/4 0 dt/2 0;0 dt*dt/4 0 dt/2; 0 0 dt/2 0;0 0 0 dt/2];
    covariance_process=[0.01 0;0 0.01];
    R=covariance_process;
   
    %%
    %time update
    state=state';
    state_update=A*state;
    P=A*param.P*(A')+covariance_state;
    Gain=P*C'/(R+C*P*C');
    
    %%
    %measurement update
    filtered_state=state_update+Gain*(z-C*state_update);
    param.P=P-Gain*C*P;
    state=filtered_state';
    predictx=state(1)+state(3)*dt;
    predicty=state(2)+state(4)*dt;
    
    %% TODO: Add Kalman filter updates
    % As an example, here is a Naive estimate without a Kalman filter
    % You should replace this code
   
end
