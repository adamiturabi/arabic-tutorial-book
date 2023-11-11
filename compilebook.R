# compile bookdown
# modified from https://stackoverflow.com/questions/55164787/conditionally-include-chapters-in-bookdown

bookdown_yml <- paste0(
"# DO NOT EDIT DIRECTLY. Eid compilebook.R instead
book_filename: 'Learn-Standard-Arabic.Rmd'
output_dir: 'book-output'
")

rmd_file_list <- c("intro.Rmd", "script.Rmd", "nouns.Rmd", "gender.Rmd", "simple_sentences.Rmd", "prepositions.Rmd", "past_verbs.Rmd", "describing_nouns.Rmd", "diptotes.Rmd", "duals.Rmd", "sound_plurals.Rmd", "broken_plurals.Rmd", "idafa.Rmd", "ism_ishara.Rmd", "elatives.Rmd", "five_nouns.Rmd", "vocative.Rmd", "imperfect_verb_indic.Rmd", "doing_verbal_nouns.Rmd", "imperfect_verb_subj.Rmd", "kana_sisters.Rmd", "ideas.Rmd", "appendix.Rmd", "hamzarules.Rmd", "further.Rmd")

rmd_file_list <- paste("srcrmd/", rmd_file_list, sep="")

cat(bookdown_yml,
"rmd_files:\n",
"  html:  ['index.Rmd', '", paste0(rmd_file_list, collapse="', '"), "']\n", 
"  latex: ['index.Rmd', '", paste0(rmd_file_list, collapse="', '"), "']\n", 
file="_bookdown.yml", sep="")

# Commands for compiling book
bookdown::render_book('index.Rmd','bookdown::gitbook', clean = FALSE)
bookdown::render_book('index.Rmd','bookdown::pdf_book')

