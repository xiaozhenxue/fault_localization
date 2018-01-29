import sys
from utility import read_file
from program import Program
from test_case import TestCase


def read_program(status_path, traces_path, instrument_path):
    statuses = read_file(status_path).split('\n')
    traces = read_file(traces_path).split('\n')
    if len(statuses) == 0:
        print 'status length 0'
    if len(traces) == 0:
        print 'traces length 0'
    if len(statuses) != len(traces):
        print 'length of traces and status are different'
    testcases = list([])
    for i in xrange(0, len(statuses)):
        status = True if 0 == statuses[i].split(':')[1] else False
        trace = traces[i].split(':')[1]
        testcase = TestCase(trace, status)
        testcases.append(testcase)
    instrument = read_file(instrument_path).split('\n')
    if len(instrument) < 2:
        print 'can not read instrument info'
    fault_line = instrument[0].split(':')[1].split(',')
    fault = [int(e) for e in fault_line]
    total = int(instrument[1].split(':')[1])
    return Program(testcases, fault, total)


def main():
    if len(sys.argv) < 4:
        print "usage: python fault_localization.py [status_path] [traces_path] [instrument_path]"
        return
    status_path = sys.argv[1]
    traces_path = sys.argv[2]
    instrument_path = sys.argv[3]
    program = read_program(status_path, traces_path, instrument_path)
    score = program.compute_suspicious_score()
    print program.localize_fault(score)


if __name__ == "__main__":
    main()

