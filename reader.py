__author__ = 'quek'


def calculator(input):
    pass


def Reader(inputfile):
    file_count = 0
    term_counter = 0
    outfile = "outdir/file_%i" % file_count
    fh_out = open(outfile, 'a+')
    previous_term = False

    with open(inputfile) as f:
        for lines in f:
            lines = lines.strip()
            fields = lines.split('\t')
            current_term = fields[-1]
            if previous_term and current_term != previous_term:
                previous_fields.append(str(term_counter))
                out_line = "\t".join(previous_fields)
                fh_out.write("%s\n" % out_line)
                term_counter = 0
            term_counter += 1
            previous_term = current_term
            previous_fields = fields

        previous_fields.append(str(term_counter))
        out_line = "\t".join(previous_fields)
        fh_out.write("%s\n" % out_line)

    fh_out.close()


if __name__ == '__main__':
    Reader('mocktest.txt')