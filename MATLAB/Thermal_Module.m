%-------------------------------------------------------------------------%
%                   Heat transfer module
%-------------------------------------------------------------------------%

function [OBJ] = Thermal_Module(a,b,t1,k1,As,h,tf,num_s,hSize,hLoad,hLoc)

a = double(a); % thermal plane X dimension
b = double(b); % thermal plane Y dimension
t1 = double(t1); % thickness of heat spreader
k1 = double(k1); % thermal conductivity of heat spreader
As = double(As); % Area heat source
h = double(h); % convective heat transfer coefficient
tf = double(tf); % temperature of fluid
numSources = double(num_s);
hSize = double(hSize); % list of heat source's sizes
hLoad = double(hLoad); % list of heat source's Load
hLoc;
res = 11;
z = 0;

T = zeros(numSources,1);





for source = 1:numSources
    c = hSize(source,1); % heat source x dimension
    d = hSize(source,2); % heat source y dimension
    xc = hLoc(source,1); % heat source centroid x
    yc = hLoc(source,2); % heat source centroid y
    Q = hLoad(source); % Watts for heat source
    
    A0 = Q/(a*b)*(t1/k1 + 1/h);
    % B0 = - Q/(k1*a*b);
    T = T + A0;% + B0*z;

    for i = 1:numSources
        x = hLoc(i,1);
        y = hLoc(i,2);
        for m = 1:res
            lambda = m*pi/a;
            [A1, B1] = calcA1B1(Q, xc, c, lambda, a, b, k1, h , t1);
            T(i) = T(i) + cos(lambda*x)*(A1*cosh(lambda*z)+B1*sinh(lambda*z));
        end

        for n=1:res
            delta = n*pi/b;
            [A2, B2] = calcA2B2(Q, yc, d, delta, a, b, k1, h , t1);
            T(i) = T(i) + cos(delta*y)*(A2*cosh(delta*z) + B2*sinh(delta*z));
        end

        for m=1:res
            lambda = m*pi/a;
           for n=1:res
               delta = n*pi/b;
               beta = sqrt(lambda^2 + delta^2);
               [A3, B3] = calcA3B3(Q, lambda, xc, c, delta, yc, d, a, b, k1, beta, h , t1);
               T(i) = T(i) + cos(lambda*x)*cos(delta*y)*(A3*cosh(beta*z) + B3*sinh(beta*z));
           end
        end
    end
end

OBJ = T+tf;

end

function [phi] = PHI(zeta, h, t1, k1)
    phi = ( zeta*sinh(zeta*t1)+h/k1*cosh(zeta*t1) ) / ( zeta*cosh(zeta*t1)+h/k1*sinh(zeta*t1) );
end

function [A1, B1] = calcA1B1(Q, xc, c, lambda, a, b, k1, h , t1)
    A1 = 2*Q*(sin((2*xc + c)/2*lambda) - sin((2*xc-c)/2*lambda)) / (a*b*c*k1*lambda^2*PHI(lambda, h , t1, k1));
    B1 = - A1*PHI(lambda, h , t1, k1);
end

function [A2, B2] = calcA2B2(Q, yc, d, delta, a, b, k1, h , t1)
    A2 = 2*Q*(sin((2*yc + d)/2*delta) - sin((2*yc-d)/2*delta)) / (a*b*d*k1*delta^2*PHI(delta, h , t1, k1));
    B2 = - A2*PHI(delta, h , t1, k1);
end

function [A3, B3] = calcA3B3(Q, lambda, xc, c, delta, yc, d, a, b, k1, beta, h , t1)
    A3 = 16*Q*cos(lambda*xc)*sin(0.5*lambda*c)*cos(delta*yc)*sin(1/2*delta*d)/ (a*b*c*d*k1*beta*lambda*delta*PHI(beta, h , t1, k1));
    B3 = - A3*PHI(beta, h , t1, k1);
end
