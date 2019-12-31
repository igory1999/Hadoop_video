* To submit a batch job running on a single node of midway 2 cluster, do on midway 2 login node:
  ```
  make single
  ```
* To submit a batch job running on multiple nodes of midway 2 cluster, do on midway 2 login node:
  ```
  make multiple
  ```
* To monitor how your jobs are running:
  ```
  make check_slurm
  ```
* To submit a batch job to Hadoop cluster, do on Hadoop login node: 
  ```
  make hadoop
  ```
* To monitor how your Hadoop jobs are running:
  ```
  make check_hadoop
  ```
* To clean output files, do 
  ```
  make clean
  ```
