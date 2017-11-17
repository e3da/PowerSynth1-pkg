%-------------------------------------------------------------------------%
%                Optimization Module for different algorthm
%-------------------------------------------------------------------------%
function [X,Fval] = Optimization_Module(generation,x0,numVars,option)
%% Multi objectie optimization implementation
LB = zeros(numVars,1);
UB = ones(numVars,1);
if option==1 %% Multi-objective optimization using weighted sums
	for i =1:generation 
	    p.alpha = (i-1)/generation;
	    options = optimset('Display', 'Iter', 'MaxIter', 10);
	    [X(i,:), Fval(i)] = fmincon(@(x)eval_pipe_1(x,p),x0,[],[],[],[],LB,UB,[],options);
    end
elseif option==2 %% Multi-objective optimization using GA multiobj 
		mogaOptions = gaoptimset('Display', 'iter', 'Generations', 50, 'PopulationSize', 50);
		[X, Fval] = gamultiobj(@(x)eval_pipe_2(x),double(numVars),[],[],[],[],LB,UB,[],mogaOptions);
elseif option==3 %% Multi-objective optimization using Sequential Hybrid Method
        

end

end



function [OBJ] = eval_pipe_2(x)
	% using for GA only
    % send the structure through pipe 
    pipe_id='test1_x';
    ret_id='test1_ret';
    success=py.send_x.send_x(mat2str(x),pipe_id);
    Res=[];
    if success==1
        data=py.receive_x.read_ret(ret_id);
        for i = 1:length(data)-1
            Res=[Res,str2num(char(data{i}))];
        end
        % Res is the list of evaluated results
        OBJ=Res;
    end

end



function [OBJ] = eval_pipe_1(x,p)
	% using for fmincon only
    % send the structure through pipe 
    pipe_id='test1_x';
    ret_id='test1_ret';
    success=py.send_x.send_x(mat2str(x),pipe_id);
    Res=[];
    if success==1
        data=py.receive_x.read_ret(ret_id);
        for i = 1:length(data)-1
            Res=[Res,str2num(char(data{i}))];
        end
        % Res is the list of evaluated results
        OBJ=0;
        alpha=p.alpha
        OBJ = double(alpha*Res(1) + (1-alpha)*Res(2));
    end

end

