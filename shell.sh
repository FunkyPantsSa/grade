#!/bin/bash

#这个函数是判断数字是否在 1-9 之间
validation(){

if ((number >= 1 && number <= 9)); then
    echo "valid number"
    pr
    #这里调用函数
else
    echo "not valid number,try again"
fi

}

#这个函数是输出乘法表
pr(){
c=$number
b=$number
echo "$number"
while ((c >= 1))
do
#    ((c--))
    val=$(($b*$c))
    echo "$c x $number = $val"
    ((c--))
done
}

#以下为主函数
echo "insert number"
#读取输入
read number
#判断 并输出
validation
echo "over"








