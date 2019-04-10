# Azure Machine Learning service による R 機械学習パイプライン

本チュートリアルでは、Azure Machine Learning service Python SDK を利用して、Rでの機械学習を実行します。現状 Azure Machine Learning service は Python環境のみをサポートしていますが、内部で [reticulate] (https://rstudio.github.io/reticulate/) というパッケージを使用しています。


## コンテンツ ###

### [1. リモート環境でのモデル学習](./Training)  
- リモート環境(Machine Learnning Compute)で R のモデル学習を実施 

### [2. ハイパーパラメータのチューニング 設定](./Hyperparameter-Tuning)  
- リモート環境(Machine Learnning Compute)で R のモデル学習を実施 
- ハイパーパラメータのチューニングを並列処理を高速実行