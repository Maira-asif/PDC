PDC  -  Parallel and Distributed Computing

This repository contains examples demonstrating both process-based and thread-based execution in Python.

Folder Structure

CHAPTER 1

- CHAPTER 1/normal_sum.py → Normal (single-thread) sum example  
- CHAPTER 1/threaded_sum.py → Thread-based sum example  
- CHAPTER 1/screenshots/ → Screenshots of Chapter 1 code execution  

CHAPTER 2
This chapter includes examples showing thread synchronization using different techniques:

- CHAPTER 2/condition_sum.py → Uses Condition for thread coordination  
- CHAPTER 2/lock_sum.py → Uses Lock to prevent race conditions  
- CHAPTER 2/rlock_sum.py → Uses RLock (re-entrant lock) for nested locking situations  
- CHAPTER 2/semaphore_sum.py → Uses Semaphore to limit concurrent access  
- CHAPTER 2/screenshots/ → Screenshots of Chapter 2 code execution  

Description

Both chapters calculate the sum of a large array (1 to 1,000,000).  

- Chapter 1 demonstrates the basic comparison between normal (single-threaded) and threaded execution.  
- Chapter 2 introduces synchronization concepts in multi-threading, ensuring safe and coordinated thread operations.  

Screenshots

Chapter 1  

| Normal Sum | Threaded Sum |
|-------------|--------------|
| ![Normal Output](CHAPTER%201/screenshots/normal_output.png) | ![Threaded Output](CHAPTER%201/screenshots/threaded_output.png) |

Chapter 2  
| Condition | Lock | RLock | Semaphore |

| ![Condition Output](CHAPTER%202/screenshots/condition_output.png) | ![Lock Output](CHAPTER%202/screenshots/lock_output.png) | ![RLock Output](CHAPTER%202/screenshots/rlock_output.png) | ![Semaphore Output](CHAPTER%202/screenshots/semaphore_output.png) |

Repository Link  
👉 View on GitHub: [https://github.com/maira-asif70/PDC](https://github.com/maira-asif70/PDC)

Technologies Used  

- Python 3.x  
- threading and time modules  

Author  
Maira Asif  
Parallel and Distributed Computing  
