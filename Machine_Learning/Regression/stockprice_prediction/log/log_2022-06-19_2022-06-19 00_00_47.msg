Error in loadNamespace(x) : there is no package called ‘outlieR’

Traceback:
10: stop(cond)
9: doWithOneRestart(return(expr), restart)
8: withOneRestart(expr, restarts[[1L]])
7: withRestarts(stop(cond), retry_loadNamespace = function() NULL)
6: loadNamespace(x)
5: data %>% outlieR::impute(flag = NULL, fill = "mean", level = 0.1, 
       nmax = NULL, side = NULL, crit = "lof", k = 5, metric = "euclidean", 
       q = 3) at preprocess_data.r#8
4: eval(ei, envir)
3: eval(ei, envir)
2: withVisible(eval(ei, envir))
1: source("scripts/preprocess_data.r")

