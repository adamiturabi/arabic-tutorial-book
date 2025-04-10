# compile bookdown
# modified from https://stackoverflow.com/questions/55164787/conditionally-include-chapters-in-bookdown

bookdown_yml <- paste0(
"# DO NOT EDIT DIRECTLY. Edit compilebook.R instead
book_filename: 'A-Learners-Grammar-of-Classical-Standard-Arabic.Rmd'
output_dir: 'docs'
")

rmd_file_list <- c("intro.Rmd"
 , "script.Rmd"
 , "nouns.Rmd"
 , "simple_sentences.Rmd"
 , "prepositions.Rmd"
 , "past_verbs.Rmd"
 , "describing_nouns.Rmd"
 , "diptotes.Rmd"
 , "duals.Rmd"
 , "sound_plurals.Rmd"
 , "broken_plurals.Rmd"
 , "idafa.Rmd"
 , "irregular_nouns.Rmd"
 , "proper_nouns.Rmd"
 , "vocative.Rmd"
 , "ism_ishara.Rmd"
 , "imperfect_verb_indic.Rmd"
 , "doing_verbal_noun.Rmd"
 , "imperfect_verb_subj.Rmd"
 , "imperfect_verb_juss.Rmd"
 , "passive_voice.Rmd"
 , "doer_verbal_noun.Rmd"
 , "kaana.Rmd"
 , "inna_and_its_sisters.Rmd"
 , "ism_mawsuul.Rmd"
 , "questions.Rmd"
 #, "group_nouns.Rmd"
 #, "elatives.Rmd"
 #, "ideas.Rmd"
 , "appendix.Rmd"
 , "hamzarules.Rmd"
 , "usage_and_style.Rmd"
)

rmd_file_list <- paste("srcrmd/", rmd_file_list, sep="")

cat(bookdown_yml,
"rmd_files:\n",
"  html:  ['index.Rmd', '", paste0(rmd_file_list, collapse="', '"), "']\n", 
"  latex: ['index.Rmd', '", paste0(rmd_file_list, collapse="', '"), "']\n", 
file="_bookdown.yml", sep="")

# Commands for compiling book
bookdown::render_book('index.Rmd','bookdown::gitbook', clean = FALSE)
warnings()
bookdown::render_book('index.Rmd','bookdown::pdf_book')

