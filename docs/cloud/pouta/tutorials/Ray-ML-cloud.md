# Ray: A Machine learning framework for cloud

## Introduction

As machine learning (ML) workloads grow in scale and complexity, efficiently utilizing compute resources becomes essential. Whether running on a single high-performance virtual machine (VM) or a cluster, managing distributed computation and parallel processing can be challenging.

Ray addresses these challenges by providing a unified framework that simplifies scaling ML workloads across CPUs, GPUs, and multi-node VM clusters.

## What is Ray

Ray is an open-source distributed computing framework built to simplify the scaling of Python and machine learning (ML) workloads. By using Ray, you can seamlessly run computations across multiple CPUs, GPUs, or virtual machines (VMs) — whether they’re on-premises or in the cloud.

Ray is developed by [Anyscale](https://www.anyscale.com/) and is becoming a popular choice for data scientists and ML engineers who want to scale training, tuning, and serving workloads without managing complex distributed infrastructure.

By running Ray on Pouta VMs, you can leverage scalable compute power while keeping your workflows flexible.

You can find more details from [here](https://docs.ray.io/en/latest/ray-overview)


## Ray framework

Ray framework consist of three layers: 

### Ray Core

[Ray Core](https://docs.ray.io/en/latest/ray-core/walkthrough.html) is the foundation of the Ray framework. It allows your Python programs to use all available processing power, whether you are working on a single VM or a cluster of multiple VMs. Instead of running tasks one after another, Ray Core can run many tasks at the same time. You can write a normal Python function, and Ray will handle the parallel execution automatically. This means you do not need to manually manage threads, processes, or cluster communication. If any task fails, Ray can retry it, keeping your program reliable. In short, Ray Core helps you use your hardware more efficiently and speeds up your work without requiring complex programming. 

### Ray AI Libraries

A set of open-source, Python, work-specific libraries are available at Ray. Every library is meant for specific task.

#### Ray Data

[Ray Data](https://docs.ray.io/en/latest/data/data.html) helps with preparing and processing large datasets before training. Instead of putting all the load on one machine, Ray Data divides the work across multiple CPU cores or multiple VMs, depending on what you have available. This means data can be loaded, cleaned, and transformed much more quickly. It also streams processed data directly into Ray Train during training so that the model doesn’t have to wait for data. This avoids bottlenecks and keeps training running smoothly and efficiently. Here are some [examples](https://docs.ray.io/en/latest/data/examples.html)

#### Ray Train

[Ray Train](https://docs.ray.io/en/latest/train/train.html) helps you train machine learning models faster by spreading the training workload across available CPUs and GPUs. Whether your setup is a single VM with multiple GPU cards or many VMs connected together, Ray Train can use all of those resources at once. It supports popular ML frameworks like PyTorch, TensorFlow, and XGBoost, so you do not need to change your existing model code. If a machine or GPU fails during training, Ray Train can pick up and continue without losing progress. This makes training large models faster, more stable, and easier to manage. Here are some [examples](https://docs.ray.io/en/latest/train/examples.html)

#### Ray Tune

[Ray Tune](https://docs.ray.io/en/latest/tune/index.html) makes hyperparameter tuning faster and more efficient. Ray Tune is designed to speed up the process of finding the best hyperparameters for machine learning models. Normally, tuning requires running many training experiments one at a time, which can take days. Ray Tune can run many experiments in parallel across all available CPU and GPU resources, whether on a single VM or across a cluster. It also automatically stops experiments that are performing poorly and focuses compute resources on the ones that are doing well. This helps reduce both time and cost while improving model accuracy. Here are some [examples](https://docs.ray.io/en/latest/tune/examples/index.html)

#### Ray Serve

[Ray Serve](https://docs.ray.io/en/latest/serve/index.html) makes it easy to deploy machine learning models so they can be used by real applications. Once your model is trained, Ray Serve allows you to expose it through a web API so that users or applications can send input and receive predictions. It can run on a single VM or scale to multiple VMs depending on the amount of traffic. If more requests come in, Ray Serve can automatically increase the number of model replicas and balance requests across them. This ensures your service remains fast and reliable in production environments. Here are some [examples](https://docs.ray.io/en/latest/serve/examples.html)

#### Ray RLlib

[Ray RLlib](https://docs.ray.io/en/latest/rllib/index.html) is focused on reinforcement learning. It accelerates the training of RL agents by running many different environment simulations at the same time. Instead of training slowly in a single environment, RLlib uses multiple CPUs and GPUs across one or more VMs to gather experience and learn faster. It supports many RL algorithms out of the box, so you can start quickly without building everything from scratch. This makes RLlib useful in areas like robotics, simulation-based control, and intelligent decision-making systems. Here are some [examples](https://docs.ray.io/en/latest/rllib/rllib-examples.html)

### Ray Clusters

A [Ray Cluster](https://docs.ray.io/en/latest/cluster/getting-started.html) is a group of one or more VMs that work together like a single large machine. In a Ray cluster, there are two types of nodes: a Head Node and one or more Worker Nodes. The head node manages the cluster, keeps track of resources (like CPUs, GPUs, and memory), and coordinates work tasks. The worker nodes do the actual computation. When you connect your Python program to the cluster, Ray automatically uses all available CPUs and GPUs across all machines. This means that if you add more VMs to the cluster, your programs, training jobs, and data processing tasks can scale up without changing your code. Ray takes care of communication, resource scheduling, and job execution internally. This makes Ray Clusters very useful for running machine learning, distributed data processing, or reinforcement learning tasks on Pouta environment.

## Ray Dashboard

[Ray Dashboard](https://docs.ray.io/en/latest/ray-observability/getting-started.html) is a simple web page that shows what Ray is doing. It helps you see how many CPUs and GPUs are being used, which tasks are running, and whether the system is working smoothly. This is helpful when using multiple VMs because you can easily understand the system’s activity without checking logs or terminals. 

You can see the dashboard by creating a SSH tunnel from your VM. If you are working on multiple VMs, you need to create tunnel form the head VM.

On VM, if you have started using Ray without connecting with dashboard, you need to first stop Ray and then start it with `include-dashbord` by commands: 

```bash
ray stop --force
ray start --head --include-dashboard true --dashboard-host 0.0.0.0

```
After this, you need to create ssh tunnel from your local machine by:

```bash
ssh -L 8265:localhost:8265 username@HEAD_VM_IP

```
Then open browser and go to 
```
http://localhost:8265

```

## How Ray help with Machine Learning on Pouta

Ray takes care of multiple challenges which can occur while running ML workload on multiple virtual machines like, managing distributed processes, synchronizing data across nodes, balancing compute loads and handling auto-scaling and fault tolerance. 

You can start with a single VM and scale to many without changing your code. Ray will automatically use available CPU/GPU resources across VMs. It can dynamically add or remove VMs based on current demand.

## How to use Ray on Pouta

You can install Ray on your VMs by:

```bash
pip install -U ray

```
More information about installation is available [here](https://docs.ray.io/en/latest/ray-overview/installation.html)

### On single VM

If you have single VM with multiple cores, for example, 6 CPU and 1 GPU, Ray can use al of them automatically. You need to install ray on that machine and you can use that directly in your python code. You can check the difference in time taken by a code when running normally (sequential processing) and when using Ray (parallel processing). 

When you are not using Ray, it will do sequential computation. Try this code
``` 
import time

def f(x):
    time.sleep(2)
    return x * x

start = time.time()
results = [f(i) for i in range(12)]  # 12 tasks
print(results)
print("Time taken:", time.time() - start)  

```
In this code, 2 second of sleep time is given for 12 tasks. So, it should take almost 24 seconds to complete.

Now, try following code:

```
import ray
import time

ray.init()  # Ray will detect and use all available cores

@ray.remote
def f(x):
    time.sleep(2)
    return x * x

start = time.time()
results = ray.get([f.remote(i) for i in range(12)])
print(results)
print("Time taken:", time.time() - start)

```
In this code, when you are initializing Ray, it will automatically distribute the tasks according to the available resources. If you have 6 CPU cores, It will reduce the time to almost 1/6. 

As you can see in both code, the only difference is that in the second code, after `import Ray`, a decorator `@ray.remote` is added and a function call is with `.remote()`. This tells Ray to run the function in parallel across many CPUs or GPUs. The logic inside the function does not need to change. Your program works the same way — the only extra step is that Ray takes care of distributing the work to available resources (like multiple CPU cores or multiple VMs). So instead of rewriting your whole code, you only make a small change in how you call functions. This is what makes Ray easy to use — you get faster performance and scalability with almost no code change.

### On multiple VMs

While working with multiple VMs, you need to set up a [Ray Cluster](https://docs.ray.io/en/latest/cluster/vms/user-guides/launching-clusters/on-premises.html#manual-setup-cluster). 

* First of all, install Ray on all the nodes

* On the head VM
```
ray start --head --port=6379
```
* The command will print out the Ray cluster address, which can be passed to `ray start` on other machines to start the worker nodes. 

``` 
ray start --address=<head-node-address:port>
```
* Now, you can use Ray in your python code. Ray will now spread work across all the VMs automatically.

```
import ray
import time

ray.init(address="auto")  # Ray will connect to the cluster

@ray.remote
def f(x):
    time.sleep(2)
    return x * x

start = time.time()
results = ray.get([f.remote(i) for i in range(12)])
print(results)
print("Time taken:", time.time() - start)

```

