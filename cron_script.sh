TODAY=$(date +%d-%h-%Y)
cd ~/webapp_crons
today=`date '+%Y_%m_%d__%H_%M_%S'`;
echo $today
ps -ef | grep packaged_daily.py | grep -v grep | awk '{print $2}' | xargs kill -9
pipenv run python packaged_daily.py 2>&1 &

