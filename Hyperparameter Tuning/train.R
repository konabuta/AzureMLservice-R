#library(caret)
library(reticulate)

azureml_core = import("azureml.core")
run = azureml_core$Run$get_context()
run$log("test", 1)

print(c("runid",run$id))

args1 = commandArgs(trailingOnly=TRUE)[1]
args2 = commandArgs(trailingOnly=TRUE)[2]

args1 = as.numeric(args1)
args2 = as.numeric(args2)

args1*args2
run$log("AUC", args1*args2)
run$'_client'$flush()
