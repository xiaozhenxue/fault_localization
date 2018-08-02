from utility import read_file, write_file


def main(traces_path, comb1_path, comb2_path, comb3_path):
    comb1, comb2, comb3 = extract_dict(traces_path)
    traces = read_file(traces_path).split('\n')
    ret1 = []
    ret2 = []
    ret3 = []
    ret1.append("combination " + " ".join(comb1))
    ret2.append("combination " + " ".join(comb2))
    ret3.append("combination " + " ".join(comb3))
    for line in traces:
        if line is not '':
            dict1, dict2, dict3 = extract_feature(comb1, comb2, comb3, line)
            line1 = line.split(":")[0] + " " + convert_to_line(comb1, dict1)
            line2 = line.split(":")[0] + " " + convert_to_line(comb2, dict2)
            line3 = line.split(":")[0] + " " + convert_to_line(comb3, dict3)
            ret1.append(line1)
            ret2.append(line2)
            ret3.append(line3)
    text1 = "\n".join(ret1)
    text2 = "\n".join(ret2)
    text3 = "\n".join(ret3)
    write_file(text1, comb1_path)
    write_file(text2, comb2_path)
    write_file(text3, comb3_path)


def convert_to_line(comb, dict):
    list = []
    for e in comb:
        list.append(str(dict[e]))
    return " ".join(list)


def extract_feature(comb1, comb2, comb3, line):
    dict1 = dict.fromkeys(comb1, 0)
    dict2 = dict.fromkeys(comb2, 0)
    dict3 = dict.fromkeys(comb3, 0)
    all = line.split(":")[1].split(",")
    all = [int(e) for e in all if e is not '']
    for i in xrange(0, len(all)):
        fea = "{}".format(all[i])
        if fea in dict1:
            dict1[fea] = dict1[fea] + 1
    for i in xrange(0, len(all)):
        for j in xrange(i + 1, len(all)):
            fea = "{},{}".format(all[i], all[j])
            if fea in dict2:
                dict2[fea] = dict2[fea] + 1
    for i in xrange(0, len(all)):
        for j in xrange(i+1, len(all)):
            for k in xrange(j+1, len(all)):
                if fea in dict3:
                    fea = "{},{},{}".format(all[i], all[j], all[k])
                    dict3[fea] = dict3[fea] + 1

    return dict1, dict2, dict3


def extract_dict(traces_path):
    traces = read_file(traces_path).split('\n')
    comb1 = set()
    comb2 = set()
    comb3 = set()
    for line in traces:
        if line is not '':
            print line
            all = line.split(":")[1].split(",")
            all = [int(e) for e in all if e is not '']
            comb1 |= get_comb1(all)
            comb2 |= get_comb2(all)
            comb3 |= get_comb3(all)
    print "1", comb1
    print "2", comb2
    print "3", comb3
    return comb1, comb2, comb3


def get_comb1(all):
    ret = set()
    for i in xrange(0, len(all)):
        ret.add("{}".format(all[i]))
    return ret


def get_comb2(all):
    ret = set()
    for i in xrange(0, len(all)):
        for j in xrange(i+1, len(all)):
            ret.add("{},{}".format(all[i], all[j]))
    return ret


def get_comb3(all):
    ret = set()
    for i in xrange(0, len(all)):
        for j in xrange(i+1, len(all)):
            for k in xrange(j+1, len(all)):
                ret.add("{},{},{}".format(all[i], all[j], all[k]))
    return ret


if __name__ == "__main__":
    main()

