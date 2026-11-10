import manage_bib

def read_file(filename):
    #in_str = ""
    with open(filename, 'r') as in_file:
        out_str = ""
        in_lines = in_file.readlines()
        #in_str += '\nkjhawkjhe'

        import re

        # search replace for subs filter
        #out_str = re.sub('(#*);([a-zA-Z0-9_]+);', r'[\1\2]{.subs}', in_str, flags = re.M)
        import manage_subs
        line_count = 1
        reset_numbered_example_list = False
        for in_line in in_lines:
            out_line = ""
            try:
                out_line = re.sub('(#*);([a-zA-Z0-9_]+);', manage_subs.get_sub_text, in_line, flags = re.M)
            except TypeError:
                print("Term sub error in ", filename, " line number ", line_count);
                print(in_line)
                raise

            try:
                out_line = re.sub('@[^ \n]+@', manage_bib.get_cite_text, out_line, flags = re.M)
            except TypeError:
                print("Cite sub error in ", filename, " line number ", line_count);
                print(in_line)
                raise

            #if not reset_numbered_example_list:
            #    try:
            #        new_line = re.sub(r'\(@(\w*)\)', r'(1@\1)', out_line, count=1)
            #        if new_line != out_line:
            #            reset_numbered_example_list = True
            #        out_line = new_line
            #    except TypeError:
            #        print("Reset numbered example list sub error in ", filename, " line number ", line_count);
            #        print(in_line)
            #        raise


            out_str += out_line
            line_count += 1

            #out_str = re.sub('(#*);([a-zA-Z0-9_]+);', manage_subs.get_sub_text, in_str, flags = re.M)

        # search replace for citations
        #out_str = re.sub('@[^ \n]+@', manage_bib.get_cite_text, out_str, flags = re.M)
        #for match in re.finditer('@[a-zA-Z0-9_]@', out_str):
        #    print(match.group())
        #    replaced_str = manage_bib.get_cite_text(match.group())
        #    out_str = out_str[:match.start()] + replaced_str + out_str[match.end():]

        # replace first instance of (@foo) with (1@foo)
        #out_str = re.sub(r"\(@\w+\)", r'(1@\1)', out_str, count=1)
        
        warning_str = "<!--!!! THIS FILE IS AUTO-GENERATED. DO NOT EDIT DIRECTLY. EDIT THE FILES IN THE SRCQMD DIR !!!-->\n\n"

        out_str = warning_str + out_str

        #with open(filename, 'w') as file:
        #    file.write(in_str)
        return out_str

def write_into_file(file_data_str: str, destination_path) -> None:

    with open(destination_path, 'w') as file:
        file.write(file_data_str)

if __name__ == "__main__":
    import os

    if not os.getenv("QUARTO_PROJECT_RENDER_ALL"):
        exit()

    in_dir = os.fsencode("srcqmd")
    out_dir = os.fsencode("content")
        
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

    bib_str = manage_bib.get_bib_str()
    filename = 'refs.qmd'
    output_file = os.path.join(out_dir, os.fsencode(filename))
    with open(output_file, 'w') as file:
        file.write(bib_str)
