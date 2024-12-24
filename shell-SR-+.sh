#!/bin/bash

# 定义起始和结束值
START_N=1
END_N=100
START_M=1
END_M=100
#OPS=('+' 'x' 'd' 's')
OPS=('+')
TRAIN_NUM_SAMPLES=100
TEST_NUM_SAMPLES=100

# 定义步长
STEP=1

for OP in ${OPS[*]}; do
  echo ${OP}
  # 循环遍历 n 和 m 的值
  for ((n=$START_N; n<=$END_N; n+=STEP)); do
      for ((m=$START_M; m<=$END_M; m+=STEP)); do
          if [ $n -le 3 ]; then
            continue
          fi
          if [ $n -eq 4 ] && [ $m -le 18 ]; then
            continue
          fi
          # 创建目录名称
          data_name="dso/dso/task/regression/data/sogn/${OP}/${TRAIN_NUM_SAMPLES}/sogn_${OP}_${n}_${m}_${TRAIN_NUM_SAMPLES}.csv"

          # 运行第一个命令
          /home/henry/Downloads/Python-3.6.15/python -m dso.run dso/dso/config/config_regression_sogn.json --b $data_name

          # 检查上一条命令是否成功执行
          if [ $? -ne 0 ]; then
              echo "Error occurred while running the first command with n=$n and m=$m"
              exit 1
          fi

      done
  done
done

echo "All iterations completed successfully."
