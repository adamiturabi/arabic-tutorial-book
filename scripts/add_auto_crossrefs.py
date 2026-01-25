ex_count = 0
sec_count = 0

def get_next_ex_label(match):
    global ex_count
    prefix = 'ex'
    num_digits = 6
    ex_count += 1
    return '(@' + prefix + str(ex_count).rjust(num_digits, '0') + ') '

def read_file(filename):
    #in_str = ""
    with open(filename, 'r') as in_file:
        out_str = ""
        in_lines = in_file.readlines()

        import re

        # search replace (@) and add example label
        line_count = 1
        for in_line in in_lines:
            out_line = ""
            try:
                out_line = re.sub(r'^\(@\) ', get_next_ex_label, in_line, flags = re.M)
            except TypeError:
                print("Term sub error in ", filename, " line number ", line_count);
                print(in_line)
                raise

            out_str += out_line
            line_count += 1

        return out_str

def write_into_file(file_data_str: str, destination_path) -> None:

    with open(destination_path, 'w') as file:
        file.write(file_data_str)

def main():

    dump_db = {}

    # save max count value to use as initial value for next run
    curr_dir = os.path.dirname(__file__)
    dump_file_path = os.path.join(curr_dir, "pre_render_vals.dump")
    global ex_count
    global sec_count
    with open(dump_file_path, 'r') as dump_file:

        import json
        dump_db = json.loads(dump_file.read())

        assert('ex_count' in dump_db.keys())
        assert('sec_count' in dump_db.keys())

        ex_count = dump_db['ex_count']
        sec_count = dump_db['sec_count']
        
    in_dir = os.fsencode("srcqmd")
    out_dir = os.fsencode("srcqmd")

    print(f"Rendering ...")
    for file in os.listdir(in_dir):
        filename = os.fsdecode(file)
        if filename.endswith(".qmd"):
            # print(os.path.join(in_dir, filename))
            input_file = os.path.join(in_dir, file)
            output_file = os.path.join(out_dir, file)

            #print("Reading from " + input_file)
            file_data_str = read_file(input_file)

            #print("Writing to " + output_file)
            write_into_file(file_data_str, output_file)
            #print("Done.")

    with open(dump_file_path, 'w') as dump_file:

        assert('ex_count' in dump_db.keys())
        assert('sec_count' in dump_db.keys())
        dump_db['ex_count']  = ex_count
        dump_db['sec_count'] = sec_count

        import json
        dump_file.write(json.dumps(dump_db))

if __name__ == "__main__":
    import os

    #if not os.getenv("QUARTO_PROJECT_RENDER_ALL"):
    #    exit()

    main()

