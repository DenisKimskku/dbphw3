hadoop jar /opt/hadoop3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -D mapreduce.job.reduces=1 -files mapper.py,reducer.py,combiner.py -input /sorting -output /sorting/output -mapper mapper.py -combiner combiner.py -reducer reducer.py