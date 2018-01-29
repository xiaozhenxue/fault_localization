# fault_localization

This utility scirpts are developed for computing the cost for localizing a bug in the program. 

Suppose we have these files ready to use for a subject program: 
1) status-file: the status of each test case
2) traces_file: the traces of each test case 
3) instrument_file: total number of imstruments,  and the buggy instrument


The usage of this scripts: 
python fault_localization.py [status_file_path] [traces_file_path] [instrument_file_path]
