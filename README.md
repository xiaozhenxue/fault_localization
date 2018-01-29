# fault_localization

This utility scirpts are developed for computing the cost for localizing a bug in the program. 

Suppose we have this file ready to use for a subject program: 
1) total number of imstruments,  and the buggy instrument
2) a test suite and traces of each test case
3) status of each test case


The usage of this scripts: 
python fault_localization.py [status_file_path] [traces_file_path] [instrument_file_path]
