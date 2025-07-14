import manage_bib

def read_file(filename):
    in_str = ""
    with open(filename, 'r') as in_file:
        in_str = in_file.read()
        #in_str += '\nkjhawkjhe'

    import re

    # search replace for subs filter
    out_str = re.sub('(#*);([a-zA-Z0-9_]+);', r'[\1\2]{.subs}', in_str, flags = re.M)

    # search replace for citations
    out_str = re.sub('@[^ ]+@', manage_bib.get_cite_text, out_str, flags = re.M)
    #for match in re.finditer('@[a-zA-Z0-9_]@', out_str):
    #    print(match.group())
    #    replaced_str = manage_bib.get_cite_text(match.group())
    #    out_str = out_str[:match.start()] + replaced_str + out_str[match.end():]
    
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
