# End-to-End-Machine-Learning-Project-with-ML-FLOW

## workflows

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py




### Dagshub credintials. 

import dagshub
dagshub.init(repo_owner='LokeshLokareddy', repo_name='End-to-End-Machine-Learning-Project-with-ML-FLOW', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)