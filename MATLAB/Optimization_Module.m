%-------------------------------------------------------------------------%
%                Optimization Module for different algorthm
%-------------------------------------------------------------------------%
function [X,Fval] = Optimization_Module(generation,x0,numVars,option)
format long % Just for checking...

%% Multi objective optimization implementation
LB = zeros(numVars,1);
UB = ones(numVars,1);
generation = double(generation); %fixes issue with generation format
tic
if option==1 %% Multi-objective optimization using weighted sums
    % EVALUATE ORIGINAL OBJECTIVES (_OPT_EVAL)
	for i =1:generation
	    p.alpha = (i-1)/(generation-1);
	    options = optimset('Display', 'none', 'MaxIter', 10, 'GradObj','on'); %Added gradient specification here
	    [X(i,:), Fval(i)] = fmincon(@(x)eval_pipe_1(x,p),x0,[],[],[],[],LB,UB,[],options);
    end
elseif option==2 %% Multi-objective optimization using GA multiobj
		mogaOptions = gaoptimset('Display', 'iter', 'Generations', 20, 'PopulationSize', 100);
		[X, Fval] = gamultiobj(@(x)eval_pipe_2(x),double(numVars),[],[],[],[],LB,UB,[],mogaOptions);
elseif option==3 %% Multi-objective optimization using Sequential Hybrid Method
    for i = 1:generation
        p.alpha - (i-1)/(generation-1);
        mogaOptions = gaoptimset('Display', 'iter', 'Generations', 20, 'PopulationSize', 100);
		[X, ~] = ga(@(x)eval_pipe_3(x),double(numVars),[],[],[],[],LB,UB,[],mogaOptions);

        options = optimset('Display', 'Iter', 'MaxIter', 10, 'GradObj'i,'on'); %Added gradient specification here
	    [X(i,:), Fval(i)] = fmincon(@(x)eval_pipe_1(x,p),X,[],[],[],[],LB,UB,[],options);
    end
end
toc
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
        OBJ= Res;
    end

end



function [OBJ, GRAD] = eval_pipe_1(x,p)
	% using for fmincon only
    % send the structure through pipe 
    pipe_id='test1_x';
    ret_id='test1_ret';
    X = [p.alpha, x]; % Data structure to send
    % DANNY EDIT - need to add alpha here to pass back to python
    success=py.send_x.send_x(mat2str(X) ,pipe_id);
    Res=[];
    if success==1
        data=py.receive_x.read_ret(ret_id);
        for i = 1:length(data)-1
            Res=[Res,str2num(char(data{i}))];
        end
        % Res is [F(x), gradF(x)]
        OBJ = Res(1);
        GRAD = Res(2:end);
    end

end

