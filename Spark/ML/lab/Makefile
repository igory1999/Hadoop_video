single:
	sbatch single.batch
check_slurm:
	squeue -u $(USER)
multiple:
	sbatch multiple.batch
hadoop:
	nohup spark2-submit --master yarn perceptron.py 1>hadoop.out 2>hadoop.err &
check_hadoop:
	yarn application -list 2>/dev/null | perl -ne 'print if(/${USER}/)'
clean:
	rm -r -f *~ *.out *.err *.log spark-warehouse logs work

