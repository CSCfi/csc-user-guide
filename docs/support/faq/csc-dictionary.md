# HPC dictionary

## 1. Core HPC Concepts

### High‑Performance Computing (HPC)

HPC refers to using supercomputers built from many interconnected compute nodes
to run large or complex computations much faster than a normal workstation. CSC
provides HPC systems such as Puhti, Mahti and LUMI for simulations, modelling,
data analysis, and AI.

### Supercomputer

A supercomputer is a collection of high‑performance compute nodes connected
with a fast interconnect and shared filesystems. CSC supercomputers provide
advanced computing power, memory, and storage to handle intensive scientific
workloads.

### Parallel Computing

Parallel computing breaks a problem into smaller tasks processed simultaneously
on multiple CPU cores or GPUs. HPC systems use both shared‑memory (OpenMP)
and distributed‑memory (MPI) parallelism to achieve scaling.

### Compute Node

A compute node is an individual server inside a supercomputer. Nodes include
multiple CPU cores, memory, and sometimes GPUs or NVMe local storage. Different
node types are optimized for different workloads.

### CPU Computing

CPU computing relies on general‑purpose processors suitable for a broad range
of simulations, analyses, and numerical tasks. Systems like Mahti provide many
high‑core‑count CPU nodes for parallel computation.

### GPU Computing

GPU computing uses massively parallel accelerators ideal for deep learning,
data analytics, and certain scientific simulations. CSC systems offer Nvidia
GPUs in Puhti and Mahti, while LUMI uses AMD MI250X GPUs.

### Accelerated Computing

Accelerated computing refers to using specialized hardware (e.g., GPUs) to
speed up workloads that benefit from parallelism. LUMI‑G is specifically
optimized for GPU‑accelerated workloads at very large scales.

### Hybrid HPC (CPU + GPU)

Many modern workloads run partly on the CPU and partly on GPUs. Hybrid
architectures improve performance for deep learning, molecular dynamics and
complex simulations.

## 2. Parallel Programming Concepts

### Distributed‑Memory Parallelism (MPI)

MPI enables programs to run across multiple nodes by exchanging messages
between processes. It is essential for large simulations on Mahti and LUMI.

### Shared‑Memory Parallelism (OpenMP)

Shared‑memory parallelism uses threads within a single node to parallelize
work. It is well suited for moderate parallelism that does not require multiple
nodes.

### Hybrid Parallelization

Combines MPI between nodes and OpenMP threads within each node. This is often
the best way to use multi‑core nodes efficiently on Mahti and LUMI.

### Embarrassingly Parallel Workloads

Workloads where tasks do not depend on one another and can run independently.
These run efficiently on HPC systems using job arrays or HTC‑style execution.

### Scalability

The ability of a workload to benefit from additional compute resources. Mahti
is optimized for workloads that scale to many cores or nodes.

## 3. HPC Job Execution Concepts

### Batch Job

A non‑interactive job submitted to the scheduler using a Slurm script. It
specifies resources (cores, memory, time) and runs automatically when resources
become available.

### Interactive Session

A session on a compute node that allows immediate execution of commands. Useful
for development, debugging, data exploration, or using notebooks.

### Job Queue

A waiting system where jobs are queued until required resources become
available. The scheduler prioritizes jobs based on policies, reservations, and
resource demand.

### Slurm Scheduler

Slurm is the workload manager used on all CSC HPC systems. It handles job
submission, queuing, resource allocation, and accounting.

### Job Array

A Slurm feature allowing the submission of many similar jobs simultaneously.
Ideal for embarrassingly parallel workloads.

### Resource Allocation

Requesting CPU cores, GPUs, memory, storage, or time when submitting a job.
Efficient resource allocation improves queueing efficiency.

## 4. Storage & Data Concepts

### Allas Object Storage

A general‑purpose cloud‑based research data storage service accessible from
CSC HPC systems and externally. Ideal for large datasets and data sharing.

### Scratch Storage

Temporary high‑performance filesystem for running jobs. Ideal for large
intermediate files, but not intended for long‑term storage.

### Local NVMe Storage

Some nodes (e.g., certain Puhti and Mahti nodes) contain extremely fast local
SSD storage. Great for I/O‑heavy workflows such as genomics or ML
preprocessing.

### High-Speed Interconnect

A low‑latency network connecting compute nodes in a cluster, crucial for MPI
performance. CSC supercomputers use advanced fabrics to support large‑scale
parallel workloads.

### Data Management Workflow

HPC workflows separate data into temporary scratch, long‑term object storage
(Allas), and local project directories for efficient handling of large datasets.

## 5. Software & Environment Concepts

### Environment Modules

Modules configure compilers, libraries, and software environments. They make it
easy to switch between different versions of software stacks on CSC systems.

### HPC Libraries

Optimized math and communication libraries (e.g., BLAS, FFTW, ScaLAPACK)
provide high‑performance numerical operations. CSC supplies several optimized
versions adapted for Puhti and Mahti.

### Compiler Toolchains

CSC offers multiple compiler suites (e.g., GCC, Intel OneAPI). Toolchains
influence performance and must be compatible with linked libraries.

### Containers in HPC

Containers provide isolated software environments for complex workflows. CSC
supports containers through Singularity/Apptainer in HPC and Docker in cloud
(Pouta).

### Python in HPC

CSC provides optimized Python environments and guidance for effective Python
usage on Puhti and Mahti, including virtual environments and HPC‑friendly
libraries.

## 6. Performance Concepts

### Profiling

Profiling examines how a program uses CPU time, memory, or I/O. Helps optimize
HPC code for better performance.
(General HPC concept; CSC recommends profiling in their guides.)

### Vectorization

A technique leveraging CPU vector instructions to perform multiple operations
at once. Modern CPUs like Xeon and EPYC use AVX to accelerate scientific
workloads.

### Load Balancing

Ensuring equal distribution of computational work across cores or nodes to
maximize performance. Critical for MPI workloads.

### Memory Bandwidth

The rate at which memory can feed data to the CPU/GPU. Many HPC workloads are
memory‑bound rather than CPU‑bounded.

## 7. CSC‑Specific HPC Operational Concepts

### CSC Project

A project is required to access CSC computing, storage, and cloud resources.
Projects define resource quotas, user membership, and billing units.

### Billing Units (BUs)

A unit measuring how much computational work a user or project consumes. Usage
is calculated per CPU/GPU hour and storage consumption.

### Puhti

A versatile supercomputer with many applications, significant GPU capacity, and
NVMe-enabled nodes. Recommended for new users and general workloads.

### Mahti

A massively parallel supercomputer optimized for large-scale CPU simulations.
Suitable for scalable MPI applications.

### LUMI

One of the world's fastest supercomputers, optimized for GPU‑accelerated
workloads and advanced simulations at extreme scale. Located in CSC's Kajaani
datacenter.

### Roihu (coming 2026)

Roihu will replace Puhti and Mahti, providing next‑generation HPC
capabilities with significantly increased performance.

### Open OnDemand (OOD)

A web‑based interface for accessing CSC supercomputers. Provides file
browsing, job submission, terminal access, and interactive applications.

## 8. Workflow & Research Computing Concepts

### Simulation Workflow

A typical HPC simulation workflow consists of pre‑processing (data
preparation), computation (running jobs), and post‑processing
(analysis/visualization). HPC environments streamline this process.

### Machine Learning in HPC

HPC supports ML by providing large GPU partitions, scalable batch training, and
fast local storage for datasets. LUMI‑G is specifically optimized for
GPU‑based ML workloads.

### Data Analytics in HPC

Large datasets can be processed efficiently using distributed computing and GPU
acceleration. CSC supports analytics workflows through HPC, Allas, and Pouta.

### Cloud + HPC Hybrid Workflows

CSC's Pouta cloud allows custom environments, while HPC systems execute heavy
computation. Together they support complete pipelines from web services to
simulations.
