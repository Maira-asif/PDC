# PDC - Parallel and Distributed Computing

This repository contains examples demonstrating **process-based, thread-based, and MPI-based execution** in Python.

## Folder Structure & Chapters

### CHAPTER 1 — Parallel Programming Basics (Threads & Processes)

- **CHAPTER 1/normal_sum.py** → Normal (single-thread) sum example  
- **CHAPTER 1/threaded_sum.py** → Thread-based sum example  
- **CHAPTER 1/screenshots/** → Screenshots of Chapter 1 code execution  

### CHAPTER 2 — Thread Synchronization

Demonstrates thread synchronization techniques:

- **CHAPTER 2/condition_sum.py** → Uses Condition for thread coordination  
- **CHAPTER 2/lock_sum.py** → Uses Lock to prevent race conditions  
- **CHAPTER 2/rlock_sum.py** → Uses RLock (re-entrant lock) for nested locking situations  
- **CHAPTER 2/semaphore_sum.py** → Uses Semaphore to limit concurrent access  
- **CHAPTER 2/screenshots/** → Screenshots of Chapter 2 code execution  

### CHAPTER 3 — Parallel Programming with Processes

Introduces process-based parallelism and synchronization:

| # | Topic | File Names |
|---|-------|------------|
| 1 | Normal Sum (Single Process) | `normal_sum.py` |
| 2 | Threaded Sum (Multi-threading) | `threaded_sum.py` |
| 3 | Killing Process | `killing_process.py` |
| 4 | Naming Processes | `name_process.py` |
| 5 | Process Pool | `process_pool.py` |
| 6 | Barrier Synchronization | `barrier.py` |
| 7 | Run Background Processes | `background_process.py` |
| 8 | No Daemon Example | `no_daemon.py` |
| 9 | Spawning Processes | `spawning_process.py` |

### CHAPTER 4 — MPI (Message Passing Interface) Basics

Introduces process communication using `mpi4py`:

| # | Topic | File Names |
|---|-------|------------|
| 1 | Hello World | `helloworld_MPI.py` |
| 2 | Point-to-Point Communication | `pointToPointCommunication.py` |
| 3 | Broadcast | `broadcast.py` |
| 4 | Scatter | `scatter.py` |
| 5 | Gather | `gather.py` |
| 6 | All-to-All Communication | `alltoall.py` |
| 7 | Reduction (Sum Example) | `reduction.py` |
| 8 | Virtual Topology (1D Cartesian) | `virtualTopology.py` |
| 9 | Deadlock Problems | `deadLockProblems.py` |

## 📌 Description

- **Chapters 1 & 2**: Focus on **threads**, showing performance improvement and thread synchronization.  
- **Chapter 3**: Focus on **process-based parallelism**, process pools, barriers, and background processes.  
- **Chapter 4**: Focus on **distributed computing with MPI**, including communication, reduction, and virtual topologies.

All chapters aim to make parallel and distributed concepts easy to understand through small, clear examples.

## ⚡ Requirements

- Python 3.x  
- `threading`, `multiprocessing`, `time`, and `mpi4py` libraries (`pip install mpi4py`)  

Author  
Maira Asif  
Parallel and Distributed Computing  
