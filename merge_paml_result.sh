# yexinhai, yexinhai@zju.edu.cn

find ./input.table.txt.aa*/paml_result -name "Group*.alter.result" -exec bash -c 'cat $0 >>Alter.all; echo >>Alter.all' {} \;
find ./input.table.txt.aa*/paml_result -name "Group*.null.result" -exec bash -c 'cat $0 >>Null.all; echo >>Null.all' {} \;
