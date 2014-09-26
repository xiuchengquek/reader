__author__ = 'quek'


def calculator(input):
    pass


def Reader(inputfile, linebreak):
    file_count = 0
    line_counter = 1
    term_counter = 0
    outfile = "outdir/file_%i" % file_count
    fh_out = open(outfile, 'a+')
    previous_term = False
    previous_id = False

    with open(inputfile) as f:
        for lines in f.readlines():
            lines = lines.strip()
            fields = lines.split('\t')
            current_id = fields[0]
            current_term = fields[-1]

            if previous_term and current_term != previous_term:
                previous_fields.append(str(term_counter))
                out_line = "\t".join(previous_fields)
                fh_out.write("%s\n" % out_line)
                term_counter = 0
                line_counter += 1

            if line_counter > linebreak:
                if previous_id != current_id and previous_id:
                    fh_out.close()
                    file_count += 1
                    print 'Completed Approx %i' % ((file_count + 1) * line_counter + 1)
                    outfile = "outdir/file_%i" % file_count
                    fh_out = open(outfile, 'a+')
                    line_counter = 1

            term_counter += 1
            previous_id = current_id
            previous_term = current_term
            previous_fields = fields

        previous_fields.append(str(term_counter))
        out_line = "\t".join(previous_fields)
        fh_out.write("%s\n" % out_line)

    fh_out.close()


if __name__ == '__main__':
    Reader('mocktest.txt', 10)