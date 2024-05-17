# Interactive apps


## Available apps

  - [Accelerated visualization](accelerated-visualization.md)
  - [Desktop](desktop.md)
  - [Jupyter](jupyter.md)
  - [Julia on Jupyter](julia-on-jupyter.md)
  - [Jupyter for courses](jupyter-for-courses.md)
  - [MATLAB](matlab.md)
  - [MLflow](mlflow.md)
  - [RStudio](rstudio.md)
  - [TensorBoard](tensorboard.md)
  - [Visual Studio Code](vscode.md)


## Launching an interactive app

1. The interactive apps can be found in the navigation bar under _Apps_, or on
   _My Interactive Sessions_ page.
2. To launch an app on a compute node, select it from the menu. 
3. After selecting an interactive app from the list you will be presented with
   a form to configure the session.
    1. Fill in appropriate billing project, partition, resources and
       app-specific settings.
4. After submitting the app form, and the Slurm job for the app has finished
   queuing, the app will be started and you will be able to connect to the
   application on the _My Interactive Sessions_ page (see below).

![Interactive sessions](../../img/ood-interactive-sessions.png)

!!! warning "Avoid idle interactive sessions"
    Note that apps keep running and consuming resources even if you close the
    browser tab for the app session. To stop the app, you can cancel the
    session from the _My Interactive Sessions_ page.
