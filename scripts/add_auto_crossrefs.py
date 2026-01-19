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

    # save max count value to use as initial value for next run
    import shelve
    with shelve.open("pre_render_vals.dump", 'c') as db:
        global ex_count
        global sec_count

        if 'ex_count' in db.keys():
            ex_count = db['ex_count']
        else:
            ex_count = 0
        if 'sec_count' in db.keys():
            sec_count = db['sec_count']
        else:
            sec_count = 0
        

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


        db['ex_count']  = ex_count
        db['sec_count'] = sec_count


if __name__ == "__main__":
    import os

    if not os.getenv("QUARTO_PROJECT_RENDER_ALL"):
        exit()

    main()

