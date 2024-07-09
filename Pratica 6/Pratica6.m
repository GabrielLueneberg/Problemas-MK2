function p6 ( seq )

N = 39; % 2 ultimos algarismos do numero USP
theta_f = (-1) * ((90 + N) / 4) * (pi / 180); % angulo de rotacao (rad)
dtheta = (-1) * (pi / 500); % passo

if seq == 1
    % 1 a sequencia [ z (theta) -> y (theta) -> x (4 * theta) ]
    theta = [0:2 * dtheta:theta_f];
    thetaxv = [0 * theta 0 * theta 4 * theta];
    thetayv = [0 * theta theta theta(end) + 0 * theta];
    thetazv = [theta theta(end) + 0 * theta theta(end) + 0 * theta];
else
    % 2 a sequencia [ simultaneamente ]
    theta = [0:0.5 * dtheta:theta_f];
    thetaxv = [4 * theta];
    thetayv = [theta];
    thetazv = [theta];
end

for k = 1:length(thetayv)
    thetax = thetaxv(k); thetay = thetayv(k); thetaz = thetazv(k);
    Rx = [1 0 0; 0 cos(thetax) -sin(thetax); 0 sin(thetax) cos(thetax)];
    Ry = [cos(thetay) 0 sin(thetay); 0 1 0; -sin(thetay) 0 cos(thetay)];
    Rz = [cos(thetaz) -sin(thetaz) 0; sin(thetaz) cos(thetaz) 0; 0 0 1];
    R(:, :, k) = Rz * Ry * Rx;
end

fcnrot3d(R)