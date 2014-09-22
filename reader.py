__author__ = 'quek'

def Reader(inputfile, linebreak):
    file_count = 0
    line_counter = 1
    outfile = "outdir/file_%i" % file_count
    fh_out = open(outfile, 'w+')

    with open(inputfile) as f:
        for lines in f.readlines():
            current_id = lines.split('\t')[0]
            if line_counter > linebreak :
                if previous_id != current_id:
                    fh_out.close()
                    file_count += 1
                    print 'Completed Approx %i' % ((file_count+1) * line_counter+1)
                    outfile = "outdir/file_%i" % file_count
                    fh_out = open(outfile, 'w+')
                    line_counter = 1
            line_counter += 1
            previous_id = current_id
            fh_out.write(lines)
    fh_out.close()

if __name__ == '__main__':
    Reader('mocktest.txt', 10)