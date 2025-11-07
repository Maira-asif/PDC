
# 🧵 Chapter 2 — Thread Synchronization Techniques

This chapter demonstrates how to manage thread synchronization in Python using various locking mechanisms.  
It helps prevent **race conditions** and ensures safe access to shared data between threads.

---

## 📘 Topics Covered

| # | Technique | File Name | Description |
|---|------------|------------|--------------|
| 1 | Condition | `condition_sum.py` | Coordinates threads using `Condition` for wait/notify mechanism. |
| 2 | Lock | `lock_sum.py` | Uses a simple `Lock` to prevent race conditions. |
| 3 | RLock (Re-entrant Lock) | `rlock_sum.py` | Allows a thread to acquire the same lock multiple times. |
| 4 | Semaphore | `semaphore_sum.py` | Limits the number of threads accessing a shared resource. |
