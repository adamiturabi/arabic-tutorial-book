---
title: "Learn Standard Arabic"
subtitle:  "A self-instruction textbook with grammar, vocabulary, and exercises"
author: "Author Names"
date: "v0.1.0-742-gea1b7db"
documentclass: book
geometry:
# A4 2 pages per sheet draft
#- paper=a5paper               # a5: 148.5 by 210mm
#- paperwidth=170mm
#- paperheight=244mm
- paperwidth=156mm
- paperheight=234mm
#- paperwidth=6in
#- paperheight=9in
- bindingoffset=16mm
- textwidth=114.8mm           # = (170 - 6)*0.7
- textheight=170.8mm          # = 244 * 0.7
- twoside
mainfont: "Charis SIL"
mainfontoptions: Numbers=OldStyle
fontsize: 10pt
lang: en
otherlangs: [ar]
fontfamilies:
  - name: \arabicfont
    font: Vazirmatn-Light
    options: Script=Arabic,Scale=1.0
  - name: \tradarab
    font: Amiri
    options: Script=Arabic,Scale=1.0
  - name: \tradarabsmall
    font: Amiri
    options: Script=Arabic,Scale=0.75
csquotes: true
output:
  bookdown::gitbook:
    includes:
      before_body: "srchtml/watermark.html"
    pandoc_args: ["--lua-filter=trn.lua"]
    keep_md: yes
    css: mystyle.css
    number_sections: true
    config:
      toc:
        collapse: section
        scroll_highlight: yes
        before: null
        after: null
      toolbar:
        position: fixed
      edit : null
      download: null
      search: yes
      fontsettings:
        theme: white
        family: serif
        size: 2
      sharing:
        facebook: yes
        github: no
        twitter: yes
        linkedin: yes
        weibo: no
        instapaper: no
        vk: no
        all: ['facebook', 'twitter', 'linkedin', 'weibo', 'instapaper']
      info: yes
  bookdown::pdf_book:
    number_sections: true
    latex_engine: xelatex
    pandoc_args: ["--lua-filter=trn.lua", "--columns=65"] # for forcing word wrap in pipe tables
    #template: default_latex_template.tex # with Brill font the PDF font is too large and this needs to be uncommented. includes and in_header should then be commented
    includes:
      before_body: "srctex/frontpage.tex"
      in_header: "srctex/preamble.tex"
    keep_tex: true
---

# Preface {-}

<!--The following line is needed because Preface is an unnumbered chapter and otherwise fancy header will print the header text for the previous chapter "Contents"-->
\markboth {\textsc{\MakeLowercase{Preface}}}{\textsc{\MakeLowercase{Preface}}}

<!--to allow git describe to run-->


<!--
::: {.otherlanguage data-latex="{arabic}" lang="ar"}
[بسم الله الرحمن الرحيم]{.ar}
:::
-->

<!--[بسم الله الرحمن الرحيم]{.ar}-->


[بسم الله الرحمن الرحيم]{lang="ar" dir="rtl" style="font-family: Amiri;"}

<!-- RTL doesn't work for some reason-->
```{=latex}
\begin{center}
\tradarab{
الرحيم
الرحمن
الله
بسم
}
\end{center}
```

<!--Sunnah are the sayings and actions of the Prophet صلى الله عليه وسلم. Hadith is the text by which we know the sunnah.-->

The primary texts of [#islAm]{.trn2} (the [#qurEAn]{.trn2} and the [#HadIv]{.trn2}) are in Arabic. So too is much of its scholarly literature. However, there is a multitude of Muslims for whom Arabic is not a native language, yet who are familiar enough with English to study textbooks written in this language. The goal of this book is to help them learn Arabic at a beginner's level so that, together with a study of the appropriate expositional texts, they are one step closer to understanding the primary texts in their original language. We hope that this will, if [#allAh]{.trn2} wills, make them feel more connected to the primary texts and their teachings. Furthermore, they can be empowered to study the vast body of Arabic [#islAm]{.trn2}ic literature.

This book is a teaching grammar and not a reference grammar. So, in the initial chapters, topics are presented sequentially at only a basic level, without treating them exhaustively, before moving on to the next topic. Furthermore, since this is a beginner's textbook, only the more common usages are explained.

We have also aimed to make this a self-instruction textbook so that a diligent student should, if [#allAh]{.trn2} wills, be able to study it without an instructor. The target learner is someone who has not been exposed to grammatical terminology like _inflection_, _case_, _mood_, etc. While terminology is necessary for a rigorous non-immersive learning of language, we have tried to steer away from Latin-based terms like _accusative_ and _jussive_. Such terms, when first encountered by an uninitiated learner, may deter from proceeding further. (Learning a language can be hard enough without getting the feeling that your grammar book is accusing you of something!) So we have in some places translated the meaning of Arabic grammar terms to English. In other places, we have used established English grammar terms where the terms are basic enough. We have even, in places, invented terms where we deemed appropriate. The drawback to this non-standard approach, however, is that the student may not be able to immediately relate the terminology he has learned in this book to established terminology in other grammar textbooks. To remedy this to some extent, we provide a glossary in the appendix which maps the grammatical terminology used in this book to other, established, Latin-based and Arabic-based counterparts.

It may also be appropriate to inform the reader that we chose to present a simplified version of Arabic grammar. As such, the grammar presented here may not be entirely consistent with the comprehensive and harmonious framework developed by the Arab grammarians. We chose this approach because we felt that exposing the beginner to complex grammatical details at this stage would be more of a hindrance than a help in learning the language.

This book is produced with the R bookdown package. The code and text are open-sourced and developed at 
[github.com/adamiturabi/arabic-tutorial-book](https://github.com/adamiturabi/arabic-tutorial-book).
The typeset output is published at 
[adamiturabi.github.io/arabic-tutorial-book/](https://adamiturabi.github.io/arabic-tutorial-book/).

[The Authors]{.smallcaps}  

<!--
[a.z.s.]{.smallcaps}  
[lahore, dec.]{.smallcaps} 2021[ce]{.smallcaps}  
[لاهور، جمادى الأولى ١٤٤٣هـ‍]{.ar}

Test:

This is the _preface_. Test trans [Parf makAn ealayhi pcv machad]{.trn} [◌َ  ◌ً  ◌ِ  ◌ٍ  ◌ُ  ◌ٌ  ◌ْ  ◌ّ  ◌ٰ  ◌ٔ  ◌ٕ  ]{.ar}

[شَيْـَٔيْنِ بَرِيـِٔينَ شَيْـًٔا خَطِيـَٔة]{.ar}

[شَيْءَيْنِ بَرِيءِينَ شَيْءًا خَطِيءَة]{.ar}


this is in [Small Caps]{.smallcaps}.



-->


<!--chapter:end:index.Rmd-->

# Introduction

All praises are due to [#allAh]{.trn2}. We praise Him, seek His help, and ask for His forgiveness. We seek refuge in [#allAh]{.trn2} from the evil in our souls and from our sinful deeds. Whomever [#allAh]{.trn2} guides, no one can mislead. Whomever [#allAh]{.trn2} leads astray, no one can guide. I bear witness that there is no one worthy of worship except [#allAh]{.trn2}. I also bear witness that [#muHammad]{.trn2} is His servant and messenger.

May the peace and blessings of [#allAh]{.trn2} be upon the Prophet [#muHammad]{.trn2}, his family, his companions, and those who followed them with good conduct.

## History of Arabic 

[#allAh]{.trn2}, may He be glorified and exalted, revealed the [#qurEAn]{.trn2} 1400 years ago to the Prophet [#muHammad]{.trn2}, may [#allAh]{.trn2} grant peace and confer blessing upon him. The language of the [#qurEAn]{.trn2} is the Arabic language, as it was understood by the Arabs at that time. 
The sayings and actions of the Prophet, may [#allAh]{.trn2} grant peace and confer blessing upon him, were recorded by his companions also in this Arabic language. 
We will call the Arabic of this pre-[#islAm]{.trn2}ic and early [#islAm]{.trn2}ic era as Classical Arabic.
The Classical Arabic language consisted of multiple dialects that were spoken by the different tribes and in the different regions of the Arabian peninsula. 

All languages change naturally over time. For example, English has changed to such a degree that the Old English language spoken 1400 years ago would be unintelligible to us today. So too did the Classical Arabic dialects begin to change. But as part of preserving His religion, [#allAh]{.trn2} preserved the Arabic language as well. This was by means of the efforts of scholars who recorded the Classical Arabic language of the time of the revelation.

In the process of preserving Arabic, one particular variety became standardized and gained prevalence as a literary language over the other dialects of the Arabic of the early-[#islAm]{.trn2}ic period. This _Standard Arabic_, in its early period after standardization, is called Classical Standard Arabic.
<!--or simply Classical Arabic[^1]. -->
The pre-[#islAm]{.trn2}ic and early [#islAm]{.trn2}ic Arabic dialects (of which Classical Standard Arabic is but a standardized variety) are then referred to, collectively, as pre-standard Classical Arabic. Classical Standard Arabic was used as the language of religious scholarship, science, and literature in the [#islAm]{.trn2}ic world. As scholars developed new branches of religious and secular sciences, new terms and meanings were added to it that are termed post-classical. A few words were also borrowed from foreign languages and Arabicized, as needed by the different scientific disciplines. (Pre-Standard Classical Arabic itself had a few Arabicized foreign borrowings from neighboring languages.) These additions were, by and large, deliberate, done by scholars who were experts in their fields and also well versed in Classical Standard Arabic, and validated by subsequent generations of scholarly discourse. Besides these needed additions, the grammar and core language remained remarkably unchanged.

<!--
[^1]: This definition of the term _Classical Arabic_ is not universally accepted, and other authors may use it to also include the Arabic of the late pre-[#islAm]{.trn2}ic and early [#islAm]{.trn2}ic period.
-->

<!--Ahmad Al-Jallad, Damascus Psalm Fragment, p. 69-->
While Standard Arabic was thus preserved from major change and was used for literary purposes, the language that was spoken by Arabs in their day-to-day lives continued to change over time from the pre-standard Classical Arabic dialects into the modern colloquial dialects. And so today, there exist two very distinct types of Arabic: the preserved Standard Arabic which is taught at schools and is primarily a written language, and the modern colloquial Arabic dialects which Arabs learn as their mother tongue and which are primarily only spoken and not written.

<div class="figure">
<embed src="Learn-Standard-Arabic_files/figure-html/unnamed-chunk-3-1.pdf" title="Timeline of the development of Standard Arabic." type="application/pdf" />
<p class="caption">(\#fig:unnamed-chunk-3)Timeline of the development of Standard Arabic.</p>
</div>

In modern times, many new words and meanings have been added to Standard Arabic, often via translation from Western languages, to keep up with technological advancements and modern media. 
<!--However, it must be said that these additions have often been done by translators rather than scholars in the field, and have sometimes lacked the deliberation seen in the post-classical additions to Standard Arabic. -->
This modern development of Standard Arabic is called Modern Standard Arabic. 
There are also a small amount of words, meanings, and grammatical usages, which existed in Classical Arabic, but which are deemed archaic, and are therefore largely unused, in Modern Standard Arabic.

Figure\ 1.1 (above) depicts this historical development of Standard Arabic.

## Scope of this book

In this book, we will study Standard Arabic. We will focus on the pre-modern language. If [#allAh]{.trn2} wills, this will help you to begin to understand the language of the [#qurEAn]{.trn2}, the [#HadIv]{.trn2}, and [#islAm]{.trn2}ic literature.

If your goal is to learn Modern Standard Arabic, then this book may still be of help because the core language and the grammar are essentially the same. However, you may prefer to study from a resource that focuses on the modern language.

This book does not touch at all upon the modern colloquial dialects that are spoken in the Arab world today.

## How to study from this book

We will start with the Arabic script and present in each chapter a new concept of Arabic grammar, together with examples. We will also give vocabulary for you to memorize and have chapter exercises. Unfortunately, some of the sentences we present, both as examples and as chapter exercises, because of their construction and subject matter, may seem of dubious usefulness to a learner wanting to learn practical usage. We ask that you overlook this and bear with us as we try to reinforce grammatical concepts. In answering the exercises, we strongly recommend that you memorize the vocabulary in full and write down the answers on paper with a pen. 

We strongly recommend that you **not**:

+ answer the exercises verbally without writing them down,
+ look up the answers before attempting to write the answer yourself,
+ look up words in the vocabulary list without memorizing them,
+ proceed to the next chapter before memorizing the vocabulary and going through the exercises.

Be aware that while Arabic grammar requires effort to master to a proficient degree, the real barrier to reading and understanding Arabic texts by oneself is vocabulary. Arabic is a very rich language and knowledge of a few thousand words is needed before the student can begin to read texts independently.

You may also find yourself having to go back a few chapters every once in a while and revising the concepts therein. This is very normal and not a cause for any alarm. It may also prove beneficial to re-do the exercises of that chapter when this occurs.


<!--chapter:end:srcrmd/intro.Rmd-->

# The Arabic script

## The Arabic alphabet

The alphabet consists of both consonants and vowels. In the English word "banana", "a" is a vowel, and "b" and "n" are called consonants.
The Arabic alphabet traditionally has 28 letters, shown in the table below.

No.|Arabic letter|Tran-scrip-tion|Name |Description
:-|:--|:--|:------|:---------------------------
 1|[ا]{.ar}|[A]{.trn}| [أَلِف]{.ar} [Ealif]{.trn2} |A vowel like in English "man". But after these letters ([خ،ر،ص،ض،غ،ق]{.ar}) it sounds like "awe" in English "awesome".
 2|[ب]{.ar}|[b]{.trn}| [بَاء]{.ar} [bAE]{.trn2} |Equivalent to English "b" in "boy".
 3|[ت]{.ar}|[t]{.trn}| [تَاء]{.ar} [tAE]{.trn2} |Similar to English "t" in "tall" but softer. Touch the tongue against the back of the top front teeth instead of just the gum.
 4|[ث]{.ar}|[v]{.trn}| [ثَاء]{.ar} [vAE]{.trn2} |Similar to to English "th" in "think" but softer. Have your lips and cheek in a wide grin. Loosely bite the tip of your tongue between your front teeth and then force air out trying to hiss "ssss". Keep your tongue touching the top and bottom teeth and the hiss should come out like a "th" sound.
 5|[ج]{.ar}|[j]{.trn}| [جِيم]{.ar} [jIm]{.trn2} |Equivalent to English "j" in "just".
 6|[ح]{.ar}|[H]{.trn}| [حَاء]{.ar} [HAE]{.trn2} |Similar to English "h" in "hat" but pronounced from the bottom of the throat. Take care there is no scraping as with [خ]{.ar}.
 7|[خ]{.ar}|[x]{.trn}| [خَاء]{.ar} [xAE]{.trn2} |Similar to "ch" in Scottish "loch". Try saying "kh" but with a scraping sound.
 8|[د]{.ar}|[d]{.trn}| [دَال]{.ar} [dAl]{.trn2} |Similar to to English "d" in "dog" but softer. Just like with [ت]{.ar}, touch the tongue against the back of the top front teeth instead of just the gum.
 9|[ذ]{.ar}|[p]{.trn}| [ذَال]{.ar} [pAl]{.trn2} |Place your tongue as in [ث]{.ar} and force air out. But this time instead of trying to hiss "ssss" try to buzz "zzzz" and again keep your tongue touching the top and bottom teeth.
10|[ر]{.ar}|[r]{.trn}| [رَاء]{.ar} [rAE]{.trn2} |Equivalent to English "r" in "rat".
11|[ز]{.ar}|[z]{.trn}| [زَاء]{.ar} [zAE]{.trn2} |Equivalent to English "z" in "zoo".
12|[س]{.ar}|[s]{.trn}| [سِين]{.ar} [sIn]{.trn2} |Equivalent to English "s" in "see".
13|[ش]{.ar}|[c]{.trn}| [شِين]{.ar} [cIn]{.trn2} |Equivalent to English "sh" in "show".
14|[ص]{.ar}|[S]{.trn}| [صَاد]{.ar} [SAd]{.trn2} |An emphatic [س]{.ar} that will be described later.
15|[ض]{.ar}|[D]{.trn}| [ضَاد]{.ar} [DAd]{.trn2} |An sound unique to Arabic that will be described later.
16|[ط]{.ar}|[T]{.trn}| [طَاء]{.ar} [TAE]{.trn2} |An emphatic [ت]{.ar} that will be described later.
17|[ظ]{.ar}|[P]{.trn}| [ظَاء]{.ar} [PAE]{.trn2} |An emphatic [ذ]{.ar} that will be described later.
18|[ع]{.ar}|[e]{.trn}| [عَيْن]{.ar} [eayn]{.trn2} |A sound similar to strangulation or gagging. Try to sound "a" from the bottom of the throat.
19|[غ]{.ar}|[g]{.trn}| [غَيْن]{.ar} [gayn]{.trn2} |Somewhat like a "gh" sound but much softer. Try pronouncing [خ]{.ar} but without any scraping.
20|[ف]{.ar}|[f]{.trn}| [فَاء]{.ar} [fAE]{.trn2}| Equivalent to English "f" in "fox".
21|[ق]{.ar}|[q]{.trn}| [قَاف]{.ar} [qAf]{.trn2}| Similar to English "k" in "kite" but further back in the throat.
22|[ك]{.ar}|[k]{.trn}| [كَاف]{.ar} [kAf]{.trn2}| Equivalent to English "k" in "kite".
23|[ل]{.ar}|[l]{.trn}| [لَام]{.ar} [lAm]{.trn2}| Equivalent to English "l" in "light".
24|[م]{.ar}|[m]{.trn}| [مِيم]{.ar} [mIm]{.trn2}| Equivalent to English "m" in "man".
25|[ن]{.ar}|[n]{.trn}| [نُون]{.ar} [nUn]{.trn2}| Equivalent to English "n" in "nut".
26|[ه]{.ar}|[h]{.trn}| [هَاء]{.ar} [hAE]{.trn2}| Equivalent to English "h" in "hat". Much softer than [ح]{.ar}
27|[و]{.ar}|[w]{.trn}/[U]{.trn}| [وَاو]{.ar} [wAw ]{.trn2} |As a consonant it is equivalent to English "w" in "water". It is also a vowel equivalent to English "oo" in "moon".
28|[ي]{.ar}|[y]{.trn}/[I]{.trn}| [يَاء]{.ar} [yAE]{.trn2} |As a consonant it is equivalent to English "y" in "yellow". It is also a vowel equivalent to English "ee" in "meek".

Note that the letters [و]{.ar} [wAw]{.trn2} and [ي]{.ar} [yAE]{.trn2} are both vowels and consonants. But that [ا]{.ar} [Ealif]{.trn2} is only a vowel. The consonant corresponding to [ا]{.ar} [Ealif]{.trn2} is [ء]{.ar} [hamzah]{.trn2}. Although [ء]{.ar} [hamzah]{.trn2} ought to be considered a letter in its own right, it was historically only pronounced and not written. So it is written as a pronunciation mark and is traditionally not considered part of the 28-letter alphabet.

No.|Arabic letter|Tran-scrip-tion|Name |Description
:-|:--|:--|:----|:---------------------------
--|[ء]{.ar}|[E]{.trn}| [هَمْزَة]{.ar} [hamzah]{.trn2} | Technically called a glottal stop, it is the sound of the breath stopping in the beginning of, and between the syllables in, the utterance "oh-oh".

### Pronunciation notes

Some of the sounds are similar to sounds in English but others are very different. Here we will attempt to describe the sounds but we recommend that you learn the correct pronunciation from an experienced Arabic or [#qurEAn]{.trn2} teacher. Online videos may also help in practicing the sounds.

#### [ص]{.ar} [SAd]{.trn2}, [ط]{.ar} [TAE]{.trn2}, and [ظ]{.ar} [PAE]{.trn2}

The letters [س]{.ar} [sIn]{.trn2}, [ت]{.ar} [tAE]{.trn2}, and [ذ]{.ar} [pAl]{.trn2} are pronounced with the mouth and lips in a wide grin. Now try pronouncing them, in turn, with the lips round forming a small circle. The sounds will be emphatic and will be [ص]{.ar} [SAd]{.trn2}, [ط]{.ar} [TAE]{.trn2}, and [ظ]{.ar} [PAE]{.trn2} respectively.

#### [ض]{.ar} [DAd]{.trn2}

[ض]{.ar} [DAd]{.trn2} is thought to be unique to Arabic. There are two ways to pronounce it. The first is similar to an emphatic [د]{.ar}. The second is almost similar to [ظ]{.ar}. We reiterate that it is best to use audio training to help with pronouncing these sounds.

## Writing Arabic words

### Letters in different positions

Arabic is written right-to-left, unlike English and most other languages which are written left-to-right. When writing, the letters in a word are generally joined to each other, except for six out of the 28 letters, which join only to the letter preceding them but not to the letter following them. These six partially-joining letters are [ا، د، ذ، ر، ز، و]{.ar}. 

When joining the letters, letters are modified in order to join to the preceding and following letter. The fully-joining letters can be in four positions:

1. by itself (isolated),
2. in the beginning of a group of joined letters,
3. in the middle of a group of joined letters,
4. in the end of a group of joined letters.

As we just mentioned, six of the letters ([ا، د، ذ، ر، ز، و]{.ar}) don't join to the following letter. So these letters can only occur only in the end of a group of joined letters, or isolated by themselves.

In this book we will show a "Simplified Arabic" writing style where, in each of the four positions, the letter maintains its basic shape and is usually only slightly modified to join to the previous and following letter with horizontal lines. 

To explain the method of modifying the letters when joining them, we will take [ب]{.ar} as an example and start with the isolated form:

Isolated form: [ب]{.ar}

To modify this into the end form, we simply join a horizontal line to the right of the letter:

End form: [ـب]{.ar}. 

To get the middle form, we take the end form [ـب]{.ar} and cut off its tail which is at its left, and replace it with a horizontal line. We also move the dot slightly to get:

Middle form: [ـبـ]{.ar}

And finally, to get the beginning form, we take the middle form [ـبـ]{.ar} and remove the horizontal line at the right:

Beginning form: [بـ]{.ar}

Now most of the letters follow this common technique but a few of them are modified a little further in each form. These, more complicated, letters are [ع، غ، ك، ه، ي]{.ar} and you can study them and the rest of the letters in the table below:

No.|Isolated|End|Middle|Beginning
:--|:----|:----|:----|:----
 1|[ا]{.ar}|[ـا]{.ar}|none|none
 2|[ب]{.ar}|[ـب]{.ar}|[ـبـ]{.ar}|[بـ]{.ar}
 3|[ت]{.ar}|[ـت]{.ar}|[ـتـ]{.ar}|[تـ]{.ar}
 4|[ث]{.ar}|[ـث]{.ar}|[ـثـ]{.ar}|[ثـ]{.ar}
 5|[ج]{.ar}|[ـج]{.ar}|[ـجـ]{.ar}|[جـ]{.ar}
 6|[ح]{.ar}|[ـح]{.ar}|[ـحـ]{.ar}|[حـ]{.ar}
 7|[خ]{.ar}|[ـخ]{.ar}|[ـخـ]{.ar}|[خـ]{.ar}
 8|[د]{.ar}|[ـد]{.ar}|none|none
 9|[ذ]{.ar}|[ـذ]{.ar}|none|none
10|[ر]{.ar}|[ـر]{.ar}|none|none
11|[ز]{.ar}|[ـز]{.ar}|none|none
12|[س]{.ar}|[ـس]{.ar}|[ـسـ]{.ar}|[سـ]{.ar}
13|[ش]{.ar}|[ـش]{.ar}|[ـشـ]{.ar}|[شـ]{.ar}
14|[ص]{.ar}|[ـص]{.ar}|[ـصـ]{.ar}|[صـ]{.ar}
15|[ض]{.ar}|[ـض]{.ar}|[ـضـ]{.ar}|[ضـ]{.ar}
16|[ط]{.ar}|[ـط]{.ar}|[ـطـ]{.ar}|[طـ]{.ar}
17|[ظ]{.ar}|[ـظ]{.ar}|[ـظـ]{.ar}|[ظـ]{.ar}
18|[ع]{.ar}|[ـع]{.ar}|[ـعـ]{.ar}|[عـ]{.ar}
19|[غ]{.ar}|[ـغ]{.ar}|[ـغـ]{.ar}|[غـ]{.ar}
20|[ف]{.ar}|[ـف]{.ar}|[ـفـ]{.ar}|[فـ]{.ar}
21|[ق]{.ar}|[ـق]{.ar}|[ـقـ]{.ar}|[قـ]{.ar}
22|[ك]{.ar}|[ـك]{.ar}|[ـكـ]{.ar}|[كـ]{.ar}
23|[ل]{.ar}|[ـل]{.ar}|[ـلـ]{.ar}|[لـ]{.ar}
24|[م]{.ar}|[ـم]{.ar}|[ـمـ]{.ar}|[مـ]{.ar}
25|[ن]{.ar}|[ـن]{.ar}|[ـنـ]{.ar}|[نـ]{.ar}
26|[ه]{.ar}|[ـه]{.ar}|[ـهـ]{.ar}|[هـ]{.ar}
27|[و]{.ar}|[ـو]{.ar}|none|none
28|[ي]{.ar}|[ـي]{.ar}|[ـيـ]{.ar}|[يـ]{.ar}

You can see that each letter maintains a basic shape and is modified for each of the four positions. 

### Joining the different forms to make a word

Notice that when we modified the isolated form to get to the beginning, middle, and end forms, we added a horizontal line to each or both sides. It is this horizontal line which joines to the horizontal line of the neighboring letter.

As an example, we would like to join the following letters (starting from the right): [م-ع-ش-ر]{.ar} into one word. The first letter is [م]{.ar} so we modify it to its beginning form [مـ]{.ar}. The next two letters are converted to their middle forms [ـعـ، ـشـ]{.ar}. And the last letter [ر]{.ar} is converted to its end form [ـر]{.ar}. Then we join the horizontal lines together and get [مــعــشــر]{.ar}. Usually, when we join letters like this we shorten the horizontal lines so you will generally see the word like this [معشر]{.ar}.

In this example, we needed the beginning, middle, and end forms of the letters. Isolated forms are used in a word when there is a partially-joining letter present that won't join to the following letter. The letter after a partially-joining letter will be in its beginning form even though it is in the middle of a word. But if it too is a partially-joining letter, or it is the last letter in the word then it will take its isolated form.

Let's take a look at some examples where a group of disjoint letters are joined to form a word:

Disjoint | Joined
:------------|:---------
[ذ-ل-ك]{.ar} | [ذلك]{.ar}
[ا-ح-م-د]{.ar} | [احمد]{.ar}
[ر-س-و-ل]{.ar} | [رسول]{.ar}
[و-ز-ي-ر]{.ar} | [وزير]{.ar}
[ر-ا-ز-ق]{.ar} | [رازق]{.ar}

Notice that in the last example, all the letters were in the isolated form.

#### Simplified and Traditional writing styles

We have just shown how letters join to each other with a horizontal line in the Simplified Arabic writing style. Traditional Arabic writing styles are a little more complex than Simplified Arabic: some letters join almost vertically instead of horizontally. But when you get familiar with the Simplified Arabic writing style, if Allah wills, it will not be too difficult for you to read the Traditional Arabic writing style as well.

Here are some comparisions of letters joining to each other in the Simplified Arabic and Traditional Arabic writing styles.


Disjoint | Joined (simplified) | Joined (traditional)
:------------|:---------|:---------
[ت-م-ر]{.ar} | [تمر]{.ar}| [تمر]{lang="ar" dir="rtl" style="font-family: Amiri;"}
[ا-ل-ح-ج-ج]{.ar} | [الحجج]{.ar} | [الحجج]{lang="ar" dir="rtl" style="font-family: Amiri;"}
[ا-ل-م-ا-س]{.ar} | [الماس]{.ar} | [الماس]{lang="ar" dir="rtl" style="font-family: Amiri;"}
[ل-م-ح-ة]{.ar} | [لمحة]{.ar} | [لمحة]{lang="ar" dir="rtl" style="font-family: Amiri;"}
[ب-ح-ر]{.ar} | [بحر]{.ar} | [بحر]{lang="ar" dir="rtl" style="font-family: Amiri;"}
[س-ح-ر]{.ar} | [سحر]{.ar} | [سحر]{lang="ar" dir="rtl" style="font-family: Amiri;"}
[ف-ي]{.ar} | [في]{.ar} | [في]{lang="ar" dir="rtl" style="font-family: Amiri;"}

```{=latex}
\begin{longtable}[]{@{}lll@{}}
\toprule
Disjoint & Joined (simplified) & Joined (traditional)\tabularnewline
\midrule
\endhead
\arabicfont{ت-م-ر} & \arabicfont{تمر} &
\tradarab{تمر}\tabularnewline
\arabicfont{ا-ل-ح-ج-ج} & \arabicfont{الحجج} &
\tradarab{الحجج}\tabularnewline
\arabicfont{ا-ل-م-ا-س} & \arabicfont{الماس} &
\tradarab{الماس}\tabularnewline
\arabicfont{ل-م-ح-ة} & \arabicfont{لمحة} &
\tradarab{لمحة}\tabularnewline
\arabicfont{ب-ح-ر} & \arabicfont{بحر} &
\tradarab{بحر}\tabularnewline
\arabicfont{س-ح-ر} & \arabicfont{سحر} &
\tradarab{سحر}\tabularnewline
\arabicfont{ف-ي} & \arabicfont{في} &
\tradarab{في}\tabularnewline
\bottomrule
\end{longtable}
```

### Looped [tAE]{.trn2}

Looped [tAE]{.trn2} [ة]{.ar} is a special letter which is merged from two letters of the alphabet. It is a [tAE]{.trn2} [ت]{.ar} but it is written as a [ه]{.ar} [hAE]{.trn2} with two dots above it. Looped [tAE]{.trn2} [ة]{.ar} is pronounced exactly as a [ت]{.ar} [tAE]{.trn2}, except when it is at the end of a sentence in which case it is pronounced as a [ه]{.ar} [hAE]{.trn2} as we'll explain later, if [#allAh]{.trn2} wills. Looped [tAE]{.trn2} occurs only at the end of a word so it has only an end form and an isolated form (used when the letter before it is a partially-joining letter). 

Examples:

+ [فاطمة]{.ar}
+ [شجرة]{.ar}
+ [فتاة]{.ar}

[ت]{.ar} is called "open [tAE]{.trn2}" when needed, to differentiate it from looped [tAE]{.trn2} [ة]{.ar}.

### Writing [hamzah]{.trn2}

We have mentioned that [hamzah]{.trn2} was a later addition to the Arabic alphabet and originally it was only sounded and not written. [#hamzah]{.trn2} can be written in a number of different ways:

1. "Seated" above (or below) a vowel letter: [#hamzah]{.trn2} can be written above the vowel letters thus: [أ ؤ ئ]{.ar}. When written over [ي]{.ar}, the [ي]{.ar} will not have any dots, thus: [ئـ، ـئـ، ـئ]{.ar}. It may also be written under an [Ealif]{.trn2} thus: [إ]{.ar}. Examples: [أفعال]{.ar}, [سؤلك]{.ar}, [فئة]{.ar}, [إن]{.ar}.
2. "Unseated" after a letter. This has two sub cases:
   a. Standalone, after a partially-joining letter or at the end of a word. Examples: [تساءل]{.ar}, [توءم]{.ar}, [عبء]{.ar}.
   a. Inline, in the middle of a word after a fully-joining letter. In this case [hamzah]{.trn2} is written above the horizontal line that joins the letters. Examples: [خطيـٔة]{.ar}, [شيـٔا]{.ar}, [بريـٔين]{.ar}.

In all cases it is pronounced the same. There are actually a set of fairly complicated rules that determine which of the above ways to choose when writing [hamzah]{.trn2}. We present these rules in Appendix \@ref(hamzarules). We recommend that for now, you memorize the spelling of each word that we present that contains a [hamzah]{.trn2}. When you are sufficiently advanced, and curious enough, you may refer to Appendix \@ref(hamzarules) to learn the full set of rules.

### Disambiguating letters that look similar

Some letters are very similar to each other and only differ in their dots or other slight differences. You should take care to distinguish between these letters. We will describe their similarities and differences here.

The letters [ب]{.ar}, [ت]{.ar}, and [ث]{.ar} differ only in their dots and are otherwise identical in all positions. [ن]{.ar} and [ي]{.ar} are similar in initial and middle positions to [ب]{.ar}, [ت]{.ar}, and [ث]{.ar} but differ from them and from each other in isolated and final positions. Compare all five in the table below:

Isolated | End | Middle | Beginnning
:--------|:----|:-------|:----------
[ب]{.ar}| [ـب]{.ar}| [ـبـ]{.ar}| [بـ]{.ar}
[ت]{.ar}| [ـت]{.ar}| [ـتـ]{.ar}| [تـ]{.ar}
[ث]{.ar}| [ـث]{.ar}| [ـثـ]{.ar}| [ثـ]{.ar}
[ن]{.ar}| [ـن]{.ar}| [ـنـ]{.ar}| [نـ]{.ar}
[ي]{.ar}| [ـي]{.ar}| [ـيـ]{.ar}| [يـ]{.ar}

These groups of letters  differ too, only in their dots:

+ [ج]{.ar}, [ح]{.ar}, and [خ]{.ar}
+ [د]{.ar} and [ذ]{.ar}
+ [ر]{.ar} and [ز]{.ar}
+ [س]{.ar} and [ش]{.ar}
+ [ص]{.ar} and [ض]{.ar}
+ [ط]{.ar} and [ظ]{.ar}
+ [ع]{.ar} and [غ]{.ar}

The letters [ف]{.ar} and [ق]{.ar} are similar in the initial and middle positions except for the dots. But in the isolated and final positions, the tail of [ق]{.ar} goes lower than that of [ف]{.ar}.

Isolated | End | Middle | Beginnning
:--------|:----|:-------|:----------
[ف]{.ar}| [ـف]{.ar}| [ـفـ]{.ar}| [فـ]{.ar}
[ق]{.ar}| [ـق]{.ar}| [ـقـ]{.ar}| [قـ]{.ar}

Be careful also not to confuse [غ]{.ar} and [ف]{.ar} in their middle forms. The loop for [ف]{.ar} is round where it is triangular and flat-topped for [غ]{.ar} (as it is for [ع]{.ar}). Compare their middle forms in the table below:

Isolated | Middle
:--------|:------
[غ]{.ar}| [ـغـ]{.ar}
[ف]{.ar}| [ـفـ]{.ar}

The letters [Ealif]{.trn2} [ا]{.ar} and [lAm]{.trn2} [ل]{.ar} could also be confused for each other. Their forms are shown here again for easy comparison:

Isolated | End | Middle | Beginnning
:--------|:----|:-------|:----------
[ا]{.ar}| [ـا]{.ar}| none | none
[ل]{.ar}| [ـل]{.ar}| [ـلـ]{.ar}| [لـ]{.ar}

### Joining [lAm]{.trn2} and [Ealif]{.trn2}

When the letter [Ealif]{.trn2} follows [lAm]{.trn2} we would expect them to be joined like this [ل+ا]{.ar} &rarr; [لـا]{.ar}. But actually, they are joined in a special way 

[ل+ا]{.ar} &rarr; [لا]{.ar}

When the combination occurs at the end of a group of joined letters, it will appear thus: 

[ـلا]{.ar}

Examples:

+ [ألا]{.ar}
+ [الإيمان]{.ar}
+ [الصلاة]{.ar}

## Vowels and pronunciation marks.

### Short Vowels

Arabic has six vowels. There are three short vowels which don't have letters in the alphabet. Instead they are shown with pronunciation marks:

1.  [a]{.trn} as the first vowel in English “manipulate”, written with an [a]{.trn}-mark [◌َ]{.ar} which is a small diagonal line above the letter like [مَـ]{.ar} [ma]{.trn}.
1.  [i]{.trn} as in English “bit”, written with an [i]{.trn}-mark [◌ِ]{.ar} which is a small diagonal line under the letter like [بِـ]{.ar} [bi]{.trn}.
1.  [u]{.trn} as in English “put”, written with an [u]{.trn}-mark [◌ُ]{.ar} which is like a tiny [و]{.ar} [wAw]{.trn2} above the letter like [فُـ]{.ar} [fu]{.trn}.

Examples of words with short vowels:

+ [فَتَحَ]{.ar} [fataHa]{.trn}
+ [عَمِلَ]{.ar} [eamila]{.trn}
+ [قُتِلَ]{.ar} [qutila]{.trn}

### Long Vowels

There are also three long vowels which are part of the alphabet:

1.  [A]{.trn} generally written with an unmarked [ا]{.ar} [Ealif]{.trn2} and with the preceding letter having an [a]{.trn}-mark. Example [مَا]{.ar} [mA]{.trn}. This vowel is mostly pronounced like the vowel in English “man”. If however, it comes after these letters [خ،ر،ص،ض،ط،ظ،غ،ق]{.ar} it is pronounced like English "awe".
1.  [I]{.trn} like in English “meek” written with an unmarked [ي]{.ar} [yAE]{.trn2} with the preceding letter having an [i]{.trn}-mark. Example [فِي]{.ar} [fI]{.trn}.
1.  [U]{.trn} like in English “moon” written with an unmarked [و]{.ar} [wAw]{.trn2} with the preceding letter having an [u]{.trn}-mark. Example [ذُو]{.ar} [pU]{.trn}.

Examples of words with long and short vowels:

+ [هَارُونُ]{.ar} [hArUnu]{.trn}
+ [كَذَا]{.ar} [kapA]{.trn}
+ [سَرَادِيبَ]{.ar} [sarAdIba]{.trn}

#### [A]{.trn} vowel written with a small [Ealif]{.trn2}

Sometimes the [A]{.trn} vowel is written as a small [Ealif]{.trn2} [◌ٰ]{.ar}, called a "dagger [Ealif]{.trn2}", instead of a regular [Ealif]{.trn2} [ا]{.ar}. This is done only for a few commonly used words. Here are some examples:

+ [هَـٰذَا]{.ar} [hApA]{.trn}
+ [ذَ ٰلِكَ]{.ar} [pAlika]{.trn}

#### [A]{.trn} vowel written with a [yAE]{.trn2} {#a-vowel-written-with-a-ya}
In some other words, the [A]{.trn} vowel is written with a [yAE]{.trn2} instead of an [Ealif]{.trn2} [ا]{.ar}. When this happens, we will write the [yAE]{.trn2} without its dots and write a dagger [Ealif]{.trn2} [◌ٰ]{.ar} above it, like this [ىٰ]{.ar}. Here are some examples:

+ [عَلَىٰ]{.ar} [ealA]{.trn}
+ [رَمَىٰ]{.ar} [ramA]{.trn}

### Zero-vowel written with a [0]{.txt}-mark

As we have seen above if an Arabic letter has a vowel after it it will take one of the three pronunciation marks: [◌َ]{.ar}, [◌ِ]{.ar}, [◌ُ]{.ar}. If, however, there is no vowel after the letter we will put a zero-vowel [0]{.txt}-mark on it [◌ْ]{.ar}. This mark can generally only occur if there is a short vowel before the letter. Examples:

+ [كَمْ]{.ar} [kam]{.trn}
+ [مُنْذُ]{.ar} [munpu]{.trn}
+ [مِنْهُمْ]{.ar} [minhum]{.trn}
+ [مِنْهَا]{.ar} [minhA]{.trn}

### Semi-vowels

Arabic has two short semi-vowels:

1. [aw]{.trn} like in English “show”. This is written with a [wAw]{.trn2} with a [0]{.txt}-mark on it and a [A]{.trn} vowel before it. Example [لَوْ]{.ar} [law]{.trn}. 
2. [ay]{.trn} like in English “bait”. This is written with a [yAE]{.trn2} with a [0]{.txt}-mark on it and a [A]{.trn} vowel before it. Example [كَيْ]{.ar} [kay]{.trn}. 
Examples with short semi-vowels:

+ [وَيْحَكَ]{.ar} [wayHaka]{.trn}
+ [غَيْرُهُ]{.ar} [gayruhu]{.trn}
+ [قَوْلُهُ]{.ar} [qawluhu]{.trn}

It also has two long semi-vowels:

1. [Aw]{.trn} like in English “cow”. This is written with a [wAw]{.trn2} with a [0]{.txt}-mark on it and a [A]{.trn} vowel before it. Example [وَاوْ]{.ar} [wAw]{.trn}. 
2. [Ay]{.trn} like in English “bye”. This is written with a [yAE]{.trn2} with a [0]{.txt}-mark on it and a [A]{.trn} vowel before it. Example [شَايْ]{.ar} [cAy]{.trn}.

These long semi-vowels are rare and may only occur at the end of a sentence.

### Doubled letters

A word may contain "doubled" letters. This is when the same letter occurs, one after the other; the first letter has a [0]{.txt}-mark, and the second letter has a vowel. For example, in the word [قَتْتَلَ]{.ar} [qattala]{.trn}, the letter [ت]{.ar} is doubled. When this occurs, we actually only write the letter once and put a "doubling mark" [◌ّ]{.ar} on it, like so: [قَتَّلَ]{.ar} [qattala]{.trn}. When pronouncing this word, stop at and stress the doubled letter [qattala]{.trn} and make sure it does not sound like the undoubled letter in [قَتَلَ]{.ar} [qatala]{.trn}. Examples with doubled letters:

+ [كَبَّرَ]{.ar} [kabbara]{.trn}
+ [حَدُّهُ]{.ar} [Hadduhu]{.trn}
+ [فَعَّالَ]{.ar} [faeeAla]{.trn}
+ [سِكِّينُ]{.ar} [sikkInu]{.trn}. Note that the [i]{.trn}-mark is below the doubling mark but above the letter [ك]{.ar}. This is the most common way to write this, although having the [i]{.trn}-mark below the letter is also sometimes done as well. (In this case, the doubling mark will still be above the letter.)
+ [سَفُّودُ]{.ar} [saffUdu]{.trn}
+ [ضَالِّينَ]{.ar} [DAllIna]{.trn}
+ [مُزَّمِّلُ]{.ar} [muzzammilu]{.trn}

### [n]{.trn}-marks

Arabic also has three distinctive pronunciation marks, collectively called [n]{.trn}-marks.

1. [an]{.trn}-mark [◌ً]{.ar}
1. [in]{.trn}-mark [◌ٍ]{.ar}
1. [un]{.trn}-mark [◌ٌ]{.ar}

These [n]{.trn}-marks may only occur on a letter at the end of a word. They are pronounced as a short vowel ([a]{.trn}, [i]{.trn}, or [u]{.trn}) followed by an [n]{.trn}. For example, [سَالِمٌ]{.ar} [sAlimun]{.trn}, [سَالِمٍ]{.ar} [sAlimin]{.trn}.

As a spelling rule, if a word ends with an [an]{.trn} mark, we will generally add a silent [Ealif]{.trn2} after it, for example [سَالِم]{.ar} becomes [سَالِمًا]{.ar} [sAliman]{.trn}. This is done for all words except:

1. If the word ends with a looped [tAE]{.trn2} [ة]{.ar}. In this case we don't add the silent [Ealif]{.trn2}. For example, [غَاضِبَة]{.ar} becomes [غَاضِبَةً]{.ar} [gADibatan]{.trn}, not [غَاضِبَةًا]{.ar} or [غَاضِبَتًا]{.ar}.

2. If the word ends with a [A]{.trn} vowel, whether written with an [Ealif]{.trn2} [ا]{.ar} or  as a [yAE]{.trn2} with dagger [Ealif]{.trn2} [ىٰ]{.ar}. In this case, the [an]{.trn} mark is put on the letter before the [Ealif]{.trn2} [ا]{.ar} or [yAE]{.trn2} [ىٰ]{.ar} and the final vowel letter becomes silent and is not pronounced. For example, [مُصْطَفَىٰ]{.ar} becomes [مُصْطَفًى]{.ar} [muSTafan]{.trn}, [عَصَا]{.ar} becomes [عَصًا]{.ar} [eaSan]{.trn}.

2. If the word ends with a [hamzah]{.trn2}. In this case, we might or might not write a silent [Ealif]{.trn2}, depending on the following rules:

   a. If there is an [Ealif]{.trn2} before an unseated [hamzah]{.trn2} [اء]{.ar}, then we don't add a silent [Ealif]{.trn2}. For example [دَاء]{.ar} becomes [دَاءً]{.ar} [dAEan]{.trn}, not [دَاءًا]{.ar}.

   b. Otherwise, we add a silent [Ealif]{.trn2} after the [hamzah]{.trn2}. However, this may affect the writing of the [hamzah]{.trn2}, for example [مُبْتَدَأ]{.ar} becomes [مُبْتَدَءًا]{.ar} [mubtadaEan]{.trn}. This is discussed further in Appendix \@ref(hamzarules).

Here are some examples of words with [n]{.trn}-marks:

+ [سَعْدٌ]{.ar}  [saedun]{.trn}   \vphantom{\huge J}
+ [ضَرْبًا]{.ar} [Darban]{.trn}   \vphantom{\huge J}
+ [قَاضٍ]{.ar}  [qADin]{.trn}    \vphantom{\huge J}
+ [سَعَةً]{.ar}  [saeatan]{.trn}  \vphantom{\huge J}
+ [دُعَاءً]{.ar} [dueAEan]{.trn}  \vphantom{\huge J}
+ [ٱِمْرَءًا]{.ar} [imraEan]{.trn} \vphantom{\huge J}
+ [شَيْـًٔا]{.ar} [cayEan]{.trn}   \vphantom{\huge J}
+ [سُوءًا]{.ar} [sUEan]{.trn}    \vphantom{\huge J}
+ [غَبَنٌ]{.ar} [gabanun]{.trn}   \vphantom{\huge J}

## Connecting [hamzah]{.trn2}

Some words in arabic begin with a [0]{.txt}-mark. When this occurs a connecting [hamzah]{.trn2} [ٱ]{.ar} (written as a tiny [صـ]{.ar} on an [Ealif]{.trn2}) is put before it. If this word comes in the beginning of the sentence the connecting alif is pronounced as a [hamzah]{.trn2}. Otherwise this connecting [hamzah]{.trn2} is not pronounced and the word is connected to the final vowel of the previous word in pronunciation. In this tutorial we will transcribe the connecting [hamzah]{.trn2} with a hyphen "-". Examples of connecting [hamzah]{.trn2}:

[ٱِفْتَحِ ٱلْبَابَ]{.ar}  
[EiftaHi -lbAba]{.trn}

[ٱُنْظُرْ]{.ar}  
[EunPur]{.trn}

If the previous word does not end with a vowel, then a helper vowel is added. The most common helper vowel is [◌ِ]{.ar}. Example:

[زَيْدٌ ٱلْكَرِيمُ]{.ar}  
[zayduni -lkarImu]{.trn}

When one word ends in a long vowel and the next word begins with a connecting [hamzah]{.trn2}, the long vowel becomes a short vowel in pronunciation, but in writing the long vowel’s letter is retained. For example:

[ أَخَذَ مِنَّا ٱلْكِتَابَ]{.ar}  
[Eaxapa minna -lkitAba]{.trn}

[ذُو ٱلْقَرْنَيْنِ]{.ar}  
[pu -lqarnayni]{.trn}

[فِي ٱلْبَيْتِ]{.ar}  
[fi -lbayti]{.trn}

## Pronouncing the end of a sentence

When a word is at the end of a sentence and it ends with a long vowel, then the final long vowel is pronounced normally. However, when a word at the end of a sentence does not end with a long vowel, then the final letter's pronunciation mark is pronounced as a [0]{.txt}-mark when vocalizing the sentence. If the final letter is a looped [tAE]{.trn2} [ة]{.ar} then it is pronounced as a [ه]{.ar} [hAE]{.trn2} with a [0]{.txt}-mark. 

This change in pronunciation is only vocal, it does not affect how we write the pronunciation mark. Here we give some examples of words pronounced if they were at the end of a sentence:

[فَتْحُ]{.ar}  
[fatH]{.trn}

[عُقْبَةٌ]{.ar}  
[euqbah]{.trn}

[وَالِدَايَ]{.ar}  
[wAlidAy]{.trn}

[وَالِدَيَّ]{.ar}  
[wAlidayy]{.trn}

If however, the final letter's pronunciation mark is a [an]{.trn} mark then it is pronounced as a long-[A]{.trn} vowel. The only exception is if the final letter were looped [tAE]{.trn2} [ةً]{.ar}, in which case it is then pronounced as a [hAE]{.trn2} with a [0]{.txt}-mark [هْ]{.ar}. Here are examples of words with [an]{.trn} marks pronounced as if they were at the end of a sentence.

[مَفْعُولًا]{.ar}  
[mafeUlA]{.trn}

[سَاجِدًا]{.ar}  
[sAjidA]{.trn}

[مَرْفُوعَةً]{.ar}  
[marfUeah]{.trn}

Note that the above exception is only for looped [tAE]{.trn2}. If a [hamzah]{.trn2} with an [an]{.trn} mark occurs at the end of a word, then it too will be pronounced as if it had a long-[A]{.trn} vowel after it. Such is the case, whether or not a silent [Ealif]{.trn2} is written after the [hamzah]{.trn2}. Examples:

+ [مُبْتَدَءًا]{.ar} is pronounced [mubtadaEA]{.trn}
+ [دُعَاءً]{.ar} is pronounced [dueAEA]{.trn}

Similarly, if the word has a final [yAE]{.trn2} that represents the long-[A]{.trn} vowel, and the letter before has an [an]{.trn} mark, it is pronounced with the long-[A]{.trn} vowel at the end of the sentence. For example:

+ [مُصْطَفًى]{.ar} is pronounced [muSTafA]{.trn}

Except in this section, we will usually transcribe Arabic into English letters without modifiying the transcription for the last word in the sentence. This is because the last vowel mark is helpful for us to learn the grammatical function of the word. But when saying the sentence out aloud you should pronounce the ending of the final word as we have just described.

For example, the sentence:  
[ذَهَبَ إِلَى ٱلْبَيْتِ]{.ar}

will be transcribed, in the remainder of this book, as:  
[pahaba Eila -lbayti]{.trn}

but should be pronounced as  
[pahaba Eila -lbayt]{.trn}

## [#qurEAn]{.trn2}ic script

In printed volumes of the [#qurEAn]{.trn2}, the spelling words is a little different from non-[#qurEAn]{.trn2}ic Standard Arabic. The reasons for this are beyond the scope of this book. Here we’ll just give a few examples and note that these differences are typically only found in printed volumes of the [#qurEAn]{.trn2}.

Standard Arabic | [#qurEAn]{.trn2}ic Arabic
:---------|:---------
[ٱلصَّلَاةَ]{.ar}| [ٱلصَّلَوٰةَ]{.ar}
[ٱلسَّمَاوَاتِ]{.ar}| [ٱلسَّمَـٰوَ ٰتِ]{.ar}
[يَا ٱبْنَ أُمَّ]{.ar} | [يَبْنَؤُمَّ]{.ar}


<!--chapter:end:srcrmd/script.Rmd-->

# Nouns
<!-- title not called "Common nouns" because concepts are general to all nouns. However, only common nouns are discussed here.-->
## Introduction

A noun is a kind of word that is the name of something or someone.

Here are some examples of common nouns in Arabic:

Arabic word | Transcription|Definition
:-----------|:-----------|:----------------
[رَجُل]{.ar}  |[rajul]{.trn}     |man
[كِتَاب]{.ar} |[kitAb]{.trn}     |book
[بَيْت]{.ar}  |[bayt]{.trn}      |house
[شَجَرَة]{.ar} |[cajarah]{.trn}   |tree
[صَبْر]{.ar}  |[Sabr]{.trn}      |patience
[وَقْت]{.ar}  |[waqt]{.trn}      |time
[طَعَام]{.ar} |[TaeAm]{.trn}     |food
[ٱِبْن]{.ar}  |[Eibn]{.trn}      |son

Note that the final letter in each word, above, does not have a vowel mark. This is because, the final vowel mark is actually variable, as we shall see later in this chapter.

When we discuss nouns outside of sentences we shall pronounce the looped [ة]{.ar} as a [h]{.trn}. Therefore, 
[شَجَرَة]{.ar} "tree", in isolation, is pronounced [cajarah]{.trn}, not [cajarat]{.trn}.

Some nouns begin with a connecting [hamzah]{.trn2}, for example: [ٱِبْن]{.ar} [Eibn]{.trn} "son". When in the beginning of a sentence, the connecting [hamzah]{.trn2} will be pronounced with an [i]{.trn}-mark [◌ِ]{.ar}.

## Definiteness

When talking about nouns it is necessary to introduce a topic called _definiteness_.

A noun is _definite_ when the person or thing it refers to is known. For example, if you say, "The man arrived." then the usage of the word "the" before "man" tells us that the man is known to us. Therefore the noun "man" is definite in this sentence.

Conversely, if we had said "A man arrived." then the use of "a" before "man" tells us that the man is unknown to us. Therefore "man" is indefinite in this sentence.

"The" is called the _definite article_ and "a" is called the _indefinite article_.

### Definite nouns in Arabic

The definite article in Arabic is 
[ٱَلْ]{.ar} [Eal]{.trn}. It corresponds to the English definite article "the".
In order to make a noun definite, we attach 
[ٱَلْ]{.ar} [Eal]{.trn}
to its beginning.

For example, the definite noun "the book" in Arabic is [ٱَلْكِتَاب]{.ar} [EalkitAb]{.trn}.

[ٱَلْ]{.ar} [Eal]{.trn}
begins with a connecting [hamzah]{.trn2}; the [hamzah]{.trn2} will be pronounced only in the beginning of a sentence. And when it occurs in the beginning of a sentence, the [hamzah]{.trn2} is pronounced with a [◌َ]{.ar} a-mark.

#### Sun letters and moon letters

The noun “man” in Arabic is [رَجُل]{.ar} [rajul]{.trn}. To make this noun definite, we add [ٱَلْ]{.ar} [Eal]{.trn} to the beginning of the word. But instead of becoming [ٱَلْرَجُل]{.ar} [Ealrajul]{.trn} the word becomes [ٱَلرَّجُل]{.ar} [Earrajul]{.trn}. The [ل]{.ar} in [ٱَلْ]{.ar} becomes silent and the [ر]{.ar} gets doubled. This happens because the first letter [ر]{.ar} in the word [رَجُل]{.ar} [rajul]{.trn} is from a group of letters called "sun letters". For all nouns beginning with sun letters, when [ٱَلْ]{.ar} [Eal]{.trn} is put in the beginning, the [ل]{.ar} in [ٱَلْ]{.ar} becomes silent and the sun letter becomes doubled.

The rest of the letters in the alphabet are called "moon letters" and for words that begin with moon letters, the [ل]{.ar} in [ٱَلْ]{.ar} does not become silent and the moon letter does not become doubled. For example, [ك]{.ar} is a moon letter and we have already seen that [كِتَاب]{.ar} [kitAb]{.trn} "book" becomes [ٱَلْكِتَاب]{.ar} [EalkitAb]{.trn} "the book".

The sun letters are [ت ث د ذ ر ز س ش ص ض ط ظ ل ن]{.ar}.  
The moon letters are [ء ب ج ح خ ع غ ف ق ك م ه و ي]{.ar}.

The names "sun letters" and "moon letters" were given because of the Arabic words for "sun" and "moon" respectively. "The sun" in Arabic is [ٱَلشَّمْس]{.ar} [Eaccams]{.trn} which begins with [ش]{.ar} which causes the [ل]{.ar} in [ٱَلْ]{.ar} to be silent. "The moon" is [ٱَلْقَمَر]{.ar} [Ealqamar]{.trn} which begins with [ق]{.ar} which does not cause the [ل]{.ar} in [ٱَلْ]{.ar} to be silent. Thus [ش]{.ar} represents the sun letters and [ق]{.ar} represents the moon letters.

Here are some examples of words that begin with sun letters:

Noun | Definite noun
:-----------|:-----------
[رَجُل]{.ar} [rajul]{.trn} "man" | [ٱَلرَّجُل]{.ar} [Earrajul]{.trn} "the man"  
[تَاجِر]{.ar} [tAjir]{.trn} "trader" | [ٱَلتَّاجِر]{.ar} [EattAjir]{.trn} "the trader"  
[لُعْبَة]{.ar} [luebah]{.trn} "toy" | [ٱَللُّعْبَة]{.ar} [Ealluebah]{.trn} "the toy"  

#### The definite article [ٱَلْ]{.ar} [Eal]{.trn} with nouns with an initial connecting [hamzah]{.trn2} {#the-definite-article-with-nouns-with-an-initial-connecting-hamzah}

If the definite article [ٱَلْ]{.ar} [Eal]{.trn} is with prefixed to nouns that have an initial connecting [hamzah]{.trn2}, then the [ل]{.ar} shall no longer have an [0]{.txt}-mark [◌ْ]{.ar}. Instead it shall have an [i]{.trn}-mark [◌ِ]{.ar}. Example:

[ٱَلِٱبْن]{.ar}  
[Eali-bn]{.trn}  
"the son"

### Indefinite nouns in Arabic

Arabic has no indefinite article corresponding to the English indefinite article "a". In order to make a noun indefinite in Arabic, it is simply written or pronounced without the definite article
[ٱَلْ]{.ar} [Eal]{.trn}.
For example, [كِتَاب]{.ar} [kitAb]{.trn} "a book".

<!--For convenience, outside of sentences, we may simply translate [كِتَاب]{.ar} [kitAb]{.trn} as "book" instead of "a book".-->

### Differences in definiteness between Arabic and English

The articles "a" and "the" are types of words called _determiners_. Besides "a" and "the", English has other determiners like "some", "this", "that", etc. that can make a noun definite or indefinite.
For example:

"This man gave that boy some food."

In the above sentence "man" and "boy" are definite, and "food" is indefinite.

English can also have definite or indefinite nouns without determiners. The definiteness of the noun is then determined by the meaning of the sentence. Consider, for example, the sentence:

"Time is valuable."

Here, we are not talking about some indefinite amount of time, but rather the general concept of time, which is known to us. Therefore, the noun "time" here is definite.

Consider now the sentence:

"We don't have to leave just yet; we have time."

Here, "time" has an indefinite meaning "[some] time".
<!--
This English usage of an indefinite meaning without an indefnite article is especially true with plurals. For example, "There are books in the bag." Here the intended meaning is "There are [some] books in the bag." Consequently, in Arabic, we will use the indefinite noun here: [كُتُب]{.ar} [kutub]{.trn} "[some] books" not [ٱَلْكُتُب]{.ar} [Ealkutub]{.trn} "the books".

However, there are times when English uses a plural without a definite or indefinite article, and a general meaning is intended. For example, "Books contain knowledge." In this case, in Arabic we will use the definite noun [ٱَلْكُتُب]{.ar} [Ealkutub]{.trn} "the books".
-->

As opposed to this complicated situation in English, Arabic uses only the definite article
[ٱَلْ]{.ar} [Eal]{.trn}
to make common nouns definite.
So when translating sentences from English to Arabic, you must first determine whether the noun is definite or not in English, and then use 
[ٱَلْ]{.ar} [Eal]{.trn}
when the noun is definite.

Examples:

+ "This man gave that boy some food."
  + man: definite; Arabic: [ٱَلرَّجُل]{.ar} [Earrujul]{.trn}
  + boy: definite; Arabic: [ٱَلْغُلَام]{.ar} [EalgulAm]{.trn}
  + water: indefinite; Arabic: [طَعَام]{.ar} [TaeAm]{.trn}

+ "Time is valuable."
  + time: definite; Arabic: [ٱَلْوَقْت]{.ar} [Ealwaqt]{.trn}

+ "We don't have to leave just yet; we have time."
  + time: indefinite; Arabic: [وَقْت]{.ar} [waqt]{.trn}

## State

Nouns in Arabic can be in one of three _states_. You may think of the grammatical states of nouns like the physical states of matter: solid, liquid, and gas. The same water can be in a solid ice state, or a liquid water state, or a gaseous water vapour state. Similarly, the same noun, in Arabic, may be in one of the three grammatical states:

1. u-state: indicated by a [u]{.trn}-mark [◌ُ]{.ar} (for definite nouns) and an [un]{.trn}-mark [◌ٌ]{.ar} (for indefinite nouns) on the final letter of the word.
2. a-state: indicated by an [a]{.trn}-mark [◌َ]{.ar} (for definite nouns) and an [an]{.trn}-mark [◌ً]{.ar} (for indefinite nouns) on the final letter of the word.
3. i-state: indicated by an [i]{.trn}-mark [◌ِ]{.ar} (for definite nouns) and an [in]{.trn}-mark [◌ٍ]{.ar} (for indefinite nouns) on the final letter of the word.

Here are the nouns "a book" and "the book" in their three states:

State         | Indefinite "a book" | Definite "the book"
:-------------|:-----------------|:--------------
u-state       |[كِتَابٌ]{.ar} [kitAbun]{.trn}  |[ٱَلْكِتَابُ]{.ar} [EalkitAbu]{.trn} 
a-state       |[كِتَابًا]{.ar} [kitAban]{.trn} |[ٱَلْكِتَابَ]{.ar} [EalkitAba]{.trn} 
i-state       |[كِتَابٍ]{.ar} [kitAbin]{.trn}  |[ٱَلْكِتَابِ]{.ar} [EalkitAbi]{.trn} 


The choice of which state a noun is in depends on its function in a sentence. For example, if the noun is a subject of a sentence, it will usually be in the u-state. And if it is used adverbially, it will often be in the a-state. And if it occurs after a preposition, it will be in the i-state. We will learn more about putting nouns in their different states throughout this book. 
Generally speaking, the u-state is the normal state. And there needs to be a reason to take the noun out of the u-state and into one of the other states.

<!--
## Flexibility of nouns

Most nouns behave as described above: their endings change with their state. These nouns are called _flexible_ nouns. In later chapters, we will learn about some nouns whose endings only partially change, or don't change at all, with their state. They will be called _semi-flexible_ nouns and _rigid_ nouns respectively.
-->
<!--
Don't use because english uses different words, not modifying the ending of the same word:
By the way, some English words have state too: the words The words "he" and "him" refer to the same person. But sometimes we will use "he" and sometimes we will use "him", depending on the function of the word in the sentence. For example,

+ "He talked to the man." The word "he" is used here because it is the subject.
+ "The man gave the book to him." The word "him" is used here because it comes after the preposition "to".

In English grammar, _state_ is called _case_ instead. The above examples in English may help you in understanding the concept of _state_ in Arabic.
-->
<!--
## Usage of definite and indefinite nouns

Consider the noun "time". In English we can make this noun definite using the definite article "the", for example, "The time to act is now." When translating this sentence to Arabic, we will correspondingly use the definite noun: [ٱَلْوَقْت]{.ar} [Ealwaqt]{.trn} "the time".

In English, we can make "time" indefinite using indefinite articles like "a" or "some". For example, "There is a time for work and a time for play." and "We have some time before we need to leave." When translating these sentences to Arabic we will correspondingly use the indefinite noun in both these sentences: [وَقْت]{.ar} [waqt]{.trn} "a time".

Consider now a third scenario: in English we can also use the word "time" with a general meaning without a definite or indefinite article. For example, "Time is money." However, in Arabic, a noun must be either definite or indefinite. So we must choose between [ٱَلْوَقْت]{.ar} [Ealwaqt]{.trn} "the time" and [وَقْت]{.ar} [waqt]{.trn} "a time". In Arabic, [وَقْت]{.ar} [waqt]{.trn}, being indefinite, can only mean "a time" or "some time". So [ٱَلْوَقْت]{.ar} [Ealwaqt]{.trn} is then used when we wish to say "time" with a general meaning. This means that, in Arabic the definite noun is used in two ways: 

i. When the definite meaning is desired. For example, "We met at the time we had agreed upon." (Use [ٱَلْوَقْت]{.ar} [Ealwaqt]{.trn} "the time".)
ii. When a general meaning is desired. For example, "There is nothing more valuable than time." (Again, use [ٱَلْوَقْت]{.ar} [Ealwaqt]{.trn} "the time".)

Conversely, the indefinite nouns is used only when an indefinite meaning is desired. For example, "We agreed to meet at a certain time."(Use [وَقْت]{.ar} [waqt]{.trn} "a time".)

In a similar manner, the nouns "home" or "school" are often used in English without either "the" or "a". For example, "He goes to school." and "She went home.". In these cases, we will us the definite article [ٱَلْ]{.ar} in Arabic. So we will say [ٱَلْبَيْت]{.ar} [Ealbayt]{.trn} "the home" for English "home" and [ٱَلْمَدْرَسَة]{.ar} [Ealmadrasah]{.trn} "the school" for English "school".

But there is an additional complication: note that English often does not use an indefinte article, even when an indefinite meaning is intended. For example, "We don't need to leave right now; we have time." meaning "we have [_some_] time." Because of the indefinite meaning intended we will use [وَقْت]{.ar} [waqt]{.trn} "a time" here.

This English usage of an indefinite meaning without an indefnite article is especially true with plurals. For example, "There are books in the bag." Here the intended meaning is "There are [some] books in the bag." Consequently, in Arabic, we will use the indefinite noun here: [كُتُب]{.ar} [kutub]{.trn} "[some] books" not [ٱَلْكُتُب]{.ar} [Ealkutub]{.trn} "the books".

However, there are times when English uses a plural without a definite or indefinite article, and a general meaning is intended. For example, "Books contain knowledge." In this case, in Arabic we will use the definite noun [ٱَلْكُتُب]{.ar} [Ealkutub]{.trn} "the books".

This topic may be a little difficult to comprehend right now because we have not yet learned how to form sentences. Later, you may refer back to this section as needed.
-->

## Grammatical gender

Some nouns designate animate beings like "man", "woman", "boy", "girl", "dog", "cow", etc.
Other nouns designate inanimate objects like "book", "house", "hand", "tree", "city", "food". 

There are three grammatical genders in English:

1. The masculine gender. This is used for nouns that designate male human beings and also some male animals. The pronouns used for the masculine gender are "he", "him", and "his".
2. The feminine gender. This is used for nouns that designate female human beings, and also some female animals. The pronouns used for the feminine gender are "she" and "her".
3. The neutral gender. This is used for nouns that designate inanimate objects and animals in general. The pronoun used for the neutral gender is "it".

In Arabic, there are only two grammatical genders: the masculine gender and the feminine gender.
All nouns in Arabic are either masculine or feminine in gender. 
Nouns that designate male human beings are assigned the masculine grammatical gender. And
nouns that designate female human beings are assigned the feminine grammatical gender.
As for nouns that designate inanimate objects and animals, these, too, are assigned either a masculine or a feminine gender. For example, [كِتَاب]{.ar} [kitAb]{.trn} "book" in Arabic is masculine. And [شَجَرَة]{.ar} [cajarah]{.trn} "tree" in Arabic is feminine.
We shall discuss this in more detail below.

### Nouns that designate animate beings.

In Arabic, in terms of their form, nouns that designate animate beings are in three categories:

1. There are separate nouns for the male and female animate being and the nouns match to each other.
2. There are separate nouns for the male and female animate being but the nouns are unrelated.
3. The same noun is used for both sexes.

We will discuss each of these categories below.

#### Matching nouns for male and female animate beings

In Arabic for some nouns that designate animate beings, the nouns for both sexes match each other. Here are some examples:
<!--
[فَتًى]{.ar}    [fatA]{.trn}      |masc.|a young man
[فَتَاة]{.ar}   [fatAh]{.trn}     |fem. |a young woman
-->

Arabic word |Gender | Definition
:----------------------|:---|:----------------
[ٱِبْن]{.ar}    [Eibn]{.trn}      |masc.|son
[ٱِبْنَة]{.ar}   [Eibnah]{.trn}    |fem. |daughter
[طِفْل]{.ar}    [Tifl]{.trn}      |masc.|child
[طِفْلَة]{.ar}   [Tiflah]{.trn}    |fem. |(female) child
[إِنْسَان]{.ar}  [EinsAn]{.trn}    |masc.|human being
[إِنْسَانَة]{.ar} [EinsAnah]{.trn}  |fem. |(female) human being
[حُرّ]{.ar}     [Hurr]{.trn}      |masc.|free man
[حُرَّة]{.ar}    [Hurrah]{.trn}    |fem. |free woman
[كَلْب]{.ar}    [kalb]{.trn}      |masc.|(male) dog
[كَلْبَة]{.ar}   [kalbah]{.trn}    |fem. |(female) dog
[هِرّ]{.ar}     [hirr]{.trn}      |masc.|(male) cat
[هِرَّة]{.ar}    [hirrah]{.trn}    |fem. |(female) cat
--                              |--   |--
[مُعَلِّم]{.ar}   [mueallim]{.trn}  |masc.|(male) teacher
[مُعَلِّمَة]{.ar}  [mueallimah]{.trn}|fem. |(female) teacher
[طَالِب]{.ar}   [TAlib]{.trn}     |masc.|(male) student
[طَالِبَة]{.ar}  [TAlibah]{.trn}   |fem. |(female) student
[صَاحِب]{.ar}   [SAHib]{.trn}     |masc.|(male) companion
[صَاحِبَة]{.ar}  [SAHibah]{.trn}   |fem. |(female) companion
[صَدِيق]{.ar}   [SadIq]{.trn}     |masc.|(male) friend
[صَدِيقَة]{.ar}  [SadIqah]{.trn}   |fem. |(female) friend 

In each of the words in the table above, the feminine noun is basically the same as the masculine noun but with the addition of a looped [tAE]{.trn2} [ة]{.ar} at the end. For example,
[طِفْل]{.ar}  [Tifl]{.trn} (masc.) is a child, and its feminine is
[طِفْلَة]{.ar} [Tiflah]{.trn} (fem.).

As a matter of fact, the looped [tAE]{.trn2} [ة]{.ar} is called a feminine marker for singular nouns. There are a couple of other, less common, feminine markers besides looped [tAE]{.trn2} that we will learn them later, if [#allAh]{.trn2} wills.
 
Note that the vowel-mark before the looped [tAE]{.trn2} [ة]{.ar} is always an [a]{.trn}-mark. 
<!--For example, in the case of [كَلْب]{.ar} [kalb]{.trn} "a male dog", in order to get the feminine noun [كَلْبَة]{.ar} [kalbatun]{.trn} "a female dog", [ب]{.ar} gets an [a]{.trn}-mark.-->

Note also that we have divided the table above into two groups. The first group contains nouns that have a primitive meaning, without a primarily adjectival or verbal quality in the meaning, for example "human" "cat", etc. 
The second group contains nouns that have an adjectival or verbal quality. For example, a "teacher" is someone who teaches. A "friend" is someone who is friendly. And so on.

This grouping will become important when, if [#allAh]{.trn2} wills, you study morphology, and the classification of nouns into primitive and derived nouns. But we can give a short preview here: Basically, for the second group (the one that has adjectival or verbal meanings), the formation of the feminine noun by adding a feminine marker (like [ة]{.ar}) to the masculine noun is normal and expected. Whereas, for the first group (the one that refers to primitive nouns without a verbal or adjectival meaning), the fact that the feminine and masuline nouns match each other and differ only by the feminine marker [ة]{.ar} is something that, although somewhat common, is more of a coincidence.

Another noteworthy point is that, for many primitive nouns (the first group), only one of the masculine/feminine pair may be used to refer to beings of either sex. What we mean by this is that, for example,
[كَلْب]{.ar} [kalb]{.trn}, while remaining a masculine noun, can be used to refer to both "a (male) dog" and "a (female) dog", especially if the animal's physical gender is not particularly important to what is being said.
And [كَلْبَة]{.ar} [kalbah]{.trn} (fem.) "a female dog" is typically only used when it is needed to specify the gender of the animal.
Conversely, [هِرَّة]{.ar} [hirrah]{.trn} "a (female) cat" may be used to refer to cat of either physical gender, especially if it is not obvious whether it is a male or female cat.

This preference of the noun of one gender to refer to beings of either physical gender is arbitrary and case-by-case. For example,
[طِفْل]{.ar} [Tifl]{.trn} (masc.) is commonly used to say "a child", regardless of whether the child is a boy or a girl. But [طِفْلَة]{.ar} [Tiflah]{.trn} is fairly common too specifically for "a female child".

As another example, the word [إِنْسَانَة]{.ar} [EinsAnah]{.trn} (fem.) "a female human being" is rarely used at all. Instead, the word
[إِنْسَان]{.ar} [EinsAn]{.trn}, while remaining a masculine noun, is almost always used to refer to "a human being" in general, regardless of actual gender.

On the other hand,
<!--[فَتًى]{.ar}    [fatA]{.trn} "a young man"
[فَتَاة]{.ar}   [fatAh]{.trn} "a young woman"-->
[ٱِبْن]{.ar}    [Eibn]{.trn}      "son" and
[ٱِبْنَة]{.ar}   [Eibnah]{.trn}    "daughter"
are only ever used for their respective gender. So 
[ٱِبْن]{.ar}    [Eibn]{.trn}   (masc.) "a son" is never used to mean "a daughter".
And [ٱِبْنَة]{.ar}   [Eibnah]{.trn}    (fem.) "a daughter" is never used to mean "a son".
<!--[فَتًى]{.ar}    [fatA]{.trn} is never used to refer to "a young woman".-->

There aren't very many of such nouns. And we have covered a few of the common ones above. A good dictionary will also provide guidance in this regard.

As for the second group of words (the one that has adjectival or verbal meanings), they are typically only ever used for their respective gender. So, for example,
[مُعَلِّم]{.ar}   [mueallim]{.trn}  (masc.) is only used for "a (male) teacher". And
[مُعَلِّمَة]{.ar}  [mueallimah]{.trn} (fem.) is only used for "a (female) teacher".

<!--is used commonly for "a dog" and [هِرَّة]{.ar} [hirrah]{.trn} (fem.) may be used for "a cat".

Even though the male and female animate beings have separate words, sometimes one of the words is used commonly two refer to both sexes. This is especially common when the actual gender is not particularly important for the meaning of the sentence. For example,
[كَلْب]{.ar} [kalb]{.trn} (masc.) is used commonly for "a dog" and [هِرَّة]{.ar} [hirrah]{.trn} (fem.) may be used for "a cat".
Similarly, [طِفْل]{.ar} [Tifl]{.trn} (masc.) is commonly used to say "a child", regardless of whether the child is a boy or a girl. This is done when the actual gender is not particularly important for the meaning of the sentence, as, for example, in the sentence: "A child entered.".

In fact, the word [إِنْسَانَة]{.ar} [EinsAnah]{.trn} (fem.) "a female human being" is rarely used at all. Instead, the word
[إِنْسَان]{.ar} [EinsAn]{.trn} (masc.) is used to refer to "a human being" in general, regardless of actual gender.-->

#### Unrelated nouns for male and female animate beings

For other nouns that designate animate beings, the nouns for the male and female sexes are completely unrelated. Here are some examples:

Arabic word  |Gender | Definition
:----------------------|:---|:----------------
[أَب]{.ar}    [Eab]{.trn}     |masc.|father
[أُمّ]{.ar}    [Eumm]{.trn}    |fem. |mother
[غُلَام]{.ar}  [gulAm]{.trn}   |masc.|boy
[جَارِيَة]{.ar} [jAriyah]{.trn} |fem. |girl
[عَبْد]{.ar}   [eabd]{.trn}    |masc.|male slave
[أَمَة]{.ar}   [Eamah]{.trn}   |fem. |female slave
[أَسَد]{.ar}   [Easad]{.trn}   |masc.|lion
[لَبْوَة]{.ar}  [labwah]{.trn}  |fem. |lioness
[ثَوْر]{.ar}   [vawr]{.trn}    |masc.|bull
[بَقَرَة]{.ar}  [baqarah]{.trn} |fem. |cow

Even in these nouns you can see that the feminine noun usually ends with a looped [tAE]{.trn2} [ة]{.ar} feminine marker. There are only a few commonly used feminine nouns that don't end with a feminine marker like looped [tAE]{.trn2}. [أُمٌّ]{.ar} [Eummun]{.trn} "mother" is one of these exceptions.

#### Using the same noun for both sexes

There are other nouns for animate beings where the same word is used for both sexes. The word itself will still be either grammatically masculine or feminine. Here are some examples:

Arabic word  |Gender | Definition
:----------------------|:---|:----------------
[شَخْص]{.ar}   [caxS]{.trn}    |masc.|person
[نَفْس]{.ar}   [nafs]{.trn}    |fem. |self
[عَدُوّ]{.ar}   [eaduww]{.trn}  |masc.|enemy
[حَيَوَان]{.ar} [HayawAn]{.trn} |masc.|animal
[طَائِر]{.ar}  [TAEir]{.trn}   |masc.|bird
[قِرْد]{.ar}   [qird]{.trn}    |masc.|monkey
[حَمَامَة]{.ar} [HamAmah]{.trn} |fem. |dove
[نَمْلَة]{.ar}  [namlah]{.trn}  |fem. |ant

So for example [قِرْد]{.ar} [qirdun]{.trn} "monkey" is grammatically masculine but it will be used for both a male and a female monkey.
Similarly, [شَخْص]{.ar}  [caxS]{.trn} is a masculine noun meaning "person". While remaining grammatically masculine, it can be used to refer to persons of male or female persons.

Note also that [نَفْس]{.ar} [nafsun]{.trn} "self" is a feminine noun but it does not end in a looped [tAE]{.trn2} [ة]{.ar}. It is one of the small number of feminine nouns that don't have a female marker, like [أُمٌّ]{.ar} [Eummun]{.trn} (fem.) "mother".
<!--Notably, [نَفْس]{.ar}  [nafs]{.trn} is treated as feminine when it refers to the soul of a person. However, in constructions like "yourself", "himself", etc. it will conform to the gender of the person it is referring to. We shall see this in later chapters, if [#allAh]{.trn2} wills.-->

### Nouns that designate inanimate objects

As mentioned earlier, nouns that designate inanimate objects are assigned a fixed grammatical gender. There is usually no discernable reason why some are assigned a masculine gender while others are assigned a feminine gender.

Arabic word  |Gender | Definition
:----------------------|:---|:----------------
[كِتَاب]{.ar}  [kitAb]{.trn}   |masc.|book
[بَيْت]{.ar}   [bayt]{.trn}    |masc.|house
[قَلَم]{.ar}   [qalam]{.trn}   |masc.|pen
[طَعَام]{.ar}  [TaeAm]{.trn}   |masc.|food
[مَاء]{.ar}   [mAE]{.trn}     |masc.|water
[مَدْرَسَة]{.ar} [madrasah]{.trn}|fem. |school
[مَدِينَة]{.ar} [madInah]{.trn} |fem. |city
[غُرْفَة]{.ar}  [gurfah]{.trn}  |fem. |room
[شَجَرَة]{.ar}  [cajarah]{.trn} |fem. |tree
[شَمْس]{.ar}   [cams]{.trn}    |fem. |sun
[قَمَر]{.ar}   [qamar]{.trn}   |masc.|moon
[عِلْم]{.ar}   [eilm]{.trn}    |masc.|knowledge
[قُوَّة]{.ar}   [quwwah]{.trn}  |fem. |strength
[حَيَاة]{.ar}  [HayAh]{.trn}   |fem. |life
[مَوْت]{.ar}   [mawt]{.trn}    |masc.|death

In these nouns as well, we note that feminine nouns usually end with the feminine marker looped [tAE]{.trn2} [ة]{.ar}. 
But here too, we find another exception:
[شَمْسٌ]{.ar} [camsun]{.trn} "sun" which is feminine but does not end with a feminine marker.
These exceptions are not very many and, if [#allAh]{.trn2} wills, we will not find it hard to memorize them.

There is a sub-group of nouns that designate inanimate objects, but can also be used to refer to animate beings. Here are a couple of examples:

Arabic word  |Gender | Definition
:----------------------|:---|:----------------
[رَهِينَة]{.ar} [rahInah]{.trn} |fem. |pledge
[عُضْو]{.ar}   [euDw]{.trn}    |masc.|member

[رَهِينَة]{.ar} [rahInah]{.trn} is a feminine noun meaning "pledge". For inanimate objects it refers to something that is held as a security or a collateral. With its animate meaning, it is used to refer to a human hostage.

Similarly,
[عُضْو]{.ar}   [euDw]{.trn} is a masculine noun meaning "member". For inanimate objects it refers to a limb which is the member of a body. With its animate meaning it refers to a person who is a member of a professional organization.

Just like we saw for the nouns in section\ \@ref(using-the-same-noun-for-both-sexes),
such nouns adhere to their fixed grammatical gender when used for either male or female persons.

### Nouns with mismatched gender

We saw that there are some nouns that are feminine, but do not end with with a feminine marker like [ة]{.ar}. These were:

+ [أُمّ]{.ar}   [Eumm]{.trn}    (fem.) "mother"
+ [نَفْس]{.ar}  [nafs]{.trn}    (fem.) "self"
+ [شَمْس]{.ar}  [cams]{.trn}    (fem.) "sun"

There are a few more nouns that are like this. One special category among them is body parts. Many prominent body parts that come in pairs or more, are grammatically feminine, whether or not they end with a feminine marker like [ة]{.ar}. Here are some examples:

<!--Arabic word  |Gender | Definition
:----------------------|:---|:------------------>

+ [يَد]{.ar} [yad]{.trn} (fem.) "hand" (sometimes "an arm")
+ [عَيْن]{.ar} [eayn]{.trn} (fem.) "eye"
+ [أُذُن]{.ar} [Eupun]{.trn} (fem.) "ear"
+ [قَدَم]{.ar} [qadam]{.trn} (fem.) "foot"
+ [رِجْل]{.ar} [rijl]{.trn} (fem.) "leg" (sometimes "foot")
+ [إِبْهَام]{.ar} [EibhAm]{.trn} (fem.) "thumb"
+ [إِصْبَع]{.ar} [EiSbae]{.trn} (fem.) "finger, toe"
+ [سِنّ]{.ar} [sinn]{.trn} (fem.) "tooth"
+ [رُكْبَة]{.ar} [rukbah]{.trn} (fem.) "knee"

There are exceptions, however. The following body parts come in pairs yet are masculine.

+ [مَنْخَر]{.ar} [manxar]{.trn} (masc.) "nostril"
+ [مِرْفَق]{.ar} [mirfaq]{.trn} (masc.) "elbow"

There are other such exceptions as well.

<!--For other body parts, the grammatical gender conforms to whether it has a feminine marker or not. Examples:-->
Body parts that don't come in pairs are typically more regular in their gender: they are feminine if they end in a feminine marker like [ة]{.ar}, and masculine if they don't. Examples:

+ [رَأْس]{.ar} [raEs]{.trn} (masc.) "head"
+ [أَنْف]{.ar} [Eanf]{.trn} (masc.) "nose"
+ [بَطْن]{.ar} [baTn]{.trn} (masc.) "belly"
+ [لِحْيَة]{.ar} [liHyah]{.trn} (fem.) "beard"

Conversely, nouns that end with a feminine marker like [ة]{.ar}, yet are masculine are very rare. Some of the more common of them are:

+ [خَلِيفَة]{.ar} [xalIfah]{.trn} (masc.) "caliph"
+ [عَلَّامَة]{.ar} [eallAmah]{.trn} (masc.) "great scholar"
+ [دَاعِيَة]{.ar} [dAeiyah]{.trn} (masc.) "great preacher"

There are also a few words which can be optionally assigned a masculine or feminine gender. Among these are:

+ [سُوق]{.ar} [sUq]{.trn} (masc. or fem.) "market"
+ [طَرِيق]{.ar} [TarIq]{.trn} (masc. or fem.) "path"

A good dictionary should mention the gender of all these exceptional words.

## Exercises

In the following English sentences, determine whether the underlined nouns will be translated with definite or indefinite nouns in Arabic.

<!--
## Genderizability

### Non-genderizable nouns

So far, we have only encountered nouns that are not _genderizable_. That is, they are fixed in gender. And we are not allowed to modify their gender. For example, the noun [شَخْص]{.ar} [caxS]{.trn} is a non-genderizable masculine noun that means "a person". The dictionary tells us that this noun may be applied to both male and female persons. 

Say that we would like to apply this noun to a female person, like [جَارِيَة]{.ar} [jAriyah]{.trn} (fem.) "a girl", by saying, for example, "The girl is a person.". In order to do this, we are not allowed to feminize the noun [شَخْص]{.ar} [caxS]{.trn}, by making it [شَخْصَة]{.ar} [caxSah]{.trn} for example. Nor does [شَخْصَة]{.ar} [caxSah]{.trn} pre-exist in the dictionary. So we are forced to apply the masculine noun [شَخْص]{.ar} [caxS]{.trn} to a female person [جَارِيَة]{.ar} [jAriyah]{.trn}. 

This may seem a little unusual because the nouns in this example apply to animate beings that have a physical gender. And so, there is a strong motive to match the grammatical gender of the noun to the physical gender of the being it is applied to. But, as we said, we are prevented from doing so because the noun 
[شَخْص]{.ar} [caxS]{.trn} is not genderizable.

This mismatch in gender will seem less unusual if we consider nouns that designate inanimate objects. As mentioned earlier, all Arabic nouns, even those that apply to inanimate objects, have a grammatical gender.

Consider, for example, the following nouns:

+ [بِنَاء]{.ar} [binAE]{.trn} (masc.) "a building"
+ [مَدْرَسَة]{.ar} [madrasah]{.trn} (fem.) "a school"

Say that we want to make a sentence: "The a building is a school."
There is no problem in applying the feminine noun 
[مَدْرَسَة]{.ar} [madrasah]{.trn} "a school"
to the masculine noun
[بِنَاء]{.ar} [binAE]{.trn} "a building".

Again, we are not allowed to masculinize the feminine noun
[مَدْرَسَة]{.ar} [madrasah]{.trn}
to make it match the masculine noun
[بِنَاء]{.ar} [binAE]{.trn}.
This is because 
[مَدْرَسَة]{.ar} [madrasah]{.trn}
is not a genderizable noun. (So isn't
[بِنَاء]{.ar} [binAE]{.trn}
for that matter.) And this mismatch in gender between the two nouns is perfectly normal.

### Genderizable nouns

There is another class of nouns that are genderizable. This means that we are allowed to modify their gender to match the entity they are applied to. Consider the word:

+ [مُعَلِّم]{.ar} [mueallim]{.trn} (masc.) "a (male) teacher" 

It is an example of a masciline genderizable noun. If we want to use it in the sentence "The father is a teacher.", then it may be applied without modification to the other masculine noun [أَب]{.ar} [Eab]{.trn} (masc.) "a father".

If, however, we want to make the sentence, "The mother is a teacher.", then we first feminine
[مُعَلِّم]{.ar} [mueallim]{.trn} (masc.)
by adding the feminine marker [ة]{.ar}. When we do so, the word becomes:

+ [مُعَلِّمَة]{.ar} [mueallimah]{.trn} (fem.) "a (female) teacher" 

Then we can apply this noun to the other feminine noun [أُمّ]{.ar} [Eumm]{.trn} "a mother".

Here is another example of a genderizable noun:

+ [طَالِب]{.ar} [TAlib]{.trn} (masc.) "a (male) student"

If we wish to apply this noun to a female person, then we feminize it into:

+ [طَالِبَة]{.ar} [TAlibah]{.trn} (masc.) "a (female) student"

### Determining genderizability

There are some nouns that, at first glance, appear genderizable, but actually are not. For example, it may appear as if the noun [طِفْلَة]{.ar} [Tiflah]{.trn} (fem.) "a female child" has been formed by feminizing [طِفْل]{.ar} [Tifl]{.trn} (masc.) "a child". But actually 
[طِفْل]{.ar} [Tifl]{.trn}
and
[طِفْلَة]{.ar} [Tiflah]{.trn}
are not genderizable words. They both just happen to pre-exist in the dictionary with their respective meanings.

Similar to 
[طِفْل]{.ar} [Tifl]{.trn}
and
[طِفْلَة]{.ar} [Tiflah]{.trn} are:

+ [إِنْسَان]{.ar} [EinsAn]{.trn}    (masc.) "a human being" and [إِنْسَانَة]{.ar} [EinsAnah]{.trn} (fem.) "a female human being"
+ [كَلْب]{.ar}  [kalb]{.trn}      (masc.) "a male dog" and [كَلْبَة]{.ar} [kalbah]{.trn}    (fem.) "a female dog"
+ [هِرّ]{.ar}   [hirr]{.trn}      (masc.) "a male cat" and [هِرَّة]{.ar}  [hirrah]{.trn}    (fem.) "a female cat"

All of the above are not genderizable nouns.

Here are some general guidelines that can help determine whether a noun is genderizable or not:

1. Most, if not all, nouns that designate inanimate objects and animals are not genderizable.
2. For nouns that designate human beings: 
   a. Those nouns that denote an entity without any verbal or adjectival meaning are usually non-genderizable. Examples:
      + [أَب]{.ar}   [Eab]{.trn}     (masc.) "a father"
      + [أُمّ]{.ar}   [Eumm]{.trn}    (fem.) "a mother"
      + [غُلَام]{.ar} [gulAm]{.trn}   (masc.) "a boy"
      + [جَارِيَة]{.ar} [jAriyah]{.trn} (fem.) "a girl"
      + [طِفْل]{.ar}    [Tifl]{.trn}      (masc.) "a child"
      + [طِفْلَة]{.ar}   [Tiflah]{.trn}    (fem.) "a female child"
      + [إِنْسَان]{.ar}  [EinsAn]{.trn}    (masc.) "a human being"
      + [إِنْسَانَة]{.ar} [EinsAnah]{.trn}  (fem.) "a female human being"
   b. Genderizable nouns will usually have an association with a verbal or adjectival quality. For example:
      + [مُعَلِّم]{.ar} [mueallim]{.trn} (masc.) "a (male) teacher" is one who teaches.
      + [طَالِب]{.ar} [TAlib]{.trn} (masc.) "a (male) student" is one who studies.

Sometimes, it may not be easy to figure out just from the meaning of the noun whether it is genderizable or not. For example, [صَدِيق]{.ar} [SadIq]{.trn} (masc.) "a (male) friend" is genderizable. But [عَدُوّ]{.ar} [eaduww]{.trn} "an enemy" is not genderizable.

As you continue studying, you will, if [#allAh]{.trn2} wills, get a feel for which nouns are genderizable. And if, at a later advanced stage in your Arabic studies, you study topics like morphology, and classification of nouns into primitive and derived nouns, that will help as well.
-->

<!--chapter:end:srcrmd/nouns.Rmd-->

# Subject-information sentences

## Introduction

In this chapter we will learn about a class of sentences called _subject-information sentences._ 
Subject-information sentences consist of two parts:

i. The _subject_. This is the topic of the sentence.
ii. The _information_. This gives us some information about the subject.

## Forming subject-information sentences

Here is a subject-information sentence:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-5-1.pdf)<!-- -->

<!--"The building is a house."-->

The subject of the sentence is "the building". This means that the sentence is about "the building". 

The information is "a house". This means that the information that the sentence is giving us about the subject is that it is "a house".

Let's try to form this sentence in Arabic.

First we assemble the individual parts:

i. "The building" in Arabic is [ٱَلْبِنَاء]{.ar} [EalbinAE]{.trn} (masc.).
ii. "A house" is [بَيْت]{.ar} [bayt]{.trn} (masc.).

Next we put them both in the u-state. For subject-information sentences, both the subject and the information shall be in the u-state. Remember that the u-state is formed by putting an [un]{.trn}-mark [◌ٌ]{.ar} at the end of an indefinite noun, and a [u]{.trn}-mark [◌ُ]{.ar} at the end of a definite noun. Here are the two nouns in the u-state:

i. [ٱَلْبِنَاءُ]{.ar} [EalbinAEu]{.trn} (masc.) "the building" (u-state)
ii. [بَيْتٌ]{.ar} [baytun]{.trn} (masc.) "a house" (u-state)

In order to form this sentence in Arabic, we put the subject first and then the information. So we get:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-6-1.pdf)<!-- -->

<!--
[ٱَلْبِنَاءُ بَيْتٌ.]{.ar}  
[EalbinAEu bayt.]{.trn}  
"The building is a house."
-->

But wait! Where is the Arabic word for "is"? It turns out that Arabic does not usually express any word for "is". Instead, the meaning of this word is implied.

Also, note that the final vowel mark at the end of the sentence is written but not pronounced. So we will write 
[بَيْتٌ]{.ar} but say
[bayt]{.trn}, not
[baytun]{.trn}.
This is in accordance with what we learned in section\ \@ref(pronouncing-the-end-of-a-sentence).

Now let's try reversing this sentence, and try making the sentence:

"The house is a building."

We follow the same procedure by assembling the individual parts of the sentence and putting them in the u-state:

i.  The subject: [ٱَلْبَيْتُ]{.ar} [Ealbaytu]{.trn} (masc.) "the house" (u-state)
ii. The information: [بِنَاءٌ]{.ar} [binAEun]{.trn} (masc.) "a building" (u-state)

And then we put them together, first the subject and then the information:

[ٱَلْبَيْتُ بِنَاءٌ.]{.ar}  
[Ealbaytu binAE.]{.trn}  
"The house is a building."

and there we have our sentence.

## Matching the gender between the subject and the information

In the sentences above, both the subject and the information were masculine nouns. Now let's try forming a sentence where the subject and the information have different genders. Let's try saying:

"The building is a school."

i.   The subject: [ٱَلْبِنَاءُ]{.ar} [EalbinAEu]{.trn} (masc.) "the building" (u-state)
ii.  The information: [مَدْرَسَةٌ]{.ar} [madrasatun]{.trn} (fem.) "a school" (u-state)

In the same manner as before, we form the sentence by first writing the subject and then the information:

[ٱَلْبِنَاءُ مَدْرَسَةٌ.]{.ar}  
[EalbinAEu madrasah.]{.trn}  
"The building is a school."

We can also reverse this sentence:

[ٱَلْمَدْرَسَةُ بِنَاءٌ.]{.ar}  
[Ealmadrasatu binAE.]{.trn}  
"The school is a building ."

So we see that it is quite normal to have a sentence where the gender of the subject does not match the gender of the information. 
<!--And we made no attempt to try change their gender by genderizing one of them to match the gender of the other. This is because both words
[ٱَلْبِنَاء]{.ar} [EalbinAE]{.trn} (masc.) "a building"
and
[مَدْرَسَة]{.ar} [madrasah]{.trn} (fem.) "a school"
are non-genderizable words.

If either the subject or the information is a genderizable noun, the in this case the subject and the information are made to match each other in gender. For example, let's try to form the sentence:
-->
This is because the words we have dealt with so far denote animate objects.
If either the subject or the information denote animate beings, then in this case the subject and the information often do match each other in gender. For example, let's try to form the sentence:

"The mother is a teacher."

Here are the indiviual words that we will use to form the sentence:

i.  The subject: "the mother": [ٱَلْأُمُّ]{.ar} [EalEummu]{.trn} (fem.) (u-state).
ii. The information: "a teacher". We have two words for "a teacher" in Arabic: 

    + [مُعَلِّم]{.ar} [mueallium]{.trn} (masc.) "a (male) teacher"
    + [مُعَلِّمَة]{.ar} [mueallimah]{.trn} (fem.) "a (female) teacher". 

    Obviously, [مُعَلِّمَة]{.ar} [mueallimah]{.trn} would apply here so we put it in the u-state: [مُعَلِّمَةٌ]{.ar} [mueallimatun]{.trn}
(u-state).

Now we can assemble the sentence:

[ٱَلْأُمُّ مُعَلِّمَةٌ.]{.ar}  
[EalEummu mueallimah.]{.trn}  
"The mother is a teacher~f~."

In the reverse sentence "The teacher is a mother.", we again use the feminine noun
[مُعَلِّمَة]{.ar} [mueallimah]{.trn} (fem.) "a (female) teacher",
which is now the subject of the sentence, to match the feminine noun in the information 
[ٱَلْأُمّ]{.ar} [Ealumm]{.trn} (fem.)
"a mother". So we get:

[ٱَلْمُعَلِّمَةُ أُمٌّ.]{.ar}  
[Ealmueallimatu Eumm.]{.trn}  
"The teacher~f~ is a mother."

<!--If the subject and the information apply to animate beings, then even if they are not genderizable, they will usually match each other in gender in order for the sentence to be meaningful. For example:-->
Here is another example:

[ٱَلرَّجُلُ أَبٌ.]{.ar}  
[Earrujulu Eab.]{.trn}  
"The man is a father."

<!--
In the above sentence, both the subject
[ٱَلرَّجُل]{.ar}
[Earrujul]{.trn}
(masc.) "the man"
and the information
[أَب]{.ar}
[Eab]{.trn}
(masc.) "a father" are non-genderizable nouns. But they match each other in gender because that is the only way for the sentence to be meaningful.

But if one of the non-genderizable nouns can be applied to both physical genders then the subject and information may mismatch in gender. For example, the noun [شَخْص]{.ar} [caxS]{.trn} "a person" is a masculine noun that is applied to both male and female persons. So if the person being referred to is a woman, for example, then we can get an apparent mismatch in gender between the grammatical gender of the subject and the grammatical subject of the information. Example:
-->
Now, let's try a sentence where we are still dealing with animate beings but the nouns mismatches in grammatical gender.

[ٱَلْأُمُّ شَخْصٌ.]{.ar}  
[EalEummu caxS.]{.trn}  
"The mother is a person."

[ٱَلشَّخْصُ مُعَلِّمَةٌ.]{.ar}  
[EaccaxSu mueallimah.]{.trn}  
"The person is a (female) teacher."

[ٱَلْمُعَلِّمَةُ شَخْصٌ.]{.ar}  
[Ealmueallimatu caxS.]{.trn}  
"The (female) teacher is a person."

In the above examples, the grammatical genders mismatch between the subject and the information. But this is because we are matching with the physical gender of the person represented by the masculine noun [شَخْص]{.ar} [caxS]{.trn} "a person", not its grammatical gender.

The same effect is seen when using the word [حَيَوان]{.ar} [HayawAn]{.trn} which is a masculine noun meaning "an animal". It can be applied to both male and female animals. So we can say:

[ٱَلْحَيَوَانُ هِرٌّ.]{.ar}  
[EalHayawAnu hirr.]{.trn}  
"The animal is a (male) cat."

and

[ٱَلْحَيَوَانُ هِرَّةٌ.]{.ar}  
[EalHayawAnu hirrah.]{.trn}  
"The animal is a (female) cat."

<!--
We assemble the individual parts of the sentence in the u-state:
and "a building" is [بِنَاءٌ]{.ar} [binAEun]{.trn}. In order to say "The house is a building" we put the [subject]{.syn} first and put its [information]{.syn} after it. Both the [subject]{.syn} and the [information]{.syn} are put in the u-state.

This kind of sentence is called a [subject-information]{.syn} sentence. It consists of two parts:

1. The part before "is": "the house". This is who the sentence is about. We call this the [subject]{.syn} of the sentence.
2. The part after "is": "a building". This is telling us some information about the [subject]{.syn}. We call this the [information]{.syn}.

Arabic does not normally express the word "is". In order to express this sentence in Arabic we put the [subject]{.syn} first and then the [information]{.syn}. For these simple sentences the [subject]{.syn} and the [information]{.syn} will be in the u-state.

"The house" is [ٱَلْبَيْتُ]{.ar} [albaytu]{.trn} and "a building" is [بِنَاءٌ]{.ar} [binAEun]{.trn}. In order to say "The house is a building" we put the [subject]{.syn} first and put its [information]{.syn} after it. Both the [subject]{.syn} and the [information]{.syn} are put in the u-state.

[ٱَلْبَيْتُ بِنَاءٌ.]{.ar}  
[Ealbaytu binAEun.]{.trn}  
"The house is a building."

Now let's try saying "The man is a teacher."

"The man" is [ٱَلرَّجُلُ]{.ar} [arrajulu]{.trn}. For "a teacher" we have two words in Arabic: 

+ [مُعَلِّمٌ]{.ar} [mueallimun]{.trn} "a male teacher" 
+ [مُعَلِّمَةٌ]{.ar} [mueallimun]{.trn} "a female teacher" 

Obviously "the man" can only be [مُعَلِّمٌ]{.ar} [mueallimun]{.trn} "a male teacher". So the sentence is:

[ٱَلرَّجُلُ مُعَلِّمٌ.]{.ar}  
[Earrajulu mueallimun.]{.trn}  
"The man is a (male) teacher."

Let's try another example: "The animal is a cat."

"The animal" is [حَيَوَانٌ]{.ar} [HayawAnun]{.trn}. For "a cat" we have two words:

+ [هِرٌّ]{.ar} [hirrun]{.trn} "a male cat"
+ [هِرَّةٌ]{.ar} [hirratun]{.trn} "a female cat"

Usually, in Arabic [هِرَّةٌ]{.ar} [hirratun]{.trn} "a female cat" is used for "a cat" if the animal's gender is not specified, or not important. So putting together the sentence we get:

[ٱَلْحَيَوَانُ هِرَّةٌ.]{.ar}  
[EalHayawAnu hirratun.]{.trn}  
"The animal is a cat."

Note that, in this sentence, the [subject]{.syn} [ٱَلْحَيَوَانُ]{.ar} [alHayawAnu]{.trn} "the animal" is a masculine noun. And the [information]{.syn} 
[هِرَّةٌ]{.ar} [hirratun]{.trn} "a cat" is a feminine noun. So the [subject]{.syn} and the [information]{.syn} do not match in gender. This is perfectly normal. We make the [information]{.syn} match the [subject]{.syn} in gender only if:

1. There are separate words for the masculine and feminine nouns for the [information]{.syn}, and
2. Only one of the two words can be correctly applied to the [subject]{.syn}.

In this case there were separate words for the masculine and feminine nouns for the [information]{.syn}:

+ [هِرٌّ]{.ar} [hirrun]{.trn} "a male cat"
+ [هِرَّةٌ]{.ar} [hirratun]{.trn} "a female cat"

but both of these can be applied to the [subject]{.syn}, because the [subject]{.syn} [ٱَلْحَيَوَانُ]{.ar} [alHayawAnu]{.trn} (masc.) "the animal" is used for both male and female animals. [هِرَّةٌ]{.ar} [hirratun]{.trn} is chosen because it is commonly used for "a cat" as we have already explained.

We have already seen an example of matching the gender of the [information]{.syn} with the [subject]{.syn} in the example:

[ٱَلرَّجُلُ مُعَلِّمٌ.]{.ar}  
[Earrajulu mueallimun.]{.trn}  
"The man is a (male) teacher."
-->

## Detached pronouns

Pronouns, in Arabic, are special nouns that can be used in place of other nouns when it is known who is being referred to. This means that they can replace definite nouns only. Pronouns in English include words like "he", "she", "it", "you", "I", etc. 

In order to explain the usage of pronouns, we will first show a sentence with a noun subject:

"The man is a teacher."

Now we you can replace the definite subject noun "the man" with the pronoun "he":

"He is a teacher."

In Arabic there are a few different kinds of pronouns. Here we will learn _detached pronouns_. They are called detached pronouns because they are detached from other words. There are another set of pronouns called _attached pronouns_ that we will learn later, if [#allAh]{.trn2} wills.

### Participants

When talking about pronouns, it is beneficial to make use of a concept of grammar called _participants_.

In any kind of speech there are there can be up to three types of _participants_ involved. A participant may be singular, i.e. consist of one individual, or plural, i.e., consist of more than one individual.  

The three participants in speech are:

1. The _speaker-participant_. This is the participant who is speaking. When the speaker-participant refers to himself or herself (or themselves if plural) in English, then he/she/they use the pronouns "I", "me", "we", and "us".
2. The _addressee-participant_. This is the participant whom the speaker-participant is directly speaking to. When the speaker-participant refers to the addressee-participant in English, he uses the "you" pronoun.
3. The _absentee-participant_. This is the participant who is not being directly spoken to. Their only participation in the speech is that they are being referred to. When the speaker-participant refers to the absentee-participant in English, he uses the pronouns "he", "him", "she", "her", "it", "they", and "them".

In this chapter we will learn the Arabic pronouns for the singular participants.

### Detached pronouns for the singular absentee-participant

Here are the Arabic detached pronouns for the singular absentee-participant:

+ singular masculine absentee-participant: [هُوَ]{.ar} [huwa]{.trn} "he".
+ singular feminine absentee-participant: [هِيَ]{.ar} [hiya]{.trn} "she".

Here are some examples of pair of sentences, each first with a noun, and then with a pronoun in place of the noun:

+ [ٱَلرَّجُلُ مُعَلِّمٌ.]{.ar}  
  [Earrajulu mueallim.]{.trn}  
  "The man is a teacher~m~."
  
  [هُوَ مُعَلِّمٌ.]{.ar}  
  [huwa mueallim.]{.trn}  
  "He is a (male) teacher~m~."

+ [ٱَلْجَارِيَةُ طَالِبَةٌ.]{.ar}  
  [EaljAriyatu Talibah.]{.trn}  
  "The girl is a student~f~."

+ [هِيَ طَالِبَةٌ.]{.ar}  
  [hiya Talibah.]{.trn}  
  "She is a student~f~."

+ [ٱَلْبَيْتُ بِنَاءٌ.]{.ar}  
  [Ealbaytu binAE.]{.trn}  
  "The house is a building."

  [هُوَ بِنَاءٌ.]{.ar}  
  [huwa binAE.]{.trn}  
  "It is a building."

  Note that Arabic uses the pronoun [هُوَ]{.ar} [huwa]{.trn} "he" to refer to the inanimate object "the house". This is because, as we know, all nouns in Arabic are either masculine or feminine. In translating the sentence to English we will employ the neutral pronoun "it" to make the sentence sound natural.

+ [ٱَلْبِنَاءُ مَدْرَسَةٌ.]{.ar}  
  [EalbinAEu madrasah.]{.trn}  
  "The building is a school."

  [هُوَ مَدْرَسَةٌ.]{.ar}
  [huwa madrasah.]{.trn}  
  or  
  [هِيَ مَدْرَسَةٌ.]{.ar}
  [hiya madrasah.]{.trn}  
  "It is a school."

  Note that either [هُوَ]{.ar} [huwa]{.trn} "he" or [هِيَ]{.ar} [hiya]{.trn} "she" can be used in the above sentence because the gender of the subject [ٱَلْبِنَاء]{.ar} [EalbinAE]{.trn} (masc.) "the building" mismatches the gender of the information [مَدْرَسَة]{.ar} [madrasah]{.trn} (fem.) "a school.".

  In such cases where the genders of the subject and the information do not match, then, generally speaking, the pronoun for either gender could be employed with the following guideline:

  Prefer to match the gender of the subject pronoun with the gender of the information, unless the noun being replaced with a pronoun is an animate being, in which case prefer to use the gender of the animate being. 

  So in the above sentence we will prefer to use [هِيَ مَدْرَسَةٌ.]{.ar} [hiya madrasah.]{.trn} because the information [مَدْرَسَةٌ]{.ar} [madrasatun]{.trn} "a school" is feminine.

+ Here is an example with an animate being as the subject:

  [ٱَلْجَارِيَةُ إِنْسَانٌ.]{.ar}  
  [EaljAriyatu InsAn.]{.trn}  
  "The girl is a human."

  [هِيَ إِنْسَانٌ.]{.ar}  
  [hiya InsAn.]{.trn}  
  "She is a human."

  Here, if we replace the noun [ٱَلْجَارِيَة]{.ar} [EaljAriyah]{.trn} "the girl" with a pronoun, we will prefer to use [هِيَ]{.ar} [hiya]{.trn} "she", because the girl is an animate being, even though the information [إِنْسَانٌ]{.ar} [EinsAnun]{.trn} "a human" is masculine.

### Detached pronouns for the singular addressee-participant and speaker-participant

Here are the pronouns for the singular addressee-participant and speaker-participant:

+ singular masculine addressee-participant: [أَنْتَ]{.ar} [Eanta]{.trn} "you~m~".
+ singular feminine addressee-participant: [أَنْتِ]{.ar} [Eanti]{.trn} "you~f~".
+ singular speaker-participant: [أَنَا]{.ar} [Eana]{.trn} "I". 

Note that the addressee-participant pronoun "you" has separate pronouns for the masculine and the feminine while the speaker-participant pronoun "I" has the same pronoun for both genders. Examples with these pronouns:

+ [أَنْتَ مُعَلِّمٌ.]{.ar}  
  [Eanta mueallim.]{.trn}  
  "You~m~ are a teacher~m~."

+ [أَنْتِ مُعَلِّمَةٌ.]{.ar}  
  [Eanti mueallimah.]{.trn}  
  "You~f~ are a teacher~f~."

+ [أَنَا مُعَلِّمٌ.]{.ar}  
  [Eana mueallim.]{.trn}  
  "I am a teacher~m~."

+ [أَنَا مُعَلِّمَة.]{.ar}  
  [Eana mueallimah.]{.trn}  
  "I am a teacher~f~."

### Definiteness of pronouns

We stated, and saw, that pronouns can replace definite nouns. This means that pronouns themselves are definite nouns (even though they are not prefixed by [ٱَلْ]{.ar} [Eal]{.trn} "the").

This fact will be useful in later chapters, if [#allAh]{.trn2} wills.

### Rigidity of pronouns

Remember in section\ \@ref(flexibility-of-nouns), we talked about the flexibility of nouns. We said that nouns whose endings change with the noun's state are called flexible nouns. Most nouns fall into this category.

Pronouns, however, are nouns whose endings don't change with their state. Therefore they fall into the category of _rigid_ nouns.

<!--
All the nouns that we've come across so far (except the pronouns we just learned about above) are a category of nouns called _flexible_ nouns. They are called flexible, because their ending will change depending on their state. Even though we've only used nouns in the u-state so far, we have learned in section \@ref(state), the state of a noun determines the vowel mark on their final letter. The table of states is reproduced here for convenience.

State         | Indefinite "a book" | Definite "the book"
:-------------|:-----------------|:--------------
u-state       |[كِتَابٌ]{.ar} [kitAbun]{.trn}  |[ٱَلْكِتَابُ]{.ar} [alkitAbu]{.trn} 
a-state       |[كِتَابًا]{.ar} [kitAban]{.trn} |[ٱَلْكِتَابَ]{.ar} [alkitAba]{.trn} 
i-state       |[كِتَابٍ]{.ar} [kitAbin]{.trn}  |[ٱَلْكِتَابِ]{.ar} [alkitAbi]{.trn} 

Because, as we said, their ending changes based on their state, they are called flexible nouns.

As opposed to flexible nouns, there are some nouns whose ending is not determined by their state. They can appear the same no matter if they are in the u-state, a-state, or i-state. We will call them _rigid_ nouns. Pronouns are rigid nouns.
-->

## A definite noun as the information {#chap-smp-sent-sec-def-info}

In all the examples so far, the information has been an indefinite noun: "a building", "a teacher", "a cat", etc. It is also possible for the information to be a definite noun:

[ٱَلرَّجُلُ ٱلْمُعَلِّمُ.]{.ar}  
[Earrajulu -lmueallim.]{.trn}  
"The man is the teacher~m~."

<!-- ضمير الفصل is not a copula. It may even have no i3raab depending on one opinion of the grammarians. -->

The above sentence, although correct, is ambiguous. It can also be interpreted as a noun-phrase, meaning "the teacher-man", instead of the complete sentence "The man is the teacher~m~." Therefore, in order to disambiguate and make it clear that we mean the complete sentence, a _disambiguating pronoun_ is usually (but not always) inserted between the subject and the information.
Disambiguating pronouns are detached pronouns that match the subject of the sentence in gender. With a disambiguating pronoun, the sentence above becomes:

[ٱَلرَّجُلُ هُوَ ٱلْمُعَلِّمُ.]{.ar}  
[Earrajulu  huwa -lmueallim.]{.trn}  
"The man is the teacher~m~."

The disambiguating pronoun here is [هُوَ]{.ar} [huwa]{.trn} and is not translated. Here are some more examples of sentences with definite informations and disambiguating pronouns.

[ٱَلْبَيْتُ هُوَ ٱلْبِنَاءُ.]{.ar}  
[Ealbaytu -lbinAEu.]{.trn}  
"The house is the building."

[ٱَلْحَيَوَانُ هِيَ ٱلْهِرَّةُ.]{.ar}  
[EalHayawAnu hiya -lhirratu.]{.trn}  
"The animal is the cat."

## An indefinite noun as the subject

In all the sentences we have seen so far, the subject has always been a definite noun. This is usually the case. A subject needs a certain amount of _weight_ in order to be the first word in a sentence. And being definite gives it this needed weight. That is: "the man" is grammatically _heavier_ than "a man". So it is easier to start a sentence with "the man".

So can we even have a sentence that has an indefinite subject? For example:
<!--How about making the subject an indefinite noun? Can we say:-->

+ A house is a building.
+ A man is the teacher.

Yes, it is possible, but sentences where the subject is an indefinite noun are not as straightforward to express in Arabic. We will explore some ways of expressing them later if [#allAh]{.trn2} wills.

## [وَ]{.ar} [wa-]{.trn} "and", [فَ]{.ar} [fa-]{.trn} "so"/"and then", and [أَوْ]{.ar} [Eaw]{.trn} "or"

### [وَ]{.ar} [wa-]{.trn} "and"

Arabic uses the particle [وَ]{.ar} [wa]{.trn} to mean "and". Being a one-letter particle, it is joined to the word after it without any space between it and the next word. 

[وَمَدْرَسَةٌ]{.ar}  
[wamadrasatun]{.trn}  
"and a school"

[وَ]{.ar} [wa]{.trn} meaning "and" does not change the state of the noun following it. Examples:

[ٱَلْبِنَاءُ مَسْجِدٌ وَمَدْرَسَةٌ.]{.ar}  
[EalbinAEu masjidun wamadrasah.]{.trn}  
"The building is a mosque and a school."

If there are more than two words, then in English, only the final word usually has "and" and the rest are separated by commas in writing. In Arabic, however, each must have [وَ]{.ar} and commas are not typically used.

[ٱَلْبِنَاءُ مَسْجِدٌ وَمَدْرَسَةٌ وَمَكْتَبَةٌ.]{.ar}  
[EalbinAEu baytun wamadrasatun wamaktabah]{.trn}  
"The building is a mosque, a school, and a library."
<!--
[أَخَذَ ٱلرَّجُلُ كِتَابًا وَقَلَمًا.]{.ar}  
[Eaxapa -rrajulu kitAban waqalaman]{.trn}  
"The man took a book and pen."

[دَخَلَتِ ٱلْمَرْأَةُ وَٱلْجَارِيَةُ ٱلْبَيْتَ.]{.ar}  
[daxalati -lmarEatu wa-ljAriyatu -lbayta]{.trn}  
"The woman and the girl entered the house."
-->

We can also use [وَ]{.ar} to begin and connect sentences. The following example is tehcnically two sentences, both beginning with [وَ]{.ar}:

[وَٱلرَّجُلُ إِنْسَانٌ وَٱلْكَلْبُ حَيَوَانٌ]{.ar}  
[warrujulu EinSAnun wa-lkalbu HayawAnun]{.trn}  
"And the man is a human and the dog is an animal."

Unlike as in English, this is not considered poor style. When translating such sentences to English, the first [وَ]{.ar} is often left out, thus:
"The man is a human and the dog is an animal."

### [فَ]{.ar} [fa-]{.trn} "so"/"and then"

The word [فَ]{.ar} [fa-]{.trn} "so"/"and then" is comparable to [وَ]{.ar} [wa-]{.trn} "and". 
[فَ]{.ar} [fa-]{.trn} "so"/"and then"
 gives a meaning of ordering, consequence, and subsequence that is missing in [وَ]{.ar} [wa-]{.trn} "and". For example,

[ٱَلْبِنَاءُ مَسْجِدٌ فَمَدْرَسَةٌ فَمَكْتَبَةٌ.]{.ar}  
[EalbinAEu baytun famadrasatun famaktabah]{.trn}  
"The building is a mosque, and then a school, and then a library."

[فَ]{.ar} [fa-]{.trn} "so"/"and then", too, is used to begin and connect sentences. Example,

[فَٱلرَّجُلُ إِنْسَانٌ وَٱلْكَلْبُ حَيَوَانٌ]{.ar}  
[farrujulu EinSAnun wa-lkalbu HayawAnun]{.trn}  
"So the man is a human and the dog is an animal."


<!--chapter:end:srcrmd/simple_sentences.Rmd-->

# Prepositions

## Introduction

Prepositions are words like "in", "on", "from", etc. They are placed directly before a noun, for example: "in a house". The preposition "in" is placed directly before the noun "a house".

In Arabic prepositions, when placed before a noun, put it in the i-state. For example the preposition [فِي]{.ar} [fI]{.trn} means "in". We can put it before the noun [بَيْت]{.ar} [bayt]{.trn} "a house":

[فِي بَيْتٍ]{.ar}  
[fI baytin]{.trn}  
"in a house"

Note how the noun [بَيْتٍ]{.ar} [baytin]{.trn} "a house" is in the i-state because of the preposition [فِي]{.ar} [fI]{.trn} "in" before it. The i-state is indicated by the [in]{.trn}-mark [◌ٍ]{.ar} on the final letter of [بَيْت]{.ar}.

Arabic has two types of prepositions: _true_ prepositions and _pseudo_-prepositions.

## True prepositions

True prepositions are _particles_. Particles are a class of words, like nouns and verbs. Particles don't have the properties of nouns. Thus, they cannot be definite or indefinite. They cannot be preceded by [ٱَلْ]{.ar} [al]{.trn} or ended with an [n]{.trn}-mark. And they don't have states (u-state, a-state, and i-state). 

Here is a list of the more common true prepositions:

Preposition | Meaning
:--------------|:-------------
[بِ]{.ar}   [bi]{.trn}   | with, by, next to
[لِ]{.ar}   [li]{.trn}   | for, to
[فِي]{.ar}  [fI]{.trn}   | in
[عَلَىٰ]{.ar} [ealA]{.trn} | on
[إِلَىٰ]{.ar} [EilA]{.trn} | to, toward
[مِنْ]{.ar}  [min]{.trn}  | from
[عَنْ]{.ar}  [ean]{.trn}  | from, about
[كَ]{.ar}   [ka]{.trn}   | like

Notes:

+ Prepositions that are a single letter (like 
[بِ]{.ar} [bi]{.trn}, [ل]{.ar} [li]{.trn}, [كَ]{.ar} [ka]{.trn}) are joined to the following noun in writing. Example:
  
  [بِقَلَمٍ]{.ar}  
  [biqalamin]{.trn}  
  "with a pen"

  [لِرَجُلٍ]{.ar}  
  [lirajulin]{.trn}  
  "for a man"

  [كَٱبْنٍ]{.ar}  
  [ka-bnin]{.trn}  
  "like a son"

+ When a single letter preposition comes before a definite noun with [ٱَلْ]{.ar} [al]{.trn}, the preposition is generally joined to the [alif]{.trn} in the [ٱَلْ]{.ar} [al]{.trn}. The [alif]{.trn} is now not pronounced (because as we know it has a connecting [hamzah]{.trn2}). Example:

  [بِٱلْقَلَمِ]{.ar}  
  [bi-lqalami]{.trn}  
  "with the pen"

  If the noun begins with a connecting [hamzah]{.trn2} then the [ل]{.ar} in [ٱَلْ]{.ar} gets an [i]{.trn}-mark [◌ِ]{.ar} instead of its usual [0]{.txt}-mark [◌ْ]{.ar}. We described this in 
section\ \@ref(the-definite-article-with-nouns-with-an-initial-connecting-hamzah).
Example:

  [كَٱلِٱبْنِ]{.ar}  
  [ka-li-bni]{.trn}  
  "like the son"

+ The only exception is the preposition [لِ]{.ar} [li]{.trn}. When joined to a definite noun with [ٱَلْ]{.ar} [al]{.trn}, the [alif]{.trn} in [ٱَلْ]{.ar} is dropped and we write the two [lAm]{.trn}s together. Example:

  [لِلرَّجُلِ]{.ar}  
  [li-rrajuli]{.trn}  
  "for the man"

  [لِلْجَارِيَةِ]{.ar}  
  [li-ljAriyati]{.trn}  
  "for the girl"

  [لِلِٱبْنِ]{.ar}  
  [li-li-bni]{.trn}  
  "for the son"

  However, in this case, if the noun too starts with a [lAm]{.trn}, then we drop the entire [ٱَلْ]{.ar} [al]{.trn} (in writing, not in meaning). This is to avoid having three [lAm]{.trn}s joined to each other. Example:

  [ٱَللُّعْبَةُ]{.ar}  
  [Ealluebatu]{.trn}  
  "the toy"

  becomes

  [لِلُّعْبَةِ]{.ar}  
  [li-lluebati]{.trn}  
  "for the toy"

  not 

  $\times$\ [لِللُّعْبَةِ]{.ar}  

  This is also true for the phrase:

  [لِلَّـٰهِ]{.ar}  
  [lillAhi]{.trn}  
  "for [#allAh]{.trn2}"

  which is formed from [لِ + ٱللَّـٰهِ]{.ar}

+ The prepositions 
[عَلَىٰ]{.ar} [ealA]{.trn} "on" and
[إِلَىٰ]{.ar} [EilA]{.trn} "to" have a long-[A]{.trn} vowel at the end but it is written with a dotless [yAE]{.trn2} [ىٰ]{.ar} instead of an [alif]{.trn}. (We have already learned that some words are written this way in section\ \@ref(a-vowel-written-with-a-ya).)

+ Prepositions that are composed of multiple letters are not joined to the following noun. Example:

  [إِلَىٰ مَدْرَسَةٍ]{.ar}  
  [EilA madrasatin]{.trn}  
  "to a school"

+ If a preposition ends with a long vowel, then, as usual, it get shortened to a short vowel when it is followed by a word which begins with a connecting [hamzah]{.trn2}. Examples:

  [فِي ٱلْبَيْتِ]{.ar}  
  [fi -lbayti]{.trn}  
  "in the house"

  [إِلَى ٱبْنٍ]{.ar}  
  [Eila -bnin]{.trn}  
  "to a son"

+ If a preposition ends with a [0]{.txt}-mark [◌ْ ]{.ar} and it is followed by a word that begins with a connecting [hamzah]{.trn2}, then the [0]{.txt}-mark is changed to a short vowel according to the following rules:

  + The ending of the preposition [عَنْ]{.ar} [ean]{.trn} gets an [i]{.trn}-mark and becomes [عَنِ]{.ar} [eani]{.trn}. Examples:
    
    [عَنِ ٱلرَّجُلِ]{.ar}  
    [eani -rrajuli]{.trn}  
    "from the man"

    [عَنِ ٱبْنٍ]{.ar}  
    [eani -bnin]{.trn}  
    "from the son"

  + The ending of the preposition [مِنْ]{.ar} [min]{.trn} gets an [a]{.trn}-mark if followed by the [ٱَلْ]{.ar} [al]{.trn} of a definite noun. Otherwise it gets an [i]{.trn}-mark if followed by any other connecting [hamzah]{.trn2}. Examples:

    [مِنَ ٱلرَّجُلِ]{.ar}  
    [mina -rrajuli]{.trn}  
    "from the man"

    [مِنِ ٱبْنٍ]{.ar}  
    [mini -bnin]{.trn}  
    "from a son"

## Pseudo-prepositions

Pseudo-prepositions are actually nouns but they are used as prepositions. The above rules of writing and pronunciation apply to them as well.

Here is a list of some common pseudo-prepositions:

Preposition | Transcription | Meaning
:-------|:-------|:-------------
[عِنْدَ]{.ar} | [einda]{.trn} | at
[لَدَىٰ]{.ar} | [ladA]{.trn}  | at
[لَدُنْ]{.ar} | [ladun]{.trn} | at
[مَعَ]{.ar}  | [maea]{.trn}  | together with
[بَيْنَ]{.ar} | [bayna]{.trn} | between, among

There are three different prepositions above that we have translated as "at". [لَدُنْ]{.ar} is relatively rarer compared to the others. Otherwise, they are largely interchangeable but there are some differences in meaning that we will explain later, if [#allAh]{.trn2} wills.

Here are some examples using pseudo-prepositions:

[مَعَ ٱلْغُلَامِ]{.ar}  
[maea -lgulAmi]{.trn}  
"with the boy"

[عِنْدَ ٱلْبَيْتِ]{.ar}  
[einda -lbayti]{.trn}  
"at the house"

[لَدَى ٱلْبَابِ]{.ar}  
[lada -lbAbi]{.trn}  
"at the door"

[بَيْنَ ٱلنَّاسِ]{.ar}  
[bayna -nnAsi]{.trn}  
"among the people"

<!--The preposition [عِنْدَ]{.ar} [einda]{.trn} "at" can be used with a person to mean  "the place of the person". For example

[عِنْدَ ٱلرَّجُلِ]{.ar}  
[einda -rrajuli]{.trn}  

can be used to mean "at the man's [house, etc]."

bayna repeated
-->
## Attached pronouns

We have already learned detached pronouns [هُوَ]{.ar}, [هِيَ]{.ar}, and [أَنَا]{.ar} in section\ \@ref(detached-pronouns). 
Detached pronouns are the equivalent of "he", "she", and "I", etc. They are used in place of nouns that are in the u-state.

Now we will learn about _attached pronouns_. Attached pronouns are, more or less, the equivalent of "him", "her", and "me", etc.
They are used in place of nouns that are in the a-state and the i-state. One place where attached pronouns are used is when the replace the noun directly following a preposition.

The singular attached pronouns are listed below. The detached pronouns are included as well for easy comparison.

Participant | Detached pronoun | Attached pronoun
:------|:----|:----
Masc. absentee | [هُوَ]{.ar}  [huwa]{.trn} "him"      | [هُ]{.ar} [-hu]{.trn} "him"
Fem. absentee  | [هِيَ]{.ar}  [hiya]{.trn} "her"      | [هَا]{.ar} [-hA]{.trn} "her"
Masc. addressee| [أَنْتَ]{.ar} [Eanta]{.trn} "you~1,m~"| [كَ]{.ar} [-ka]{.trn} "you~1,m~"
Fem. addressee | [أَنْتِ]{.ar} [Eanti]{.trn} "you~1,f~"| [كِ]{.ar} [-ki]{.trn} "you~1,f~"
Speaker        | [أَنَا]{.ar} [Eana]{.trn} "I"        | [ي]{.ar} "me"

<!--
Attached pronouns have many uses and we will see in later chapters, if [#allAh]{.trn2} wills, how they attach to nouns and particles. Here we will learn how they are attach to prepositions. 

Attached pronouns are used with prepositions when we want to replace the noun after a preposition with a pronoun. For example, if instead of saying "from the man" we would like to say "from him", or "from me", etc., we will attach the one of attached pronouns above to the end of the preposition.
-->

### Attached pronouns with prepositions

As mentioned above, one place the attached pronouns are used are after prepositions.
Here are some notes regarding how they attach to prepositions:

1. Generally, these pronouns attach to the last letter of the preposition before it. Examples:
   + [مِنْكَ]{.ar} [minka]{.trn} "from you"
   + [مَعَهُ]{.ar} [maeahu]{.trn} "with him"
   + [عَنْهَا]{.ar} [eanhA]{.trn} "from her"
2. The [ىٰ]{.ar} [A]{.trn} ending of prepositions become [◌َيْ]{.ar} [-ay]{.trn} when attaching an attached pronoun. Examples:
   + [إِلَيْهَا]{.ar} [EilayhA]{.trn} "to her"
   + [عَلَيْكَ]{.ar} [ealayka]{.trn} "on you~m~"
6. The pronoun [هُ]{.ar} [-hu]{.trn} "him" becomes [هِ]{.ar} [hi]{.trn} when it is preceded by the vowels [◌ِ]{.ar} [-i]{.trn}, [◌ِي]{.ar} [-I]{.trn}, or the semi-vowel [◌َيْ]{.ar} [-ay]{.trn}. So we get
   + [بِهِ]{.ar} [bihi]{.trn} "with him"
   + [فِيهِ]{.ar} [fIhi]{.trn} "in him"
   + [إِلَيْهِ]{.ar} [Eilayhi]{.trn} "to him"
4. The attached pronoun for the speaker deserves special attention.  The pronoun itself is the letter [ي]{.ar}. But it has two variants:
   i.  [◌ِي]{.ar} [-I]{.trn}
   ii. [◌ِيَ]{.ar} [-iya]{.trn} <!--This has a sub-variant: [يَ]{.ar} [-ya]{.trn}-->

   Generally, both of these variants cause the final letter of the word before them, if a consonant, to have an [i]{.trn}-mark [◌ِ]{.ar}, regardless of the whether or not that letter originally had an [i]{.trn}-mark. Examples:
   + [لِي]{.ar} [lI]{.trn} and      [لِيَ]{.ar} [liya]{.trn} "for me"
   + [بِي]{.ar} [bI]{.trn} and      [بِي]{.ar} [biya]{.trn} "with/by me"
   + [مَعِي]{.ar} [maeI]{.trn} and   [مَعِيَ]{.ar} [maeiya]{.trn} "together with me"
   + [عِنْدِي]{.ar} [eindI]{.trn} and [عِنْدِيَ]{.ar} [eindiya]{.trn} "at me"

   Between these two, variants, [◌ِي]{.ar} [-I]{.trn} is more commonly used generally, except in the cases described in the next point, below:
3. For any word that ends with a long vowel ([-A]{.trn}, [-I]{.trn}, or [-U]{.trn}) or a semi-vowel ([-ay]{.trn} or [-aw]{.trn}), the variant [◌ِي]{.ar} [-I]{.trn} for the speaker attached pronoun is not used. Instead, only the variant [يَ]{.ar} [-ya]{.trn} may be used with such words. 

   Prepositions that fall under this category are [فِي]{.ar} [fI]{.trn}, [عَلَىٰ]{.ar} [ealA]{.trn}, [إِلَىٰ]{.ar} [EilA]{.trn}, and [لَدَىٰ]{.ar} [ladA]{.trn}. Furthermore, the [ىٰ]{.ar} [-A]{.trn} ending in these will become [◌َيْ]{.ar} [ay]{.trn} instead when attaching the pronoun.

   In addition, the pronoun [يَ]{.ar} [-ya]{.trn} will not cause the final letter of word before it to have an [i]{.trn}-mark because it does that only to consonants, not to vowels or semivowels.

   So we get:

   + [يَ]{.ar} + [فِي]{.ar} = [فِيَّ]{.ar} [fiyya]{.trn} "in me"
   + [يَ]{.ar} + [إِلَيْ]{.ar} = [إِلَيَّ]{.ar} [Eilayya]{.trn} "to me"
   + [يَ]{.ar} + [عَلَيْ]{.ar} = [عَلَيَّ]{.ar} [ealayya]{.trn} "on me"
   + [يَ]{.ar} + [لَدَيْ]{.ar} = [لَدَيَّ]{.ar} [ladayya]{.trn} "at me".
7. The preposition [كَ]{.ar} [ka]{.trn} "like" is not used with any attached pronoun. So, for example, we don't say:

   + $\times$\ [كَهُ]{.ar} [kahu]{.trn} for "like him."

   Instead, we will learn another method to express this meaning in later chapters, if [#allAh]{.trn2} wills.
8. The word "between", because of its meaning, is typically used with two or more individuals. For example, "between us", "between you and him", etc. In Arabic, when the pseudo-preposition [بَيْنَ]{.ar} [bayna]{.trn} is used with a singular attached pronoun, it is repeated. For example,

   + [بَيْنِي وَبَيْنَكَ]{.ar} [baynI wabaynaka]{.trn} "between me and you"

<!--
1. When the attached pronoun for the speaker is attached to prepositions that end with [نْ]{.ar}, like [مِنْ]{.ar} [min]{.trn}, [عَنْ]{.ar} [ean]{.trn}, and [لَدُنْ]{.ar} [ladun]{.trn}, an additional intervening [ن]{.ar} is added between the preposition and the attached pronoun. We then get: 
   + [ي]{.ar} + [نِ]{.ar} + [مِنْ]{.ar} = [مِنِّي]{.ar} [minnI]{.trn}
   + [ي]{.ar} + [نِ]{.ar} + [عَنْ]{.ar} = [عَنِّي]{.ar} [eannI]{.trn}
   + [ي]{.ar} + [نِ]{.ar} + [لَدُنْ]{.ar} = [لَدُنِّي]{.ar} [ladunnI]{.trn}
5. The preposition [لِ]{.ar} [li]{.trn} "for" becomes [لَ]{.ar} [la]{.trn} when followed by an attached pronoun, for all pronouns except the speaking person pronoun, where it remains [لِ]{.ar} [li]{.trn}:
   + [لَهُ]{.ar} [lahu]{.trn} "for him"
   + [لَهَا]{.ar} [lahA]{.trn} "for her"
   + [لَكَ]{.ar} [laka]{.trn} "for you~m~"
   + [لَكِ]{.ar} [laki]{.trn} "for you~f~"
   + [لِي]{.ar} [lI]{.trn} and [لِيَ]{.ar} [liya]{.trn} "for me"

1. There are two attached pronouns for the singular person: the long vowel [-I]{.trn}, written as [◌ِي]{.ar}, and [يَ]{.ar} [-ya]{.trn}. 
Generally speaking, they are interchangeable but in normal usage [◌ِي]{.ar} [-I]{.trn} is much more commonly used than [يَ]{.ar} [-ya]{.trn}. 
However, there are certain cases where the long vowel [◌ِي]{.ar} [-I]{.trn} is not permitted and [يَ]{.ar} [-ya]{.trn} is required. 
We will mention those cases below.
2. When using the speaking person attached pronouns [◌ِي]{.ar} [-I]{.trn} and [يَ]{.ar} [-ya]{.trn}, if there is a consonant before either of them it is forced to have a short [i]{.trn}-vowel [◌ِ]{.ar}, if it already doesn't have one. For example:
   + [عِنْدَ]{.ar} [einda]{.trn} followed by [◌ِي]{.ar} [-I]{.trn} becomes [عِنْدِي]{.ar} [eindI]{.trn}.
   + [مَعَ]{.ar} [maea]{.trn} followed by [يَ]{.ar} [-ya]{.trn} becomes [مَعِيَ]{.ar} [maeiya]{.trn}.
1. When the speaking person attached pronoun is attached to prepositions that end with [نْ]{.ar}, like [مِنْ]{.ar} [min]{.trn}, [عَنْ]{.ar} [ean]{.trn}, and [لَدُنْ]{.ar} [ladun]{.trn}, an additional intervening [ن]{.ar} is added between the preposition and the attached pronoun. Being a consonant, this [ن]{.ar} is forced to have a short [i]{.trn}-vowel [◌ِ]{.ar} according to the rule above, and becomes [نِ]{.ar}. In writing, [ن]{.ar} is written only once and is doubled with a doubling mark [◌ّ]{.ar} on it. So we get:
   + [ي]{.ar} + [نِ]{.ar} + [مِنْ]{.ar} = [مِنِّي]{.ar} [minnI]{.trn}
   + [ي]{.ar} + [نِ]{.ar} + [عَنْ]{.ar} = [عَنِّي]{.ar} [eannI]{.trn}
   + [ي]{.ar} + [نِ]{.ar} + [لَدُنْ]{.ar} = [لَدُنِّي]{.ar} [ladunnI]{.trn}
2. The [ىٰ]{.ar} [A]{.trn} ending of prepositions is forced to become [◌َيْ]{.ar} [ay]{.trn} when attaching an attached pronoun. Examples:
   + [إِلَيْهَا]{.ar} [EilayhA]{.trn} "to her"
   + [عَلَيْكَ]{.ar} [ealayka]{.trn} "on you~masc.~"
3. The speaking person attached pronoun [◌ِي]{.ar} [-I]{.trn} is not permitted to used with any word that ends with a long vowel ([-A]{.trn}, [-I]{.trn}, or [-U]{.trn}) or a semi-vowel ([-ay]{.trn} or [-aw]{.trn}). Instead, only [يَ]{.ar} [-ya]{.trn} may be used with such words. 

   Prepositions that end with long vowels and semi-vowels include [فِي]{.ar} [fI]{.trn}, [عَلَىٰ]{.ar} [ealA]{.trn}, [إِلَىٰ]{.ar} [EilA]{.trn}, and [لَدَىٰ]{.ar}  [ladA]{.trn}. 
   And remember that the previous rule forces [ىٰ]{.ar} [A]{.trn} ending in prepositions to become [◌َيْ]{.ar} [ay]{.trn} when attaching a pronoun.

   So when adding the speaking person attached pronoun [يَ]{.ar} [-ya]{.trn} with these prepositions, only one [◌ِي]{.ar} is written and it is doubled thus: [يَّ]{.ar}. Examples:

   + [يَ]{.ar} + [فِي]{.ar} = [فِيَّ]{.ar} [fiyya]{.trn} "in me"
   + [يَ]{.ar} + [إِلَيْ]{.ar} = [إِلَيَّ]{.ar} [Eilayya]{.trn} "to me"
   + [يَ]{.ar} + [عَلَيْ]{.ar} = [عَلَيَّ]{.ar} [ealayya]{.trn} "on me"
   + [يَ]{.ar} + [لَدَيْ]{.ar} = [لَدَيَّ]{.ar} [ladayya]{.trn} "at me".

   Note that the letter before the speaking person attached pronoun [يَ]{.ar} [-ya]{.trn} in these prepositions is not a consonant so it is not forced to have a short [i]{.trn}-vowel [◌ِ]{.ar}.
5. The preposition [لِ]{.ar} [li]{.trn} "for" becomes [لَ]{.ar} [la]{.trn} when followed by an attached pronoun, for all pronouns except the speaking person pronouns [◌ِي]{.ar} [-I]{.trn} and [يَ]{.ar} [ya]{.trn} "me", where it remains [لِ]{.ar} [li]{.trn}:
   + [لَهُ]{.ar} [lahu]{.trn} "for him"
   + [لَهَا]{.ar} [lahA]{.trn} "for her"
   + [لَكَ]{.ar} [laka]{.trn} "for you~masc.~"
   + [لَكِ]{.ar} [laki]{.trn} "for you~fem.~"
   + [لِي]{.ar} [lI]{.trn} and [لِيَ]{.ar} [liya]{.trn} "for me"
6. The pronoun [ـهُ]{.ar} [-hu]{.trn} "him" becomes[هِ]{.ar} [hi]{.trn} when it is preceded by the vowels [◌ِ]{.ar} [i]{.trn}, [ـِي]{.ar} [I]{.trn}, or the semi-vowel [ـَيْ]{.ar} [ay]{.trn}. So we get
   + [بِهِ]{.ar} [bihi]{.trn} "with him"
   + [فِيهِ]{.ar} [fIhi]{.trn} "in him"
   + [إِلَيْهِ]{.ar} [Eilayhi]{.trn} "to him"
7. The preposition [كَ]{.ar} [ka]{.trn} "like" is not used with attached pronouns. So, for example, [كَهُ]{.ar} [kahu]{.trn} is not allowed for "like him."

bayna repeated with pronouns
-->

## Translating prepositions

For each preposition that we have listed above, we have also given its meaning. For example,

+ [فِي]{.ar} [fI]{.trn} "in"
+ [بِ]{.ar} [bi]{.trn} "with", "by", "next to"

These meanings are not always fixed. And there is some degree of overlap in meanings as well. For example, in order to say "in the city" we will usually say
[فِي ٱلْمَدِينَةِ]{.ar} [fi -lmadInati]{.trn} but sometimes we can also say
[بِٱلْمَدِينَةِ]{.ar} [bi -lmadInati]{.trn} with the same meaning. As you keep learning, practicing, and reading Arabic, you will learn how to choose which preposition to use, if Allah wills.

Similarly, sometimes we have two or more prepositions with almost the same meaning. For example,

+ [مِنْ]{.ar}  [min]{.trn}   "from"
+ [عَنْ]{.ar}  [ean]{.trn}   "from", "about"

Knowing when to use one or the other will also take practice.

<!--We will also see that English often uses one preposition to express a meaning, while Arabic will use another preposition to express the same meaning. For example, in English we say "angry _with_".  But Arabic usually uses the preposition [مِنْ]{.ar} [min]{.trn} "from" with [غَاضِبٌ]{.ar} [gADibun]{.trn} "angry" instead of using [بِ]{.ar} [bi]{.trn} "with". So in Arabic we would say [غَاضِبٌ مِنْ]{.ar} [gADibun min]{.trn} but we will still translate it as "angry with". This usage is idiomatic, and as you keep learning you will learn which prepositions to use in which circumstances.-->

## Sentences and phrases with prepositions

We have seen how a noun can be used after a preposition to get a prepositional phrase, for example:

[فِي ٱلْبَيْتِ]{.ar}  
[fi -lbayti]{.trn}  
"in the house"
<!--
[ إِلَى ٱلْمَدِينَةِ]{.ar}  
[Eila -lmadInati]{.trn}  
"to the city"
-->

We can put an indefinite noun in front of this structure:

<!--
[طَريقٌ إِلَى ٱلْمَدِينَةِ]{.ar}  
[TarIqun Eila -lmadInati]{.trn}  
"a way to the city"  
-->

[رَجُلٌ فِي ٱلْبَيْتِ]{.ar}  
[rajulun fi -lbayti]{.trn}  
"a man in the house"

This is a phrase and not a complete sentence.
Note that the preposition [فِي]{.ar} [fI]{.trn} "in" only puts the noun after it ([ٱلْبَيْتِ]{.ar} [Ealbayti]{.trn} "the house") in the i-state. It has no effect on the state of the noun before it ([رَجُلٌ]{.ar} [rajulun]{.trn} "a man"). In this case, it is in the u-state.

Instead of an indefnite noun, we can also put a definite noun in front of the prepositional phrase. Now the resulting structure can, in general, have two meanings: (i) a complete sentence, and (ii) an incomplete sentence. For example,

<!--
[ٱَلطَّريقُ إِلَى ٱلْمَدِينَةِ]{.ar}  
[EaTTarIqu Eila -lmadInati]{.trn}  
1. "The way is to the city."  
2. "The way to the city"
-->

[ٱَلرَّجُلُ فِي ٱلْبَيْتِ]{.ar}  
[Earrujulu fi -lbayti]{.trn}  
(i) "The man is in the house."  
(ii) "The man in the house"

Usually, it will be clear from the context which of the two meanings is valid. For example, the second meaning, "The man in the house", can be part of a complete sentence:
<!--
[ٱَلطَّريقُ إِلَى ٱلْمَدِينَةِ طَوِيلٌ]{.ar}  
[EaTTarIqu Eila -lmadInati TawIlun]{.trn}  
"The way to the city is long."
-->

[ٱَلرَّجُلُ فِي ٱلْبَيْتِ مُعَلِّمٌ.]{.ar}  
[Earrujulu fi -lbayti mueallim.]{.trn}  
"The man in the house is a teacher~m~."

## Sentences with an indefinite subject

We said, in section\ \@ref(an-indefinite-noun-as-the-subject), that the subject of a sentence is usually a definite noun. Now, we shall explore one way of allowing a sentence with an indefinite subject.

We have seen that if an indefinite noun is placed in front of a prepositional phrase, we get an incomplete sentence. For example,

[رَجُلٌ فِي ٱلْبَيْتِ]{.ar}  
[rajulun fi -lbayti]{.trn}  
"a man in the house"

Now we will see how to make the complete sentence (with an indefinite subject): 

"A man **is** in the house."

<!--We have already stated that sentences with indefinite subjects are not straightforward in Arabic. -->
In order to express this sentence, we put the prepositional phrase first, and place the indefinite subject after it:

[فِي ٱلْبَيْتِ رَجُلٌ.]{.ar}  
[fi -lbayti rajul.]{.trn}  
"In the house is a man." = "A man is in the house."

In English, it may sometimes be more convenient to translate this type of sentence using the expression "there is":

"There is a man in the house."

<!--In Arabic, however, we will not use the equivalent of "there" and will express this, as we have just explained, by placing the prepositional phrase first, and the indefinite subject after it.-->

## Prepositions with multiple nouns/pronouns

In English, we can use a preposition with multiple nouns separated by "and", thus:

"The boy went to the school and the house."

A similar meaning can be achieved by repeating the preposition before each noun:

"The boy went to the school and **to** the house."

In Arabic as well, if there are multiple nouns associated with a preposition then you may choose to repeat the preposition or not. Examples:

[إِلَى ٱلمَدْرَسَةِ وَإِلَى ٱلْبَيْتِ]{.ar}  
[Eila -lbayti walmadrasati]{.trn}  
"to the school to and the house"

[إِلَى ٱلمَدْرَسَةِ وَٱلْبَيْتِ]{.ar}  
[Eila -lbayti walmadrasati]{.trn}  
"to the school and the house"

Note that when you don't repeat the preposition, the second noun is still in the i-state.

In English, you have a similar option when you use pronouns instead of nouns. All of the following should be acceptable:

"to the boy and me"  
"to the boy and to me"  
"to him and me"  
"to him and to me"

In Arabic, however, if one or more pronouns is used then the prepositions must be repeated. Examples:

[إِلَيَّ وَإِلَى ٱلْغُلَامِ]{.ar}  
[Eilayya waEila -lgulAmi]{.trn}  
"to me and to the boy"

[إِلَيَّ وَإِلَيْهِ]{.ar}  
[Eilayya waEilayhi]{.trn}  
"to me and to him"

## To have something

English uses the verb "have" or "has" to express that someone 
Arabic does not have a verb for "have" or "has". In order to express sentences like

"I have a book."  
"The boy has a father."  

Arabic uses prepositions like 

+ [لِ]{.ar} [li]{.trn} "for"
+ [عِنْدَ]{.ar} [einda]{.trn} "at"
+ [لَدَىٰ]{.ar} [ladA]{.trn} "at"
+ [مَعَ]{.ar} [maea]{.trn} "together with"

Here are some examples:

[لِلْغُلَامِ أَبٌ.]{.ar}  
[li -lgulAmi Eab.]{.trn}  
"The boy has a father." (literally: "For the boy is a father.")

[عِنْدَ ٱلرَّجُلِ كِتَابٌ.]{.ar}  
[einda -rrajuli kitAb.]{.trn}  
"The man has a book." (literally: "At the man is a book.")

[مَعَ ٱلْجَارِيَةِ لُعْبَةٌ.]{.ar}  
[maea -ljAriyati luebah.]{.trn}  
"The girl has a toy." (literally: "With the girl is a toy.")

Here are some notes that can help you choose which preposition to use to express "has" or "have":

+ [لِ]{.ar} [li]{.trn} "for" is used to express personal relationships, like "I have a friend", "I have a son", etc. It is also used when you wish to imply that you own the object. For example, the sentence

  [لِلرَّجُلِ كِتَابٌ.]{.ar}  
  [li -rrajuli kitAb.]{.trn}  

  implies that the man owns a book. But it is possible that he has lent it to someone else so he does not actually have it on his person or at his house, etc.

+ [عِنْدَ]{.ar} [einda]{.trn} "at" is used to express that the person has the object in his possession, but not necessarily that he has it with him right now. For example the sentence

  [عِنْدَ ٱلرَّجُلِ كِتَابٌ.]{.ar}  
  [einda -rrajuli kitAb.]{.trn}  

  implies that the man has a book in his possession. But it is possible that it may not be with him right now. It may be at his house or elsewhere.

+ [لَدَىٰ]{.ar} [ladA]{.trn} "at" is used to express that the person has the object in his possession and that he has it with him right now. For example the sentence

  [لَدَى ٱلرَّجُلِ كِتَابٌ.]{.ar}  
  [lada -rrajuli kitAb.]{.trn}  

  implies that the man has a book in his possession and that he has it with him right now.

+ [مَعَ]{.ar} [maea]{.trn} "together with" is used to express that the person has the object with him right now. But it doesn't necessarily imply ownership. For example, the sentence 

  [مَعَ ٱلرَّجُلِ كِتَابٌ.]{.ar}  
  [maea -rrajuli kitAb.]{.trn}  

  means that the man has a book with him right now. But it is possible that he does not own it and that someone else has lent it to him.

There is some degree of overlap in meaning and you will get a feeling of which preposition is more appropriate in which circumstance as you progress in your learning, if Allah wills. For now, if you find that the object can be used with all of these prepositions, you might go with [عِنْدَ]{.ar} [einda]{.trn} as it is the more commonly used.


<!--chapter:end:srcrmd/prepositions.Rmd-->

# Completed-action verbs

## Introduction

Verbs are action words. Verbs can be either _completed-action_ verbs where the action of the verb has been completed, e.g., "The boy went." or _incomplete-action_ verbs where the action of the verb is on-going or not yet completed, e.g., "The boy goes." In this chapter we will study _completed-action_ verbs.

## Arabic word roots

We take this opportunity to learn about Arabic roots. 
Native Arabic words, both nouns and verbs, are generally derived from roots. Most roots are comprised of three letters. A smaller number are comprised of four or more letters. 

Words are derived from their roots according to patterns. In traditional Arabic grammar studies, the root [فعل]{.arroot} is used as a paradigm for three-letter roots to showcase word and meaning patterns. 

So for example, the word [بَيْت]{.ar} [bayt]{.trn} "a house" is derived from the root [بيت]{.arroot}. Using the paradigm root [فعل]{.arroot}, we can see that the pattern of the word [بَيْت]{.ar} [bayt]{.trn} is [فَعْل]{.ar} [fael]{.trn}.
The [أَمْر]{.ar} [Eamr]{.trn} "a matter" is derived from the root [ءمر]{.arroot}. Its pattern is also [فَعْل]{.ar} [fael]{.trn}.

Similarly, the word [مَكْتَب]{.ar} [maktab]{.trn} "a library" is derived from the root [كتب]{.arroot}. And [مَلْعَب]{.ar} [maleab]{.trn} "a playground" is derived from the root [لعب]{.arroot}. Using the paradigm root [فعل]{.arroot}, we can see that the pattern of both these words is [مَفْعَل]{.ar} [mafeal]{.trn}. Here, the letter [م]{.ar} [m]{.trn} is an extraneous letter added to form the words and is not part of their roots.

Not only nouns, but verbs, too, are derived from roots. All verbs are derived from their roots in a fixed set of patterns called _forms_ which are numbered 1 onward. For example, the completed-action form 2 verb pattern is [فَعَّلَ]{.ar} [faeeala]{.trn} and the completed-action form 3 verb pattern is [فَاعَلَ]{.ar} [fAeala]{.trn}. There are approximately 9-10 forms that are in common usage. In addition, there are a few higher order forms (11 onward) that are less common. In this chapter will study the completed-action form 1 verb only.

## The form 1 completed-action verb

Here are some examples of completed-action form 1 verbs in Arabic:

Root | Completed-action form 1 verb| Meaning
:----|:----|:----
[فعل]{.arroot} |[فَعَلَ]{.ar} [faeala]{.trn} |"did"
[ذهب]{.arroot} |[ذَهَبَ]{.ar} [pahaba]{.trn} |"went"
[كتب]{.arroot} |[كَتَبَ]{.ar} [kataba]{.trn} |"wrote"
[قرء]{.arroot} |[قَرَأَ]{.ar} [qaraEa]{.trn} |"read"
[جلس]{.arroot} |[جَلَسَ]{.ar} [jalasa]{.trn} |"sat"
[سءل]{.arroot} |[سَأَلَ]{.ar} [saEala]{.trn} |"questioned"
[سكت]{.arroot} |[سَكَتَ]{.ar} [sakata]{.trn} |"became quiet"
[جعل]{.arroot} |[جَعَلَ]{.ar} [jaeala]{.trn} |"made"
[علم]{.arroot} |[عَلِمَ]{.ar} [ealima]{.trn} |"knew"
[عمل]{.arroot} |[عَمِلَ]{.ar} [eamila]{.trn} |"worked"
[كبر]{.arroot} |[كَبُرَ]{.ar} [kabura]{.trn} |"grew"

Note that [فعل]{.arroot}, in addition to being used as a paradigm root, also has a verb in its own right: [فَعَلَ]{.ar} [faeala]{.trn} "did".

Note, also, that the completed-action form 1 verb consists only of the three letters of the root. The first and the final letter always have an [a]{.trn}-mark while the middle letter's vowel is variable. It may have an [a]{.trn}-mark, [i]{.trn}-mark, or an [u]{.trn}-mark, depending on the verb. Using the paradigm root [فعل]{.arroot}, we can say that the form 1 verb occurs in the patterns [فَعَلَ]{.ar}, [فَعِلَ]{.ar}, and [فَعُلَ]{.ar}. 

A good dictionary will tell us the middle vowel mark of a particular verb. However, as a trend, the [a]{.trn}-mark is the most common for the middle vowel mark, followed by the [i]{.trn}-mark, while the [u]{.trn}-mark is the least common.

Interestingly, there can exist multiple verbs from the same root, each with its own distinct meaning, that differ only in the vowel mark on the middle letter. An example of two such verbs is:

+ [حَسَبَ]{.ar} [Hasaba]{.trn} "calculated"
+ [حَسِبَ]{.ar} [Hasiba]{.trn} "deemed"

You can see above how the verb [كَتَبَ]{.ar} [kataba]{.trn} "wrote" is derived from the root [كتب]{.arroot}. We have already, by the way, learned another word derived from this root: the noun [كِتَاب]{.ar} [kitAb]{.trn} "a book", which is on the pattern [فِعَال]{.ar} [fieAl]{.trn}. Note how both the verb and the noun derived from this root have a meaning that is common and has to do with writing or of something written. 
In a similar manner, you will often see that words derived from the same root generally share some common meaning, although this common meaning may not always be obvious or straightforward.

## Verbal sentences

We have already learned of subject-information sentences. Here we will learn of a new type of sentence called a _verbal sentence_. A verbal sentence is one that begins with a verb.

When a verb is in a sentence, it requires a doer. The doer is a noun which represents the person who does the action of the verb. For example, in the sentence "The boy went.", the noun "the boy" is the doer of the verb.

### Verbs with a masculine doer noun

Consider the sentence:

"The boy went." 

In order to express this sentence in Arabic, we will say:

[ذَهَبَ ٱلْغُلَامُ.]{.ar}  
[pahaba -lgulAm.]{.trn}  
"The boy went." 

[ذَهَبَ]{.ar} [pahaba]{.trn} "went" is the verb and [ٱلْغُلَامُ]{.ar} [algulAmu]{.trn} "the boy" is the doer. Note how the doer is in the u-state. Also note that in English the doer comes before the verb whereas in Arabic the doer comes after the verb in sentence word order. We can state this as a rule of Arabic grammar: 

**In Arabic, every verb in a sentence shall have a doer noun. The doer noun shall be in the u-state and shall come after the verb in sentence word order.**

<!--In Arabic, a doer noun shall always be in the u-state and shall come after the verb in word order.

The basic form of the verb [ذَهَبَ]{.ar} [pahaba]{.trn} is specifically for masculine doers. We shall see in the next section how the verb is modified for feminine doers. 

The doer may be definite, indefinite, a common noun, or a proper noun. Examples:

A boy went.

Muhammad went.

The time went.
-->

In the above example the doer noun was definite, but a doer may be indefinite too. Example:

[ذَهَبَ رَجُلٌ إِلَىَ ٱلسُّوقِ.]{.ar}  
[pahaba rajulun Eila -ssUq.]{.trn}  
"A man went to the market."

In the above sentence, the doer noun [رَجُلٌ]{.ar} [rajulun]{.trn} is indfinite.

### Verbs with a feminine doer noun

Now consider the sentence:

"A girl went." 

In order to express this sentence in Arabic, we will say:

[ذَهَبَتْ جَارِيَةٌ.]{.ar}  
[pahabat jAriyah.]{.trn}  
"A girl went." 

Note that we have modified the verb by adding on the letter [تْ]{.ar} at the end. This [تْ]{.ar} is used when the doer is ia feminine noun. It is called the [تْ]{.ar} of femininity. 

If the word following the noun begins with a connecting [hamzah]{.trn2} then we add a helper vowel to the [تْ]{.ar} and it becomes [تِ]{.ar}. Examples:

[جَلَسَتِ ٱلْهِرَّةُ عَلَى ٱلْكُرْسِيِّ.]{.ar}  
[jalasati -lhirratu eala -lkursiyyi.]{.trn}  
"A cat~f~ sat on the chair."

[لَعِبَتِ ٱلطِّفْلَةُ فِي ٱلْبَيْتِ.]{.ar}  
[laeibati -TTiflatu fi -lbayt.]{.trn}  
"The child~f~ played in the house."
<!--
[عَلِمَتْ ٱمْرَأَةٌ.]{.ar}  
[pahabati -mraEatun.]{.trn}  
"A woman went."

Note that whether or not we add a helper vowel to [تْ]{.ar}, the letter before it always has an [a]{.trn}-mark.
-->

## Verbs with doees

### Direct doees

Consider the sentence:

"The man wrote a book."

In this sentence, "wrote" is the verb, "the man" is the doer, and "a book" is what we shall call the _doee_. In fact, it is what we shall call a _direct doee_ because it comes directly after the verb without an intermediate preposition. A doee is the noun to whom the action of verb is done. 

In Arabic, we will express the sentence "The man wrote a book." by saying:

[كَتَبَ ٱلرَّجُلُ كِتَابًا.]{.ar}  
[kataba -rrajulu kitAbA.]{.trn}  
"The man wrote a book."

Note how in Arabic the doee [كِتَابًا]{.ar} [kitAban]{.trn} "a book" is in the a-state. This is because, in Arabic, verbs shall cause a direct doee to be in the a-state. This is true whether the direct doee is definite or indefinite. Here is another example:

<!--[ضَرَبَتِ ٱلْمَرْأَةُ ٱلْجَارِيَةَ.]{.ar}  
[Darabati -lmarEatu -ljAriyata.]{.trn}  
"The woman hit the girl."
-->

[سَأَلَتِ ٱلْأُمُّ ٱلْجَارِيَةَ.]{.ar}  
[saEalati -lEummu -ljAriyah.]{.trn}  
"The mother questioned the girl."

Note again how [ٱلْجَارِيَةَ]{.ar} [aljAriyata]{.trn} "the girl" is in the a-state because it is a direct doee.

### Multiple direct doees

Some verbs can take more than one direct doee. In this case, all direct doees shall be in the a-state. For example,

[جَعَلَ ٱللَّـٰهُ ٱلرَّجُلَ مُسْلِمًا.]{.ar}  
[jaeala -llAhu -rrajula muslimA.]{.trn}  
"[#allAh]{.trn2} made the man a Muslim."

In this sentence both [ٱلرَّجُلَ]{.ar} [arrajula]{.trn} "the man" and [مُسْلِمًا]{.ar} [musliman]{.trn} "a Muslim" are direct doees of the verb [جَعَلَ]{.ar} [jaeala]{.trn} and therefore both are placed in the a-state.

### Indirect doees

Instead of, or in addition to, direct doees, some verbs take an _indirect doee_. An indirect doee is one before which there is a preposition. For example, in English we might say:

"The man looked at the moon."

In this sentence, "the moon" is an indirect doee because it is preceded by the preposition "at". Similarly, in Arabic, we will say:

[نَظَرَ ٱلرَّجُلُ إِلَى ٱلْقَمَرِ.]{.ar}  
[naPara -rrajulu Eila -lqamar.]{.trn}  
"The man looked at the moon."

In this sentence [ٱَلْقَمَرِ]{.ar} [alqamari]{.trn} "the moon" is an indirect doee of the verb [نَظَرَ]{.ar} [naPara]{.trn} "looked" because it is preceded by the preposition [إِلَىٰ]{.ar} [EilA]{.trn} "to". The preposition, as usual, causes the word after it (the indirect doee [ٱَلْقَمَرِ]{.ar} [Ealqamari]{.trn}) to be in the i-state, as opposed to the a-state of the direct doee.

Note also, that the verb "looked" in English used the preposition "at" whereas the Arabic verb [نَظَرَ]{.ar} [naPara]{.trn} used the preopsition [إِلَىٰ]{.ar} [EilA]{.trn} "to" for the same meaning. This is very common and you should not expect Arabic to use exact counterparts of the prepositions used in English. In fact, everytime you learn a new verb, you should also learn the prepositions that go with it.

It is also possible for the same verb to take different prepositions with possibly different meanings. So, for example, we can say:

[نَظَرَ ٱلرَّجُلُ فِي ٱلْأَمْرِ.]{.ar}  
[naPara -rrajulu fi -lEamri.]{.trn}  
"The man looked into the matter."
<!-- « فَنَظَرَ نَظْرَة فِي النُّجُومِ» سورة الصافات(88) -->

It may also be possible for the same verb to take a direct doee. So we could also say:

[نَظَرَ ٱلرَّجُلُ ٱلْمَكْتُوبَ فِي ٱلْكِتَابِ.]{.ar}  
[naPara -rrajulu -lmaktUba fi -lkitAbi.]{.trn}  
"The man viewed what was written in the book."
<!--This example from Lane. Also: « يَوْمَ يَنظُرُ الْمَرْءُ مَا قَدَّمَتْ يَدَاهُ» سورة النبأ،(40)-->

A good dictionary will tell us which prepositions are used with indirect doees with a given verb and also whether it takes a direct doee.

Some verb take a direct doee and another indirect doee, both at the same time. For example,

[سَأَلَ ٱلْغُلَامُ ٱلْمُعَلِّمَةَ عَنْ أَمْرٍ.]{.ar}  
[saEala -lgulAmu -lmueallimata ean Eamr.]{.trn}  
"The boy asked the teacher~f~ about a matter."

[ٱَلْمُعَلِّمَةَ]{.ar} [Ealmueallimata]{.trn} "the teacher~f~" is the direct doee, and therefore it is in the a-state.
[أَمْرٍ]{.ar} [Eamrin]{.trn} "a matter" is an indirect doee, and so it is in the i-state.
The preposition [عَنْ]{.ar} [ean]{.trn} is translated, here, as "about".

It is also possible that an English verb may take a direct doee, while the corresponding Arabic verb may only take an indirect doee. The reverse is also quite possible. For example,

[غَفَرَ ٱللَّـٰهُ لِلْمُسْلِمِ.]{.ar}  
[gafara -llAhu lilmuslimi.]{.trn}  
"[#allAh]{.trn2} forgave the Muslim."

The verb "forgave" in English takes a direct doee for the person who is forgiven. In Arabic, however, the corresponding verb [غَفَرَ]{.ar} [gafara]{.trn} "forgave" takes the forgiven person as an indirect doee, using the preposition [لِ]{.ar} [li]{.trn}.

## Verbs with doer pronouns

We have learned that a pronoun is a special kind of noun that can be used to replace a definite noun. And we have already learned two category of pronouns in Arabic:

i.  Detached pronouns, like [هُوَ]{.ar}, [هِيَ]{.ar}, etc.
ii. Attached pronouns, like [هُ]{.ar}, [هَا]{.ar}, etc.

Now we would like to replace the doer noun of a verb with a pronoun. For example, instead of saying:

"The man went."

we would like to say:

"He went."

For this we will have to learn a third category of pronoun pronouns called _doer pronouns_ for completed-action verbs.
Doer pronouns are of two types: visible and invisible.

Here we list the singular doer pronouns in Arabic. 

Singular participant | Doer pronoun
:------|:--
Masc. absentee ("he")      | invisible
Fem. absentee ("she")      | invisible
Masc. addressee ("you~1,m~") | [تَ]{.ar} [-ta]{.trn}
Fem. addressee ("you~1,f~")  | [تِ]{.ar} [-ti]{.trn}
Speaker ("I")              | [تُ]{.ar} [-tu]{.trn}

We will now give an explanation of the above doer pronouns.

### Doer pronouns for the singular absentee-participant ("he"/"she")

The doer pronouns of the absentee-participant are the equivalent of "he" and "she". For example, let's try to replace the doer-noun "the man" in the sentence: "The man went."

[ذَهَبَ ٱلرَّجُلُ.]{.ar}  
[pahaba -rrajul.]{.trn}  
"The man went."

When we replace the doer noun [ٱلرَّجُل]{.ar} [Earrujul]{.trn} "the man" with the doer pronoun "he", we get:

[ذَهَبَ.]{.ar}  
[pahab.]{.trn}  
"[He] went."

As you can see, all we did was omit the doer-noun [ٱَلرَّجُل]{.ar} [Earrujul]{.trn}, and we didn't add any word to replace it as the doer pronoun. This is because the doer pronoun for "he" is _invisible_ and automatically comes into place when we omit the doer noun.

The doer pronoun for "she" is similarly invisible.
For example, if we replace the doer noun in the sentence:

[قَرَأَتِ ٱلْجَارِيَةُ كِتَابًا.]{.ar}  
[qaraEati -ljAriyatu kitAbA.]{.trn}  
"The girl read a book."

we get:

[قَرَأَتْ كِتَابًا.]{.ar}  
[qaraEat kitAbA.]{.trn}  
"[She] read a book."

#### Explanation of invisible pronouns

Why do we have to go to all the trouble of saying that the doer-pronouns of the singular masculine absentee-participant "he"/"she" are invisible? Why can't we simply say that there are no doer-pronouns for the singular masculine absentee-participant?

The reason is that making the statement that these pronoun exist but are invisible is useful to us from the perspective of the grammar theory that we are building.

That is: we need to be able to state, as a rule of grammar, that every verb needs to have a doer, whether visible or not. And that doer shall come after the verb in sentence word order.

If we are able to make this a rule, then we will see, if [#allAh]{.trn2} wills, that it will help us later. For example, when we study verbs with plural doers.

### Doer pronouns for the singular addressee ("you~1~") and speaker ("I") participants

It is only the doer pronouns for the singular absentee participant that are invisible for completed-action verbs. The doer pronouns for the singular addressee and speaker participants are visible. When visible, the doer pronouns are attached to the verb.

Here we show how the visible doer pronouns are attached to the verb using the root paradigm [فعل]{.arroot}. The middle root letter ([ع]{.ar}) has an [a]{.trn}-vowel [◌َ]{.ar} here but this vowel will vary for other verbs.

Singular participant | Doer pronoun | Doer pronoun with verb
:------|:--|:--
Addressee "you~1,m~" | [تَ]{.ar} [-ta]{.trn} | [فَعَلْتَ]{.ar} [faealta]{.trn}
Addressee "you~1,f~" | [تِ]{.ar} [-ti]{.trn} | [فَعَلْتِ]{.ar} [faealti]{.trn}
Speaker "I"          | [تُ]{.ar} [-tu]{.trn} | [فَعَلْتُ]{.ar} [faealtu]{.trn}

Note also how the visible singular doer pronouns modify the verb by replacing the [a]{.trn}-mark [◌َ]{.ar} on its final letter by a [0]{.txt}-mark [◌ْ]{.ar}.

Furthermore, note how the doer pronoun for the addressed person "you" is differentiated for masculine and feminine doers whereas the doer pronoun for the speaking person "I" is the same for both genders.

Here are some examples of sentences with visible doer pronouns:

[كَتَبْتَ كِتَابًا.]{.ar}  
[katabta kitAbA.]{.trn}  
"You~m~ wrote a book."

[ذَهَبْتُ]{.ar}  
[pahabt.]{.trn}  
"I went."

The above sentence ends with the doer pronoun, so the vowel-mark on the doer pronoun is not pronounced ([pahabt]{.trn}). So, how would be know which doer pronoun it is? That is, does the sentence say "I went." or "You~m~ went." or "You~f~. went."? The answer is that the sentence by itself is ambiguous and context would tell us which of the three options is intended.

Take care to note that the singular doer pronouns modify the final letter of the basic verb, whereas the [تْ]{.ar} of femininity does not. So make sure you see the difference in the following two sentences:

[قَرَأْتِ ٱلْكِتَابَ.]{.ar}  
[qaraEti -lkitAb.]{.trn}  
"You~f~ read the book."

[قَرَأَتِ ٱلْكتَابَ.]{.ar}  
[qaraEati -lkitAb.]{.trn}  
"She read the book."

### Assimilation of the doer pronoun

If the final letter of the root of a verb is [ت]{.ar}, then it gets assimililated with the [ت]{.ar} which is the doer pronoun and only one [ت]{.ar}, representing both, is written. Consider the verb:

[سكت]{.arroot} [سَكَتَ]{.ar} [sakata]{.trn} "became quiet"

When we add a visible doer pronoun to this verb, we get:

[سَكَتُّ]{.ar}  
[sakattu]{.trn}  
"I became quiet"

[سَكَتَّ]{.ar}  
[sakatta]{.trn}  
"You~1,m~ became quiet"

[سَكَتِّ]{.ar}  
[sakatti]{.trn}  
"You~1,f~ became quiet"

Assimilation is treated in more detail in chapter/appendix TODO.

## Verbs with doee pronouns

Just like doer nouns may be replaced with doer pronouns, so, too, may doee nouns be replaced with _doee pronouns_. Doee pronouns are also attached to the end of the verb but they don't modify the vowel on the final letter of the verb. The doee pronouns are the same attached pronouns that are also used with prepositions:

Singular participant | Doee pronoun
:------|:--
Masc. absentee  | [هُ]{.ar} [-hu]{.trn}    "him"   
Fem. absentee   | [هَا]{.ar} [-hA]{.trn}   "her"   
Masc. addressee | [كَ]{.ar} [-ka]{.trn}    "you~1,m~"
Fem. addressee  | [كِ]{.ar} [-ki]{.trn}    "you~1,f~"
Speaker         | [ي]{.ar}                "me"    

Here are some notes regarding their usage:

+ Doee pronouns shall always be attached to the verb. So if there is a doer noun then it shall be placed after the attached doee pronoun. For example:

  [سَأَلَهُ ٱلْغُلَامُ.]{.ar}  
  [saEalahu -lgulAm.]{.trn}  
  "The boy asked him."

+ If however, the doer is also a pronoun, then it shall be attached first to the verb and then the doee pronoun shall be attached to the doer pronoun. For example,

  [سَأَلْتُكِ.]{.ar}  
  [saEaltuk.]{.trn}  
  "I asked you~f~."

+ If the doer pronoun is invisible, then the doee pronoun shall be attached to the verb again directly with only a possible [تْ]{.ar} of femininity intervening. For example:

  [سَأَلَهَا.]{.ar}  
  [saEalahA.]{.trn}  
  "He asked her."

  [سَأَلَتْكَ.]{.ar}  
  [saEalatk.]{.trn}  
  "She asked you~m~."

+ If the doee pronoun [هُ]{.ar} [-hu]{.trn} "him" is preceded by the vowels [i]{.trn}, [I]{.trn}, or [ay]{.trn} then it shall instead become [هِ]{.ar} [hi]{.trn} with no change in meaning. (We've already learned this rule.) For example,

  [سَأَلْتِهِ.]{.ar}  
  [saEaltih]{.trn}  
  "You~f~ asked him."

+ An intervening [ن]{.ar} is always used between the verb and the speaker-participant doee pronoun variants [◌ِي]{.ar} [-I]{.trn} and [◌ِيَ]{.ar} [-iya]{.trn}. Remember that these pronouns force any consonant before it to have a [i]{.trn}-mark [◌ِ]{.ar}. Therefore, the combination will be written as [نِي]{.ar} [-nI]{.trn} and [نِيَ]{.ar} [-niya]{.trn} respectively. For example:

  [سَأَلَنِي رَجُلٌ.]{.ar}  
  [saEalanI rajul.]{.trn}  
  "A man asked me."

  [سَأَلَنِيَ ٱلرَّجُلُ.]{.ar}  
  [saEalaniya -rrajul.]{.trn}  
  "The man asked me."

  <!--The [ن]{.ar} is purely for intervening between the verb and the doee pronoun and has no meaning on its own.-->
  If there is a visible doer pronoun, the intervening [ن]{.ar} shall come after it so that the [ن]{.ar} is always connected to the doee pronoun. For example,

  [سَأَلْتَنِي.]{.ar}  
  [saEaltanI]{.trn}  
  "You~m~ asked me."

  By the way, we have already seen this intervening [ن]{.ar} before when it was used with some prepositions, e.g. [مِنِّي]{.ar} [minnI]{.trn}, [عَنِّي]{.ar} [eannI]{.trn}, and [لَدُنِّي]{.ar} [ladunnI]{.trn}
  <!--So why don't we simply incorporate the [ن]{.ar} with the doee pronoun and say that the doee pronoun for "me" is [نِي]{.ar} [-nI]{.trn} and [نِيَ]{.ar} [-niya]{.trn}? This is because in addition to their use as doee pronouns, these same pronouns are also used in other places as we shall see later, if [#allAh]{.trn2} wills, and in those cases there is often no intervening [ن]{.ar} for the speaking person pronoun. -->

  Even though, the variant [◌ِي]{.ar} [-I]{.trn} is, in general, more commonly used, when the noun following it begins with a connecting [hamzah]{.trn2} then the variant [◌ِيَ]{.ar} [-ya]{.trn} is preferred. That is why we used the variant [◌ِيَ]{.ar} [-ya]{.trn} when it was followed by a connecting [hamzah]{.trn2} ([سَأَلَنِيَ ٱلرَّجُلُ.]{.ar}), and the variant [◌ِي]{.ar} [-I]{.trn} when it was not followed by a connecting [hamzah]{.trn2} ([سَأَلَنِي رَجُلٌ.]{.ar}). 

  This preference is not mandatory. So it is allowed for [◌ِي]{.ar} [-I]{.trn} to be used when followed by a connecting [hamzah]{.trn2}. When this happens, the long vowel [-I]{.trn} will be shortened to [-i]{.trn} in connecting it to the next word, although the [◌ِي]{.ar} is retained in writing. For example,

  [سَأَلَنِي ٱلرَّجُلُ.]{.ar}  
  [saEalani -rrajul.]{.trn}  
  "The man asked me."

  <!--However, [يَ]{.ar} [-ya]{.trn} is typically not used as a doee pronoun if not followed by a connecting [hamza]{.trn}. -->

  <!--To summarize, generally speaking, although both are often permissible, [◌ِي]{.ar} [-I]{.trn} is the more commonly used in all circumstances except in specific cases where [◌ِي]{.ar} [-I]{.trn} is impermissible and [يَ]{.ar} [-ya]{.trn} is required. We will mention those cases when we encounter them, if [#allAh]{.trn2} wills.-->

<!--Examples from Quran: لا يَنَالُ عَهْدِي الظَّالِمِينَ).

2- في كلمات أخرى، هي: (مَعِيَ) حيثما وقعت، و(أَجْرِيَ إلاَّ) وهي في تسعة مواضع، و(يَدِيَ إِلَيْكَ) بالمائدة، (وَأُمِّيَ إِلَهَيْنِ) بالمائدة، و(بَيْتِيَ لِلطَّائِفِينَ) بالبقرة والحج، و(بَيْتِيَ مُؤْمِنًا) بنوح، و(وَجْهِيَ للهِ) بآل عمران، و(وَجْهِيَ لِلَّذِي) بالأنعام 

http://www.alfaseeh.com/vb/showthread.php?t=93064A-->

## Multiple verbs for one doer

In this section we will use the verbs:

Root | Completed-action form 1 verb| Meaning
:----|:----|:----
[دخل]{.arroot} |[دَخَلَ]{.ar} [daxala]{.trn} |"entered"
[خرج]{.arroot} |[خَرَجَ]{.ar} [xaraja]{.trn} |"exited"
[ءكل]{.arroot} |[أَكَلَ]{.ar} [Eakala]{.trn} |"ate"
[شرب]{.arroot} |[شَرِبَ]{.ar} [cariba]{.trn} |"drank"

Consider, now, the sentence:

"I entered the room, ate, drank, and exited."

The doer in this sentence is the pronoun "I". This same doer is doing the action of multiple verbs:
"entered", "ate", "drank", and "exited".
When we try to express this sentence in Arabic we must remember that every verb shall have its own doer, and that the doer shall occur after it in sentence word order. So we will say:

[دَخَلْتُ ٱلْغُرْفَةَ فَأَكَلْتُ فَشَرِبْتُ فَخَرَجْتُ.]{.ar}  
[daxaltu -lgurfata faEakaltu facaribtu faxarajt.]{.trn}  
"I entered the room and then I ate and then I drank and then I exited."

Note also, that we need to replace the commas by connecting particles like [وَ]{.ar} [wa-]{.trn} "and", or [فَ]{.ar} [fa-]{.trn} "so"/"and then", etc. We chose
[فَ]{.ar} [fa-]{.trn} which implies consequence or subsequence between the individual events.

Let's now try this sentence with a doer noun instead of a doer pronoun:

"The girl entered the room, ate, drank, and exited."

Here is our translation:

[دَخَلَتِ ٱلْجَارِيَةُ ٱلْغُرْفَةَ فَأَكَلَتْ فَشَرِبَتْ فَخَرَجَتْ.]{.ar}  
[daxalati -ljAriyatu -lgurfata faEakalat facaribat faxarajat.]{.trn}  
"The girl entered the room and then she ate and then she drank and then she exited."

Each verb again has its own doer, which is coming after the verb in sentence word order. The doer of the first verb [دَخَلَ]{.ar} [daxala]{.trn} "entered" is the noun 
[ٱَلْجَارِيَةُ]{.ar} [EaljAriyatu]{.trn} "the girl".
The subsequent verbs all have doers too but they are the invisible doer pronouns for the singular feminine absentee participant. That is why we don't write them. Note also that every verb has the [تْ]{.ar} of femininity attached to it to indicate its singular feminine absentee doer.
<!--
In a sentence that has multiple verbs separated by "and", normally one of them is placed before the doer and the rest after it. For example,

[أَكَلَ ٱلرَّجُلُ وَشَرِبَ.]{.ar}  
[Eakala -rrajulu wacariba.]{.trn}  
"The man ate and drank."

The first verb [أَكَلَ.]{.ar} [Eakala]{.trn} has the doer [ٱلرَّجُلُ]{.ar} [Earrajulu]{.trn}, and the second verb [شَرِبَ]{.ar} [cariba]{.trn} has an invisible doer pronoun "he".
-->

## Order of words in a sentence

### Changing the order of words for emphasis {#past-verbs-order-of-words}

In Arabic, the doer always follows the verb. So the normal order of a sentence is verb-doer-doee. For example,

[كَتَبَ ٱلرَّجُلُ كِتَابًا.]{.ar}  
[kataba -rrajulu kitAbA.]{.trn}  
"The man wrote a book."

However, we will often come across sentences like:

[ٱَلرَّجُلُ كَتَبَ كِتَابًا.]{.ar}  
[Earrajulu kataba kitAbA.]{.trn}

It may appear as if [ٱَلرَّجُلُ]{.ar} [arrajulu]{.trn} is the doer and it is coming before the verb [كَتَبَ]{.ar} [kataba]{.trn}. But actually, this is not the case. As a matter of fact, this sentence is basically a subject-information sentence. 

Here [ٱَلرَّجُلُ]{.ar} [arrajulu]{.trn} "the man" is the subject of the sentence, and [كَتَبَ كِتَابًا]{.ar} [kataba kitAban]{.trn} "he wrote a book", itself a verbal sentence with an invisible doer pronoun, is the information about the subject. So the translation of the sentence is technically:

"The man, he wrote a book."

However, this is an awkward translation so we will usually translate it as "The man wrote a book." <!--But this is also the translation of:

[كَتَبَ ٱلرَّجُلُ كِتَابًا.]{.ar}  
[kataba -rrajulu kitAban.]{.trn}  
"The man wrote a book."
-->

The question arises: if both sentences above have the same translation, then would we say [ٱَلرَّجُلُ كَتَبَ كِتَابًا.]{.ar} [Earrajulu kataba kitAban.]{.trn} instead of the more normal [كَتَبَ ٱلرَّجُلُ كِتَابًا.]{.ar} [kataba -rrajulu kitAban.]{.trn}? The answer is that this change in the sentence's word order is done in order to give more emphasis to the doer, as if to say:

"_The man_ wrote a book."

So in Arabic, the order of words is generally more flexible than in English and this is often used to give emphasis to certain words.

### Verbs pull definite nouns towards them

When a verb has a doer noun and a doee noun, the normal order of words in a sentence is: verb, doer noun, doee noun. For example,

[كَتَبَ ٱلرَّجُلُ ٱلْكِتَابَ.]{.ar}  
[kataba -rrajulu -lkitAba.]{.trn}  
"The man wrote the book."

There is a tendency, in Arabic, for verbs to _pull_ definite nouns towards them. This means that if there are any indefinite nouns, they have a tendency to get pushed father away. So, for example,
if a verb's doer is an indefinite noun and the doee is a definite noun, the doee will often (but not always) precede the doer. For example,

[كَتَبَ ٱلْكِتَابَ رَجُلٌ.]{.ar}  
[kataba -lkitAba rajul.]{.trn}  
"A man wrote the book."

The vowel-marks at the end of the nouns, and context, will tell us which is the doer and which is the doee. In this particular example, it was optional, and not mandatory to make the definite doee precede the doer in sentence word order. So we could have also said, instead:

[كَتَبَ رَجُلٌ ٱلْكِتَابَ.]{.ar}  
[kataba rajuluni -lkitAb.]{.trn}  
"A man wrote the book."

Now let's take a look at sentences with pronouns. Remember that pronouns are a category of nouns, and also (from section\ \@ref(definiteness-of-pronouns)) that they are definite nouns. In fact they are stronger in definiteness than words that are made definite using [ٱَلْ]{.ar}. This because if when we say "The man wrote the book." instead of "A man wrote the book.", we assume that everyone knows which man we are referring to. Now if we replace "the man" with the pronoun "he": "He wrote the book.", then this assumption becomes stronger. "He" is, in a sense, more definite than "the man.".

So now, when the direct doee noun [ٱلْكِتَابَ]{.ar} [EalkitAba]{.trn} "the book" is replaced with the pronoun "it", the doee pronoun must be attached to the verb, and then the doer noun follows the doee pronoun:

[كَتَبَهُ ٱلرَّجُلُ.]{.ar}  
[katabahu -rrajulu.]{.trn}  
"The man wrote it."

This can be seen as a mandatory case of the verb pulling the definite noun toward it.

Now, consider a sentence with an indirect doee. Again, the normal order of words in a sentence is verb, doer noun, preposition, doee noun. For example,

[ذَهَبَ ٱلْغُلَامُ إِلَى ٱلْمَدْرَسَةِ.]{.ar}  
[pahaba -lgulAmu Eila -lmadrasah.]{.trn}  
"The boy went to the school."

Now, if we replace the indirect doee noun [ٱلْمَدْرَسَةِ.]{.ar} [Ealmadrasati]{.trn} "the school" with the pronoun "it", the indirect doee pronoun [هَا]{.ar} [-hA]{.trn} "it" is attached, not to the verb, but to the preposition [إِلَىٰ]{.ar} [EilA]{.trn} thus: [إِلَيْهَا]{.ar} [EilayhA]{.trn} "to it". So it possible to preserve the original order of words in the sentence:

[ذَهَبَ ٱلْغُلَامُ إِلَيْهَا.]{.ar}  
[pahaba -lgulAmu EilayhA.]{.trn}  
"The boy went to it."

While the above sentence is correct, it is in fact more common to place the preposition and doee pronoun [إِلَيْهَا]{.ar} [EilayhA]{.trn} "to it" right after the verb, and before the doer noun, thus:

[ذَهَبَ إِلَيْهَا ٱلْغُلَامُ.]{.ar}  
[pahaba Eilayha -lgulAmu.]{.trn}  
"The boy went to it."

This is because the pronoun [هَا]{.ar} [-hA]{.trn} "it" is stronger in definiteness than [ٱلْغُلَام]{.ar} [EalgulAm]{.trn} "the boy". So the verb has a stronger pull towards it.
<!--This is because if there is a doee pronoun for a verb, whether direct or indirect, the verb has an effect of pulling the doee pronoun toward it. When it is a direct doee pronoun, the doee pronoun is necesarrily attached to the verb. But even when it is an indirect doee pronoun, the effect persists, and it tends to pull the preposition and doee pronoun toward the verb, even before the verb's doer noun.-->

This ordering of words due to the attractive pull of the verb is largely learned by experience. The more you read Arabic, the better feel you will get for it, if [#allAh]{.trn2} wills.

## Negating completed-action verbs

In order to negate a completed-action verb, the particle [مَا]{.ar} [mA]{.trn} is placed before it. This gives the meaning of the action of the verb did not get, or has not got, done. So for example:

[مَا ذَهَبَ ٱلرَّجُلُ.]{.ar}  
[mA pahaba -rrajulu.]{.trn}  
"The man did not go." or,  
"The man has not gone."

## The particle [قَدْ]{.ar} [qad]{.trn}

The particle [قَدْ]{.ar} [qad]{.trn}, when placed before a completed-action verb emphasizes that the action of the verb has already or definitely occured.

[قَدْ ذَهَبَ ٱلرَّجُلُ.]{.ar}  
[qad pahaba -rrajulu.]{.trn}  
"The man has already gone." or,  
"The man did go."

## Separating doee pronouns from the verb

FIXME: move to imperfect verb chapter

We have mentioned that doee pronouns are attached to the verb. Sometimes there is a need to separate the doee pronoun from the verb. When separating the doee pronoun from the verb, it is instead attached to the prefix [إِيَّا]{.ar} [EiyyA]{.trn}. So then we get the following doee pronouns:

Person | Doee pronoun
:------|:--
Absent person (masc.) "him" | [إِيَّاهُ]{.ar} [EiyyAhu]{.trn} 
Absent person (fem.)  "her" | [إِيَّاهَا]{.ar} [EiyyAhA]{.trn}
Addressed person (masc.)  "you~masc.~" | [إِيَّاكَ]{.ar} [EiyyAka]{.trn} 
Addressed person (fem.)  "you~fem.~"   | [إِيَّاكِ]{.ar} [EiyyAki]{.trn} 
Speaking person (masc. and fem.)  "me" | [إِيَّايَ]{.ar} [EiyyAya]{.trn} 

Note that for the speaking person "me", there is no intervening [ن]{.ar} between the prefix [إِيَّا]{.ar} [EiyyA]{.trn} and the doee pronoun. Note also that only [يَ]{.ar} [-ya]{.trn} is allowed to be attached to the prefix [إِيَّا]{.ar} [EiyyA]{.trn}. This is because [◌ِي]{.ar} [-I]{.trn} is not permitted to be used with words that end in a long vowel ([-A]{.trn}, [-I]{.trn}, or [-U]{.trn}) or a semi-vowel ([-ay]{.trn} or [-aw]{.trn}). And the prefix [إِيَّا]{.ar} [EiyyA]{.trn} ends with the long-vowel [A]{.trn}.

But we may ask why is there a need to separate the doee pronoun from the verb? This can occur for a couple of reasons:

i. If there are multiple doee pronouns, only one of them can be attached to the verb. Example,

   [ضَرَبَتْنِي وَإِيَّاهُ.]{.ar}  
   [DarabatnI wa EiyyAhu.]{.trn}  
   "She hit me and him."

ii. If the doee is placed before the verb for emphasis. Example,

    [إِيَّايَ ضَرَبَتْ.]{.ar}  
    [EiyyAya Darabat.]{.trn}  
    "She hit _me_."

## TODO

1. Multiple verb doers: Copy over from sound plurals and rework.
2. [جواز تأنيث الفعل ووجوبه]{.ar}


<!--chapter:end:srcrmd/past_verbs.Rmd-->

# Adjectival nouns and descriptive noun phrases

## Introduction

So far we have studied common nouns like [رَجُل]{.ar} [rajul]{.trn} "a man" and  [بَيْت]{.ar} [bayt]{.trn} "a house". 
<!--These are called designative nouns because the noun designates a specific object or entity.-->

In this chapter we will study *adjectival nouns*. Adjectival nouns are a class of nouns that don't denote objects. Rather they describe some quality of an object.

## Adjectives in English

In English we usually use adjectives to describe nouns. For example, the word "big" is an adjective. It can be used in a couple of different ways:

1. It can be used to describe a noun in an descriptive noun-phrase. For example:

   "a big car"

2. The adjective "big" can also be used as the information of a sentence, describing the subject noun. For example:

   "The car is big."

But the adjective "big" cannot be used by itself as a noun, for example, as the subject of a sentence. So we can't say:

$\times$ "The big is fast."

We would have to say something like:

"The big car is fast."

instead.

## Terminology: the _describer_ and the _describee_

We take this opportunity to introduce some grammatical terminology. The descriptive noun-phrase "a big car" consists of two parts:

i. The adjective "big". It is describing the car. We will call it the _describer_ in the noun-phrase.
ii. The common noun "a car": It is being described by the describer. We will call it the _describee_.

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-7-1.pdf)<!-- -->

We will reserve this terminology of _describer_ and _describee_ only for the noun and adjective in an descriptive noun-phrase. So we won't use this terminology for the sentence: "The car is big."

Instead, here we will continue to use the existing terminology of _subject_ and _information_. The definite noun "the car" is the subject of this sentence, and the adjective "big" is the information.

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-8-1.pdf)<!-- -->

## Adjectival nouns in English

Consider the English word "antique". It is what we will call a _adjectival noun_. 
<!--It describes some quality of the object it refers to.-->

It can be used just like an adjective to describe a noun as part of a noun-phrase. For example:

"The antique table is expensive."

In the above sentence the adjective "antique" is a describer and is describing the noun "table".

It can also be used as the information of a sentence, just like an adjective. For example:

"The table is antique."

But what makes it different from an normal adjective is that it can also be used by itself as a noun. For example:

"The antique is expensive."

Here "the antique" could refer to any entity that can be described by the quality of being old and valuable. The adjectival noun does not require any other noun in this sentence and can stand on its own as the subject of the sentence.

Adjectival nouns are rare in English. Instead, adjectives are usually used when we want to describe a noun.

## Adjectival nouns in Arabic and genderizability

<!--In Arabic, however, the situation is reversed. -->
Arabic does not have adjectives. It only has adjectival nouns.

The word [صَغِير]{.ar} [SagIr]{.trn} is an example of an indefinite adjectival noun in Arabic. It describes the quality of being "small" or "little". It can be used to denote any person, animal, or things that can be described as being small. Technically we could translate it as "a little one~m~" or "a small one~m~".

Being a noun [صَغِير]{.ar} [SagIr]{.trn}, like all other nouns in Arabic, will have a grammatical gender. Since it does not end with a feminine marker like [ة]{.ar}, we can state that 
[صَغِير]{.ar} [SagIr]{.trn} is a masculine noun.

Adjectival nouns, typically, are genderizable. This means that we can feminize 
[صَغِير]{.ar} [SagIr]{.trn} (masc.) to get the feminine noun.
We will feminize 
[صَغِير]{.ar} [SagIr]{.trn} (masc.) with the feminine marker [ة]{.ar} to get the feminine adjectival noun
[صَغِيرَة]{.ar} [SagIrah]{.trn} (fem.) "a little one~f~".

Generally, the dictionary will typically only supply the masculine adjectival noun.
And we are expected to know how to feminize it to get the feminine adjectival noun.

As opposed to adjectival nouns, common nouns are not genderizable. So, for example, if we know that the noun
[غُلَام]{.ar} [gulAm]{.trn} "a boy" exists, we cannot assume that we can feminize it, by using the feminine marker [ة]{.ar}, for example, getting: $\times$ [غُلَامَة]{.ar} [gulAmah]{.trn}. This would be a misguided attempt to obtain the meaning for "a girl" in Standard Arabic. Instead, we have to look up the Arabic word for "a girl" in the dictionary separately, and we find that it is [جَارِيَة]{.ar} [jAriyah]{.trn}.

Many times times, a masculine/feminine common noun pair will exist, that differ only by the feminine marker [ة]{.ar}. For example: 

+ [ٱِبْن]{.ar} [Eibn]{.trn} "a son" and [ٱِبْنَة]{.ar} [Eibnah]{.trn} "a daughter".
+ [مُعَلِّم]{.ar} [mueallim]{.trn} "a teacher~m~" and [مُعَلِّمَة]{.ar} [mueallimah]{.trn} "a teacher~f~"

This does not indicate that the common noun is genderizable. Rather, when the common noun masc./fem. pair has a meaning that is derived from a verb or an adjective (like
[مُعَلِّم]{.ar}/[مُعَلِّمَة]{.ar}),
then the masculine/feminine pair are co-derived as separate non-genderizable words. We will discuss this in more detail in later chapters, if [#allAh]{.trn2} wills.

And when the common noun masc./fem. pair has a primitive (non-verbal and non-adjectival) meaning, (like
[ٱِبْن]{.ar}/[ٱِبْنَة]{.ar}),
then this is only a coincidence. We alluded to this in section\ \@ref(related-nouns-for-male-and-female-animate-beings).

### Examples of Arabic adjectival nouns

Here are some examples of Arabic adjectival nouns that we will use in this chapter.

Arabic adjectival noun    | Meaning
:------------------|:------------
[كَبِير]{.ar}    [kabIr]{.trn}  | a big one
[صَغِير]{.ar}    [SagIr]{.trn}  | a small one
[طَيِّب]{.ar}     [Tayyib]{.trn} | a good one
[قَدِيم]{.ar}    [qadIm]{.trn}  | an old one
[جَدِيد]{.ar}    [jadId]{.trn}  | a new one
[طَوِيل]{.ar}    [TawIl]{.trn}  | a long/tall one
[وَاسِع]{.ar}    [wAsie]{.trn}  | a wide one
[عَرَبِيّ]{.ar}    [earabiyy]{.trn} | an Arab
[مَشْهُور]{.ar}   [machUr]{.trn} | a famous one

## The describer and the describee in descriptive noun-phrases

Let's learn how descriptive noun-phrases are formed in Arabic.

We learned in section\ \@ref(terminology-the-describer-and-the-describee)
above that descriptive noun-phrases consist of a describer and a describee. 

In English descriptive noun-phrases, like "the small house", the adjective describer ("small") comes before the describee ("house"). Also, only one definite article ("the") is used before the entire noun-phrase.

Here is the equivalent Arabic descriptive noun-phrase:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-9-1.pdf)<!-- -->

<!--
[ٱَلْبَيْتُ ٱلصَّغِيرُ]{.ar}  
[Ealbaytu -SSagIru]{.trn}  
"the small-one house" = "the small house"
-->

Note the following:

+ The adjectival noun describer [ٱَلصَّغِير]{.ar} [EaSSagIr]{.trn} "the small one~m~" comes after the describee [ٱَلْبَيْت]{.ar} [Ealbayt]{.trn} "the house".
+ Both the adjectival noun describer [ٱَلصَّغِير]{.ar} [EaSSagIr]{.trn} "the small one~m~" and the describee [ٱَلْبَيْت]{.ar} [Ealbayt]{.trn} "the house" get the definite article [ٱَلْ]{.ar} "the".
+ The adjectival noun describer [ٱَلصَّغِير]{.ar} [EaSSagIr]{.trn} "the small one~m~" is genderized to match the describee [ٱَلْبَيْت]{.ar} [Ealbayt]{.trn} "the house" in gender.
+ The adjectival noun describer [ٱَلصَّغِير]{.ar} [EaSSagIr]{.trn} "the small one~m~" matches the describee [ٱَلْبَيْت]{.ar} [Ealbayt]{.trn} "the house" in state. In this example, they were both in the u-state but we will see examples in the other states as well.
+ The word-for-word equivalence of the above descriptive noun-phrase is "the small-one house" but we will usually give the more natural translation: "the small house"

Let's try another example: let's try to translate the sentence: "The little girl took a new book from the good mother."

Here is the sentence in Arabic:

[أَخَذَتِ ٱلْجَارِيَةُ ٱلصَّغِيرَةُ كِتَابًا جَدِيدًا مِنْ ٱلْأُمِّ ٱلطَّيِّبَةِ.]{.ar}  
[Eaxapati -ljAriyatu -SSagIratu kitaban jadIdan mina -lEummi -TTayyibah.]{.trn}  
"The little girl took a new book from the good mother."

This sentence has three descriptive noun-phrases. We will analyze each one individually:

i. [ٱَلْجَارِيَةُ ٱلصَّغِيرَةُ]{.ar}  
   [EaljAriyatu -SSagIratu]{.trn}  
   "the little girl"

   In this phrase the definite feminine noun [ٱلْجَارِيَةُ]{.ar} [EaljAriyatu]{.trn} is the doer of the verb [أَخَذَ]{.ar} [Eaxapa]{.trn} "took". Therefore it is in the u-state. It is also the describee in the descriptive noun-phrase. Its describer [ٱَلصَّغِيرَةُ]{.ar} [EaSSagIratu]{.trn} follows the describee and is made to match the describee in state (u-state), gender (feminine), and definiteness (definite).

ii. [كِتَابًا جَدِيدًا]{.ar}  
    [kitAban jadIdan]{.trn}  
    "a new book"

    In this phrase the indefinite masculine noun [كِتَابًا]{.ar} [kitAban]{.trn} is the doee of the verb [أَخَذَ]{.ar} [Eaxapa]{.trn} "took". Therefore it is in the a-state. It is also the describee in the descriptive noun-phrase. Its describer [جَدِيدًا]{.ar} [jadIdan]{.trn} follows the describee and is made to match the describee in state (a-state), gender (masculine), and definiteness (indefinite).

iii. [ٱَلْأُمِّ ٱلطَّيِّبَةِ]{.ar}  
     [EalEummi -TTayyibati]{.trn}  
     "the good mother"

      In this phrase the definite feminine noun [ٱلْأُمِّ]{.ar} [EalEummi]{.trn} is following the preposition [مِنْ]{.ar} [min]{.trn} "from". Therefore it is in the i-state. It is also the describee in the descriptive noun-phrase. Its describer [ٱَلطَيِّبَةِ]{.ar} [EaTTayyibati]{.trn} follows the describee and is made to match the describee in state (i-state), gender (feminine), and definiteness (definite). 

      Note carefully that the describer matches the describee in gender, not necessarily in having the same [ة]{.ar} ending. The feminine adjectival noun describer [ٱَلطَيِّبَة]{.ar} [EaTTayyibah]{.trn} is still formed using the feminine marker [ة]{.ar}, despite the feminine describee [ٱَلْأُمّ]{.ar} not having the [ة]{.ar} feminine marker.

<!--
[حَمَلَتِ ٱلْأُمُّ ٱلطَّيِّبُ جَارِيَةً صَغِيرَةً بِيَدٍ قَوِيَّةٍ.]{.ar}  

"The tall strong mother took an old and heavy book from the little girl."
-->

Sometimes, a common noun of one gender is used to refer to persons of either gender. For example:

+ the noun [شَخْص]{.ar} [caxS]{.trn} is itself a masculine noun but it may be used to refer to both male and female persons. 

If such a noun is a describee, then we will prefer to match the describer to the grammatical gender of the noun, not the physical gender of the person it is referring to. For example:

[ٱَلْجَارِيَةُ شَخْصٌ طَيِّبٌ.]{.ar}  
[EaljAriyatu caxSun Tayyib.]{.trn}  
"The girl is a good person."

See how we preferred to use the masculine adjectival noun [طَيِّب]{.ar} [Tayyib]{.trn} instead of using the feminine [طَيِّبَة]{.ar} [Tayyibah]{.trn}.

## Adjectival nouns as the information of a sentence

### Indefinite adjectival noun

Let's see how to use Arabic adjectival nouns as the information of a sentence.

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-10-1.pdf)<!-- -->

<!--
[ٱَلْبَيْتُ صَغِيرٌ.]{.ar}  
[Ealbaytu SagIr.]{.trn}  
"The house is a small one." = "The house is small."
-->

In the above sentence, the indefinite adjectival noun 
[صَغِير]{.ar} [SagIr]{.trn} "a small one"
is used as the information of a sentence. Its indefiniteness and u-state is indicated by the [un]{.trn}-mark [◌ٌ]{.ar} on its end.

When an adjectival noun is the information of a sentence, then it shall be genderized to match the gender of the subject noun. The subject noun in this case ([ٱَلْبَيْت]{.ar}) is masculine. Therefore, the masculine adjectival noun ([صَغِير]{.ar}) is chosen.

Technically, the translation of this sentence is "The house is a small one."
However, because Arabic has only adjectival nouns and not adjectives, it is how we can express the English sentence "The house is small." Therefore we can also translate it into English as such.

Now let's try a sentence with a feminine subject:

[ٱَلْجَارِيَةُ صَغِيرَة.]{.ar}  
[EaljAriyatu SagIrah]{.trn}  
"The girl is a little one~f~." = "The girl is little."

In the above example the subject ([ٱَلْجَارِيَة]{.ar} "the girl") was feminine. Therefore, we feminized the masculine adjectival noun [صَغِير]{.ar} [SagIr]{.trn} with the feminine marker [ة]{.ar} to get the feminine adjectival noun
[صَغِيرَة]{.ar} [SagIrah]{.trn} "a little one~f~"
and used the feminine adjectival noun in the sentence.

### Definite adjectival noun

Let's see if a definite adjectival noun can be used in the information. For example, we would like to say "The old tree is the big one."

The subject of the sentence is [ٱَلشَّجَرَةُ ٱلْقَدِيمَةُ]{.ar} [Eaccajaratu -lqadImuiatu]{.trn} "the old tree".
And the information is [ٱلْكَبِيرَةُ]{.ar} [EalkabIratu]{.trn} "the big one". When we put the two together we get:

[ٱَلشَّجَرَةُ ٱلْقَدِيمَةُ ٱلْكَبِيرَةُ]{.ar}  
[Eaccajaratu -lqadImatu -lkabIratu]{.trn}

The problem is that the above could also be interpreted as one phrase "the big old tree", and not as the complete sentence "The old tree is the big one." This is the same problem that we highlighted in section\ \@ref(chap-smp-sent-sec-def-info).

The solution, too, is the same. We insert a detached pronoun, that matches the gender of the subject, between the subject and the information. So in order to get our intended meaning, we will say:

[ٱَلشَّجَرَةُ ٱلْقَدِيمَةُ هِيَ ٱلْكَبِيرَةُ.]{.ar}  
[Eaccajaratu -lqadImatu hiya -lkabIratu.]{.trn}  
"The old tree is the big one."

## Adjectival nouns used without a described noun

We have mentioned that adjectival nouns are just like other nouns that we have learned so far, in that they have gender, state, and definiteness. Can we then use
an adjectival noun by itself and not when it is describing another noun?

The answer is yes, we can. So for example, you can say:

[شَرِبَ ٱلصَّغِيرُ حَلِيبًا.]{.ar}  
[cariba -SSagIru HalIbA.]{.trn}  
"The little one drank some milk."

The above is a correct sentence. But, by itself, it is not very clear. What do we mean by "the little one"? Is it a little boy, or a little cat, or something else? So, context would be needed to know what exactly is being denoted by the adjectival noun when it is used by itself independently.

Here is the same sentence again, but this time with some clarifying context.

[حَمَلَتِ ٱلْأُمُّ ٱلصَّغِيرَ. وَشَرِبَ ٱلصَّغِيرُ حَلِيبًا.]{.ar}  
[Hamalati -lEummu -SSagIra. wacariba -SSagIru HalIbA.]{.trn}  
"The mother carried the little one. And the little one drank some milk."

So now we can tell that what is meant by [ٱلصَّغِير]{.ar} [EaSSagIr]{.trn} "the little one" here is "the baby".

## Adjectival nouns re-used as common nouns

Sometimes, an adjectival noun, through much usage, acquires the meaning of a common noun. It then gets listed with this meaning in the dictionary. We actually just saw an example above. The adjectival noun 
[صَغِير]{.ar} [SagIr]{.trn} "a little one" is commonly used to mean "a baby". Of course, context would be needed to know whether, in a particular sentence, it has its common noun meaning: "a baby", or its general adjectival noun meaning: "a little one".

The opposite of 
[صَغِير]{.ar} [SagIr]{.trn} "a little one" 
is [كَبِير]{.ar} [kabIr]{.trn} "a big one". It too has acquired the common noun meaning of "an elder person". Here is an example of its usage:

[قَدِمَ ٱلْكَبِيرُ وَوَعَظَ ٱلْغُلَامَ.]{.ar}  
[qadima -lkabIru wawaeaPa -lgulAma.]{.trn}  
"The elder arrived and admonished the boy."

When an adjectival noun gets re-used as a common noun, it loses its genderizability.
For example, the feminine adjectival noun [حَسَنَة]{.ar} [Hasanah]{.trn} (fem.) "a good one" is re-used as a common noun meaning "a good deed". So we can use it in a sentence:

[ٱلصِّيَامُ حَسَنَةٌ.]{.ar}  
[EaSSiyAmu Hasanah.]{.trn}  
"Fasting is a good deed."

The subject in this sentence is the masculine noun [ٱَلصِّيَام]{.ar} [EaSSiyAm]{.trn} "fasting". 
And the information is the feminine noun [حَسَنَة]{.ar} [Hasanah]{.trn} "a good deed".
Note that the information does not match the subject in gender. This is because it lost its genderizability since it is no longer acting as an adjectival noun "a good one~f~", but rather as the common noun "a good deed".

What if we have the sentence:

[ٱَلصَّدَقَةُ حَسَنَةٌ.]{.ar}  
[EaSSadaqatu Hasanah.]{.trn}

The feminine gender of the subject 
[ٱَلصَّدَقَة.]{.ar} 
[EaSSadaqah]{.trn} "charity" now matches the gender of the information
[حَسَنَة]{.ar} [Hasanah]{.trn}.
So now, technically, the information could be the adjectival noun, meaning "a good one~f~". So the sentence could mean:

"Charity is good."

Or the information could be the common noun, meaning "a good deed". Then the sentence would mean:

"Charity is a good deed."

Context would be needed to tell us which meaning is intended.

## Common-nouns used as describers in a noun-phrase

Usually, adjectival nouns are used as the describer in an descriptive noun-phrase. However, we also often find a common noun used as a describer. For example,

[هُوَ رَجُلٌ مُعَلِّمٌ.]{.ar}  
[huwa rajulun mueallim.]{.trn}  
"He is a teacher~m~ man."  
= "He is a man who is a teacher~m~."

## Multiple adjectival nouns describing the same noun

In English we can have a noun described by multiple adjectives separated by commas and the word "and". For example, "The building is big, tall, and wide." In Arabic we will separate the multiple adjectival nouns with [وَ]{.ar} [wa-]{.trn} "and":

[ٱَلْبِنَاءُ كَبِيرٌ وَطَوِيلٌ وَوَاسِعٌ.]{.ar}  
[EalbinAEu kabIrun waTawIlun wawAsiEun]{.trn}  
"The building is big and tall and wide."

In an English descriptive noun-phrase, multiple describers may describe the same describee, without being separated by the word "and". For example, "The man is a famous Arab writer." In Arabic, we can do the same, except the describees will be in the reverse order:

[ٱَلرَّجُلُ كَاتِبٌ عَرَبِيٌّ مَشْهُورٌ.]{.ar}  
[Earrujulu kAtibun earabiyyun machUr.]{.trn}  
"The man is a famous Arab writer." 


## A prepositional phrase separating the describer from the describee

Consider the phrase:

[كِتَابٌ مِنَ ٱلْمَكْتَبَةِ]{.ar}  
[kitAbun mina -lmaktabati]{.trn}  
"a book from the library"

<!--The prepositional phrase [مِنَ ٱلْمَكْتَبَةِ]{.ar} [mina -lmaktabati]{.trn} "from the library" is not a adjectival noun. Yet it still acts as a describer for the noun [كِتَابٌ]{.ar} [kitAbun]{.trn} "a book", in that it is describing a quality of the book.
-->
If we want to add a adjectival noun as to describe "the book", we may add it either before or after the prepositional phrase describer. Here are both examples as complete sentences:

[قَرَأَ كِتَابًا صَغِيرًا مِنَ ٱلْمَكْتَبَةِ.]{.ar}  
[qaraEa kitAban SagIran mina -lmaktabati.]{.trn}  
AND  
[قَرَأَ كِتَابًا مِنَ ٱلْمَكْتَبَةِ صَغِيرًا.]{.ar}  
[qaraEa kitAban mina -lmaktabati SagIran.]{.trn}  
"a small book from the library"

The first option is usually chosen as a matter of preference but the second option is legitimate too.

<!--
## A prepositional phrase as the describer

Consider the phrase:

[كِتَابٌ مِنَ ٱلْمَكْتَبَةِ]{.ar}  
[kitAbun mina -lmaktabati]{.trn}  
"a book from the library"

The prepositional phrase [مِنَ ٱلْمَكْتَبَةِ]{.ar} [mina -lmaktabati]{.trn} "from the library" is not a adjectival noun. Yet it still acts as a describer for the noun [كِتَابٌ]{.ar} [kitAbun]{.trn} "a book", in that it is describing a quality of the book.

If we want to add a adjectival noun as an additional describer, we may add it either before or after the prepositional phrase describer. Here are both examples as complete sentences:

[قَرَأَ كِتَابًا صَغِيرًا مِنَ ٱلْمَكْتَبَةِ.]{.ar}  
[qaraEa kitAban SagIran mina -lmaktabati.]{.trn}  
AND  
[قَرَأَ كِتَابًا مِنَ ٱلْمَكْتَبَةِ صَغِيرًا.]{.ar}  
[qaraEa kitAban mina -lmaktabati SagIran.]{.trn}  
"a small book from the library"

The first option is usually chosen as a matter of preference but the second option is legitimate too.
-->


<!--chapter:end:srcrmd/describing_nouns.Rmd-->

# Semi-flexible nouns

## Introduction

Nouns are of two main categories of nouns, with regard to their endings in the different noun states:

1. Rigid nouns.
2. Flexible nouns. These are further sub-divided into:
   i. Fully-flexible nouns.
   ii. Semi-flexible nouns.

So far we have been mostly studying fully-flexible nouns. In this chapter we will learn about semi-flexible nouns.

Here is an example of the kind of nouns we have learned so far:

State  | Indefinite | Definite
:------|:-----------|:---------
u-state| [رَجُلٌ]{.ar} | [ٱَلرَّجُلُ]{.ar}
a-state| [رَجُلًا]{.ar}| [ٱَلرَّجُلَ]{.ar}
i-state| [رَجُلٍ]{.ar} | [ٱَلرَّجُلِ]{.ar}

As you can see, the noun has [n]{.trn}-marks when it is indefinite, and also, the vowel mark on the last letter changes for each state that the noun is in. These kinds of nouns are called _fully-flexible_ nouns. They are by far the most common type of noun.

There are some nouns, however, that are _semi-flexible_. 
Here is an example of a semi-flexible noun, [صَحْرَاء]{.ar} [SaHrAE]{.trn} "a desert":

State  | Indefinite | Definite
:------|:-----------|:---------
u-state| [صَحْرَاءُ]{.ar} | [ٱَلصَّحْرَاءُ]{.ar}
a-state| [صَحْرَاءَ]{.ar} | [ٱَلصَّحْرَاءَ]{.ar}
i-state| [صَحْرَاءَ]{.ar} | [ٱَلصَّحْرَاءِ]{.ar}

As you can see, when [صَحْرَاء]{.ar} [SaHrAE]{.trn} is indefinite, it does not have an [n]{.trn}-mark. Also, when it is indefinite and in the i-state, the vowel mark on its final letter is not [◌ِ]{.ar}, as you might expect but [◌َ]{.ar} . And so the noun looks identical in the a-state and i-state when it is indefinite.

When it is definite, however, it looks just like fully-flexible nouns.

So there are two differences between fully-flexible and semi-flexible nouns:

1. When indefinite, a semi-flexible noun does not have an [n]{.trn}-mark.
2. When indefinite and in the i-state, a semi-flexible noun's final letter does not have an [i]{.trn}-mark. Instead it shall have an [a]{.trn}-mark, just like when it is in the a-state.

The other category of nouns are _rigid_ nouns. Rigid nouns don't change their endings due to their state. They are much fewer in number compared to flexible nouns. Pronouns are an example of rigid nouns.

## Feminine markers

Before we discuss semi-flexible nouns in more detail, we will discuss feminine markers. We already know of one feminine marker: the looped-[tAE]{.trn2} [ة]{.ar}. When a singular noun ends with [ة]{.ar}, then that is an indication, with very few exceptions, that it is a feminine noun. Examples are:

Root | Feminine noun | Masculine noun from same root (if any)
:-|:-------|:-------
[جري]{.arroot} | [جَارِيَة]{.ar}  "a girl~f~"             | --
[علم]{.arroot} | [عَالِمَة]{.ar}  "a scholar~f~"          | [عَالِم]{.ar}  "a scholar~m~"
[كلب]{.arroot} | [كَلْبَة]{.ar}  "a dog~f~"               | [كَلْب]{.ar}  "a dog~m~"
[شجر]{.arroot} | [شَجَرَة]{.ar}  "a tree"                 | --
[صغر]{.arroot} | [صَغِيرَة]{.ar}  _adj._ "small~f~"   | [صَغِير]{.ar}  _adj._ "small~m~"

As you can see, the feminine marker [ة]{.ar} is never part of the noun's root. It is thus considered _extrinsic_ to the root. Also, sometimes, but not always, the feminine noun is formed by adding the feminine marker [ة]{.ar} to the end of a masculine noun.

It is also important to note that [ة]{.ar} is only a feminine marker for singular nouns. When we learn plurals, if [#allAh]{.trn2} wills, we will see that [ة]{.ar} is used frequently with masculine plurals.

Now we will learn of two more feminine markers: [اء]{.ar} and [ىٰ]{.ar}. 

Here are some examples of nouns that end with these two feminine markers:

Root | Feminine noun | Masculine noun (if any)
:-|:-------|:-------
[صحر]{.arroot} | [صَحْرَاء]{.ar}  "a desert"            | --
[حمر]{.arroot} | [حَمْرَاء]{.ar}  _adj._ "red~f~"       | [أَحْمَر]{.ar}  _adj._ "red~m~"
[ذكر]{.arroot} | [ذِكْرَىٰ]{.ar}  "a remembrance"        | --
[غضب]{.arroot} | [غَضْبَىٰ]{.ar}  _adj._ "very angry~f~" | [غَضْبَان]{.ar}  _adj._ "very angry~m~"

When extrinsic to the word's root, [اء]{.ar} and [ىٰ]{.ar} are feminine markers, just like [ة]{.ar}. However, one important difference from [ة]{.ar} is that sometimes
[اء]{.ar} and [ىٰ]{.ar} may not be extrinsic to the word's root. In this case, they will not be feminine markers, and the noun will regularly be a masculine noun. Examples:

Root | Noun | Pattern using paradigm [فعل]{.arroot}
:--|:----------|:----
[هدي]{.arroot} | [ٱلْهُدَىٰ]{.ar}  (masc.) "the guidance" | [ٱَلْفُعَل]{.ar}
[خبء]{.arroot} | [خِبَاء]{.ar}  (masc.) "a tent" | [فِعَال]{.ar}

These cases will become more clear, if [#allAh]{.trn2} wills, when we study weak roots (roots that contain a weak letter like [ء، و، ي]{.ar}).

Otherwise, 
when extrinsic to the word's root, [اء]{.ar}, and [ىٰ]{.ar} are consistently feminine markers, just like [ة]{.ar}. 

Also, just like [ة]{.ar}, [اء]{.ar} and [ىٰ]{.ar} are only feminine markers for singular nouns. We will see, if [#allAh]{.trn2} wills, that they are used frequently with masculine plurals.

By the way, another difference from [ة]{.ar} is that when 
[اء]{.ar} and [ىٰ]{.ar} are feminine markers, and a masculine counterpart exists, then the feminine noun is not formed by simply adding the feminine marker to the end of the masculine noun. The masculine and feminine nouns are different internally as well. For example, the feminine noun
[حَمْرَاء]{.ar}  _adj._ "red~f~"
is not formed simply by adding the feminine marker [اء]{.ar} to the end of the masculine noun
[أَحْمَر]{.ar}  _adj._ "red~m~".

We will discuss this in more detail below.

## Categories of semi-flexible nouns

We now return to our discussion of semi-flexible nouns. Semi-flexible nouns, in terms of their formation, fall under different categories. We will discuss them below.

When discussing semi-flexible nouns in isolation we will add the numeral\ 2 as a superscript to their ending, thus: 
^2^[صَحْرَاء]{.ar} [SaHrAE]{.trn}^2^. This is to indicate their semi-flexibility.
<!--
[صَحْرَاء]{.ar}$^2$ [SaHrAE]{.trn}$^2$. This is to indicate their semi-flexibility.

$^2$[صَحْرَاء]{.ar} [SaHrAE]{.trn}$^2$. This is to indicate their semi-flexibility.
-->

### Nouns that end with an extrinsic [اء]{.ar}

If a noun ends with an [اء]{.ar}, which is extrinsic to the word's root, then it shall be a semi-flexible noun.

We have already seen an example of such a noun above: ^2^[صَحْرَاء]{.ar} [SaHrAE]{.trn}^2^ "a desert". The root of this noun is [صحر]{.arroot}. You can see that the ending [اء]{.ar} is not part of the root. Therefore it is a semi-flexible noun.

Furthermore, we have also learned that this [اء]{.ar}, which is extrinsic to the word's root, is a feminine marker for singular nouns, just like [ة]{.ar}, except that [ة]{.ar} does not generally make a noun semi-flexible.

Here is an example sentence with this noun:

[ذَهَبَ ٱلرَّجُلُ إِلَىٰ صَحْرَاءَ وَاسِعَةٍ.]{.ar}  
[pahaba -rrajulu EilA SaHrAEa wAsieah.]{.trn}  
"The man went to a wide desert."

Note that the vowel mark on the final letter of [صَحْرَاءَ]{.ar} [SaHrAEa]{.trn} is [◌َ]{.ar}, not [◌ٍ]{.ar}, even though it is indefinite and in the i-state (because it is preceded by the preposition [إِلَىٰ]{.ar} [EilA]{.trn} "to"). This is because it is a semi-flexible noun.

^2^[صَحْرَاء]{.ar} [SaHrAE]{.trn}^2^ in this sentence
is also a describee, whose describer is [وَاسِعَةٍ]{.ar} [wAsieatin]{.trn} "wide". The final vowel mark [◌َ]{.ar} on the describee [صَحْرَاءَ]{.ar} [SaHrAEa]{.trn} has no effect on the final vowel mark on the describer [وَاسِعَةٍ]{.ar} [wAsieatin]{.trn} "wide". All that matters in this regard is the state of the describee. 

Note, also, that the describer [وَاسِعَة]{.ar} is feminine to match the gender of the describee 
^2^[صَحْرَاء]{.ar} [SaHrAE]{.trn}^2^. 

Note, as well, that the describer [وَاسِعَةٍ]{.ar} has an [n]{.trn}-mark as it is indefinite and fully-flexible. The inability of its describee 
^2^[صَحْرَاء]{.ar} [SaHrAE]{.trn}^2^ 
to have an [n]{.trn}-mark (because of its semi-flexibility) does not affect the describer.

Also, beware, as we've already mentioned, that there are some words where the [اء]{.ar} ending may be part of the word's root, for example 
 [خِبَاء]{.ar} [xibAE]{.trn} "a tent" from the root [خبء]{.arroot} on the pattern [خِبَاء]{.ar}. Such words will be fully flexible.
<!--
[ibtidAEun]{.trn} "a beginning" whose root is [بدء]{.arroot} and which is on the pattern [ٱِفْتِعَالٌ]{.ar} [iftieAlun]{.trn}. Because here the [ء]{.ar} in [ٱبْتِدَاءٌ]{.ar} is part of the word's root, therefore it shall not be a semi-flexible noun. That is why you can see that it has an [n]{.trn} mark when it is indefinite. 
-->
Also, for the same reason, [اء]{.ar} in this word is not a feminine marker, and the word is masculine.

### Nouns that end with an extrinsic [ىٰ]{.ar}

If a noun ends with an [ىٰ]{.ar} which is extrinsic to the word's root, then it shall be a semi-flexible noun.

We've already seen an example of such a word: ^2^[ذِكْرَىٰ]{.ar} [pikrA]{.trn}^2^ "a remembrance". The root of this word is [ذكر]{.arroot} and it is on the pattern [فِعْلَىٰ]{.ar}.

We've also learned that, similar to [اء]{.ar}, this [ىٰ]{.ar}, which is extrinsic to the word's root, is a feminine marker for singular nouns.

Since ^2^[ذِكْرَىٰ]{.ar} [pikrA]{.trn}^2^ already ends with the vowel-mark [◌ٰ]{.ar}, the last letter won't have any additional vowel markers and therefore the word will appear the same in all states:

  State  | Indefinite | Definite
  :------|:-----------|:---------
  u-state| [ذِكْرَىٰ]{.ar} | [ٱَلذِّكْرَىٰ]{.ar}
  a-state| [ذِكْرَىٰ]{.ar} | [ٱَلذِّكْرَىٰ]{.ar}
  i-state| [ذِكْرَىٰ]{.ar} | [ٱَلذِّكْرَىٰ]{.ar}

Therefore, the state of such nouns cannot be determined by the vowel mark on their final letter, and has to be deduced otherwise by their function in the sentence.
Nevertheless, these nouns are still included in the category of semi-flexible nouns, and not rigid nouns. This is because rigid nouns are closed set consisting only of pronouns and other similar words.

Here is an example of this word in a sentence:

[ٱَلْكِتَابُ ذِكْرَىٰ جَمِيلةٌ.]{.ar}  
[EalkitAbu pikrA jamIlah.]{.trn}  
"The book is a beautiful remembrance."

Note, again how the describer [جَمِيلَة]{.ar} [jamIlah]{.trn} is feminine and in the u-state, in order to match the gender and state of the describee ^2^[ذِكْرَىٰ]{.ar} [pikrA]{.trn}^2^.

Beware also that, just like in the case of [اء]{.ar}, there are some words where [ىٰ]{.ar} may be part of the word's root, e.g. [ٱَلْهُدَىٰ]{.ar} [EalhudA]{.trn} "the guidance" whose root is [هدي]{.arroot}. Because here the [ىٰ]{.ar} in [ٱلْهُدَىٰ]{.ar} is part of the word's root, therefore it shall not be a semi-flexible noun. So, when it is indefinite, it will have an [n]{.trn}-mark when it is indefinite: [هُدًى]{.ar} [hudan]{.trn} "a guidance". Also, for the same reason, [ىٰ]{.ar} in this word is not a feminine marker, and the word is masculine.

### Nouns on the pattern [أَفْعَل]{.ar}

If a noun is on the pattern [أَفْعَل]{.ar} [Eafeal]{.trn} then it shall be a semi-flexible noun. By the way, there is no feminine marker on such words, so they will be masculine by default.

Most colors and many physical characteristics fall into this pattern. Colors and physical characteristics are adjectival nouns. The masculine noun for such adjectival-nouns is on the pattern [أَفْعَل]{.ar} [Eafeal]{.trn}. And the feminine adjectival noun is on the pattern [فَعْلَاء]{.ar} [faelAE]{.trn} (which is itself a semi-flexible noun pattern because of the extrinsic [اء]{.ar} ending). Here are some examples of such adjectival nouns:

Root | Masc. Noun | Fem. noun | Meaning
:----|:-----------|:-------------|:------------
[حمر]{.arroot} | ^2^[أَحْمَر]{.ar}  | ^2^[حَمْرَاء]{.ar}  | red
[سود]{.arroot} | ^2^[أَسْوَد]{.ar}  | ^2^[سَوْدَاء]{.ar}  | black
[بيض]{.arroot} | ^2^[أَبْيَض]{.ar}  | ^2^[بَيْضَاء]{.ar}  | white
[عرج]{.arroot} | ^2^[أَعْرَج]{.ar}  | ^2^[عَرْجَاء]{.ar}  | lame
[حور]{.arroot} | ^2^[أَحْوَر]{.ar}  | ^2^[حَوْرَاء]{.ar}  | beautiful eyed
[بكم]{.arroot} | ^2^[أَبْكَم]{.ar}  | ^2^[بَكْمَاء]{.ar}  | mute

Example:

[لَبِسَ ٱلرَّجُلُ قَمِيصًا أَبْيَضُ.]{.ar}  
[labisa -rrajulu qamISan EabyaD.]{.trn}  
"The man wore a white shirt."

### Adjectival nouns that end with an extrinsic [ان]{.ar} {#adjectival-noun-an-diptote}

The letters [ان]{.ar} may be an extrinsic ending for nouns. This ending is not a feminine marker so the noun would typically be masculine. This ending may cause the noun to be semi-flexible.

This category is more complicated than the previous ones. The following conditions must be satisfied for a word that ends with [ان]{.ar} to be a semi-flexible noun:

1. The noun must be a adjectival-noun on the pattern [فَعْلَان]{.ar}. So the common noun [ثُعْبَان]{.ar} [vuebAn]{.trn} "a serpent" of the root [ثعي]{.arroot} is a common noun and therefore, not a semi-flexible noun.
2. The [ان]{.ar} must be extrinsic to the word's root. So [جَبَان]{.ar} [jabAnun]{.trn} "cowardly", an adjectival noun of the root [جبن]{.arroot}, is not a semi-flexible noun.
3. The feminine of the adjectival noun shall not be formed by adding [ة]{.ar} to the masculine noun. So [نَدْمَان]{.ar} [nadmAn]{.trn} "regretful", an adjectival-noun from the root [ندم]{.arroot}, is not a semi-flexible noun, because its feminine is [نَدْمَانَة]{.ar} [nadmAnah]{.trn}.

It is rare that this last condition fails. Most adjectival nouns that end with an extrinsic [ان]{.ar} are of the pattern [فَعْلَان]{.ar} [faelAn]{.trn} and their feminine is of the pattern [فَعْلَىٰ]{.ar} [faelA]{.trn} (which is itself a semi-flexible noun pattern). These adjectival-nouns typically have an emphatic meaning. The following are examples of semi-flexible adjectival-nouns that fall into this category:

Root | Masc. Noun | Fem. noun | Meaning
:----|:-----------|:-------------|:------------
[غضب]{.arroot} | ^2^[غَضْبَان]{.ar} | ^2^[غَضْبَىٰ]{.ar}   | very angry
[عطش]{.arroot} | ^2^[عَطْشَان]{.ar} | ^2^[عَطْشَىٰ]{.ar}   | very thirsty
[جوع]{.arroot} | ^2^[جَوْعَان]{.ar} | ^2^[جَوْعَىٰ]{.ar}   | very hungry

### Nouns of the patterns [فَفَافِف]{.ar} and [فَفَافِيف]{.ar} {#fafafif-diptote}

Nouns that are of the patterns [فَفَافِف]{.ar} and [فَفَافِيف]{.ar} are also semi-flexible nouns. Here each letter [ف]{.ar} could be any letter of the alphabet. 

Here are some examples of these nouns:

+ ^2^[مَسَاجِد]{.ar} [masAjid]{.trn}^2^ "mosques"
+ ^2^[مَفَاتِيح]{.ar} [mafAtIH]{.trn}^2^ "keys"

These patterns are only used for plurals and we will study them in more detail in chapter\ \@ref(broken-plurals)
, if [#allAh]{.trn2} wills.


<!--chapter:end:srcrmd/diptotes.Rmd-->

# Duals

## Introduction

For any number greater than one, English uses the plural. For example, the plural of "house" is "houses". So in English we will say:

"two houses"

Arabic, on the other hand, uses the plural only for nouns in number three and higher. For nouns that are two in number Arabic uses the _dual_.

Since English does not have a dual, we will sometimes indicate it using the the subscript 2, thus: "houses~2~", to mean "two houses".

## Forming the dual

The dual is formed by appending the dual suffix [◌َانِ]{.ar} [-Ani]{.trn} when the noun is in the u-state and [◌َيْنِ]{.ar} [-ayni]{.trn} when the noun is in the a-state or i-state. Definite nouns, which have [ٱَلْ]{.ar} in their beginning are dualized the same way. 

For example, when we dualize [بَيْت]{.ar} [bayt]{.trn} "a house" in order to say "houses~2~", we get:

| States | Indefinite | Definite
|:----|:-------|:-------
|u-state         | [بَيْتَانِ]{.ar} [baytAni]{.trn}  | [ٱَلْبَيْتَانِ]{.ar} [EalbaytAni]{.trn}
|a- and i-states | [بَيْتَيْنِ]{.ar} [baytayni]{.trn} | [ٱَلْبَيْتَيْنِ]{.ar} [Ealbaytayni]{.trn}   

Note that indefinite duals don't have [n]{.trn} marks. The only difference between definite and indefinite duals is the definite article [ٱَلْ]{.ar} "the". 

Here are examples of duals in sentences:

+ u-state:

  [ٱَلْكِتَابَانِ فِي ٱلْحَقِيبَةِ.]{.ar}  
  [EalkitAbAni fi -lHaqIbah.]{.trn}  
  "The books~2~ are in the bag."

+ a-state:

  [قَرَأَ ٱلْغُلَامُ كِتَابَيْنِ.]{.ar}  
  [qaraEa -lgulAmu kitAbayn.]{.trn}  
  "The boy read two books."

+ i-state:

  [غَضِبَتِ ٱلْأُمُّ عَلَى ٱلْجَارِيَتَيْنِ.]{.ar}  
  [gaDibati -lEummu eala -ljAriyatayn.]{.trn}  
  "The mother became angry at the girls~2~."
<!--
## Duals of nouns that end with feminine markers
-->
### Nouns ending in [ة]{.ar}

If a noun ends with a looped [tAE]{.trn2} [ة]{.ar}, then it is converted to an open [tAE]{.trn2} [ت]{.ar} before appending the dual suffix. For example, dualizing [شَجَرَة]{.ar} [cajarah]{.trn} "a tree", we get "trees~2~":

| States | Indefinite | Definite
:----|:-------|:-------
u-state         | [شَجَرَتَانِ]{.ar} [cajaratAni]{.trn} | [ٱَلشَّجَرَتَانِ]{.ar} [EaccajaratAni]{.trn}
a- and i-states | [شَجَرَتَيْنِ]{.ar} [cajaratayni]{.trn}| [ٱَلشَّجَرَتَيْنِ]{.ar} [Eaccajaratayni]{.trn}

Example:

[ٱَلشَّجَرَتَانِ فِي ٱلْحَدِيقَةِ.]{.ar}  
[EaccaratAni fi -lHadIqah.]{.trn}  
"The trees~2~ are in the garden."

If a feminine noun does not have a looped [tAE]{.trn2} then it will simply be appended with [◌َانِ]{.ar} [-Ani]{.trn} and [◌َيْنِ]{.ar} [-ayni]{.trn}. For example, dualizing [أُمّ]{.ar} [Eumm]{.trn} "a mother" in order to get "mothers~2~", we get:

+ u-state: [أُمَّانِ]{.ar} [EummAni]{.trn}
+ a-state and i-state: [أُمَّيْنِ]{.ar} [Eummayni]{.trn}

There are some nouns that end with an [Ealif]{.trn2} before the [ة]{.ar}, like [فَتَاة]{.ar} [fatAh]{.trn} "a young woman". We will learn how to dualize these nouns later, if [#allAh]{.trn2} wills.

<!--
### Nouns ending with [اء]{.ar}, [ىٰ]{.ar}, and [ا]{.ar}

Nouns that end with [اء]{.ar}, [ىٰ]{.ar}, and [ا]{.ar} are treated specially when forming their dual. Examples of such nouns are:

+ [صَحْرَاء]{.ar} [SaHrAE]{.trn} "a desert"
+ [بِنَاء]{.ar} [binAE]{.trn} "a building"
+ [سَمَاء]{.ar} [samAE]{.trn} "a sky"
+ [غَضْبَىٰ]{.ar} [gaDbA]{.trn} _adj._ "very angry~f~"
+ [فَتْوَىٰ]{.ar} [fatwA]{.trn} "a formal legal opinion"
+ [ٱَلْهُدَىٰ]{.ar} [EalhudA]{.trn} "the guidance"
+ [ٱَلْعَصَا]{.ar} [EaleaSA]{.trn} "the staff"

We will learn how to form duals of these words in later chapters, if [#allAh]{.trn2} wills.
-->
### Nouns ending with [اء]{.ar} {#duals-of-extrinsic-alif-mamduda}

If a noun ends with the feminine marker [اء]{.ar} which is extrinsic to the word's root then the [ء]{.ar} shall be replaced with a [و]{.ar} when forming the dual.
Examples:

|Root|Singular| Dual (u-state) |Dual (a- and i-states)|
|:-|:-----|:--|:--|
|[صحر]{.arroot}|[صَحْرَاء]{.ar} [SaHrAE]{.trn} "a desert" |[صَحْرَاوَانِ]{.ar} [SaHrAwAni]{.trn} |[صَحْرَاوَيْنِ]{.ar} [SaHrAwayni]{.trn}|
|[حمر]{.arroot}|[حَمْرَاء]{.ar} [HamrAE]{.trn} "red~f~" |[حَمْرَاوَانِ]{.ar} [HamrAwAni]{.trn} |[حَمْرَاوَيْنِ]{.ar} [HamrAwayni]{.trn}|

There are other words where the [ء]{.ar} in the [اء]{.ar} ending originates from the word's root. 
Example:

+ [خبء]{.arroot} [خِبَاء]{.ar}  (masc.) "a tent", pattern: [فِعَال]{.ar}

We will learn how to form duals of these words in later chapters, if [#allAh]{.trn2} wills.
<!--
There are some words where the [ء]{.ar} in the [اء]{.ar} is part of the word's root. In this case it remains a hamzah when forming the dual. For example:

The word [خِبَاء]{.ar} [xibAE]{.trn} "a tent" is from the root [خبء]{.arroot} and is on the pattern [فِعَال]{.ar}. Its duals are [خِبَاءَانِ]{.ar} (u-state), and [خِبَاءَيْنِ]{.ar} (a-state and i-state) "tents~2~".


There are other words where the [ء]{.ar} in the [اء]{.ar} ending was originally a [و]{.ar} or a [ي]{.ar} in the word's root. For example,

+ [دُعَاء]{.ar} [dueAE]{.trn} "a call" from the root [دعو]{.arroot} on the pattern [فُعَال]{.ar}.
+ [جَزَاء]{.ar} [jazAE]{.trn} "a reward" from the root [جزي]{.arroot} on the pattern [فَعَال]{.ar}.
We will learn about forming the duals for these words when we study roots that have weak letters, if [#allAh]{.trn2} wills.
-->

### Nouns ending with [ىٰ]{.ar} {#duals-of-extrinsic-alif-maqsura}

If a noun ends with [ىٰ]{.ar} which is extrinsic to the word's root then the [ىٰ]{.ar} shall be changed to a [يَ]{.ar} when adding the dual suffixes. Examples:

|Root|Singular| Dual (u-state) |Dual (a- and i-states)|
|:-|:-----|:--|:--|
|[غضب]{.arroot}|[غَضْبَىٰ]{.ar} [gaDbA]{.trn} "very angry~f~" | [غَضْبَيَانِ]{.ar} [gaDbayAni]{.trn} | [غَضْبَيَيْنِ]{.ar} [gaDbayayni]{.trn}|
|[ذكر]{.arroot}|[ذِكْرَىٰ]{.ar} [pikrA]{.trn} "a remembrance" | [ذِكْرَيَانِ]{.ar} [pikrayAni]{.trn} | [ذِكْرَيَيْنِ]{.ar} [pikrayayni]{.trn} |

Just like in the case of [اء]{.ar}, there are some words where [ىٰ]{.ar} is not extrinsic to the word's root.
Example:

+ [هدي]{.arroot} [ٱلْهُدَىٰ]{.ar}  (masc.) "the guidance", pattern: [ٱَلْفُعَل]{.ar}

We will learn how to form duals of these words in later chapters, if [#allAh]{.trn2} wills.

## Dual describers and describees in descriptive noun-phrases

We learned that when an adjectival noun is a describer in an descriptive noun-phrase, then it matches the describee in definiteness, state, and gender.  For example:

[ذَهَبْتُ إِلَى ٱلْمَدِينَةِ ٱلْقَدِيمَةِ.]{.ar}  
[pahabtu Eila -lmadInati -lqadImah.]{.trn}  
"I went to the old city."

To this we add that the describer shall also match the describee in number. So if the describee is a dual then the adjectival-noun describer shall be dualzed to match it. Examples:

[ٱَلْأُمَّانِ ٱلطَّيِّبَتَانِ فِي ٱلْبَيْتِ.]{.ar}  
[EalEummAni -TTayyibatAni fi -lbayt.]{.trn}  
"The good mothers~2~ are in the house."

[قَرَأَ ٱلْغُلَامُ كِتَابَيْنِ ثَقِيلَيْنِ قَدِيمَيْنِ.]{.ar}  
[qaraEa -lgulAmu kitAbayni vaqIlatayni qadImatayn.]{.trn}  
"The boy read two old heavy books."

<!--
[سَكَبَتِ ٱلْجَارِيَةُ حَلِيبًا لِلْهِرَّيْنِ ٱلْعَطْشَانَيْنِ.]{.ar}  
[sakabati -ljAriyatu HalIban lilhirrayni -leaTcAnayn.]{.trn}  
"The girl poured some milk for the very thirsty cats~m,\ 2~.
-->

<!--Just like common nouns, adjectival nouns are also dualized. When a adjectival noun is used to describe a dual noun, the adjectival noun will also be dual. Examples:

The two women are noble.

The two men are very angry.

The big books are heavy.

The man read two heavy books.
-->

## Duals in subject-information sentences

In subject-information sentences, if the subject is a dual, and the information is a adjectival noun, then the information will typically match the subject in being a dual. For example:

[ٱَلْأُمَّانِ كَرِيمَتَانِ.]{.ar}  
[EalEummAni karImatAn.]{.trn}  
"The mothers~2~ are generous."

<!--
[ٱلْمُعَلِّمَتَانِ غَضْبَيَانِ.]{.ar}  
[EalmueallimatAni gaDbayAn.]{.trn}  
"The teachers~f,2~ are very angry."
-->

[ٱَلْكِتَابَانِ ٱلْكَبِيرَانِ ثَقِيلَانِ.]{.ar}  
[EalkitAbAni -lkabIrAni vaqIlAn.]{.trn}  
"The big books~2~ are heavy."

<!--Note that both [ٱَلْمَرْأَتَانِ]{.ar} [EalmarEatAni]{.trn} "the two women" and [أُمَّانِ]{.ar}  [EummAni]{.trn}  "two mothers" are in the u-state because, just like for sentences with singulars, the subject and information are put in the u-state.-->

Such is usually also the case even when the information is a common noun, not an adjectival noun. For example,

[ٱَلرَّجُلَانِ مُعَلِّمَانِ.]{.ar}  
[EarrujulAni mueallimAn.]{.trn}  
"The men~2~ are teachers~m,2~."

Sometimes, however, the subject and information may not match in number because of the meaning of the sentence. For example,

<!--
Don't use because بناء is defective
[ٱَلْبِنَاءَانِ مَدْرَسَةً]{.ar}  
[EalbinAEAni madrasatan]{.trn}  
"The two buildings are a school"
-->

[ٱَلْوِسَادَتَانِ سَرِيرٌ.]{.ar}  
[EalwisAdatAni sarIr.]{.trn}  
"The two cushions are a bed."

In the above example, the information does not match the subject in both number, and, as it happens, in gender.

## Detached dual pronouns

We have already learned the detached pronouns that are used in place of singular nouns. They are repeated here:

|Singular participant|Detached pronoun|
|:---|:-|
|Masc. absentee     |[هُوَ]{.ar} [huwa]{.trn}   "he"      |
|Fem.  absentee     |[هِيَ]{.ar} [hiya]{.trn}   "she"    |
|Masc. addressee    |[أَنْتَ]{.ar} [Eanta]{.trn} "you~m,1~"|
|Fem.  addressee    |[أَنْتِ]{.ar} [Eanti]{.trn} "you~f,1~"|
|Speaker            |[أَنَا]{.ar} [Eana]{.trn}  "I"      |

Now we will learn the detached pronouns for the dual participants:

|Dual participant|Detached pronoun|
|:---|:-|
|Absentee   |[هُمَا]{.ar} [humA]{.trn}      "they~2~" |
|Addressee  |[أَنْتُمَا]{.ar} [EantumA]{.trn} "you~2~" |
|Speaker     | -- |

Note that the dual detached pronouns are the same for both genders.
Also, there is no detached pronoun for the dual speaker-participant. If the speaker-pariticipant consists of two individuals then we will use the plural pronoun, which we will learn in the next chapter, if [#allAh]{.trn2} wills.

Here are some examples of their use:

[هُمَا ٱلرَّجُلَانِ.]{.ar}  
[huma -rrajulAn.]{.trn}  
"They~2~ are the men~2~."

[هُمَا مُعَلِّمَتَانِ كَرِيمَتَانِ.]{.ar}  
[humA mueallimatAni karImatAni.]{.trn}  
"They~2~ are noble teachers~f~."

[قَالَتِ ٱلأُمُّ لِلْجَارِيَتَيْنِ أَنْتُمَا قَرِيبَتَانِ مِنِّي.]{.ar}  
[qAlati -lEummu liljAriyatayni EantumA qarIbatAni minnI.]{.trn}  
"The mother said to the girls~2~, 'You~2~ are near me.'"

In the last example, the feminine adjectival-noun [قَرِبَتَانِ]{.ar} [qarIbatAni]{.trn} is used because it is referring to the feminine noun [ٱَلْجَارِيَتَيْنِ]{.ar} [EaljAriyatayni]{.trn} "the girls~2~".

## Attached dual pronouns

We have also already learned the attached pronouns for the singular participant. They too are repeated here:

|Singular participant | Attached pronoun|
|:------|:--|
|Masc. absentee      | [هُ]{.ar} [-hu]{.trn}   "him"      |
|Fem.  absentee      | [هَا]{.ar} [-hA]{.trn}  "her"     |
|Masc. addressee     | [كَ]{.ar} [-ka]{.trn}   "you~m,1~"|
|Fem.  addressee     | [كِ]{.ar} [-ki]{.trn}   "you~f,1~"|
|Speaker             | [ي]{.ar}               "me"      |

Now we will learn the attached pronouns for the dual participant:

|Dual participant|Attached pronoun|
|:---|:-|
|Absentee   |[هُمَا]{.ar} [-humA]{.trn}  "them~2~" |
|Addressee  |[كُمَا]{.ar} [-kumA]{.trn}  "you~2~" |
|Speaker     | -- |

Note the following points about them:

+ Like the dual detached pronouns, the dual attached pronouns are the same for both genders. Also, there is no attached pronoun for the dual speaker-participant. Again, the plural pronoun will be used in this case.

+ The dual absentee-participant detached and attached pronouns ("they~2~"/"them~2~") are the same [هُمَا]{.ar} [-humA]{.trn}.

+ Just like the absentee-participant singular masculine attached pronoun [هُ]{.ar} [hu]{.trn} "him", the dual absentee-participant attached pronoun "them~2~" [هُمَا]{.ar} [-humA]{.trn} becomes [هِمَا]{.ar} [-himA]{.trn} when preceded by the vowels [◌ِ]{.ar} [-i]{.trn}, [◌ِي]{.ar} [-I]{.trn}, or the semi-vowel [◌َيْ]{.ar} [-ay]{.trn}. Examples:
   + [بِهِمَا]{.ar} [bihimA]{.trn} "with them~2~"
   + [فِيهِمَا]{.ar} [fIhimA]{.trn} "in them~2~"
   + [إِلَيْهِمَا]{.ar} [EilayhimA]{.trn} "to them~2~"
+ The preposition [لِ]{.ar} [li]{.trn} "for" becomes [لَ]{.ar} [la]{.trn} when followed by the dual attached pronouns:
   + [لَهُمَا]{.ar} [lahumA]{.trn} "for them~2~"
   + [لَكُمَا]{.ar} [lakumA]{.trn} "for you~2~"
+ As expected, the long [A]{.trn} vowel at the ends of the dual attached pronouns becomes a short [a]{.trn} vowel when followed by a connecting hamzah [ٱ]{.ar}. Example:
  + [ذَهَبَ إِلَيْكُمَا ٱلرَّجُلُ.]{.ar}  
    [pahaba Eilaykuma -rrajulu.]{.trn}  
    "The man went toward you~2~."

### Dual doee pronouns

The dual attached pronouns that we have just learned are also used as doee pronouns. 
<!--Again, there is no additional intervening [ن]{.ar} for the speaking participant dual attached pronoun [نَا]{.ar} [-nA]{.trn}. -->
Examples:

[سَأَلَهُمَا ٱلرَّجُلُ.]{.ar}  
[saEalahuma -rrajulu.]{.trn}  
"The man asked them~2~."

[سَأَلْتُكُمَا.]{.ar}  
[saEaltukumA]{.trn}  
"I asked you~2~."

[سَأَلَتْكُمَا.]{.ar}  
[saEalatkumA.]{.trn}  
"She asked you~2~."

## Verbs with dual doers

### Dual nouns for the doer

We learned that the completed-action verb for a masculine doer is on the pattern [فَعَلَ]{.ar}. And when the doer is feminine, the [ت]{.ar} of femininity is attached to the verb thus: [فَعَلَتْ]{.ar}. We have used these verbs with singular doer nouns. The doer noun always comes after the verb and shall be in the u-state. Examples:

[ذَهَبَ ٱلْغُلَامُ.]{.ar}  
[pahaba -lgulAmu.]{.trn}  
"The boy went." 

[ذَهَبَتْ جَارِيَةٌ.]{.ar}  
[pahabat jAriyatun]{.trn}  
"A girl went." 

These same verbs are used when the doer noun is a dual. Examples:

[ذَهَبَ ٱلْغُلَامَانِ.]{.ar}  
[pahaba -lgulAmAni.]{.trn}  
"The boys~2~ went." 

[ذَهَبَتْ جَارِيَتَانِ.]{.ar}  
[pahabat jAriyatAni.]{.trn}  
"Two girls went." 

### Dual pronouns for the doer

We have already learned the singular doer pronouns:

|Singular participant | Doer pronoun |Meaning| Doer pronoun with verb|
|:--|:--|:--|:--|
|Masc. absentee    | invisible            |"he"      | [فَعَلَ]{.ar} [faeala]{.trn}|
|Fem.  absentee    | invisible            |"she"     | [فَعَلَتْ]{.ar} [faealat]{.trn}|
|Masc. addressee   | [تَ]{.ar} [-ta]{.trn} |"you~m,2~"| [فَعَلْتَ]{.ar} [faealta]{.trn}|
|Fem.  addressee   | [تِ]{.ar} [-ti]{.trn} |"you~f,2~"| [فَعَلْتِ]{.ar} [faealti]{.trn}|
|Speaker           | [تُ]{.ar} [-tu]{.trn} |"I"       | [فَعَلْتُ]{.ar} [faealtu]{.trn}|

Now we will learn the dual doer pronouns:

|Dual participant | Doer pronoun | Meaning |Doer pronoun with verb|
|:--|:--|:--|:---|
|Absentee    | [◌َا]{.ar} [-A]{.trn}     | "them~2~" | masc.: [فَعَلَا]{.ar} [faealA]{.trn}, fem: [فَعَلَتَا]{.ar} [faealatA]{.trn}|
|Addressee   | [تُمَا]{.ar} [-tumA]{.trn} | "you~2~"  | [فَعَلْتُمَا]{.ar} [faealtumA]{.trn} |
|Speaker     | -- | "us~2~" | --|

Note the following regarding the dual doer pronouns:

The dual doer pronouns are the same for both genders.

However, when the absentee-participant doer pronoun ([◌َا]{.ar} [-A]{.trn}) is used for a feminine doer, it is attached to the verb with an intervening [ت]{.ar} of femininity thus: [فَعَلَتَا]{.ar} [faealatA]{.trn} "they~f,2~ did"
Here are some examples of the dual doer pronouns:

[سَأَلْتُمَانَا]{.ar}  
[saEaltumAnA]{.trn}  
"You~2~ asked us"

[سَأَلَتَاكُمَا]{.ar}  
[saEalatAkumA]{.trn}  
"They~f,2~ asked you~2~"

[سَأَلَاهُمَا]{.ar}  
[saEalAhumA]{.trn}  
"They~m,2~ asked them~2~"

### Sentence word order with dual doers

As we've mentioned, the doer, whether a noun or a pronoun, always comes after the verb. Here are a couple of examples of verbal sentences with dual doers:

[ذَهَبَا إِلَىٰ بَيْتٍ.]{.ar}  
[pahabA EilA baytin.]{.trn}  
"They~2~ went to a house."

[ذَهَبَ ٱلرَّجُلَانِ إِلَىٰ بَيْتٍ.]{.ar}  
[pahabA -rrujalAni EilA baytin.]{.trn}  
"The men~2~ went to a house."

The above verbal sentence can be rearranged to be a subject-information sentence. This gives more emphasis to the subject. In this case, the verb shall follow the subject and will need a doer pronoun after it.

[ٱَلرَّجُلَانِ ذَهَبَا إِلَىٰ بَيْتٍ.]{.ar}  
[EarrujalAni pahabA EilA baytin.]{.trn}  
"The men~2~, they~2~ went to a house."  
= "_The men~2~_ went to a house."

If there are multiple verbs associated with the same doer in a verbal sentence, the doer noun will follow the first verb  and the rest of the verbs will have doer pronouns. For example:

[أَكَلَ ٱلرَّجُلَانِ وَشَرِبَا وَذَهَبَا.]{.ar}  
[Eakala -rrajulAni wacaribA wapahabA.]{.trn}  
"The men~2~ ate and they~2~ drank and they~2~ went."  
= "The men~2~ ate and drank and went."

The above verbal sentence can be rearranged to be a subject-information sentence. In that case, all the verbs shall have doer pronouns. The sentence will have the same translation as above, except for an emphasis on the subject of the sentence.

[ٱَلرَّجُلَانِ أَكَلَا وَشَرِبَا وَذَهَبَا.]{.ar}  
[EarrajulAni EakalA wacaribA wapahabA.]{.trn}  
"The men~2~, they~2~ ate and they~2~ drank and they~2~ went."  
= "_The men~2~_ ate and drank and went."


<!--chapter:end:srcrmd/duals.Rmd-->

# Sound plurals

## Introduction

Arabic uses the plural for nouns in number three and higher. The formation and use of plurals in Arabic can be somewhat complicated. One of these complications is that, in using plurals, Arabic distinguishes between intelligent beings and non-intelligent beings. Intelligent beings are those living beings that are endowed with reason like humans, angels, and jinn. Non-intelligent beings include animals, inanimate objects, abstract concepts, etc.

As a further complication, there is sometimes more than one way to use plurals. In this chapter we will explain the most common usages to keep things as simple as possible.

Arabic has two categories of plurals:

1. The _sound plural:_ 
   English regularly forms the plural by adding the plural ending "s" to the end of a singular noun. For example:
   
   | Singular | Plural |
   |:-----------|:-----------|
   | book       | books      |
   | house      | houses     |
   | boy        | boys       |
   | girl       | girls      |
   
   Arabic also forms some plurals by adding plural endings to to the singular noun. This kind of plural is call a _sound_ plural because the singular noun is kept more or less sound (intact) when adding the plural ending.
   
   Arabic has two types of sound plurals:
   
   i.  The [Un]{.trn} sound plural.
   ii. The [At]{.trn} sound plural.

  We will describe each of these in this chapter.

2. The _broken plural_: When forming this plural the singular noun is not kept intact. We will learn about this plural in the next chapter, if [#allAh]{.trn2} wills.

<!--When translating plurals to English, we may use the subscript "3+" thus "teachers~m,3+~" in order to distinguish it from the dual "teachers~m,2~".-->

## The [Un]{.trn} sound plural

The [Un]{.trn} sound plural is formed by adding the ending [◌ُونَ]{.ar} [-Una]{.trn} to the singular noun when it is in the u-state, and [◌ِينَ]{.ar} [-Ina]{.trn} when the noun is in the a-state or i-state. For convenience, we will call it the "[Un]{.trn} sound plural" instead of the "[-Una]{.trn}/[-Ina]{.trn} plural".

Here is the [Un]{.trn} sound plural of [مُعَلِّم]{.ar} [mueallim]{.trn} "a teacher~m~":

| State | Indefinite [Un]{.trn} plural "teachers~m~"| Definite [Un]{.trn} plural "the teachers~m~"|
|:---------|:-------------|:-------------|
| u-state         | [مُعَلِّمُونَ]{.ar} [mueallimUna]{.trn} |[ٱَلْمُعَلِّمُونَ]{.ar} [EalmueallimUna]{.trn}|
| a- and i-states | [مُعَلِّمِينَ]{.ar} [mueallimIna]{.trn} |[ٱَلْمُعَلِّمِينَ]{.ar} [EalmueallimIna]{.trn}|

Note that, just like for duals, the indefinite [Un]{.trn} sound plural doesn't have [n]{.trn} marks. The only difference between the definite and indefinite [Un]{.trn} sound plural is the definite article [ٱَلْ]{.ar} "the". 

The duals of [مُعَلِّم]{.ar} [mueallim]{.trn} "a teacher~m~" are included here for comparison:

| State | Indefinite [Un]{.trn} sound plural "teachers~m,2~" | Definite [Un]{.trn} sound plural "the teachers~m,2~"|
|:---------|:-------------|:-------------|
| u-state         | [مُعَلِّمَانِ]{.ar} [mueallimAni]{.trn} |[ٱَلْمُعَلِّمَانِ]{.ar} [EalmueallimAni]{.trn}|
| a- and i-states | [مُعَلِّمَيْنِ]{.ar} [mueallimayni]{.trn} |[ٱَلْمُعَلِّمَيْنِ]{.ar} [Ealmueallimayni]{.trn}|

Here are some examples of the [Un]{.trn} sound plural in sentences:

+ u-state:

  [ٱلْمُعَلِّمُونَ فِي ٱلْمَدْرَسَةِ.]{.ar}  
  [EalmueallimUna fi -lmadrasah]{.trn}  
  "The teachers are in the school."

+ a-state:

  [سَأَلَ ٱلْغُلَامُ مُعَلِّمِينَ عَنْ أَمْرٍ.]{.ar}  
  [saEala -lgulAmu mueallimIna fI Eamr.]{.trn}  
  "The boy asked some teachers about a matter."

+ i-state:

  [طَلَبَ ٱلْغُلَامُ مِنَ ٱلْمُعَلِّمِينَ عِلْمًا.]{.ar}  
  [Talaba -lgulAmu mina -lmueallimIna eilmA.]{.trn}  
  "The boy sought some knowledge from the teachers."

### Applicability of the [Un]{.trn} sound plural {#applicability-of-the-un-sound-plural}

Except for very few exceptions, the [Un]{.trn} sound plural is used only for male intelligent beings. 

<!--We will learn some of these exceptions in chapter\ \@ref(irregular-nouns).-->

<!--Of these exceptions, the word [سَنَةٌ]{.ar} [sanatun]{.trn} "a year" is the most common. It is pluralized as [سِنُونَ]{.ar} [sinUna]{.trn} in the u-state and [سِنِينَ]{.ar} [sinIna]{.trn} in the a-state and i-state.-->

The few exceptions of common nouns that denote non-male intelligent beings, yet have an [Un]{.trn} sound plural include:

+ [عَالَم]{.ar} [eAlam]{.trn} "a world" forms the [Un]{.trn} plural [عَالَمُونَ]{.ar} [EAlamUna]{.trn} "worlds".
+ [أَرْض]{.ar} [EarD]{.trn} (fem.) "a land", "an earth" forms the [Un]{.trn} plural [أَرْضُونَ]{.ar} [EarDUna]{.trn} "lands", "earths".
+ [أَهْل]{.ar} [Eahl]{.trn} "a family" forms the [Un]{.trn} plural [أَهْلُونَ]{.ar} [EahlUna]{.trn} "families".


## The [At]{.trn} sound plural

The [At]{.trn} sound plural is formed by adding the ending [ات]{.ar} [At]{.trn} to the indefinite singular noun. <!-- when it is in the u-state, and [ـَاتٍ]{.ar} [Atin]{.trn} when the noun is in the a-state or i-state.-->

Here is the [At]{.trn} sound plural of [حَيَوَان]{.ar} [HayawAn]{.trn} "an animal":

| State | Indefinite [Un]{.trn} plural "animals"| Definite [Un]{.trn} plural "the animals"|
|:---------|:-------------|:-------------|
| u-state         | [حَيَوَانَاتٌ]{.ar} [HayawAnAtun]{.trn} |[ٱَلْحَيَوَانَاتُ]{.ar} [EalHayawAnAtu]{.trn}|
| a- and i-states | [حَيَوَانَاتٍ]{.ar} [HayawAnAtin]{.trn} |[ٱَلْحَيَوَانَاتِ]{.ar} [EalHayawAnAti]{.trn}|

Note that: <!-- there _are_ [n]{.trn} marks for the [At]{.trn} sound plural. Definite plural nouns are also formed in the same way but they won't have [n]{.trn} marks:-->

+ Unlike the [Un]{.trn} sound plural, the [At]{.trn} sound plural takes [n]{.trn} marks. Also, just like for singular nouns, the final vowel on the plural ending [ات]{.ar} [At]{.trn} indicates the state of the plural.
+ The [At]{.trn} sound plural does not take the [a]{.trn}-mark [◌َ]{.ar} and the [an]{.trn}-mark [◌ً]{.ar}. Instead the [i]{.trn}-mark [◌ِ]{.ar} and the [in]{.trn}-mark [◌ٍ]{.ar}-mark are used to indicate both the a-state and the i-state.

| State | the animal | the animals
|:-----------|:-------------|:-------------|
| u-state | [ٱَلْحَيَوَانُ]{.ar} [EalHayawAnu]{.trn}| [ٱَلْحَيَوَانَاتُ]{.ar} [EalHayawAnAtu]{.trn}|
| a-state | [ٱَلْحَيَوَانَ]{.ar} [EalHayawAna]{.trn}| [ٱَلْحَيَوَانَاتِ]{.ar} [EalHayawAnAti]{.trn}|
| i-state | [ٱَلْحَيَوَانِ]{.ar} [EalHayawAni]{.trn}| [ٱَلْحَيَوَانَاتِ]{.ar} [EalHayawAnAti]{.trn}|

### Nouns ending in [ة]{.ar}

If a noun ends with a looped [tAE]{.trn2} [ة]{.ar}, then it is removed before appending the [At]{.trn} sound plural ending. 
Here, for example, is the [At]{.trn} sound plural of [مُعَلِّمَة]{.ar} [mueallimah]{.trn} "a teacher~f~":

| State | Indefinite [Un]{.trn} plural "teachers~f~"| Definite [Un]{.trn} plural "the teachers~f~"|
|:---------|:-------------|:-------------|
| u-state         | [مُعَلِّمَاتٌ]{.ar} [mueallimAtun]{.trn} |[ٱَلْمُعَلِّمَاتُ]{.ar} [EalmueallimAtu]{.trn}|
| a- and i-states | [مُعَلِّمَاتٍ]{.ar} [mueallimAtin]{.trn} |[ٱَلْمُعَلِّمَاتِ]{.ar} [EalmueallimAti]{.trn}|

Here are some examples of the [At]{.trn} sound plural in sentences:

+ u-state:

  [فِي ٱلْمَدْرَسَةِ مُعَلِّمَاتٌ .]{.ar}  
  [fi -lmadrasati mueallimAtun.]{.trn}  
  "In the school are teachers."

+ a-state:

  [نَصَرَ ٱللَّـٰهُ ٱلْمُسْلِمِينَ.]{.ar}  
  [naSara -llAhu -lmuslimIna.]{.trn}  
  "[#allAh]{.trn2} aided the Muslims.

+ i-state:

  [نَظَرَ ٱلْغُلَامُ إِلَى ٱلْحَيَوَانَاتِ.]{.ar}  
  [naPara -lgulAmu Eila -lHayawAnAti.]{.trn}  
  "The boy looked at the animals."

There are some nouns that end with an [Ealif]{.trn2} before the [ة]{.ar}, like [فَتَاة]{.ar} [fatAh]{.trn} "a young woman". We will learn how to pluralize these nouns later, if [#allAh]{.trn2} wills.

### Nouns ending with [اء]{.ar}

Consistent with what we learned for duals in section\ \@ref(duals-of-extrinsic-alif-mamduda),
if a noun ends with the feminine marker [اء]{.ar} which is extrinsic to the word's root then the [ء]{.ar} shall be replaced with a [و]{.ar} when forming the [At]{.trn} sound plural.
Example:

|Root|Singular| [At]{.trn} sound plural|
|:-|:-----|:--|
|[صحر]{.arroot}|^2^[صَحْرَاء]{.ar} [SaHrAE]{.trn}^2^ "a desert" |[صَحْرَاوَات]{.ar} [SaHrAwAt]{.trn} |


### Nouns ending with [ىٰ]{.ar} 

Consistent with what we learned for duals in section\ \@ref(duals-of-extrinsic-alif-maqsura),
If a noun ends with [ىٰ]{.ar} which is extrinsic to the word's root then the [ىٰ]{.ar} shall be changed to a [يَ]{.ar} when when forming the [At]{.trn} sound plural. Examples:

|Root|Singular| [At]{.trn} sound plural|
|:-|:-----|:--|
|[ذكر]{.arroot}|^2^[ذِكْرَىٰ]{.ar} [pikrA]{.trn}^2^ "a remembrance" | [ذِكْرَيَات]{.ar} [pikrayAt]{.trn} |

<!--
### Nouns ending with [اء]{.ar}, [ىٰ]{.ar}, [ا]{.ar}, and [اة]{.ar} {#at-plural-for-defective-nouns}

As with duals, nouns that end with [اء]{.ar}, [ىٰ]{.ar}, [ا]{.ar}, and [اة]{.ar} are treated specially when forming their [At]{.trn} sound plural. Examples of such nouns are:

+ [سَمَاء]{.ar} [samAE]{.trn} "a sky"
+ [غَضْبَىٰ]{.ar} [gaDbA]{.trn} _adj._ "very angry~f~"
+ [ٱَلْعَصَا]{.ar} [EaleaSA]{.trn} "the staff"
+ [فَتَاة]{.ar} [fatAh]{.trn} "a young woman"

We will learn how to form the [At]{.trn} sound plural of these words in later chapters, if [#allAh]{.trn2} wills.

### The [At]{.trn} sound plural for words ending with [اء]{.ar}

If a noun ends with an [اء]{.ar} then the [hamzah]{.trn2} may either be retained or get converted to a [و]{.ar} when forming the [At]{.trn} sound plural. This is done based on the same rules as for the dual which we explained in the previous chapter.

Thus,

+ REMOVE because plurals of qualitative nouns not yet discussed: [صَفْرَاءُ]{.ar} [SafrAE]{.trn} (root: [صفر]{.arroot}) becomes [صَفْرَاوَاتٌ]{.ar} [SafrAwAtun]{.trn}.
+ [صَحْرَاءُ]{.ar} [SaHrAE]{.trn} (root: [صحر]{.arroot}) becomes [صَحْرَاوَاتٌ]{.ar} [SaHrAwAtun]{.trn}.
+ [إِبْطًاءٌ]{.ar} [EibTAEun]{.trn} (root: [بطء]{.arroot}) becomes [إِبْطَاءَاتٌ]{.ar} [EibTAEAtun]{.trn}.
+ [سَمَاءٌ]{.ar} [samAEun]{.trn} (root: [سمو]{.arroot}) becomes [سَمَاءَاتٌ]{.ar} [samAEAtun]{.trn} or [سَمَاوَاتٌ]{.ar} [samAwAtun]{.trn}.

### The [At]{.trn} sound plural for words ending with [يٰ]{.ar}

If a noun ends with [ىٰ]{.ar}, then whether the [ىٰ]{.ar} is a feminine marker or not, it becomes a [yAE]{.trn2} with an [a]{.trn}-mark [يَ]{.ar} when forming the [At]{.trn} sound plural. For example,  

+ [حُبَارَىٰ]{.ar} [HubArA]{.trn} becomes [حُبَارَيَاتٌ]{.ar} [HubArayAtun]{.trn}.

### Designative nouns of the pattern [فَُِعْل]{.ar} and [فَُِعْلَة]{.ar}
-->

### Common nouns of the patterns [فَعْل]{.ar}/[فَعْلَة]{.ar}, [فِعْل]{.ar}/[فِعْلَة]{.ar}, and [فُعْل]{.ar}/[فُعْلَة]{.ar}

Common nouns of the patterns [فَعْل]{.ar}/[فَعْلَة]{.ar}, [فِعْل]{.ar}/[فِعْلَة]{.ar}, and [فُعْل]{.ar}/[فُعْلَة]{.ar} are treated specially when forming their [At]{.trn} sound plural.

If a common noun is of these patterns and the middle root letter is not [و]{.ar} or [ي]{.ar}, and the middle and final root letters are not the same, then the word is modified internally when forming the [At]{.trn} sound plural.

There are two separate rules to consider:

1.  If a common noun is of the pattern [فَعْل]{.ar} [fael]{.trn} or [فَعْلَة]{.ar} [faelah]{.trn}, then the [0]{.txt}-mark on the middle letter shall be converted to an [a]{.trn}-mark [◌َ]{.ar} when forming the [At]{.trn} sound plural. For example:

    + [نَحْلَة]{.ar} [naHlah]{.trn} "a bee" becomes [نَحَلَات]{.ar} [naHalAt]{.trn} "bees", not $\times$\ [نَحْلَات]{.ar} [naHlAt]{.trn}.
    + [ضَرْبَة]{.ar} [Darbah]{.trn} "a strike" becomes [ضَرَبَات]{.ar} [DarabAt]{.trn} "strikes", not $\times$\ [ضَرْبَات]{.ar} [DarbAt]{.trn}.
    + [صَفْحَة]{.ar} [SafHah]{.trn} "a page" becomes [صَفَحَات]{.ar} [SafaHAt]{.trn} "pages", not $\times$\ [صَفْحَات]{.ar} [SafHAt]{.trn}.

    If the middle root letter is [و]{.ar} or [ي]{.ar}, or the middle and final root letters are the same then this modification is not done. For example,

    + [جَوْزَة]{.ar} [jawzah]{.trn} "a walnut" becomes [جَوْزَات]{.ar} [jawzAt]{.trn}.
    + [حَجَّة]{.ar} [Hajjah]{.trn} "a pilgrimage" becomes [حَجَّات]{.ar} [HajjAt]{.trn}.

2.  If a common noun is of the pattern [فِعْل]{.ar} [fiel]{.trn}, [فِعْلَة]{.ar} [fielah]{.trn}, [فُعْل]{.ar} [fuel]{.trn}, or [فُعْلَة]{.ar} [fuelah]{.trn} then the [0]{.txt}-mark on the middle letter can, optionally, either:

    i.   be retained,
    ii.  be converted to an [a]{.trn} mark, or
    iii. be converted to the vowel mark on the first letter.

    For example:

    + [ظُلْمَة]{.ar} [Pulmah]{.trn} "a darkness" can become, optionally, either [ظُلْمَات]{.ar} [PulmAt]{.trn} or [ظُلَمَات]{.ar} [PulamAt]{.trn}, or [ظُلُمَات]{.ar} [PulumAt]{.trn} "darknesses".
    + [كِسْرَة]{.ar} [kisrah]{.trn} "a piece" can become, optionally, either [كِسْرَات]{.ar} [kisrAt]{.trn} or [كِسَرَات]{.ar} [kisarAt]{.trn}, or [كِسِرَات]{.ar} [kisirAt]{.trn} "pieces".

Note that this rule of changing the vowel mark is only true for common nouns. Adjectival-nouns on these patterns will retain the [0]{.txt}-mark when forming the [At]{.trn} sound plural. So [صَعْب]{.ar} [Saeb]{.trn} and [صَعْبَة]{.ar} [Saebah]{.trn} "a difficult one" become only [صَعْبَات]{.ar} [SaebAt]{.trn}, not $\times$\ [صَعَبَات]{.ar} [SaeabAt]{.trn}.

### Applicability of the [At]{.trn} sound plural

We had mentioned that the [Un]{.trn} sound plural is used, with very few exceptions, only for male intelligent beings. Conversely, the [At]{.trn} is used for both female intelligent beings, and for non-intelligent beings (both masculine and feminine) like animals, inanimate objects, and abstract concepts. Rarely, it is also used for male intelligent beings.


<!--
Examples:

[ٱَلْمُعَلِّمَاتُ فِي ٱلْمَدْرَسَةِ.]{.ar}  
[EalmueallimAtu fi -lmadrasati.]{.trn}  
"The female teachers are in the school."

[ٱَلْحَيَوَانَاتُ فِي ٱلْغَابَاتِ.]{.ar}  
[EalHayawAnAtu fi -lgAbAti.]{.trn}  
"The animals are in the forests."
-->

## Conditions for forming the sound plural

Many times, a noun can form both an [Un]{.trn} sound plural and an [At]{.trn} sound plural.
<!--However, some nouns form only an [Un]{.trn} sound plural, and not an [At]{.trn} sound plural.
Conversely, some nouns form only an [At]{.trn} sound plural, and not an [Un]{.trn} sound plural.
-->
However, there are many nouns that can form only one of the two sound plurals.
And many nouns don't form either sound plural; they only form broken plurals. (We will learn about broken plurals in the next chapter, if [#allAh]{.trn2} wills.) There are even nouns that can form both sound and broken plurals.

Here we will learn some of the conditions which a noun needs to satisfy in order for it to form the sound plurals.

### Conditions for the [Un]{.trn} sound plural

The [Un]{.trn} sound plural is used, with very few exceptions, only for nouns that denote male intelligent beings. These guidelines will help you determine which nouns form the [Un]{.trn} sound plural. 

We will treat common nouns and adjectival nouns separately.

#### Common nouns

<!--Common nouns will form an [Un]{.trn} sound plural if it is listed in their vocabulary/dictionary definition. 
You can often determine if a common noun will regularly form a sound plural based on the pattern of the noun. But that is an advanced technique that we will learn later, if [#allAh]{.trn2} wills. For now, we will rely on the dictionary/vocabulary definition to tell us whether a noun forms the [Un]{.trn} sound plural.
-->
With very few exceptions (some of which we saw in 
section\ \@ref(applicability-of-the-un-sound-plural)),
the only common nouns that _may_ be allowed to form [Un]{.trn} sound plurals are those that denote male intelligent beings, and whose feminine is formed by adding a [ة]{.ar} to the masculine noun. So, [غُلَام]{.ar} [gulAm]{.trn} "a boy" is disqualified from forming a [Un]{.trn} sound plural because its feminine counterpart is [جَارِيَة]{.ar} [jAriyah]{.trn} "a girl", not $\times$\ [غُلَامَة]{.ar} [gulAmah]{.trn}. In addition, a further restriction is imposed, which we will explain below:

We learned in section\ \@ref(related-nouns-for-male-and-female-animate-beings) that, in terms of their meaning, nouns that denote animate beings are of two kinds:

i.  Nouns that have a primitive meaning. That is, their meaning is not derived from a verbal or adjectival meaning. Examples (for male intelligent beings whose feminine is formed by adding [ة]{.ar} to the masculine noun):

    Arabic word | Definition
    :----------------|:----------------
    [ٱِبْن]{.ar}    [Eibn]{.trn}      |a son
    [طِفْل]{.ar}    [Tifl]{.trn}      |a child
    [إِنْسَان]{.ar}  [EinsAn]{.trn}    |a human being
    [حُرّ]{.ar}     [Hurr]{.trn}      |a free man

    Such nouns, in general, won't be expected to form [Un]{.trn} sound plurals, unless the [Un]{.trn} sound plural is explicitly allowed in their dictionary definition.

ii. Nouns that have a meaning that is derived from a verbal or adjectival meaning. Examples (for male intelligent beings whose feminine is formed by adding [ة]{.ar} to the masculine noun):

    |Word | Definition | [Un]{.trn} plural|
    |:--------------|:----------------|:------------|
    |[مُعَلِّم]{.ar}  |a  teacher~m~   |[مُعَلِّمُونَ]{.ar}|
    |[مُسْلِم]{.ar}  |a  Muslim~m~ (one who submits)  |[مُسْلِمُونَ]{.ar}|
    |[كَافِر]{.ar}  |a  disbeliever~m~ |[كَافِرُونَ]{.ar}|
    |[لَاعِب]{.ar}  |a  player~m~    |[لَاعِبُونَ]{.ar}|

    Such nouns, in general, can be expected to form [Un]{.trn} sound plurals. 
    
<!--Many of these nouns also, as we will see in the next chapter, if [#allAh]{.trn2} wills, form broken plurals. In general, then, the broken plural is preferred to be used over the sound plural, and the sound plural is only used in specific cases (that we will also see later, if [#allAh]{.trn2} wills).-->

The above condition, as we have explained it, is somewhat imprecise. For example, the word 
    [حُرّ]{.ar}     [Hurr]{.trn}      (masc.) "a free man" seems to have a meaning that is derived from the adjective "free" and it forms its feminine by adding [ة]{.ar} to it thus: 
[حُرَّة]{.ar}    [Hurrah]{.trn}    (fem.) "a free woman".
Yet it is considered a primitve noun, and thus does not form an [Un]{.trn} sound plural.

In later chapters, once we have studied the patterns of the derived nouns, we will try to make this condition more precise, if [#allAh]{.trn2} wills.

#### Adjectival nouns

If an adjectival noun forms its feminine by adding the feminine marker [ة]{.ar} to the masculine noun, then we may assume that it forms the [Un]{.trn} sound plural. 

Most adjectival nouns satisfy this condition. For example, consider the adjectival noun:

+ [كَبِير]{.ar} [kabIr]{.trn} (masc.) "a big one"

It forms its feminine by adding a [ة]{.ar} to the masculine noun, thus:

+ [كَبِيرَة]{.ar} [kabIrah]{.trn} (fem.) "a big one"

The above condition is satisfied; therefore,
[كَبِير]{.ar} [kabIr]{.trn} (masc.) "a big one" forms the [Un]{.trn} sound plural [كَبِيرُونَ]{.ar} [kabIrUna]{.trn} "big ones".

By the way, it is only the masculine adjectival noun that will form the [Un]{.trn} sound plural. Nouns with a [ة]{.ar} are not allowed to form the [Un]{.trn} sound plural.

We have come across two patterns on adjectival nouns that don't form their feminine by adding [ة]{.ar} to masculine noun. These are:

i.  ^2^[فَعْلَان]{.ar} [faelAn]{.trn}^2^, whose feminine is on the pattern ^2^[فَعْلَىٰ]{.ar} [faelA]{.trn}^2^. Example: ^2^[غَضْبَان]{.ar} [gaDbAn]{.trn}^2^ (masc.) "very angry" whose feminine is ^2^[غَضْبَىٰ]{.ar} [gaDbA]{.trn}^2^.
ii. ^2^[أَفْعَل]{.ar} [Eafeal]{.trn}^2^, whose feminine is on the pattern ^2^[فَعْلَاء]{.ar} [faelAE]{.trn}^2^. Example: ^2^[أَحْمَر]{.ar} [EaHmar]{.trn}^2^ (masc.) "red", whose feminine is ^2^[حَمْرَاء]{.ar} [HamrAE]{.trn}^2^.

Because the above two patterns don't form their feminine by adding [ة]{.ar} to the masculine noun, therefore the masculine nouns don't form the [Un]{.trn} sound plural. We will see, if [#allAh]{.trn2} wills, that they form broken plurals instead.

### Conditions for the [At]{.trn} sound plural {#conditions-for-the-at-plural}

Just like the [Un]{.trn} plural, there are conditions that should be fulfilled in order for a noun to form an [At]{.trn} plural.
We provide the following guidelines to help you determine if a noun can form an [At]{.trn} plural.

#### Nouns that end with a feminine marker

Generally, all nouns that end with a feminine marker like
[ة]{.ar}, [اء]{.ar}, and [ىٰ]{.ar}
are able to form an [At]{.trn} plural.
<!--
This includes both common nouns and adjectival nouns.

As mentioned in section\ \@ref(at-plural-for-defective-nouns) above, we will learn how to form plurals for nouns that end with 
[اء]{.ar}, and [ىٰ]{.ar}
later, if [#allAh]{.trn2} wills.
So, for now, we will focus on nouns that end with [ة]{.ar}.
-->
Examples are:

|Singular| [At]{.trn} sound plural|
|:-------|:--|
|[حَسَنَة]{.ar} [Hasanah]{.trn} _adj._ "a good one~f~"     |[حَسَنَات]{.ar} [HasanAt]{.trn}|
|[حَسَنَة]{.ar} [Hasanah]{.trn} (common noun) "a good deed"| [حَسَنَات]{.ar} [HasanAt]{.trn}|
|[صَدِيقَة]{.ar} [SadIqah]{.trn} "a friend~f~"             |[صَدِيقَات]{.ar} [SadIqAt]{.trn}|
|^2^[صَحْرَاء]{.ar} [SaHrAE]{.trn}^2^ "a desert"           |[صَحْرَاوَات]{.ar} [SaHrAwAt]{.trn} |
|^2^[ذِكْرَىٰ]{.ar} [pikrA]{.trn}^2^ "a remembrance"        | [ذِكْرَيَات]{.ar} [pikrayAt]{.trn} |

The following are exceptions to this general rule, and don't form [At]{.trn} sound plurals:

+ Adjectival nouns of the pattern ^2^[فَعْلَاء]{.ar} which is the feminine of the masculine adjectival noun pattern ^2^[أَفْعَل]{.ar}. For example, [حمر]{.arroot} [حَمْرَاء]{.ar} [HamrAE]{.trn} "red~f~".

+ Adjectival nouns of the pattern ^2^[فَعْلَىٰ]{.ar} which is the feminine of the masculine adjectival noun pattern ^2^[فَعْلَان]{.ar}. For example, [غضب]{.arroot} [غَضْبَىٰ]{.ar} [gaDbA]{.trn} "very angry~f~".

+ The following exceptional nouns:

  + [أُمَّة]{.ar} [Eummah]{.trn} "a nation"
  + [أَمَة]{.ar} [Eamah]{.trn} "a female slave"
  + [شَفَة]{.ar} [cafah]{.trn} "a lip"

  There are a few more such nouns, some of which we will introduce later.

All these exceptional nouns form broken plurals instead of the [At]{.trn} sound plural.

#### Nouns that don't end with a feminine marker

##### Common nouns {-}

Common nouns that don't end with a feminine marker will form the [At]{.trn} plural only if they don't have a broken plural listed in the dictionary. Furthermore, it is preferred if the noun have five or more letters.

+ [حَيَوَان]{.ar} [HayawAn]{.trn} "an animal" forms the [At]{.trn} plural [حَيَوَانَات]{.ar} [HayawAnAt]{.trn} "animals".
+ [حَمَّام]{.ar} [HammAm]{.trn} forms the [At]{.trn} plural [حَمَّامَات]{.ar} [HammAmAt]{.trn} "bathrooms". (The doubled [م]{.ar} counts as two letters.)

##### Masculine adjectival nouns {-}

Masculine adjectival nouns are permitted to form an [At]{.trn} sound plural, but only when they are applied to non-intelligent beings.

For example, if the masculine adjectival noun [صَعْب]{.ar} [Saeb]{.trn} "a difficult one" is applied to "books", which is the plural of the masculine noun [كِتَاب]{.ar} [kitAb]{.trn} "a book", then the masculine adjectival noun [صَعْب]{.ar} [Saeb]{.trn} is permitted to form the [At]{.trn} plural [صَعْبَات]{.ar} [SaebAt]{.trn} "difficult ones".

By the way, note that both the masculine adjectival noun [صَعْب]{.ar} [Saeb]{.trn}, and its feminine [صَعْبَة]{.ar} [Saebah]{.trn} form the same [At]{.trn} sound plural [صَعْبَات]{.ar} [SaebAt]{.trn}.

<!--
## Usage of plural adjectival nouns

We will defer the discussion on how to use plural adjectival nouns until the next chapter, when we will learn broken plurals, if [#allAh]{.trn2} wills.
-->

<!--
## Plurals of adjectival nouns 

Most adjectival-nouns form sound plurals. For now you can assume, unless told otherwise, that any adjectival noun can form an [Un]{.trn} sound plural applicable to male intelligent beings, and an [At]{.trn} sound plural applicable to female intelligent beings and non-intelligent beings.

In later chapters, we will give a more complete list of conditions that need to be satisfied for a noun to form sound plurals.

So the masculine adjectival-noun [طَيِّب]{.ar} "Tayyib" (masc.) "a good one" will form the following plurals:

+ the [Un]{.trn} sound plural [طَيِّبُونَ]{.ar} [TayyibUna]{.trn} applicable to male intelligent beings, and
+ the [At]{.trn} sound plural [طَيِّبَات]{.ar} [TayyibAt]{.trn} applicable to masculine nouns non-intelligent beings.

And the feminine adjectival noun [طَيِّبَة]{.ar}

It is not just designative nouns that have plurals. Many qualitative nouns may be pluralized with sound plurals as well. For example, [طَيِّبٌ]{.ar} [Tayyibun]{.trn} has the [Un]{.trn} sound plural [طَيِّبُونَ]{.ar} [TayyibUna]{.trn} and the [At]{.trn} sound plural [طَيِّبَاتٌ]{.ar} [TayyibAtun]{.trn}. The complete rules of whether a qualitative noun has a sound plural are somwehat complicated. For now, you may use the following rule of thumb:

Only masculine qualitative nouns that form their feminine by the addition of [ة]{.ar} may be pluralized with the [Un]{.trn} sound plural. And all feminine qualitative noun that ends with [ة]{.ar} may be pluralized with the [At]{.trn} sound plural. But there do exist feminine qualitative nouns that don't end with [ة]{.ar} that form the [At]{.trn} sound plural. For example,

+ [كَبِيرٌ]{.ar} [kabIrun]{.trn} "big (masc.)" forms its feminine with the addition of [ة]{.ar}: [كَبِيرَةٌ]{.ar} [kabIratun]{.trn}. Therefore it can be pluralized with the sound [Un]{.trn} sound plural [كَبِيرُونَ]{.ar}. And [كَبيرَةٌ]{.ar} can be pluralized as [كَبِيرَاتٌ]{.ar}.
+ [غَضْبَانُ]{.ar} [gaDbAnu]{.trn} "very angry (masc.)" forms its feminine without [ة]{.ar}: [غَضْبَىٰ]{.ar} [gaDbA]{.trn}. Therefore it will not form the sound [Un]{.trn} sound plural.

In using plurals of qualitative nouns, Arabic distinguishes between intelligent beings and non-intelligent beings. Here we explain the usage of qualitative noun plurals with intelligent beings. We will explain the usage of qualitative noun plurals with non-intelligent beings in the next chapter, if Allah wills.

When a qualitative noun is describing plural intelligent beings, then the qualitative noun will be pluralized. For example,

[ٱَلْمُعَلِّمُونَ طَيِّبُونَ.]{.ar}  
[EalmueallimUna TayyibUna]{.trn}  
"The male teachers are good."

[كَانَتِ ٱلْجَارِيَاتُ ٱلطَّوِيلَاتُ سَرِيعَاتٍ.]{.ar}  
[kAnati -ljAriyAtu -TTawIlAtu sarIeAtin]{.trn}  
"The tall girls were fast."
-->

## Detached plural pronouns

We have already learned the detached pronouns for singular and dual nouns. They are repeated here:

|Participant|Detached pronoun|
|:---|:-|
|Absentee  sing. masc.    |[هُوَ]{.ar} [huwa]{.trn}   "he"      |
|Absentee  sing. fem.     |[هِيَ]{.ar} [hiya]{.trn}   "she"    |
|Absentee  dual           |[هُمَا]{.ar} [humA]{.trn}      "they~2~" |
|Addressee sing. masc.    |[أَنْتَ]{.ar} [Eanta]{.trn} "you~1,m~"|
|Addressee sing. fem.     |[أَنْتِ]{.ar} [Eanti]{.trn} "you~1,f~"|
|Addressee dual           |[أَنْتُمَا]{.ar} [EantumA]{.trn} "you~2~" |
|Speaker   sing.          |[أَنَا]{.ar} [Eana]{.trn}  "I"      |
|Speaker   dual           | -- |

Now we will learn the detached pronouns for the plural participants:

|Participant|Detached pronoun|
|:---|:-|
|Absentee  pl. masc. |[هُمْ]{.ar} [hum]{.trn}        "they~3,m~" |
|Absentee  pl. fem.  |[هُنَّ]{.ar} [hunna]{.trn}      "they~3,f~" |
|Addressee pl. masc. |[أَنْتُمْ]{.ar} [Eantum]{.trn}   "you~3,m~" |
|Addressee pl. fem.  |[أَنْتُنَّ]{.ar} [Eantunna]{.trn} "you~3,f~" |
|Speaker   pl.       |[نَحْنُ]{.ar} [naHnu]{.trn}     "we" |

Note that the plural detached pronoun for the speaker participant 
[نَحْنُ]{.ar} [naHnu]{.trn}     "we"
are the same for both genders.

Also, remember that there is no detached pronoun for the dual speaker-participant. 
So, if the speaker-pariticipant consists of two individuals then we will use the plural pronoun.

Here are some examples of their use:

[هُمْ مُسْلِمُونَ.]{.ar}  
[hum muslimUn.]{.trn}  
"They~3,m~ are men~3~."

[هُنَّ مُعَلِّمَاتٍ.]{.ar}  
[hum mueallimaAt.]{.trn}  
"They~3,f~ are teachers~f~."

[أَنْتُمْ لَاعِبُونَ.]{.ar}  
[Eantum lAeibUn.]{.trn}  
"You~3,m~ are players~3,m~."

[أَنْتُنَّ صَدِيقَاتٍ.]{.ar}  
[Eantunna SadIqAt.]{.trn}  
"You~3,f~ are friends~3,f~."

[نَحْنُ رَجُلَانِ فَقِيرَانِ.]{.ar}  
[naHnu rajulAni faqIrAn.]{.trn}  
"We~2,m~ are poor men~2~." (Note the plural pronoun subject with a dual noun in the information.)

[نَحْنُ مُسْلِمَاتٍ.]{.ar}  
[naHnu muslimAt.]{.trn}  
"We~3,f~ are Muslims~3,f~."

## Attached plural pronouns

We have also already learned the attached pronouns for the singular and dual participants. They too are repeated here:

|Participant | Attached pronoun|
|:------|:--|
|Absentee   sing. masc.    | [هُ]{.ar} [-hu]{.trn}   "him"       |
|Absentee   sing. fem.     | [هَا]{.ar} [-hA]{.trn}  "her"       |
|Absentee   dual           | [هُمَا]{.ar} [-humA]{.trn}  "them~2~"|
|Addressee  sing. masc.    | [كَ]{.ar} [-ka]{.trn}   "you~m,1~"  |
|Addressee  sing. fem.     | [كِ]{.ar} [-ki]{.trn}   "you~f,1~"  |
|Addressee  dual           | [كُمَا]{.ar} [-kumA]{.trn}  "you~2~" |
|Speaker    sing.          | [ي]{.ar}               "me"        |
|Speaker    dual | -- |

Now we will learn the attached pronouns for the plural participant:

|Participant | Attached pronoun|
|:------|:--|
|Absentee   pl. masc.    | [هُمْ]{.ar} [-hum]{.trn}   "them~3,m~  |
|Absentee   pl. fem.     | [هُنَّ]{.ar} [-hunna]{.trn} "them~3,f~  |
|Addressee  pl. masc.    | [كُمْ]{.ar} [-kum]{.trn}   "you~3,m~"  |
|Addressee  pl. fem.     | [كُنَّ]{.ar} [-kunna]{.trn} "you~3,f~"  |
|Speaker    pl           | [نَا]{.ar} [-nA]{.trn}    "us"        |

Note the following points about them:

+ The plural absentee-participant detached and attached pronouns ("they~3,m~"/"them~3,m~") are the same:
  + masculine: [هُمْ]{.ar} [-hum]{.trn}.
  + feminine: [هُنَّ]{.ar} [-hunna]{.trn}.
+ Just like [هُ]{.ar} [hu]{.trn} "him" and [هُمَا]{.ar} [-humA]{.trn} "them~2~", the plural absentee-participant attached pronouns
[هُمْ]{.ar} [-hum]{.trn}   "them~3,m~" and
[هُنَّ]{.ar} [-hunna]{.trn} "them~3,f~"
become [هِمَا]{.ar} [-himA]{.trn} and [هِنَّ]{.ar} [-hinna]{.trn} respectively, when preceded by the vowels [◌ِ]{.ar} [-i]{.trn}, [◌ِي]{.ar} [-I]{.trn}, or the semi-vowel [◌َيْ]{.ar} [-ay]{.trn}. Examples:
   + [بِهِمْ]{.ar} [bihimA]{.trn} "with them~3,m~"
   + [فِيهِنَّ]{.ar} [fIhinna]{.trn} "in them~3,f~"
   + [إِلَيْهِمْ]{.ar} [Eilayhim]{.trn} "to them~3,m~"
+ The final [0]{.txt}-mark on the [مْ]{.ar} in the masculine plural pronouns ([هُمْ]{.ar} [hum]{.trn}, [أَنْتُمْ]{.ar} [Eantum]{.trn}, and [كُمْ]{.ar} [-kum]{.trn}) becomes a [u]{.trn}-mark ([هُمُ]{.ar} [humu]{.trn}, [أَنْتُمُ]{.ar} [Eantumu]{.trn},  and[كُمُ]{.ar} [-kumu]{.trn} respectively) when followed by a connecting [hamzah]{.trn2}. Examples:
  + [هُمُ ٱلْمُعَلِّمُونَ.]{.ar}  
    [humu -lmueallimUn.]{.trn}  
    "They~pl.\ masc.~ are the (male) teachers."
  + [ذَهَبَ إِلَيْكُمُ ٱلرَّجُلُ.]{.ar}  
    [pahaba Eilaykumu -rrajul.]{.trn}  
    "The man went to you~3,m~."
  + [أَنْتُمُ ٱلْمُسْلِمُونَ.]{.ar}  
    [Eantumu -lmuslimUn.]{.trn}
    "You~3,m~ are the Muslims~3,m~."
+ When the speaker plural attached pronoun [نَا]{.ar} is attached to a word that ends with a [نْ]{.ar} with a [0]{.txt}-mark, there is only one [ن]{.ar} written and it is doubled with a doubling mark [◌ّ]{.ar} on it. So we get:
   + [نَا]{.ar} + [مِنْ]{.ar} = [مِنَّا]{.ar} [minnA]{.trn}
   + [نَا]{.ar} + [عَنْ]{.ar} = [عَنَّا]{.ar} [eannA]{.trn}
   + [نَا]{.ar} + [لَدُنْ]{.ar} = [لَدُنَّا]{.ar} [ladunnA]{.trn}
+ The preposition [لِ]{.ar} [li]{.trn} "for" becomes [لَ]{.ar} [la]{.trn} when followed by the plural attached pronouns:
   + [لَهُمْ]{.ar} [lahum]{.trn} "for them~3,m~"
   + [لَهُنَّ]{.ar} [lahunna]{.trn} "for them~3,f~"
   + [لَكُمْ]{.ar} [lakum]{.trn} "for you~3,m~"
   + [لَكُنَّ]{.ar} [lakunna]{.trn} "for you~3,f~"
   + [لَنَا]{.ar} [lanA]{.trn} "for us"

### Plural doee pronouns

The plural attached pronouns that we have just learned are also used as doee pronouns. 
<!--Again, there is no additional intervening [ن]{.ar} for the speaking participant dual attached pronoun [نَا]{.ar} [-nA]{.trn}. -->
Examples:

[سَأَلَهُمُ ٱلرَّجُلُ.]{.ar}  
[saEalahumu -rrajul.]{.trn}  
"The man asked them~3,m~."

[سَأَلْتُكُمْ.]{.ar}  
[saEaltukum]{.trn}  
"I asked you~3,m~."

[سَأَلَتْكُنَّ.]{.ar}  
[saEalatkunn.]{.trn}  
"She asked you~3,f~."

[سَأَلَانَا.]{.ar}  
[saEalAnA.]{.trn}  
"They~2,m~ asked us."

[سَأَلَتَاهُ.]{.ar}  
[saEalatAh.]{.trn}  
"They~3,m~ asked him."

## Verbs with plural doers

### Plural nouns for the doer

We learned that the completed-action verb for a masculine doer is on the pattern [فَعَلَ]{.ar}. And when the doer is feminine, the [ت]{.ar} of femininity is attached to the verb thus: [فَعَلَتْ]{.ar}. We have used these verbs with singular and dual doer nouns. The doer noun always comes after the verb and shall be in the u-state. Examples:

[ذَهَبَ ٱلْغُلَامُ.]{.ar}  
[pahaba -lgulAmu.]{.trn}  
"The boy went." 

[ذَهَبَتْ جَارِيَةٌ.]{.ar}  
[pahabat jAriyatun]{.trn}  
"A girl went." 

[ذَهَبَ ٱلْغُلَامَانِ.]{.ar}  
[pahaba -lgulAmAni.]{.trn}  
"The boys~2~ went." 

[ذَهَبَتْ جَارِيَتَانِ.]{.ar}  
[pahabat jAriyatAni.]{.trn}  
"Two girls went." 

These same verbs are used when the doer noun is a plural. Examples:

[ذَهَبَ ٱلْمُعَلِّمُونَ.]{.ar}  
[pahaba -lmueallimUn.]{.trn}  
"The teacherm~3,m~ went." 

[ذَهَبَتْ مُعَلِّمَاتٌ.]{.ar}  
[pahabat mueallimAt.]{.trn}  
"Teachers~3,f~ went." 

### Plural pronouns for the doer

We have already learned the singular and dual doer pronouns. They are repeated here:

|Participant | Doer pronoun |Meaning| Doer pronoun with verb|
|:--|:--|:--|:--|
|Absentee  sing. masc.   | invisible            |"he"      | [فَعَلَ]{.ar} [faeala]{.trn}|
|Absentee  sing. fem.    | invisible            |"she"     | [فَعَلَتْ]{.ar} [faealat]{.trn}|
|Absentee  dual          | [◌َا]{.ar} [-A]{.trn}     | "them~2~" | masc.: [فَعَلَا]{.ar} [faealA]{.trn}, fem: [فَعَلَتَا]{.ar} [faealatA]{.trn}|
|Addressee sing. masc.   | [تَ]{.ar} [-ta]{.trn} |"you~m,2~"| [فَعَلْتَ]{.ar} [faealta]{.trn}|
|Addressee sing. fem.    | [تِ]{.ar} [-ti]{.trn} |"you~f,2~"| [فَعَلْتِ]{.ar} [faealti]{.trn}|
|Addressee dual          | [تُمَا]{.ar} [-tumA]{.trn} | "you~2~"  | [فَعَلْتُمَا]{.ar} [faealtumA]{.trn} |
|Speaker   sing.         | [تُ]{.ar} [-tu]{.trn} |"I"       | [فَعَلْتُ]{.ar} [faealtu]{.trn}|
|Speaker   dual          | -- | "us~2~" | --|

Now we will learn the plural doer pronouns:

|plural participant | Doer pronoun | Meaning |Doer pronoun with verb|
|:--|:--|:--|:---|
|Absentee  pl. masc.   | [و]{.ar}                 |"they~3,m~" | [فَعَلُوا]{.ar} [faealU]{.trn}|
|Absentee  pl. fem.    | [نَ]{.ar} [-na]{.trn}     |"they~3,f~" | [فَعَلْنَ]{.ar}  [faealna]{.trn}|
|Addressee pl. masc.   | [تُمْ]{.ar} [-tum]{.trn}   |"you~m,3~"  | [فَعَلْتُمْ]{.ar} [faealtum]{.trn}|
|Addressee pl. fem.    | [تُنَّ]{.ar} [-tunna]{.trn} |"you~f,3~"  | [فَعَلْتُنَّ]{.ar} [faealtunna]{.trn}|
|Speaker   pl.         | [نَا]{.ar} [-nA]{.trn}    |"we"        | [فَعَلْنَا]{.ar} [faealnA]{.trn}|

Note the following regarding the plural doer pronouns:

+ The [تْ]{.ar} of femininity does not attach to the absentee  plural feminine doer pronoun [نَ]{.ar} [-na]{.trn} "they~3,f~" [فَعَلْنَ]{.ar}. Example:
  
  + [ذَهَبْنَ]{.ar} [pahabna]{.trn} "they~3,f~ went"

  This is different from the behavior of the absentee dual doer pronoun [◌َا]{.ar} [-A]{.trn} "them~2,f~" which, for a feminine doer, does attach to the [تْ]{.ar} of femininity. Example:

  + [ذَهَبَتَا]{.ar} [pahabatA]{.trn} "they~2,f~ went"
+ The final [0]{.txt}-mark on the [مْ]{.ar} in the masculine plural doer pronoun [تُمْ]{.ar} [-tum]{.trn} becomes a [u]{.trn}-mark [تُمُ]{.ar} [-tumu]{.trn} when followed by a connecting [hamzah]{.trn2}. Examples:
  + [أَكَلْتُمْ خُبْزًا.]{.ar}  
    [Eakaltum xubzA.]{.trn}  
    "You~3,m~ ate some bread."
  + [أَكَلْتُمُ ٱلْخُبْزَ.]{.ar}  
    [Eakaltumu -lxubz.]{.trn}  
    "You~3,m~ ate the bread."
+ The absentee plural masculine verb doer pronoun "they~3,m~" [و]{.ar} [U]{.trn} is written with a silent [Ealif]{.trn2} after it which is written only and not pronounced. This [Ealif]{.trn2} is dropped when a doee pronoun is attached. For example: 
  + [ضَرَبُوا ٱلرَّجُلَ.]{.ar}  
    [Darabu -rrajul.]{.trn}  
    "They~3,m~ hit the man.
  + [ضَرَبُوهُ.]{.ar}  
    [DarabUh.]{.trn}  
    "They~3,m~ hit him."
+ The plural masculine verb doer pronoun for the addressed person "you~3,m~" [تُمْ]{.ar} [-tum]{.trn} becomes [تُمُو]{.ar} [tumU]{.trn} when a doee pronoun is attached. For example:
  + [ضَرَبْتُمُ ٱلرَّجُلَ.]{.ar}  
    [Darabtumu -rrajul.]{.trn}  
    "You~3,m~ hit the man."
  + [ضَرَبْتُمُوهُ.]{.ar}  
    [DarabtumUh.]{.trn}  
    "You~pl.\ masc.~ hit him."
+ The plural speaking participant doer pronoun [نَا]{.ar} [-nA]{.trn} is the same as the plural speaking participant attached pronoun [نَا]{.ar} [-nA]{.trn}. But you can tell them apart because the doer pronoun, when attached to the verb, causes the final letter of the verb to have a [0]{.txt}-mark. Consider the following two sentences:

  [سَأَلْنَا.]{.ar}  
  [saEalnA.]{.trn}  
  "We asked."

  [سَأَلَنَا.]{.ar}  
  [saEalanA.]{.trn}  
  "He asked us."

<!--
[سَأَلْتُمَانَا]{.ar}  
[saEaltumAnA]{.trn}  
"You~2~ asked us"

[سَأَلَتَاكُمَا]{.ar}  
[saEalatAkumA]{.trn}  
"They~f,2~ asked you~2~"

[سَأَلَاهُمَا]{.ar}  
[saEalAhumA]{.trn}  
"They~m,2~ asked them~2~"
-->

### Sentence word order with plural doers

As we've mentioned, the doer, whether a noun or a pronoun, always comes after the verb. Here are a couple of examples of verbal sentences with plural doers:

[ذَهَبَ ٱلْمُعَلِّمُونَ إِلَىٰ مَدْرَسَةٍ.]{.ar}  
[pahaba -lmueallimUna EilA madrasah.]{.trn}  
"The teachers~3,m~ went to a school."

[ذَهَبُوا إِلَىٰ مَدْرَسَةٍ.]{.ar}  
[pahabA EilA madrasah.]{.trn}  
"They~3,m~ went to a school."

[لَعِبَتِ ٱلصَّدِيقَاتُ فِي ٱلْبَيْتِ.]{.ar}  
[laeibati -SSadIqAtu fi -lbayt.]{.trn}  
"The friends~3,f~ played in the house."

[لَعِبْنَ فِي ٱلْبَيْتِ.]{.ar}  
[laeibna fi -lbayt.]{.trn}  
"They~3,f~ played in the house."

The above verbal sentences with plural doers can be rearranged to be a subject-information sentences. This gives more emphasis to the subject. In this case, the verb shall follow the subject and will need a doer pronoun after it.

[ٱَلْمُعَلِّمُونَ ذَهَبُوا إِلَىٰ مَدْرَسَةٍ.]{.ar}  
[EalmueallimUna pahabU EilA madrasah.]{.trn}  
"The teachers~3,m~, they~3,m~ went to a school."
= "_The teachers~3,m~_ went to a school."

[ٱلصَّدِيقَاتُ لَعِبْنَ فِي ٱلْبَيْتِ.]{.ar}  
[EaSSadIqAtu laeibna fi -lbayt.]{.trn}  
"The friends~3,f~, they~3,f~ played in the house."
= "_The friends~3,f~_ played in the house."

If there are multiple verbs associated with the same doer in a verbal sentence, the doer noun will follow the first verb and the rest of the verbs will have doer pronouns. For example:

[أَكَلَ ٱللَّاعِبُونَ وَشَرِبُوا وَذَهَبُوا.]{.ar}  
[Eakala -llAeibUna wacaribU wapahabU.]{.trn}  
"The players~3,m~ ate and they~3,m~ drank and they~3,m~ went."  
= "The players~3,m~ ate and drank and went."

The above verbal sentence can be rearranged to be a subject-information sentence. In that case, all the verbs shall have doer pronouns. The sentence will have the same translation as above, except for an emphasis on the subject of the sentence.

[ٱَللَّاعِبُونَ أَكَلُوا وَشَرِبُوا وَذَهَبُوا.]{.ar}  
[EallAeibUna EakalU wacaribU wapahabU.]{.trn}  
"The players~3,m~, they~3,m~ ate and they~3,m~ drank and they~3,m~ went."  
= "_The players~3,m~_ ate and drank and went."

Similarly,

[أَكَلَتِ ٱللَّاعِبَاتُ وَشَرِبْنَ وَذَهَبْنَ.]{.ar}  
[Eakalati -llAeibAtu wacaribna wapahabn.]{.trn}  
"The players~3,f~ ate and they~3,f~ drank and they~3,f~ went."  

and

[ٱَللَّاعِبَاتُ أَكَلْنَ وَشَرِبْنَ وَذَهَبْنَ.]{.ar}  
[EallAeibAtu Eakalna wacaribna wapahabn.]{.trn}  
"The players~3,f~, they~3,f~ ate and they~3,f~ drank and they~3,f~ went."  
= "_The players~3,f~_ ate and drank and went."

<!--
## Pronouns for the plural

Here are the detached, attached, and doer pronouns for the plural:

|Person|Detached pronoun|Completed-action verb doer pronoun|Completed-action verb with doer pronoun|Attached pronoun|
|:---|:----|:----|:----|
| they/them~pl.\ masc.~ |[هُمْ]{.ar} [hum]{.trn}        | [◌ُو]{.ar} [-U]{.trn}     |[فَعَلُوا]{.ar} [faealU]{.trn}     |[هُمْ]{.ar} [-hum]{.trn}|
| they/them~pl.\ fem.~  |[هُنَّ]{.ar} [hunna]{.trn}      | [نَ]{.ar} [-na]{.trn}     |[فَعَلْنَ]{.ar} [faealna]{.trn}     |[هُنَّ]{.ar} [-hunna]{.trn}|
| you~pl.\ masc.~       |[أَنْتُمْ]{.ar} [Eantum]{.trn}   | [تُمْ]{.ar} [-tum]{.trn}   |[فَعَلْتُمْ]{.ar} [faealtum]{.trn}   |[كُمْ]{.ar} [-kum]{.trn}|
| you~pl.\ fem.~        |[أَنْتُنَّ]{.ar} [Eantunna]{.trn} | [تُنَّ]{.ar}  [-tunna]{.trn}|[فَعَلْتُنَّ]{.ar} [faealtunna]{.trn} |[كُنَّ]{.ar} [-kunna]{.trn}|
| we/us~pl.\ masc.\ and fem.~ |[نَحْنُ]{.ar} [naHnu]{.trn}     | [نَا]{.ar} [-nA]{.trn}    |[فَعَلْنَا]{.ar} [faealnA]{.trn}    |[نَا]{.ar} [-nA]{.trn}|


Here are some rules for the plural pronouns:

+ The plural attached and detached pronouns for the absent person "they/them~pl.\ masc.~" are pronounced the same: [هُمْ]{.ar} [hum]{.trn}.
+ Similar to the singular and dual,the pronouns for the speaking person (we, us) do not differentiate between the masculine and feminine genders plural either.
+ The speaking person pronouns are the same for the dual and plural: [نَحْنُ]{.ar} [naHnu]{.trn} and [نَا]{.ar} [-nA]{.trn}.
+ Similar to [هُ]{.ar} [-hu]{.trn}, [هُمَا]{.ar} [-humA]{.trn}, the [u]{.trn}-mark on the plural attached pronoun [هُمْ]{.ar} [-hum]{.trn} becomes an [i]{.trn}-mark ([هِمْ]{.ar} [-him]{.trn}) when it is preceded by the vowels [◌ِ]{.ar} [i]{.trn}, [ـِي]{.ar} [I]{.trn}, or the semi-vowel [ـَيْ]{.ar} [ay]{.trn}. Examples: 
  + [عَلَيْهِ]{.ar}, [ealayhi]{.trn} "on him"
  + [فِيهِمْ]{.ar} [fIhim]{.trn} "in them~pl.~"
  + [بِهِمْ]{.ar} [bihim]{.trn} "with them~pl.~".
+ The final [0]{.txt}-mark on the [مْ]{.ar} in the masculine plural pronouns ([هُمْ]{.ar} [hum]{.trn}, [هُمْ]{.ar} [-hum]{.trn}, [أَنْتُمْ]{.ar} [Eantum]{.trn}, [تُمْ]{.ar} [-tum]{.trn}, [كُمْ]{.ar} [-kum]{.trn}) becomes a [u]{.trn}-mark ([هُمُ]{.ar} [humu]{.trn}, [هُمُ]{.ar} [-humu]{.trn}, [أَنْتُمُ]{.ar} [Eantumu]{.trn}, [تُمُ]{.ar} [-tumu]{.trn}, [كُمُ]{.ar} [-kumu]{.trn} respectively) when followed by a connecting [hamzah]{.trn2}. Examples:
  + [هُمُ ٱلْمُعَلِّمُونَ.]{.ar}  
    [humu -lmueallimUna.]{.trn}  
    "They~pl.\ masc.~ are the (male) teachers."
+ The plural masculine verb doer pronoun for the absent person "they~pl.\ masc.~" [ـُوا]{.ar} [U]{.trn} has a silent [Ealif]{.trn2} which is written only and not pronounced. This [Ealif]{.trn2} is dropped when a doee pronoun is attached. For example: 
  + [ضَرَبُوا ٱلرَّجُلَ.]{.ar}  
    [Darabu -rrajula.]{.trn}  
    "They hit the man.
  + [ضَرَبُوهُ.]{.ar}  
    [DarabUhu.]{.trn}  
    "They~pl.\ masc.~ hit him."
+ The plural masculine verb doer pronoun for the addressed person "you~pl.\ masc.~" [تُمْ]{.ar} [-tum]{.trn} becomes [تُمُو]{.ar} [tumU]{.trn} when a doee pronoun is attached. For example:
  + [ضَرَبْتُمُ ٱلرَّجُلَ.]{.ar}  
    [Darabtumu -rrajula.]{.trn}  
    "You~pl.\ masc.~ hit the man."
  + [ضَرَبْتُمُوهُ.]{.ar}  
    [DarabtumUhu.]{.trn}  
    "You~pl.\ masc.~ hit him."
+ The [ن]{.ar} in the speaking participant attached pronoun "us" [نَا]{.ar} [-nA]{.trn} is part of the pronoun and is not an intervening [ن]{.ar} as was the case for the singular speaking participant pronouns. So we get:
   + [عَلَيْنَا]{.ar} [ealaynA]{.trn} "on us"
   + [بِنَا]{.ar} [binA]{.trn} "with us"

  However, when attached to a word that ends with a [نْ]{.ar} with a [0]{.txt}-mark, there is only one [ن]{.ar} written and it is doubled with a doubling mark [◌ّ]{.ar} on it. So we get:
   + [نَا]{.ar} + [مِنْ]{.ar} = [مِنَّا]{.ar} [minnA]{.trn}
   + [نَا]{.ar} + [عَنْ]{.ar} = [عَنَّا]{.ar} [eannA]{.trn}
   + [نَا]{.ar} + [لَدُنْ]{.ar} = [لَدُنَّا]{.ar} [ladunnA]{.trn}
+ The preposition [لِ]{.ar} [li]{.trn} "for" becomes [لَ]{.ar} [la]{.trn} when followed by the plural attached pronouns:
   + [لَهُمْ]{.ar} [lahum]{.trn} "for them~3+~"
   + [لَكُمْ]{.ar} [lakum]{.trn} "for you~3+~"
   + [لَنَا]{.ar} [lanA]{.trn} "for us"
+ The plural speaking participant doer pronoun [نَا]{.ar} [-nA]{.trn} is the same as the plural speaking participant attached pronoun [نَا]{.ar} [-nA]{.trn}. But you can tell them apart because the doer pronoun, when attached to the verb, causes the final letter of the verb to have a [0]{.txt}-mark. Consider the following two sentences:

  [سَأَلْنَا.]{.ar}  
  [saEalnA.]{.trn}  
  "We asked."

  [سَأَلَنَا.]{.ar}  
  [saEalanA.]{.trn}  
  "He asked us."


## Verbs with plural intelligent doers

Remember that in Arabic, a doer, whether a noun or a pronoun, always after a verb. 

[ذَهَبُوا إِلَىٰ بَيْتٍ.]{.ar}  
[pahabU EilA baytin.]{.trn}  
"They~pl.\ masc.~ went to a house."

When the doer is a plural noun then the plural doer pronoun is not employed.

[ذَهَبَ ٱلْمُعَلِّمُونَ إِلَىٰ بَيْتٍ.]{.ar}  
[pahabA -lmueallimUna EilA baytin.]{.trn}  
"The teachers went to a house."

The above verbal sentence can be rearranged to be a subject-information sentence. This gives more emphasis to the subject. In this case, the verb shall follow the subject and will need a doer pronoun after it.

[ٱَلْمُعَلِّمُونَ ذَهَبُوا إِلَىٰ بَيْتٍ.]{.ar}  
[EalmueallimUna pahabU EilA baytin.]{.trn}  
"The teachers, they~pl.\ masc.~ went to a house."

If there are multiple verbs associated with the same doer in a verbal sentence, the doer noun will follow the first verb  and the rest of the verbs will have doer pronouns. For example:

[أَكَلَ ٱلْمُعَلِّمُونَ  وَشَرِبُوا وَذَهَبُوا.]{.ar}  
[Eakala -rrajulAni wacaribU wapahabU.]{.trn}  
"The two men ate and they~pl.\ masc.~ drank and they~pl.\ masc.~ went."  
= "The two men ate and drank and went."

The above verbal sentence can be rearranged to be a subject-information sentence. In that case, all the verbs shall have doer pronouns. The sentence will have the same translation as above, except for an emphasis on the subject of the sentence.

[ٱَلْمُعَلِّمُونَ أَكَلُوا وَشَرِبُوا وَذَهَبُوا.]{.ar}  
[EalmueallimUna EakalU wacaribU wapahabU.]{.trn}  
"The two men, they~pl.\ masc.~ ate and they~pl.\ masc.~ drank and they~pl.\ masc.~ went."  
= "_The two men_ ate and drank and went."
-->

### Verbs with multiple doers mentioned individually

If there are multiple doers of a verb, and each is mentioned individually, then there is often more than one way to handle them. Here we will give the more common usage.

If the verb is followed by multiple doers, only the first is the true doer with respect to  modifying the verb according to its gender and number. Examples:

[ذَهَبَتِ ٱلْأُمُّ وَٱلْغُلَامُ.]{.ar}  
[pahabati -lEummu wa-lgulAmu.]{.trn}  
"The mother and the boy went."

[ذَهَبَ ٱلْغُلَامُ وَٱلْأُمُّ .]{.ar}  
[pahaba -lgulAmu wa -lEummu.]{.trn}  
"The boy and the mother went."

If the doers consist of different persons (speaking person, addressed person, and absent person), then they are placed in order of strength: The speaking person is stronger than the addressed person, who is stronger than the absent person. The verb doer pronoun of the first (true) doer is then used. Example:
  
[ذَهَبْتُ أَنَا وَأَنْتَ وَهُوَ.]{.ar}  
[pahabtu Eana waEanta wahuwa.]{.trn}  
"I, you, and he went."

Note how the speaking person detached pronoun [أَنَا]{.ar} [Eana]{.trn} is used in addition to the doer pronoun [تُ]{.ar} [-tu]{.trn} in order to add [وَ]{.ar} [wa]{.trn} "and" to it.

If the sentence is a subject information sentence, and the verb is in the information, then the doer pronoun corresponding to the number of the subject is used. Examples:

[أنْتَ وَهُوَ ذَهَبْتُمَا.]{.ar}  
[Eanta wahuwa pahabtumA.]{.trn}  
"You~1,m~ and he, you~2~ went."

[أَنَا وَمُحَمَّدٌ ذَهَبْنَا.]{.ar}  
[Eana wamuHammadun pahabnA.]{.trn}  
"I and [#muHammad]{.trn2}, we went."

<!--If the verb follows the doers, then it will have the doer pronoun corresponding to number of the doers. Example:-->

[ٱلْأُمُّ وَٱلْجَارِيَةُ ذَهَبَتَا.]{.ar}  
[EalEummu wa-ljAriyatu pahabatA.]{.trn}  
"The mother and the girl went."

[ٱلْأُمُّ وَٱلْجَارِيَتَانِ ذَهَبْنَ.]{.ar}  
[EalEummu wa-ljAriyatAni pahabna.]{.trn}  
"The mother and the two girls, they~3,f~ went."

If the doers consist of both male and female persons, then the verb will have the masculine doer prenoun corresponding to the number of the doers. Example:

[ٱلْأُمُّ وَٱلْجَارِيَةُ وَٱلْغُلَامُ ذَهَبُوا.]{.ar}  
[EalEummu wa-ljAriyatu wa-lgulAmu pahabU.]{.trn}  
"The mother, the girl, and the boy, they~3,m~ went."
<!-- Al-Nahw Al Wafy vol. i. p. 268, point 9 -->


<!--chapter:end:srcrmd/sound_plurals.Rmd-->

# Broken plurals

## Introduction

In the previous chapter we introduced sound plurals, which are formed by appending suffixes to the singular noun. The singular noun in these plurals remains, more or less, intact when forming these plurals. The sound plurals correspond to English regular plurals which are formed by appending "s" to the singular noun. However, English has some plurals that are not formed by adding the plural ending "s". Here are some examples,

| Singular | Plural |
|:-----------|:-----------|
| man        | men        |
| woman      | women      |
| child      | children   |
| mouse      | mice       |

In these plurals, the singular noun is altered to form the plural.

Arabic also forms such plurals. They are called _broken_ plurals because the singular noun is not kept intact but its structure is, in most cases, altered, or "broken-up" when forming the plural.

While English only forms such plurals for a handful of nouns, Arabic forms broken plurals for many nouns.

## Review of word patterns and semi-flexible nouns

Before we begin our discussion about broken plurals, we will do a quick review of word patterns and semi-flexible nouns. This will, if [#allAh]{.trn2} wills, facilitate the explanation of broken plurals.

Most words in Arabic are formed from three letter roots. We use the paradigm root [فعل]{.arroot} to show word patterns. For example, the noun [رَجُل]{.ar} [rajul]{.trn} "a man" is formed from the root [رجل]{.arroot} on the pattern [فَعُل]{.ar} [faeul]{.trn}.

Most nouns in Arabic are _fully-flexible_. This means that, when indefinite, they take [n]{.trn}-marks and the i-state is shown by an [in]{.trn}-mark [◌ٍ]{.ar} at the end of the noun. For example, [رَجُل]{.ar} [rajul]{.trn} "a man" and [بَيْت]{.ar} [bayt]{.trn} "a house" are fully-flexible nouns. So, you can see, below, that they take [n]{.trn}-marks, and the indefinite i-state is indicated by an [in]{.trn}-mark [◌ٍ]{.ar}:

[ذَهَبَ رَجُلٌ إِلَىٰ بَيْتٍ.]{.ar}  
[pahaba rajulun EilA bayt.]{.trn}  
"A man went to a house."

Some nouns are _semi-flexible_. This means that they don't take [n]{.trn} marks, and also, the indefinite i-state is indicated by an [a]{.trn} mark [◌َ]{.ar}. Examples of such nouns are:

+ ^2^[غَضْبَىٰ]{.ar} [gaDbA]{.trn}^2^ _adj._ (fem.) "a very angry one~f~" from the root [غضب]{.arroot}
+ ^2^[صَحْرَاء]{.ar} [SaHrAE]{.trn}^2^ (fem.) "a desert~f~" from the root [صحر]{.arroot}

[ذَهَبَتْ جَارِيَةٌ غَضْبَىٰ إِلَىٰ صَحْرَاءَ.]{.ar}  
[pahabat jAriyatun gaDbA EilA SaHrAE.]{.trn}  
"A very angry girl went to a desert."

When definite, semi-flexible nouns are identical to fully-flexible nouns:

[ذَهَبَتِ ٱلْجَارِيَةُ ٱلْغَضْبَىٰ إِلَى ٱلصَّحْرَاءِ.]{.ar}  
[pahabati -ljAriyatu -lgaDbA Eila -SSaHrAE.]{.trn}  
"The very angry girl went to the desert."

All nouns that have the endings [اء]{.ar} and [ىٰ]{.ar}, that are extrinsic to the word's root, are semi-flexible.
[اء]{.ar} and [ىٰ]{.ar} are also feminine markers for singular nouns, just like [ة]{.ar}. (Except that [ة]{.ar} does not, in general, make a noun semi-flexible.) 

It is important to note that [ة]{.ar}, [اء]{.ar}, and [ىٰ]{.ar} are only feminine markers for singular nouns. We will see that they are also endings for broken plural nouns and, in that case, they are not feminine markers. However, 
[اء]{.ar} and [ىٰ]{.ar}, when endings for broken plural nouns, will make the broken plural nouns semi-flexible, just as they do for singular nouns.

Nouns that are of the patterns [فَفَافِف]{.ar} and [فَفَافِيف]{.ar} are also semi-flexible nouns. Here each letter [ف]{.ar} could be any letter of the alphabet. 
These are patterns for broken plurals, as we will see very soon. 
We had mentioned this in section\ \@ref(fafafif-diptote).

This concludes our short review of word patterns and semi-flexible nouns. We will use these concepts in our discussion of broken plurals.

## Patterns of the broken plural

Broken plurals occur in specific patterns, which we will show using the paradigm [فعل]{.arroot} for three-letter roots. Ararbic also has (comparatively fewer) four-letter roots and we will show patterns for broken plurals of four-letter roots using the paradigm root [فعلل]{.ar}. We will also use the letter [ف]{.ar}, when needed, to indicate any letter of the alphabet.

We now give all but the rarest broken plural patterns below. The singular and plural and given together separated by a colon character ":", the singular on the right, and its plural on the left.

1.  **[فُعَل]{.ar} [fueal]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[صُورَة: صُوَر]{.ar}  |a picture|[دَوْلَة: دُوَل]{.ar} |a dynasty/state
    |[أُمَّة: أُمَم]{.ar}   |a nation |[رُكْبَة: رُكَب]{.ar} |a knee

2.  **[فُعْل]{.ar} [fuel]{.trn}**. Examples:

    ||
    |---:|:-|---:|:-
    |[أَحْمَر^2^، حَمْرَاء^2^: حُمْر]{.ar}  |red    |[أَعْمَىٰ^2^، عَمْيَاء^2^: عُمْي]{.ar}  |blind
    |[أَحْوَر^2^، حَوْرَاء^2^: حُور]{.ar}  |a beautiful eyed one |[أَصَمّ^2^، صَمّاء^2^: صُمّ]{.ar}     |deaf
    |[أَسْوَد^2^، سَوْدَاء^2^: سُود]{.ar}  |black  |[أَبْكَم^2^، بَكْمَاء^2^: بُكْم]{.ar}  |mute
    |[أَبْيَض^2^، بَيْضَاء^2^: بِيض]{.ar}  |white  |[نَاقَة: نُوق]{.ar}               |a camel~f~

3.  **[فُعُل]{.ar} [fueul]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[كِتَاب: كُتُب]{.ar}  |a book|[رَسُول: رُسُل]{.ar}  |a messenger
    |[جِدَار: جُدُر]{.ar}  |a wall|[سَفِينَة: سُفُن]{.ar} |a ship
 
4.  **[فِعَل]{.ar} [fieal]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[قِطْعَة: قِطَع]{.ar}  |a piece|[سِيرَة: سِيَر]{.ar}  |a course of life
    |[هِرَّة: هِرَر]{.ar}   |a cat~f~||

5.  **[فِعَال]{.ar} [fieAl]{.trn}**. Examples:

    ||
    |---:|:---|---:|:-----
    |[رَجُل: رِجَال]{.ar}     |a man             |[حَسَن: حِسَان]{.ar}     |_adj._ a good one~m~
    |[ٱِمْرَأَة: نِسَاء]{.ar}   |a woman           |[حَسَنَة: حِسَان]{.ar}    |_adj._ a good one~f~
    |[أُنْثَىٰ^2^: إِنَاث]{.ar} |a female          |[صَعْب: صِعَاب]{.ar}     |_adj._ a difficult one~m~
    |[عَبْد: عِبَاد]{.ar}     |a slave~m~        |[صَعْبَة: صِعَاب]{.ar}    |_adj._ a difficult one~f~
    |[أَمَة: إِمَاء]{.ar}     |a slave~f~        |[صَغِير: صِغَار]{.ar}    |_adj._ a small one~m~
    |[جَبَل: جِبَال]{.ar}     |a mountain        |[صَغِيرَة: صِغَار]{.ar}   |_adj._ a small one~f~
    |[ثَوب: ثِيَاب]{.ar}     |a garment         |[كَبِير: كِبَار]{.ar}    |_adj._ a big one~m~
    |[رِيح: رِيَاح]{.ar}     |a wind            |[كَبِيرَة: كِبَار]{.ar}   |_adj._ a big one~f~
    |[مَرَّة: مِرَار]{.ar}     |an occasion       |[ضَعِيف: ضِعَاف]{.ar}    |_adj._ a weak one~m~
    |[بَحْر: بِحَار]{.ar}     |a sea             |[ضَعِيفَة: ضِعَاف]{.ar}   |_adj._ a weak one~f~
    |[عَمُود: عِمَاد]{.ar}    |a pillar          |[كِرَام: كَرِيم]{.ar}    |_adj._ a generous one~m~
    |[رَوْضَة: رِيَاض]{.ar}    |a garden          |[غَضْبَان^2^: غِضَاب]{.ar}|_adj._ a very angry~m~
    |[رُمْح: رِمَاح]{.ar}     |a spear           |[غَضْبَىٰ^2^: غِضَاب]{.ar} |_adj._ a very angry~f~

6.  **[فُعُول]{.ar} [fueUl]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[أَمْر: أُمُور]{.ar} |a matter         |[جَيْش: جُيُوش]{.ar} |an army
    |[بَيْت: بُيُوت]{.ar} |a house          |[قَلْب: قُلُوب]{.ar} |a heart
    |[حَقّ: حُقُوق]{.ar}  |a truth, a right |[رَأْس: رُؤُوس]{.ar} |a head
    |[مَلِك: مُلُوك]{.ar} |a king           |[شَهْر: شُهُور]{.ar} |a month
    |[سَيْف: سُيُوف]{.ar} |a sword          |[نَفْس: نُفُوس]{.ar} |a self
    |[شَيْخ: شُيُوخ]{.ar} |an old man       |[عَيْن: عُيُون]{.ar} |a (water) spring
    |[شَاهِد: شُهُود]{.ar}|a witness        ||

7.  **[فُعَّل]{.ar} [fueeal]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[رَاكِع: رُكَّع]{.ar}  |one who bowes~m~ |[غَائِب: غُيَّب]{.ar} |absent
    |[راكعَة: رُكَّع]{.ar} |one who bowes~f~ ||

8.  **[فُعَّال]{.ar} [fueeAl]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[قَارِئ: قُرَّاء]{.ar}  |a reader~m~       |[كَافِر: كُفَّار]{.ar}    |a disbeliever~m~
    |[تَاجِر: تُجَّار]{.ar}  |a trader~m~       |[جَاهِل: جُهَّال]{.ar}    |an ignorant one~m~
    |[عَامِل: عُمَّال]{.ar}  |a worker~m~       ||

9.  **[فَعَلَة]{.ar} [faealah]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[سَاحِر: سَحَرَة]{.ar}  |a magician~m~     |[قَاتِل: قَتَلَة]{.ar}   |a killer~m~
    |[عَامِل: عَمَلَة]{.ar}  |a labourer~m~     |[سَيِّد: سَادَة]{.ar}    |a chief~m~

10. **[فُعَلَة]{.ar} [fuealah]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[قَاضٍ: قُضَاة]{.ar}  |a judge~m~     |[رَاوٍ: رُوَاة]{.ar}   |a narrator~m~

11. **[فِعَلَة]{.ar} [fiealah]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[دُبّ: دِبَبَة]{.ar}  |a bear     |[قِرْد: قِرَدَة]{.ar}   |a monkey
    |[هِرّ: هِرَرَة]{.ar}  |a cat~m~   ||

12. **[فِعْلَة]{.ar} [fielah]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[أَخ: إِخْوَة]{.ar}  |a brother     |[فَتًى: فِتْيَة]{.ar}   |a young man

13. **[أَفْعُل]{.ar} [Eafeul]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[رِجْل: أَرْجُل]{.ar}  |a leg         |[شَهْر: أَشْهُر]{.ar}   |a month
    |[نَفْس: أَنْفُس]{.ar}  |a self        |[عَيْن: أَعْيُن]{.ar}   |an eye

14. **[أَفْعَال]{.ar} [EafeAl]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[بَاب: أَبْوَاب]{.ar}  |a door        |[مَيِّت: أَمْوَات]{.ar}    |dead
    |[قَلَم: أَقْلَام]{.ar}  |a pen         |^2^[شَيْء: أَشْيَاء]{.ar} |a thing
    |[قَدَم: أَقْدَام]{.ar}  |a foot        |[ٱِسْم: أَسْمَاء]{.ar}    |a name
    |[صَاحِب: أَصْحَاب]{.ar} |a companion~m~|[يَوْم: أَيَّام]{.ar}     |a day
    |[شَرِيف: أَشْرَاف]{.ar} |a noble one~m~|[عَدُوّ: أَعْدَاء]{.ar}    |an enemy
    |[طِفْل: أَطْفَال]{.ar}  |a child       |[عَيْن: أَعْيَان]{.ar}    |an eminent person
    |[بِئْر: آبَار]{.ar}   |a (water) well||

15. **[أَفْعِلَة]{.ar} [Eafeilah]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[لِسَان: أَلْسِنَة]{.ar}  |a tongue      |[طَعَام: أَطْعِمَة]{.ar} |a food
    |[إِمَام: أَئِمَّة]{.ar}   |a leader~m~   |[إِلَـٰه: آلِهَة]{.ar}  |a god

16. **^2^[فَوَاعِل]{.ar} [fawAeil]{.trn}^2^**. (Semi-flexible because of ^2^[فَفَافِف]{.ar} pattern.) Examples:

    ||
    |---:|:---|---:|:---
    |^2^[صَاحِبَة: صَوَاحِب]{.ar} |a companion~f~      |^2^[عَامِل: عَوَامِل]{.ar} |a factor
    |^2^[جَارِيَة: جَوَارٍ]{.ar}  |a girl              |^2^[شَاهِد: شَوَاهِد]{.ar} |a corroborating evidence
    |^2^[أَمْر: أَوَامِر]{.ar}   |a command           |^2^[خَاتَم: خَوَاتِم]{.ar} |a ring (jewelry)
    |^2^[نَادِرَة: نَوَادِر]{.ar} |a joke, a witticism |^2^[فَارِس: فَوَارِس]{.ar} |a horseman

17. **^2^[فَعَائِل]{.ar} [faeAEil]{.trn}^2^**. (Semi-flexible because of ^2^[فَفَافِف]{.ar} pattern.) Examples:

    ||
    |---:|:---|---:|:---
    |^2^[حُرَة: حَرَائِر]{.ar}      |a free woman|^2^[جَزِيرَة: جَزَائِر]{.ar} |an island
    |^2^[ضَرّة: ضَرَائِر]{.ar}      |a co-wife   |^2^[رِسَالَة: رَسَائل]{.ar} |a message
    |^2^[حَدِيقَة: حَدَائِق]{.ar}    |a garden    |^2^[حَاجَة: حَوَائِج]{.ar}  |a need
    |^2^[حَقِيبَة: حَقَائِب]{.ar}    |a bag       |^2^[دَلِيل: دَلَائِل]{.ar}  |an evidence
    |^2^[كَبِيرَة: كَبَائِر]{.ar}    |a major sin |^2^[خَلِيفَة: خَلَائِف]{.ar} |a successor
    |^2^[كَرِيمَة: كَرَائِم]{.ar}    |a generous one~f~ ||

18. **[فِعْلَان]{.ar} [fielAn]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[غُلَام: غِلْمَان]{.ar}  |a boy     |[ثَوْر: ثِيرَان]{.ar}   |a bull
    |[جَار: جِيرَان]{.ar}   |a neighbor|[غُرَاب: غِرْبَان]{.ar}  |a crow
    |[أَخ: إِخْوَان]{.ar}    |a brother |[فَأْر: فِئْرَان]{.ar}   |a mouse
    
19. **[فُعْلَان]{.ar} [fuelAn]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[بَلَد: بُلْدَان]{.ar}  |a country     |[شُجَاع: شُجْعَان]{.ar} |a brave one
    |[جِدَار: جُدْرَان]{.ar} |a wall        |[شَابّ: شُبَّان]{.ar}   |a young man

20. **^2^[فُعَلَاء]{.ar} [fuealAE]{.trn}^2^**. Examples:

    ||
    |---:|:---|---:|:---
    |^2^[أَمِير: أُمَرَاء]{.ar} |a commander~m~ |^2^[خَلِيفَة: خُلَفَاء]{.ar} |a caliph
    |^2^[فَقِير: فُقَرَاء]{.ar} |a poor one~m~  |^2^[عَالِم: عُلَمَاء]{.ar}  |a scholar~m~
    |^2^[بَخِيل: بُخَلَاء]{.ar} |a miser~m~     |^2^[شَاعِر: شُعَرَاء]{.ar}  |a poet~m~
    |^2^[ضَعِيف: ضُعَفَاء]{.ar} |a weak one~m~  ||

21. **^2^[أَفْعِلَاء]{.ar} [EafeilAE]{.trn}^2^**. Examples:

    ||
    |---:|:---|---:|:---
    |^2^[نَبِيّ: أَنْبِيَاء]{.ar} |a prophet~m~  |^2^[شَدِيد: أَشِدَّاء]{.ar} |a forceful one~m~
    |^2^[صَدِيق: أَصْدِقَاء]{.ar}|a friend~m~   |^2^[قَوِيّ: أَقْوِيَاء]{.ar} |a strong one~m~
    |^2^[غَنِيّ: أُغْنِيَاء]{.ar} |a rich one~m~ |^2^[شَقِيّ: أَشْقِيَاء]{.ar} |a wretched one~m~

22. **^2^[فَعْلَىٰ]{.ar} [faelA]{.trn}^2^**. Examples:

    ||
    |---:|:---|---:|:---
    |^2^[مَرِيض: مَرْضَىٰ]{.ar} |a sick one~m~  |^2^[جَرِيح: جَرْحَىٰ]{.ar} |a wounded person
    |^2^[أَسِير: أَسْرَىٰ]{.ar} |a captive      ||

23. **^2^[فَعَالِي]{.ar} [faeAlI]{.trn}^2^**. (Semi-flexible because of ^2^[فَفَافِف]{.ar} pattern.) Examples:

    ||
    |---:|:---|---:|:---
    |^2^[لَيْلَة: لَيَالٍ]{.ar}|a night  |^2^[أَرْض: أَرَاضٍ]{.ar} |a land, an earth
    |^2^[أَهْل: أَهَالٍ]{.ar} |a family ||

24. **^2^[فَعَالَىٰ]{.ar} [faeAlA]{.trn}^2^**. Examples:

    ||
    |---:|:---|---:|:---
    |[صَحْرَاء^2^: صَحَارَىٰ^2^]{.ar}|a desert  |[فَتْوَىٰ^2^: فَتَاوَىٰ^2^]{.ar} |a formal legal opinion
    |^2^[يَتِيم: يَتَامَىٰ]{.ar}|an orphan     |^2^[هَدِيَّة: هَدَايَا]{.ar}    |a gift

25. **[فَعِيل]{.ar} [faeIl]{.trn}** (rare). Examples:

    ||
    |---:|:---|---:|:---
    |[عَبْد: عَبِيد]{.ar}|a slave~m~  |[حِمَار: حَمِير]{.ar} |a donkey~m~

26. **[فُعُولَة]{.ar} [fueUlah]{.trn}** (rare). Examples:

    ||
    |---:|:---|---:|:---
    |[بَعْل: بُعُولَة]{.ar}|a husband  ||

27. **[فِعَالَة]{.ar} [fieAlah]{.trn}** (rare). Examples:

    ||
    |---:|:---|---:|:---
    |[حَجَر: حِجَارَة]{.ar}|a stone  ||

28. **[فَعَل]{.ar} [faeal]{.trn}** (rare). Examples:

    ||
    |---:|:---|---:|:---
    |[حَلْقَة: حَلَق]{.ar}|a circular ring  ||

29. **[فَعْل]{.ar} [fael]{.trn}** (very rare). Examples:

    ||
    |---:|:---|---:|:---
    |[صَاحِب: صَحْب]{.ar}|a companion  ||

30. **^2^[فَفَافِف]{.ar} [fafAfif]{.trn}^2^**. Includes the sub-patterns:

    + **^2^[فَعَالِل]{.ar} [faeAlil]{.trn}^2^**
    + **^2^[أَفَاعِل]{.ar} [EafAeil]{.trn}^2^**
    + **^2^[تَفَاعِل]{.ar} [tafAeil]{.trn}^2^**
    + **^2^[مَفَاعِل]{.ar} [mafAeil]{.trn}^2^**

    Examples:

    ||
    |---:|:---|---:|:---
    |^2^[ثَعْلَب: ثَعَالِب]{.ar}  |a fox         |^2^[تَجْرِبَة: تَجَارِب]{.ar} |an experience
    |^2^[عَنْكَبُوت: عَنَاكِب]{.ar}|a spider      |^2^[مَسْجِد: مَسَاجِد]{.ar}  |a mosque      
    |^2^[دِرْهَم: دَرَاهِم]{.ar}  |a dirham      |^2^[مَعَانٍ: مَعْنًى]{.ar}   |a meaning     
    |^2^[جَوْهَر: جَوَاهِر]{.ar}  |a gem         |^2^[مَحَالّ: مَحَلَّة]{.ar}   |a locality
    |^2^[إِصْبَع: أَصَابِع]{.ar}  |a finger      |^2^[مَعِيشَة: مَعَاىِش]{.ar} |a means of subsistence      
    |^2^[أَنْمُلَة: أَنَامِل]{.ar} |a finger tip  ||

31. **^2^[فَفَافِيف]{.ar} [fafAfIf]{.trn}^2^**. Includes the sub-patterns:

    + **^2^[فَعَالِيل]{.ar} [faeAlIl]{.trn}^2^**
    + **^2^[أَفَاعِيل]{.ar} [EafAeIl]{.trn}^2^**
    + **^2^[تَفَاعِيل]{.ar} [tafAeIl]{.trn}^2^**
    + **^2^[مَفَاعِيل]{.ar} [mafAeIl]{.trn}^2^**
    + **^2^[يَفَاعِيل]{.ar} [yafAeIl]{.trn}^2^**
    + **^2^[فَوَاعِيل]{.ar} [fawAeIl]{.trn}^2^**

    Examples:

    ||
    |---:|:---|---:|:---
    |^2^[سُلْطَان: سَلَاطِين]{.ar}  |a sultan         |^2^[إِعْصَار: أَعَاصِير]{.ar}  |a whirlwind
    |^2^[شَيْطَان: شَيَاطِين]{.ar}  |a devil          |^2^[تَأْرِيخ: تَوَارِيخ]{.ar}  |a history
    |^2^[سِكِّين: سَكَاكِين]{.ar}   |a knife          |^2^[تَصْوِير: تَصَاوِير]{.ar}  |a picture
    |^2^[دِينَار: دَنَانِير]{.ar}  |a [dInAr]{.trn2} |^2^[مِفْتَاح: مَفَاتِيح]{.ar}  |a key       
    |^2^[مِسْكِين: مَسَاكِين]{.ar}  |a needy person   |^2^[مَلْعُون: مَلَاعِين]{.ar}  |an accursed one~m~
    |^2^[كُرْسِيّ: كَرَاسِيّ]{.ar}    |a chair          |^2^[يُنْبُوع: يَنَابِيع]{.ar}  |a (water) spring
    |^2^[أُمْنِيَّة: أَمَانِيّ]{.ar}   |a wish           |^2^[جَامُوس: جَوَامِيس]{.ar}  |a buffalo

32. **[فَعَالِلَة]{.ar} [faeAlilah]{.trn}**. Examples:

    ||
    |---:|:---|---:|:---
    |[أُسْتَاذ: أَسَاتِذَة]{.ar}  |a professor  |[مَلَك: مَلَائِكَة]{.ar}  |an angel
    |[فَيْلَسُوف: فَلَاسِفَة]{.ar} |a philosopher|[جَبَّار: جَبَابِرَة]{.ar} |a tyrant

Note the following from the above broken plural patterns and examples:

+ Both common nouns and adjectival nouns form broken plurals.

+ There are comparatively fewer broken plurals for female intelligent beings than for male intelligent beings. We will expand on this in a subsequent section.

+ Some patterns of the broken plural are also patterns singular nouns. For example, the pattern [فِعَال]{.ar} [fieAl]{.trn} has both singular nouns, like [كِتَاب]{.ar} [kitAb]{.trn} "a book" and broken plurals, like [رِجَال]{.ar} [rijAl]{.trn} "men"

+ The broken plural patterns [فِعْلَان]{.ar} [fielAn]{.trn} and [فُعْلَان]{.ar} [fuelAn]{.trn} are fully-flexible nouns. Although they end with the [ان]{.ar} ending which is extrinsic to the root, they are not semi-flexible nouns. Only singular adjectival nouns that end with an extrinsic [ان]{.ar} on the pattern [فَعْلَان]{.ar}, and that also fulfil the other conitions listed in section\ \@ref(adjectival-noun-an-diptote), are semi-flexible.

+ There is often a correlation between the pattern of a singular noun and the pattern of its plural.

  Sometimes this correlation is very strong:

  + All singular nouns of the patterns ^2^[أَفْل]{.ar} [Eafeal]{.trn}^2^ and ^2^[فَعْلَاء]{.ar} [faelAE]{.trn} that denote colors and physical characteristics, have broken plurals on the pattern [فُعْل]{.ar} [fuel]{.trn}. Example:

    |Singular | Plural|
    |:---|:---|
    |[أَحْمَر^2^، حَمْرَاء^2^]{.ar}  "red"  |[حُمْر]{.ar} |
    |[أَبْكَم^2^، بَكْمَاء^2^]{.ar}  "mute" |[بُكْم]{.ar} |

  + Singular nouns that have four or more consonant letters (excluding [ة]{.ar}) regularly form their broken plurals on the patterns ^2^[فَفَافِف]{.ar} and ^2^[فَفَافِيف]{.ar}. The pattern ^2^[فَفَافِيف]{.ar} is used when there is an intermendiate long vowel between the consonants. Examples:

    |Singular | Plural|
    |:---|:---|
    |[إِصْبَع]{.ar} "a finger" |^2^[أَصَابِع]{.ar} |  
    |[مِفْتَاح]{.ar}  "a key"  |^2^[مَفَاتِيح]{.ar}|

  + Singular nouns of the patterns [فِعْلَة]{.ar} [fielah]{.trn} and [فُعْلَة]{.ar} [fuelah]{.trn} regularly form their broken plurals on the pattern [فِعَل]{.ar} [fieal]{.trn} and [فُعَل]{.ar} [fueal]{.trn} respectively. Examples:
    
    |Singular | Plural|
    |:---|:---|
    |[قِطْعَة]{.ar}  "a piece"|[قِطَع]{.ar} |
    |[رُكْبَة]{.ar}  "a knee" |[رُكَب]{.ar} |

  Other times, this correlation is more like a tendency:

  + Singular nouns on the pattern [فَعِيلَة]{.ar} [faeIlah]{.trn} tend to form broken plurals on the pattern ^2^[فَعَائِل]{.ar} [faeAEil]{.trn}^2^. Examples:

    |Singular | Plural|
    |:---|:---|
    |[حَدِيقَة]{.ar}     "a garden"|^2^[حَدَائِق]{.ar} |
    |[حَقِيبَة]{.ar}     "a bag"   |^2^[حَقَائِب]{.ar} |

  + Singular nouns on the pattern [فَاعِل]{.ar} [fAeil]{.trn}, that denote male intelligent beings, tend to form broken plurals on the pattern [فُعَّل]{.ar} [fueeal]{.trn}, [فُعَّال]{.ar} [fueeAl]{.trn}, and [فَعَلَة]{.ar} [faealah]{.trn}. Examples:

    |Singular | Plural|
    |:---|:---|
    |[غَائِب]{.ar}  "absent"     |[غُيَّب]{.ar}  |
    |[قَارِئ]{.ar}  "a reader~m~"|[قُرَّاء]{.ar} |
    |[قَاتِل]{.ar}  "a killer~m~"|[قَتَلَة]{.ar} |

  + Singular nouns on the pattern [فَاعِل]{.ar} [fAeil]{.trn} and [فَاعِلَة]{.ar} [fAeilah]{.trn}, that don't denote male intelligent beings, tend to form broken plurals on the pattern [فَوَاعِل]{.ar} [fawAeil]{.trn}. Examples:

    |Singular | Plural|
    |:---|:---|
    |[صَاحِبَة]{.ar}  "a companion~f~"|^2^[صَوَاحِب]{.ar} |
    |[عَامِل]{.ar}   "a factor"      |^2^[عَوَامِل]{.ar} |

    [فَارِس]{.ar} [fAris]{.trn} "a horseman" with the plural ^2^[فَوَارِس]{.ar} is one of a number of exceptions.

+ Some words have roots that have the same letter repeated in the root. These are called _doubled_ roots. 

  + For example:
  
    |Root | Word | Pattern
    |:----|:--|:--
    |[دبّ]{.arroot}|[دُبّ]{.ar}   "a bear"            | [فُعْل]{.ar}
    |[حلّ]{.arroot}|[مَحَلَّة]{.ar} "a locality"        | [مَفْعَلَة]{.ar}
    |[أمّ]{.arroot}|[إِمَام]{.ar} "a leader"          | [فِعَال]{.ar}
    |[حقّ]{.arroot}|[حَقّ]{.ar}   "a truth, a right"  | [فَعْل]{.ar}
    |[هرّ]{.arroot}|[هِرّ]{.ar}   "a cat~m~"          | [فِعْل]{.ar}

  We will discuss doubled roots in detail in chapter\ \@ref(doubled-roots). For now we will mention the following:

  + The repeated letter in the word root may get doubled or separated in the word's pattern. Frequently, the repeated letter may be doubled in the singular, and separated in the plural. Examples:

    |Singular | Plural|
    |:---|:---|
    |[حَقّ]{.ar}   "a truth, a right"|[حُقُوق]{.ar} |
    |[دُبّ]{.ar}   "a bear"          |[دِبَبَة]{.ar} |
    |[هِرّ]{.ar}   "a cat~m~"        |[هِرَرَة]{.ar} |

    The reverse also occurs, where the repeated letter may be separated in the singular, and doubled in the plural. Examples:

    |Singular | Plural|
    |:---|:---|
    |[إِمَام]{.ar}    "a leader~m~"|[أَئِمَّة]{.ar} |

  + The doubled letter may modify the basic word pattern somewhat. For example:

    |Root | Word pattern | Expected word | Actual word
    |:-|:--|:--|:--
    |[شدّ]{.arroot} |^2^[أَفْعِلَاء]{.ar} |$\times$\ ^2^[أَشْدِدَاء]{.ar} |^2^[أَشِدَّاء]{.ar}
    |[حلّ]{.arroot} |^2^[مَفَاعِل]{.ar}  |$\times$\ ^2^[مَحَالِل]{.ar}  |^2^[مَحَالّ]{.ar} 
    |[صمّ]{.arroot} |^2^[أَفْعَل]{.ar}  |$\times$\ ^2^[أَصْمَم]{.ar}  |^2^[أَصَمّ]{.ar} 

+ We have previously learned that the endings [ة]{.ar}, [اء]{.ar}, and [ىٰ]{.ar} that are extrinsic to the word's root are feminine markers for singular nouns. These extrinsic endings also occur for broken plurals but there, they are _not_ feminine markers.

  In fact, in a sort of role reversal, the endings [ة]{.ar} in a broken plural tends to indicate that the singular is a masculine noun. And the [اء]{.ar} ending is only for broken plurals of male intelligent beings.  Examples:

  |Singular | Plural|
  |:---|:---|
  |[لِسَان]{.ar} "a tongue"      |[أَلْسِنَة]{.ar} |
  |[هِرّ]{.ar}   "a cat~m~"      |[هِرَرَة]{.ar}  |
  |[أَمِير]{.ar} "a commander~m~"|[أُمَرَاء]{.ar} |
  |[صَدِيق]{.ar} "a friend~m~"   |[أَصْدِقَاء]{.ar}|

+ There often exist multiple broken plurals for the same singular noun. Many times, in fact, a singular noun may have a sound plural in addition to one or more broken plurals. Examples:

  |Singular | Plural
  |:---|---:
  |[شَهْر]{.ar} |[أَشْهُر، شُهُور]{.ar}
  |[عَيْن]{.ar} |[أَعْيُن، عُيُون، أَعْيَان]{.ar}
  |[عَامِل]{.ar}|[عَامِلُونَ، عَوَامِل^2^، عَمَلَة، عُمَّال]{.ar}

  We will discuss how to manage these multiple plurals in a subsequent section.

+ Occasionally, multiple singular nouns will share the same broken plural. Examples:

  |Singular | Plural
  |:---|---:
  |[مَكْتَب]{.ar} "an office" |^2^[مَكَاتِب]{.ar}
  |[مَكْتَبَة]{.ar} "a library"|^2^[مَكَاتِب]{.ar}

  Context will then tell us which of two meanings is intended.

+ The letters [ء]{.ar}, [ا]{.ar}, [و]{.ar}, and [ي]{.ar} are considered _weak_ letters. Words that one or more these weak letters in their roots are called _defective_ words. We will discuss defective words more completely in later chapters, if [#allAh]{.trn2} wills. For now, we will note the following:

  + Weak letters often get interchanged with one another when going from a singular to a plural. Examples:

    |Root |Singular | Plural|
    |:--|:---|:---|
    |[أرخ]{.arroot} | [تَأْرِيخ]{.ar} | ^2^[تَوَارِيخ]{.ar}
    |[نوق]{.arroot} | [نَاقَة]{.ar}  | [نُوق]{.ar}
    |[ثور]{.arroot} | [ثَوْر]{.ar}   | [ثِيرَان]{.ar}

  + Weak letters can affect surrounding vowels. For example:

    |Root | Word pattern | Expected word | Actual word
    |:-|:--|:--|:--
    |[بيض]{.arroot} |[فُعْل]{.ar} |$\times$\ [بُيْض]{.ar} |[بِيض]{.ar}

  + The weak letter [ي]{.ar}, when followed by the [ىٰ]{.ar} ending, usually modifies (in writing) it to an [ِEalif]{.trn} instead. The pronunciation is the same. For example:

    |Root | Word pattern | Expected word | Actual word
    |:-|:--|:--|:--
    |[هدي]{.arroot} |^2^[فَعَالَىٰ]{.ar} |$\times$\ ^2^[هَدَايَىٰ]{.ar} |^2^[هَدَايَا]{.ar}

  + A [ي]{.ar} at the end of a word, in some states, gets omitted  and replaced by an [in]{.trn}-mark [◌ٍ]{.ar} on the preceding letter. This happens even when the [ي]{.ar} is extrinsic to the root, and even if the word is semi-flexible (and thus would not normally accept an [n]{.trn} mark). Examples:

    |Root | Word pattern | Expected word  | Actual word 
    |:-|:--|:--|:--
    |[قضي]{.arroot} |[فَاعِل]{.ar} |$\times$\ [قَاضِي]{.ar} |[قَاضٍ]{.ar}
    |[جري]{.arroot} |^2^[فَوَاعِل]{.ar} |$\times$\ ^2^[جَوَارِي]{.ar} |^2^[جَوَارٍ]{.ar}
    |[ليل]{.arroot} |^2^[فَعَالِي]{.ar} |$\times$\ ^2^[لَيَالِي]{.ar} |^2^[لَيَالٍ]{.ar}

  + Weak letters can also get omitted in the singular and resurface in the plural. Examples:

    |Root |Singular | Plural|
    |:--|:---|:---|
    |[أخو]{.arroot} | [أَخ]{.ar} | [إِخْوَان، إِخْوَة]{.ar}
    |[أمو]{.arroot} | [أَمَة]{.ar} | [إِمَاء]{.ar}


+ If there are more than four consonant letters in a word, then only four of them are selected to form the broken plural. For example:

  |Singular | Plural
  |:---|---:
  |[عَنْكَبُوت]{.ar} "a spider" |^2^[عَنَاكِب]{.ar}

+ Some words have individual irrgularities as well and we will discuss them below:

  + The word [ٱِمْرَأَة]{.ar} and its plural [نِسَاء]{.ar} are both irregular and we will discuss them separately in chapter\ \@ref(irregular-nouns).

  + The broken plural ^2^[أَشْيَاء]{.ar} [EacyAE]{.trn} (of the singular noun [شَيْء]{.ar} [cayE]{.trn} "a thing") is irregular in that it is semi-flexible. Otherwise its pattern [أَفْعَال]{.ar} [EafeAl]{.trn} is regularly fully-flexible.

  + The broken plural of the singular noun [مَلَك]{.ar} [malak]{.trn} "an angel" is [مَلَائِكَة]{.ar} [malAEikah]{.trn}. It is on the pattern [فَعَالِلَة]{.ar} [faeAlilah]{.trn}. But it is unusual in that the plural has an extra letter [ء]{.ar} that is missing in the singular. This is because the singular has a lesser-used variant: [مَلْأَك]{.ar} [malEak]{.trn} that is used to form the plural.

  + The broken plural of the singular noun [دِينَار]{.ar} "a [dInAr]{.trn2}" is ^2^[دَنَانِير]{.ar}. It is on the pattern ^2^[فَعَالِيل]{.ar}. It is irregular in that there are two [ن]{.ar}'s in the plural whereas the singular only has one.

  + The root of [بِئْر]{.ar} [biEr]{.trn} "a (water) well" is [بأر]{.arroot}. The pattern of its broken plural is [أَفْعَال]{.ar}. Based on its root letters, its plural on this pattern ought regularly to have been [أَبْآر]{.ar} [EabEAr]{.trn}. And this plural exists but is not very commonly used. Instead, in forming the plural, the root letters [ب]{.ar} and [أ]{.ar} get swapped irregularly, and the more commonly used plural is actually [آبَار]{.ar} ['EAbAr]{.trn}.

  There are other words as well with similar irregularities.

## Co-existence of multiple broken plurals

We noted that there are often multiple broken plurals for the same singular noun. Many singular nouns even have a sound plural in addition to one or more broken plurals. Here are some examples.

  |Singular | Meanings | Plural
  |:---|:---|---:
  |[جِدَار]{.ar}|a wall              |[جُدُر، جُدْرَان]{.ar}
  |[شَهْر]{.ar} |a month             |[أَشْهُر، شُهُور]{.ar}
  |[ضَعِيف]{.ar}|a weak one~m~       |^2^[ضِعَاف، ضُعَفَاء]{.ar}
  |[أَمْر]{.ar} |a matter; a command |^2^[أُمُور، أَوَامِر]{.ar}
  |[عَيْن]{.ar} |an eye; a (water) spring; an eminent person |[أَعْيُن، عُيُون، أَعْيَان]{.ar}
  |[عَامِل]{.ar}|a worker; a labourer; a factor              |[عَامِلُونَ، عَوَامِل^2^، عَمَلَة، عُمَّال]{.ar}

We will deal with the co-existence of sound and broken plurals in the next section. In this section, we will explain the existence of multiple broken plurals, and when one of them is preferred or required to be used over the other. Basically, there could be a few things going on:

1. Sometimes it is more or less optional which of the multiple broken plurals to use. For example, the singular noun [جِدَار]{.ar} has two broken plurals:
[جُدُر، جُدْرَان]{.ar}
Either could be used, more or less, interchangeably.

2. Sometimes, the usage of one of the plurals may be restricted. For example, [ضِعَاف]{.ar} and [ضُعَفَاء]{.ar} are both broken plurals of the masculine adjectival noun [ضَعِيف]{.ar} "a weak one~m~". For male intelligent beings, like "weak men", either of the two plurals could be used. But remember that broken plurals that end with an extrinsic [اء]{.ar} ending may only be used for male intelligent beings. So the plural [ضُعَفَاء]{.ar} may only be used for male intelligent beings like "men" or "boys", and not for masculine nouns that denote non-intelligent beings like "lions" or "pens", etc.

   Interestingly, [ضِعَاف]{.ar} is also shared as the broken plural for the feminine adjectival noun [ضَعِيفَة]{.ar} "a weak one~f~". So it can be used for plurals of feminine nouns, both for female intelligent beings like "women" and "girls", and for feminie nouns that denote non-intelligent beings like "trees".

3. Other times, the singular has multiple distinct meanings, and each of these distinct meanings is associated with its own broken plural(s). Here are some examples:

   + The word [أَمْر]{.ar} [Eamr]{.trn} has two distinct meanings, each with it's own plural:

     i. "a matter". This has the broken plural [أُمُور]{.ar} [EumUr]{.trn}.
     ii. "a command". This has the broken plural ^2^[أَوَامِر]{.ar} [EawAmir]{.trn}^2^.

   + The word [عَيْن]{.ar} [Eayn]{.trn} has multiple distinct meanings. There are three main meanings, and they share the broken plural with each other in the following way:

     i. "an eye". This meaning primarily uses the plural [أَعْيُن]{.ar} [Eaeyun]{.trn} but it may also use the plural [عُيُون]{.ar} [euyUn]{.trn}, and rarely also the plural [أَعْيَان]{.ar} [EaeyAn]{.trn}.
     ii. "a (water) spring". This meaning primarily uses the plural [عُيُون]{.ar} [euyUn]{.trn} but it may also use the plural [أَعْيُن]{.ar} [Eaeyun]{.trn}, and rarely also the plural [أَعْيَان]{.ar} [EaeyAn]{.trn}.
     iii. "an eminent person". This meaning only uses the plural [أَعْيَان]{.ar} [EaeyAn]{.trn}.

   + The word [عَامِل]{.ar} [eAmil]{.trn} has the following meanings and plurals:
     
     i. "a worker~m~". Generally, this has the plural [عُمَّال]{.ar} [eummAl]{.trn}.
     ii. "a labourer~m~". This uses the plural [عَمَلَة]{.ar} [eamalah]{.trn}.
     iii. "a factor". This uses the plural ^2^[عَوَامِل]{.ar} [eawAmil]{.trn}^2^.

4. Arabic has what are known as _plurals of fewness_. These are specific patterns that may (sometimes, but not always) be used when the persons or things denoted by the plural are only a few (ten or less) and not many. These patterns are:

   i. [فِعْلَة]{.ar} [fielah]{.trn}
   ii. [أَفْعُل]{.ar} [Eafeul]{.trn}
   iii. [أَفْعَال]{.ar} [EafeAl]{.trn}
   iv. [أَفْعِلَة]{.ar} [Eafeilah]{.trn}

   For example:
   
   i. [شَهْر]{.ar} [cahr]{.trn} "a month", plurals: [أَشْهُر، شُهُور]{.ar}. The plural [أَشْهُر]{.ar} could be used when the number of months are only a few (ten or less), and the plural [شُهُور]{.ar} could be used when the number of months are large.
   ii. The plurals [أَعْيُن]{.ar} and [عُيُون]{.ar} of the word [عَيْن]{.ar} could also possibly be used similarly in this manner for both meanings: "an eye" and "a (water) spring". (But not for the meaning "an eminent person" which only uses the plural [أَعْيَان]{.ar}).

   Of course, this distinction only applies when the singular noun has additional plurals, not just one from the above four patterns. If a noun has only one of the about four plural patterns then it may be used indiscriminately and will not indicate any limitation in number.

## Co-existence of sound and broken plurals

Some nouns have both sound and broken plurals for more or less the same meaning. Here are some examples:

|Singular | Meaning | Sound plural |Broken plural
|:---|:---|:---|:---
|[قَاتِل]{.ar}  | a killer       |[قَاتِلُونَ]{.ar} |[قَتَلَة]{.ar}
|[كَافِر]{.ar}  | a disbeliever  |[كَافِرُونَ]{.ar} |[كُفَّار]{.ar}
|[كَبِير]{.ar}  | a big one~m~   |[كَبِيرُونَ]{.ar} |[كِبَار]{.ar}
|[كَبِيرَة]{.ar} | a big one~f~   |[كَبِيرَات]{.ar} |[كِبَار]{.ar}
|[صَغِير]{.ar}  | a small one~m~ |[صَغِيرُونَ]{.ar} |[صِغَار]{.ar}
|[صَغِيرَة]{.ar} | a small one~f~ |[صَغِيرَات]{.ar} |[صِغَار]{.ar}
|[رَاكِع]{.ar}  | one who bows~m~|[رَاكِعُونَ]{.ar} |[رُكَّع]{.ar}
|[رَاكِعَة]{.ar} | one who bows~f~|[رَاكِعَات]{.ar} |[رُكَّع]{.ar}
|[صَاحِبَة]{.ar} | a companion~f~ |[صَاحِبَات]{.ar} |^2^[صَوَاحِب]{.ar}
|[جَارِيَة]{.ar} | a girl         |[جَارِيَات]{.ar} |^2^[جَوَارٍ]{.ar}
|[حَدِيقَة]{.ar} | a garden       |[جَدِيقَات]{.ar} |^2^[حَدَائِق]{.ar}

We will treat the [Un]{.trn} and [At]{.trn} sound plurals separately.

### [Un]{.trn} plurals and broken plurals

Remember from chapter\ \@ref(sound-plurals) that [Un]{.trn} plurals are, with very few exceptions, only used for male intelligent beings.

If a singular noun has both an [Un]{.trn} sound plural and one or more broken plurals, then the use of the broken plural is generally preferred. The sound plural is then, generally, reserved for certain verbal usages. (We will study these in later chapters, if [#allAh]{.trn2} wills.)

So, for example, [قَتَلَة]{.ar} is preferred over [قَاتِلُونَ]{.ar} generally for the meaning: "killers".

### [At]{.trn} plurals and broken plurals

[At]{.trn} plurals are used for both female intelligent beings and non-intelligent beings. We will discuss each of these separately.

#### Female intelligent beings

Remember from section\ \@ref(conditions-for-the-at-plural) that, generally, all nouns that end with feminine markers
([ة]{.ar}, [اء]{.ar}, and [ىٰ]{.ar}) 
can form the [At]{.trn} sound plural.

There are some nouns that are excepted from this statement. These nouns only have broken plurals and don't form sound plurals. For female intelligent beings, these nouns are:

+ Adjectival nouns of the pattern ^2^[فَعْلَاء]{.ar} which is the feminine of the masculine adjectival noun pattern ^2^[أَفْعَل]{.ar}. For example, [حور]{.arroot} [حَوْرَاء]{.ar} [HawrAE]{.trn} "a beautiful eyed one~f~" uses the broken plural [حُور]{.ar} [HUr]{.trn}

+ Adjectival nouns of the pattern ^2^[فَعْلَىٰ]{.ar} which is the feminine of the masculine adjectival noun pattern ^2^[فَعْلَان]{.ar}. For example, [غضب]{.arroot} [غَضْبَىٰ]{.ar} [gaDbA]{.trn} "very angry~f~" uses the broken plural [غِضَاب]{.ar} [giDAb]{.trn}.

+ The following exceptional nouns:

  + [ٱِمْرَأَة]{.ar} "a woman", broken plural: [نِسَاء]{.ar}
  + [أَمَة]{.ar} "a slave~f~", broken plural: [إِمَاء]{.ar}

In the case of these nouns we have no choice but to use the broken plural.

For other nouns that denote female intelligent beings, the use of the [At]{.trn} sound plural is preferred over any broken plurals that the noun may have.

So, for example,
the use of the [At]{.trn} sound plural
[صَغِيرَات]{.ar}
is preferred over the broken plural
[صِغَار]{.ar} 
for the adjectival noun
[صَغِيرَة]{.ar} 
"a small one~f~"

The following are excepted from this general statement:

+ [أُنْثَىٰ]{.ar} "a female", plural: [إِنَاث]{.ar}. The [At]{.trn} sound plural is almost unused for this word.

+ Broken plurals of the patterns:
 
  + ^2^[فَوَاعِل]{.ar} [fawAeil]{.trn}^2^
  + ^2^[فَعَائِل]{.ar} [faeAEil]{.trn}^2^

  These broken plural patterns are, in fact, predominantly used for female intelligent beings and non-intelligent beings, and only rarely for male intelligent beings. So the broken plural ^2^[جَوَارٍ]{.ar} "girls" may be used freely as the plural of [جَارِيَة]{.ar} "a girl" and is not preferred over by [جَارِيَات]{.ar}. Similarly, ^2^[صَوَاحِب]{.ar} may freely be used as the plural of [صَاحِبَة]{.ar}.

  Only a few nouns denoting male intelligent beings have broken plurals on these patterns, like:

  + [فَارِس]{.ar} "a horseman", plural: ^2^[فَوَارِس]{.ar}
  + [خَلِيفَة]{.ar} "a successor", plural: ^2^[خَلَائِف]{.ar}

In conclusion, with the general preference of using the [At]{.trn} sound plural over the broken plural for female intelligent beings, you will find that [نِسَاء]{.ar} [nisAE]{.trn} "women" is the only widely found broken plural for female intelligent beings in normal usage.

#### Non-intelligent beings

For non-intelligent beings, the broken plural is preferred for use over [At]{.trn} sound plurals.

So, for example, ^2^[حَدَائِق]{.ar} [HadAEiq]{.trn}^2^ is preferred over [حَدِيقَات]{.ar} [HadIqAt]{.trn} as the plural of [حَدِيقَة]{.ar}, though both are correct. 

## Usage of plurals of intelligent beings

We will now discuss how plurals are used in Arabic. Using plurals is more complicated than using duals.

In order to explain their usage systematically, we will treat plurals of intelligent beings separately from the plurals of non-intelligent beings.

The usage of plurals of intelligent beings is more straightforward and in line with what we have studied for duals. We will discuss descriptive noun-phrases, subject-information sentences, and verbal sentences.

### Plurals in descriptive noun-phrases

Consistent with what we have learned so far, when the describee in a noun-phrase is plural, then the describer comes after it, and matches it in state, definiteness, gender, and number.

Either or both of the describer and the describee may be sound plurals or broken plurals.

Here are some examples:

[لَعِبَ ٱلطِّفْلُ ٱلصَّغِيرُ مَعَ ٱلْغِلْمَانِ ٱلْكِبَارِ.]{.ar}  
[laeiba -TTiflu -SSagIru maea -lgilmAni -lkibAr.]{.trn}  
"The small child played with the big boys."

[أَخَذَ ٱلتِّلْمِيذُ ٱلْعِلْمَ عَنِ ٱلْمُعَلِّمِينَ ٱلْكِرَامِ.]{.ar}  
[Eaxapa -ttilmIpu -leilma eani -lmueallimIna -lkirAm.]{.trn}  
"The pupil took knowledge from the noble teachers."

[لِلْجَارِيَةِ صَوَاحِبُ طَيِّبَاتٌ.]{.ar}  
[liljAriyati SawAhibu TayyibAt.]{.trn}  
"The girl has good companions~f~."

[فِي ٱلسُّوقِ تُجَّارٌ صَادِقُونَ.]{.ar}  
[fi -ssUqi tujjArun SadiqUn.]{.trn}  
"In the market are honest traders."

[خَدَمَ ٱلرَّجُلُ ٱلصَّالِحُ ٱلْغَنِيُّ ٱلْفُقَرَاءَ ٱلضِّعَافَ مِنَ ٱلْيَتَامَىٰ ٱلصِّغَارِ.]{.ar}  
[xadama -rrajulu -SSAliHu -lganiyyu -lfuqarAEa -DDieAfa mina -lyatAmA -SSigAr.]{.trn}  
"The rich righteous man served the weak poor ones from the little orphans."

### Plurals in subject-information sentences

If the subject of a sentence is a plural denoting intelligent beings then the information typically matches it in being a plural. This is especially the case if the information is an adjectival noun. For example:

[ٱلْغِلْمَانُ أَطْفَالٌ طَيِّبُونَ.]{.ar}  
[EalgilmAnu EaTfAlun TayyibUn.]{.trn}  
"The boys are good children."

[ٱَلرِّجَالُ أَغْنِيَاءُ.]{.ar}  
[EarrijAlu EagniyAE.]{.trn}  
"The men are rich."

[ٱَلْمُعَلِّمَاتُ عَالِمَاتٌ.]{.ar}  
[EalmueallimAtu eAlimAt,]{.trn}  
"The teachers~f~ are scholars~f~."

Sometimes the information may not match the subject in plurality because of the meaning of the sentence. For example:

[ٱَلْمُسْلِمُونَ أَمَّةٌ.]{.ar}  
[EalmuslimUna Eummah.]{.trn}  
"The Muslims are a nation."

[ٱَلْجِيرَانُ ٱلطَّيِّبُونَ نِعْمَةٌ مِنَ ٱللَّـٰهِ.]{.ar}  
[EaljIrAnu -TTayyibUna niematun mina -llAh.]{.trn}  
"Good neighbors are a blessing from Allah."

With regards to detached pronouns, the same detached pronouns are used with detached plurals that we learned for in section\ \@ref(detached-plural-pronouns) for sound plurals. Examples:

[أَنْتُنَّ نِسَاءٌ كَرِيمَاتٌ.]{.ar}  
[Eantunna nisAEun karImAt.]{.trn}  
"You~3,f~ are generous women."

[أَنْتُمْ شُبَّانٌ شُجْعَانٌ.]{.ar}  
[Eantum cubbAnun cujeAnun]{.trn}  
"You~m,3~ are courageous young men."

[ٱَلشَّيَاطِينُ هُمُ ٱلْمَلَاعِنُ.]{.ar}  
[EaccayATInu humu -lmalAeIn.]{.trn}  
"The devils are the accursed ones."

[هُنَّ نِسَاءٌ غَنِيَّاتٌ.]{.ar}  
[hunna nisAEun ganiyyAt.]{.trn}  
"They~3,f~ are rich women."

[نَحْنُ غِلْمَانٌ أَصْدِقَاءُ.]{.ar}  
[naHnu gilmAnun EaSdiqAE.]{.trn}  
"We are boys who are friends."

### Plurals with verbs

We have already studied verbs with sound plurals in section\ \@ref(verbs-with-plural-doers). The same discussion applies to broken plurals as well. The doer and doee pronouns are the same. Here are a couple of examples:

[قَرَأَتِ ٱلنِّسَاءُ وَكَتَبْنَ.]{.ar}  
[qaraEati -nnisAEu wakatabn.]{.trn}  
"The women read and wrote."

[ٱَلْغِلْمَانُ لَعِبُوا بِكُرَةٍ حَمْرَاءَ.]{.ar}  
[EalgilmAnu laeibU bikuratin HamrAE.]{.trn}  
"The boys, they played with a red ball."

[طَبَخَتِ ٱلنِّسَاءُ طَعَامًا لِلرِّجَال فَأَكَلُوهُ وَشَكَرُوهُنَّ.]{.ar}  
[Tabaxati -nnisAEu TaeAman lirrijAli faEakalUhu wacakarUhunn.]{.trn}  
"The women prepared some food for the men, so they~3,m~ ate it and they~3,m~ thanked them~3,f~.

[ظَلَمَ ٱلْجَبَابِرَةُ ٱلْمَسَاكِينَ وَقَتَلُوهُمْ.]{.ar}  
[Palama -ljabAbiratu -lmasAkIna waqatalUhum.]{.trn}  
"The tyrants wronged the needy ones~3,m~ and killed them~3,m~."

## Usage of plurals of non-intelligent beings

We now turn our attention to plurals of non-intelligent beings. They treatment of plurals of non-intelligent beings is very different from everything we have learned so far. Regardless of the grammatical or physical gender of the singular noun, plurals of non-intelligent beings are treated, for the purposes of matching adjectival nouns and pronouns, as:

i. grammatically feminine singular
i. grammatically feminine plural

It is optional which of the above two treatments one uses. However, the former option (feminine singular) is more common and is generally preferred.

For the second option (feminine plural), in addition to the sound feminine plural of adjectival nouns, broken plurals are allowed to be used as well, as long as their meaning allows them to be used for non-intelligent beings.
<!--not specifc to male intelligent beings (those that end with [اء]{.ar}).-->

So, for example, the noun [بَيت]{.ar} [bayt]{.trn} denotes the inanimate object "a house". It's plural is [بُيُوت]{.ar}. This plural is treated as either feminine singular or feminine plural. This is despite the fact that the singular noun [بَيْت]{.ar} [bayt]{.trn} "a house" is grammatically masculine. See how the [بُيُوت]{.ar} [buyUt]{.trn} is used in the examples below:

[ٱَلْبُيُوتُ كَبِيرَةٌ.]{.ar}  
[ٱَلْبُيُوتُ كَبِيرَاتٌ.]{.ar}  
[ٱَلْبُيُوتُ كِبَارٌ.]{.ar}  
"The houses are big."  

[سَكَنُوا فِي بُيُوتٍ صَغِيرَةٍ.]{.ar}  
[سَكَنُوا فِي بُيُوتٍ صَغِيرَاتٍ.]{.ar}  
[سَكَنُوا فِي بُيُوتٍ صِغَارٍ.]{.ar}  
"They~3,m~ lived in ssmall houses."

[سَقَطَتِ ٱلْبُيُوتُ.]{.ar}  
"The houses fell."

[ٱَلْبُيُوتُ سَقَطَتْ.]{.ar}  
[ٱَلْبُيُوتُ سَقَطْنَ.]{.ar}  
"The houses, they fell."

[هِيَ بُيُوتٌ لِلْفُقَرَاءِ.]{.ar}  
[هُنَّ بُيُوتٌ لِلْفُقَرَاءِ.]{.ar}  
"They are houses for the poor."

Plurals of inanimate objects and animals (both male and female) are treated the same way. It doesn't matter what the grammatical or physical gender of the singular is or whether it has a sound or broken plural. Examples:

[هِيَ ثِيرَانٌ وَحْشَةٌ.]{.ar}  
[هِيَ ثِيرَانٌ وُحُوشٌ.]{.ar}  
[هُنَّ ثِيرَانٌ وَحْشَاتٌ.]{.ar}  
"They are wild bulls."

[ٱَلْهِرَرَةُ شَرِبَتِ ٱلْحَلِيبَ.]{.ar}  
[ٱَلْهِرَرَةُ شَرِبْنَ ٱلْحَلِيبَ.]{.ar}  
"The cats~m~, they drank the milk."

[ٱَلْهِرَرُ شَرِبَتِ ٱلْحَلِيبَ.]{.ar}  
[ٱَلْهِرَرُ شَرِبْنَ ٱلْحَلِيبَ.]{.ar}  
"The cats~f~, they drank the milk."

[ٱَلسُّفُنُ طَوِيلَة.]{.ar}  
[ٱَلسُّفُنُ طِوَالٌ.]{.ar}  
[ٱَلسُّفُنُ طَوِيلَاتٌ.]{.ar}  
"The ships are tall."

[فِي ٱلصُّنْدُوقُ أَشْيَاءُ عَجِيبَةٌ.]{.ar}  
[فِي ٱلصُّنْدُوقُ أَشْيَاءُ عَجِيبَاتٌ.]{.ar}  
"In the box are wonderful things."  
(Note how ^2^[أَشْيَاء]{.ar} is indefinite but has no [n]{.trn}-mark. This is because it is irregularly semi-flexible.)

By the way, this rule only applies to adjectival nouns in the describee or the information. A common noun in the describer or information will continue match the describee or subject in gender and number.

For example, if you say:

[ٱَلْأَفْعَالُ ٱلصَّالِحَةُ هِيَ ٱلْحَسَنَةُ.]{.ar}  
"The righteous acts are the good ones."

then [حَسَنَة]{.ar} may only be the feminine adjectival noun "a good one".

If instead you want to use [حَسَنَة]{.ar} with its common noun meaning of "a good deed", then you have the use the plural:

[ٱَلْأَفْعَالُ ٱلصَّالِحَةُ هِيَ ٱلْحَسَنَاتُ.]{.ar}  
"The acts are the good deeds."

The plural [هِي]{.ar} may continue to be used instead of [هُنَّ]{.ar}, although the latter is also valid:

[ٱَلْأَفْعَالُ ٱلصَّالِحَةُ هُنَّ ٱلْحَسَنَاتُ.]{.ar}  
"The acts are the good deeds."

Similarly, if an adjectival noun connoting a non-intelligent being is used not as a describer or an information in a sentence, then it should be pluralized to indicate plurality.

[ٱَلْحَيَوَانَاتُ صَغِيرَةٌ وَكَبِيرَةٌ. ٱَلْكَبِيرَاتُ وَحْشَةٌ.]{.ar}  
"The animals are big and small. The big ones are wild."

In the second sentence above, we could not have said (for the same meaning):

$\times$\ [ٱَلْحَيَوَانَاتُ صَغِيرَةٌ وَكَبِيرَةٌ. __ٱَلْكَبِيرَةُ__ وَحْشَةٌ.]{.ar}  

<!--
[ٱَلْحَيَوَانَاتُ كِلَاب.]{.ar}  
for  
"They are male dogs."
not  
$\times$\ [ٱَلْحَيَوَانَاتُ كَلْبَة.]{.ar}
-->

It is important to note that treating non-intelligent beings as grammatically feminine is only for the plural. Singular and dual nouns for non-intelligent beings are treated according to the gender of singular noun, as we have learned in previous chapters. So, for example,

[ٱَلْبَيْتُ كَبِيرٌ.]{.ar}  
"The house is big."  
not  
$\times$\ [ٱَلْبَيْتُ كَبِيرَة.]{.ar}

[أَكَلَ ٱلْأَسَدَانِ ٱلظَّبْيَ.]{.ar}  
"The lions~2~ ate the gazelle."  
not  
$\times$\ [أَكَلَتِ ٱلْأَسَدَانِ ٱلظَّبْيَ.]{.ar}  

### Preferring the feminine plural instead of the feminine singular

In most cases we will prefer to use the feminine singular over the feminine plural for plurals of non-intelligent beings. So,

[ٱلْأُسُودُ أَكَلَتِ ٱلظَّبْيَ.]{.ar}  
"The lions, they ate the gazelle."

is generally preferred over 

[ٱلْأُسُودُ أَكَلْنَ ٱلظَّبْيَ.]{.ar}  
"The lions, they ate the gazelle."

However, there may be a couple of reasons to prefer the feminine plural instead of the feminine singular. We will explain them below.

#### Using the feminine plural to indicate fewness

In some circumstances 
the feminine plural may be used to indicate fewness
whereas
the feminine singular will be used to indicate a multitude.

So if we say,

[ٱلْأُسُودُ أَكَلْنَ ٱلظَّبْيَ.]{.ar}  
"The lions, they ate the gazelle."

then this would indicate that there were only a few lions (say ten or less).

And if, instead, we said:

[ٱلْأُسُودُ أَكَلَتِ ٱلظَّبْيَ.]{.ar}  
"The lions, they ate the gazelle."

then this would indicate that there were many lions.

This may seem counter-intuitive at first but you may understand it this way: 

If there are many lions then we treat them as _one_ group.

And if there are only a few lions, then we treat them _one-by-one_.

#### Using the feminine plural to avoid confusion

Sometimes, if the plural noun is not immediately mentioned, then using the feminine singular may be misinterpreted to only mean one instead of the plural. For example, consider the following example:

[شَرِبَتِ ٱلْهِرَرُ ٱلْحَلِيبَ وَمَا شَرِبَتْهُ هِرَّةٌ.]{.ar}  
"The cats~f~ drank the milk and one cat~f~ didn't drink it."

If we want to follow this sentence with another sentence: "Then they went.", if we use the feminine singular:

[ثُمَّ ذَهَبَتْ.]{.ar}  

then this might be misinterpreted to mean that only one cat (the one that didn't drink the milk) went.

So we might prefer to say, instead:

[ثُمَّ ذَهَبْنَ.]{.ar}  


<!--chapter:end:srcrmd/broken_plurals.Rmd-->

# Annexation

## Introduction

Consider the following expression:

"the boy's book"

This expression establishes a relation of _belonging_ between the two nouns: (i)\ "the boy", and (ii)\ "the book". It says that the book _belongs_ to the boy.

Arabic expresses this meaning using a construction called _annexation_. In this chapter we will learn about this construction.

## Forming the annexation

The word "annexation" means the addition of a new _annexed_ item to an existing _base_ item. We use the term _annexation_ in Arabic grammar when an _annexe_ noun is annexed to a _base_ noun by being placed right before it. Here is an example of an annexation:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-11-1.pdf)<!-- -->

<!--"the boy's book"  -->

The annexation construction consists of two nouns:

1. The _annexe_ noun: This is the first noun in the annexation.
1. The _base_ noun: This is the second noun in the annexation.

The annexe noun [كِتَاب]{.ar} is annexed to, and belongs to, the base noun [ٱَلْغُلَام]{.ar}. 
You can use the alphabetical  order (A,\ B) to help you remember that the **a**nnexe noun comes before the **b**ase noun.

<!--
Take note of the following points regarding the annexation construction:

+ The base noun in an annexation shall always be in the i-state.
+ The state of the annexe noun is variable and shall depend on its function in the sentence.
+ The annexe noun in an annexation shall neither have an [n]{.trn}-mark nor the prefix [ٱَلْ]{.ar}.

## Remove

In Arabic we may chain two or more nouns in a sequence to establish an "of" relationship between them, in order to express, for example,

+ "the mother of the boy", or, equivalently" "the boy's mother".
+ "a house of a man", or, equivalently, "a man's house".
+ "the sword of Zayd", or equivalently, "Zayd's sword".

In English, as you can see there we can express this relationship using the word "of" or using apostrophe-s "'s" between two nouns. In some phrases, using apostrophe-s is more natural than using the word "of".

In Arabic we express these types of phrases by chaining the two nouns together thus:

[أُمُّ ٱلْغُلَامِ]{.ar}  
[Eummu -lgulAmi]{.trn}  
"the mother of the boy", or, equivalently" "the boy's mother"

We can identify noun-chains by noting that the first noun in the chain has neither an [n]{.trn} mark, nor an [ٱَلْ]{.ar}, and the second noun in the chain will be in the i-state. 

The first noun in the chain is the noun before "of" and the second noun in the chain is the noun after "of".
-->
## State of the annexe and base nouns

The base noun in an annexation is always in the i-state. The annexe noun may be in any state, depending on its function in the sentence. For example,
<!--
   + [أُمُّ ٱلْغُلَامِ مُعَلِّمَةٌ.]{.ar}  
     [Eummu -lgulAmi mueallimatun.]{.trn}  
     "The mother of the boy is a teacher.", or, equivalently, "The boy's mother is a teacher."
   + [وَجَدَ أُمَّ ٱلْغُلَامِ.]{.ar}  
     [wajada Eumma -lgulAmi.]{.trn}  
     "He found the boy's mother." (Note that [أُمَّ]{.ar} is in the a-state.)
   + [كَتَبَتْ إِلَىٰ أُمِّ ٱلْغُلَامِ.]{.ar}  
     [katabat EilA Eummi -lgulAmi.]{.trn}  
     "She wrote to the boy's mother." (Note that [أُمِّ]{.ar} is in the i-state.)
-->

[كِتَابُ ٱلْغُلَامِ ثَقِيلٌ.]{.ar}  
"The boy's book is heavy."  
(The annexe noun is in the u-state.)

[أَخَذَتِ ٱلْجَارِيَةُ كِتَابَ ٱلْغُلَامِ.]{.ar}  
"The girl took the boy's book."  
(The annexe noun is in the a-state.)

[كَتَبَ ٱلْمُعَلِّمُ فِي كِتَابِ ٱلْغُلَامِ.]{.ar}  
"The teacher~m~ wrote in the boy's book."  
(The annexe noun is in the i-state.)

## Definiteness of the annexation

Consider again the annexation expression we have been using so far:

[كِتَابُ ٱلْغُلَامِ]{.ar}  
"the boy's book"  

The base noun [ٱَلْغُلَام]{.ar} is definite because it is prefixed by [ٱَلْ]{.ar} "the".
Therefore we have translated it as "the boy".
The annexe noun [كِتَاب]{.ar} is not made definite by [ٱَلْ]{.ar}.
Nor is it made indefinite by an [n]{.trn}-mark. 
<!--Its definiteness is determined by the base noun. -->
Rather, its definiteness is determined by the base noun.
Because the base noun [ٱَلْغُلَام]{.ar} is definite, therefore the annexe noun [كِتَاب]{.ar} is also definite.
The entire annexation is definite.
<!--If the base noun is definite (as it is above) then the annexe noun shall also be definite.
And if the base noun is indefinite (as below) then the annexe noun shall also be indefinite.-->

Consider now the case when the base noun is indefinite.

[كِتَابُ غُلَامٍ]{.ar}  
"a boy's book"  

In the above example, the base noun [غُلَامٍ]{.ar} is indefinite because it has the [n]{.trn}-mark\ [◌ٍ]{.ar} and because it does not prefixed by [ٱَلْ]{.ar}. Therefore we have translated it as "a boy".
The annexe noun [كِتَاب]{.ar} has neither an [n]{.trn}-mark, nor the prefix [ٱَلْ]{.ar}.
Its definiteness is, again, determined by the base noun.
Because the base noun [غُلَامٍ]{.ar} is indefinite, therefore the annexe noun [كِتَاب]{.ar} is also indefinite.
The entire annexation is indefinite.

We will see soon, if [#allAh]{.trn2} wills, why the definiteness of the annexe noun is important.

<!--

As you can see above English has two constructs to translate the annexation:

i. using "'s"
ii. using "of"

Sometimes both of the above constructs will fit for the translation, and sometimes only one will fit. For convenience, we will often translate with only one of them.

The annexe noun in an annexation can have neither an [n]{.trn} mark, nor an [ٱَلْ]{.ar}. 
The base noun is permitted to have an [n]{.trn} mark or an [ٱَلْ]{.ar} prefix. 
The definiteness of the base noun then determines the definiteness of the annexation. If the second noun is definite, then both the annexe and the base nouns be definite. And if the base noun is indefinite, then both the nouns in the chain will be indefinite. 

[بَيْتُ مُحَمَّدٍ]{.ar}  
[baytu muHammadin]{.trn}  
"the  house of [#muHammad]{.trn2}"

[بَيْتُ ٱلرَّجُلِ]{.ar}  
[baytu -rrajuli]{.trn}  
"The house of the man"

[بَيْتُ رَجُلٍ]{.ar}  
[baytu rajulin]{.trn}  
"a house of a man"
-->

Here are some examples of definite and indefinite annexations.

[لَبِسَ ٱلطِّفْلُ قَمِيصَ رَجُلٍ.]{.ar}  
"The child wore _a_ man's shirt."

[أَخَذَ أَمِيرُ ٱلْجَيْشِ رَايَةَ ٱلْمَلِكِ وَرَفَعَهَا.]{.ar}  
"_The_ army's commander took _the_ king's flag and raised it."

[جَلَسَ ٱلرَّجُلُ فِي ظِلِّ شَجَرَةٍ.]{.ar}  
"The man sat in _a_ tree's shade."

### Translating the annexation using "of"

So far we have been using the English "'s" to translate the Arabic annexation. Examples:

[بَيْتُ رَجُلٍ]{.ar}  
"a man's house"

[بَيْتُ ٱلرَّجُلِ]{.ar}  
"the man's house"

Instead of using "'s" we may use "of" as well. For example:

[بَيْتُ رَجُلٍ]{.ar}  
"a/the house of a man"

[بَيْتُ ٱلرَّجُلِ]{.ar}  
"a/the house of the man"

Note that the annexe noun "house" may be prefixed with either "a" or "the". This will depend on what is more natural in English. Often time both will fit. Here are some examples:

[لَبِسَ ٱلطِّفْلُ قَمِيصَ رَجُلٍ.]{.ar}  
"The child wore a/the shirt of a man."

[أَخَذَ أَمِيرُ ٱلْجَيْشِ رَايَةَ ٱلْمَلِكِ وَرَفَعَهَا.]{.ar}  
"_The_ commander of the army took _the_ flag of the king and raised it."

[جَلَسَ ٱلرَّجُلُ فِي ظِلِّ شَجَرَةٍ.]{.ar}  
"The man sat in _the_ shade of a tree."

[فَتَحَ ٱلِّصُّ شُبَّاكَ ٱلْبَيْتِ وَدَخَلَ ٱلْبَيْتَ.]{.ar}  
"The thief opened _a/the_ window of the house and entered the house."

It is important to understand that translating the annexe noun into English with "a" or "the" is purely for the reason of obtaining a natural translation. This does not affect whether or not the annexe noun is grammatically considered definite in Arabic.

As we mentioned earlier, the definiteness of the annexe noun in Arabic depends only on the definiteness of the base noun. 
If the base noun is definite then the annexe noun shall be considered definite as well.
And if the base noun is indefinite then the annexe noun shall be considered indefinite as well.

The need to maintain this distinction will become apparent in the next section.

If the base noun is definite, and it is desired to make the annexe noun grammatically indefinite, then it is necassary to break the annexation, and use a prepositional phrase instead, usually with the preposition [لِ]{.ar}, which, here, will mean "of". Example:

[ذَهَبَ ٱلْغُلَامُ إِلَىٰ بَيْتٍ لِلرَّجُلِ.]{.ar}  
"The boy went to a house of the man."

[فَتَحَ ٱلِّصُّ شُبَّاكًّا مِنَ ٱلْبَيْتِ وَدَخَلَ ٱلْبَيْتَ.]{.ar}  
"The thief opened a window of the house and entered the house."

## Broken plurals and [At]{.trn} sound plurals in annexations {#broken-plurals-and-at-sound-plurals-in-annexations}

There is no special rules for broken plurals and [At]{.trn} sound plurals in annexations. They behave just like singular nouns. Remember only that [At]{.trn} plurals end with [◌ٍ]{.trn} and [◌ِ]{.ar} in the a-state. Here are some examples:

[حَيَوَانَاتُ ٱلْغَابَةِ وَحْشَةٌ.]{.ar}  
"The animals of the forest are wild."

<!--
[كَتَبَتْ طَالِبَاتُ ٱلْمَدْرَسَةِ بِأَقْلَامِ مُعَلِّمَاتٍ.]{.ar}  
"The school's students~f~ wrote with teachers'~f~ pens."
-->

[قَرَأَتْ طَالِبَاتُ ٱلْمَدْرَسَةِ صَفَحَاتِ ٱلْكُتُبِ]{.ar}  
"The school's students~f~ read the pages of the books."

[فِي ٱلْخِزَانَةِ أَقْلَامُ مُعَلِّمَاتٍ.]{.ar}  
"In the cupboard are teachers'~f~ pens.

Contrary to broken plurals and [At]{.trn} plurals, duals and [Un]{.trn} sound plurals behave differently in annexations. We will deal with them in section\ \@ref(duals-and-sound-un-plurals-in-annexations)

## Describers in an annexation

### Describing the base noun

Consider the following expression:

[كِتَابُ ٱلْجَارِيَةِ]{.ar}  
"the girl's book"

Now say that we want to form an descriptive noun-phrase "the small girl's book". 
Basically, we want to describe the base noun [ٱَلْجَارِيَة]{.ar} "the girl" with the adjectival noun [صَغِير]{.ar} "a small one". 
Here is how we will express this in Arabic:

[كِتَابُ ٱلْجَارِيَةِ ٱلصَّغِيرَةِ]{.ar}  
"the small girl's book"

In the manner we are already familiar with, we place the describer [صَغِير]{.ar} "a small one" after the describee
[ٱَلْجَارِيَة]{.ar} "the girl"
and match the describer with the describee in definiteness, state, gender and number (singular, dual, or plural).

Similarly, if we had an indefinite annexation, we would get:

[كِتَابُ جَارِيَةٍِ صَغِيرَةٍ]{.ar}  
"a small girl's book"

Here are some more examples:

[لَعِبَتِ ٱلْجَارِيَةُ فِي حَدِيقَةِ ٱلْبَيْتِ ٱلْكَبِيرِ.]{.ar}  
"The girl played in the garden of the big house."

[قَرَأَ ٱلْغُلَامُ سُورَةَ ٱلْقُرْآنِ ٱلْكَرِيمِ.]{.ar}  
"The boy read the [sUrah]{.trn2} of the Noble [#qurEAn]{.trn2}."

[جَلَسَ ٱلرَّجُلُ فِي ظِلِّ شَجَرَةٍ عَرِيضَةٍ وَسِيعَةٍ.]{.ar}  
"The man sat in the shade of a wide broad tree."

### Describing the annexe noun

Consider, again, the same annexation:

[كِتَابُ ٱلْجَارِيَةِ]{.ar}  
"the girl's book"

Say, now, that we want to describe the annexe noun [كِتَاب]{.ar} "book" with the adjectival noun [صَغِير]{.ar} "a small one". Normally, nothing can come between the annexe noun and the base noun in an annexation. So, the describer needs to be placed, again, after the base noun.
However, this time it will match the annexe noun, not the base noun, in state, definiteness, gender, and number. So we get:

[كِتَابُ ٱلْجَارِيَةِ ٱلصَّغِيرُ]{.ar}  
"the girl's small book"

Note how the describer 
[ٱَلصَّغِيرُ]{.ar} matches the annexe noun [كِتَابُ]{.ar} in state and gender.
Note also how the describer is definite with an [ٱَلْ]{.ar}. This is because it is matching the annexe noun [كِتَابُ]{.ar} in definiteness.
The annexe noun [كِتَاب]{.ar} is definite, not with [ٱَلْ]{.ar}, but rather because of the definite base noun [ٱَلْجَارِيَةِ]{.ar} "the girl".
We've already learned this rule in 
section\ \@ref(definiteness-of-the-annexation)
above.

Similarly, if we describe the annexe noun [كِتَاب]{.ar} in an indefinite annexation, we get:

[كِتَابُ جَارِيَةٍ صَغِيرٌ]{.ar}  
"a girl's small book"

This time
the describer 
[صَغِيرٌ]{.ar}
is indefinite with an [un]{.trn}-mark [◌ٌ]{.ar}. 
This is because 
the annexe noun [كِتَابُ]{.ar} is indefinite. It is indefinite because base noun [جَارِيَةٍ]{.ar} "a girl" is indefinite.

Now, you might be foreseeing a problem. What if the annexe noun and the base noun have the same gender, and the annexe too is in the i-state? For example, in the sentence:

[ذَهَبَ ٱلْغُلَامُ إِلَىٰ بَيْتِ ٱلرَّجُلِ ٱلْكَبِيرِ.]{.ar}  
"The boy went to the big/old man's house."  
or  
"The boy went to the man's big house."  

How do we know whether the describer [كَبِير]{.ar} is meant to describe the annexe noun [بَيْتِ]{.ar} or the base noun [ٱَلرَّجُل]{.ar}?
The annexe noun [بَيْتِ]{.ar} and the base noun [ٱَلرَّجُل]{.ar} are both masculine, singular, definite, and in the i-state.

The answer is that in such cases, context will have to be clear to tell us which of the two meanings is intended.
If the context makes it clear then there is no harm in using such a sentence for either of the two meanings.
<!--https://www.m-a-arabia.com/vb/showthread.php?t=40547
دفع اللبس في احتمالية النعت للمضاف والمضاف إليه-->

Also, sometimes, the meaning of the describer is such that it will likely apply to only one of the two nouns. For example,

[ذَهَبَ ٱلْغُلَامُ إِلَىٰ بَيْتِ ٱلرَّجُلِ ٱلْكَرِيمِ.]{.ar}  
"The boy went to a noble/generous man's house."  

In the sentence above the describer [كَرِيم]{.ar} "noble/generous" is likely to apply to a man, and not to a house.

If, however, the context is not clear, and the meaning of the describer can apply to both the annexe noun and the base noun, then the describer is likely to apply to the base noun and not to the annexe noun. So then, this interpretation is more likely:

[ذَهَبَ ٱلْغُلَامُ إِلَىٰ بَيْتِ ٱلرَّجُلِ ٱلْكَبِيرِ.]{.ar}  
"The boy went to the big/old man's house."  

In order to apply a describer to the annexe noun in such a case, it is better to break the annexation and form a prepositional phrase instead, usually with the preposition [لِ]{.ar}, which, here, will mean "of". Example:

[ذَهَبَ ٱلْغُلَامُ إِلَىٰ ٱلْبَيْتِ ٱلْكَبِيرِ لِلرَّجُلِ .]{.ar}  
"The boy went to the big house of the man."  

Here are some more examples:

[لَعِبَتِ ٱلْجَارِيَةُ بِكُرَةِ ٱلْغُلَامِ ٱلْحَمرَاءِ.]{.ar}  
"The girl played with the boy's red ball."  
(Note that [حَمْرَاء]{.ar} feminine to match [كُرَة]{.ar}.)

[سَقَطَتْ وَرَقَةُ ٱلشَّجَرَةِ ٱلْخَضْرَاءُ عَلَىٰ مَاءِ ٱلنَّعْرِ ٱلْعَرِيضِ.]{.ar}  
"The green leaf of the tree fell on the water of the broad river."  
(Note that [خَضْرَاء]{.ar} is in the u-state to match [وَرَقَة]{.ar})

[حَمَلَ ٱلْغُلَامُ حَقِيبَةَ ٱلْمَدْرَسَةِ ٱلثَّقِيلَةَ.]{.ar}  
"The boy carried the heavy school-bag."  
(literally: the heavy bag of the school).

[كَتَبَ ٱلرَّجُلُ عَلَىٰ صَفْحَةِ كِتَابٍ بَيْضَاءَ.]{.ar}  
"The man wrote on the white page of a book."  
(Note that [بَيْضَاءَ]{.ar} is feminine to match [صَفْحَة]{.ar}. However, also note that it has an a-mark [◌َ]{.ar} in the i-state because it is semi-flexible.)

<!--
[ذَهَبَ ٱلطَّالِبُ إِلَىٰ مَدْرَسَةِ مَدِينَةٍ عَظِيمَةٍ.]{.ar}
"The student went to a great city's school."  
or  
"The student went to a great school of a city."  
-->

## Semi-flexible nouns in an annexation

Remember that semi-flexible nouns don't take [n]{.trn}-marks and that when indefinite, the i-state is indicated by an [a]{.trn}-mark [◌َ]{.ar}. 
But when definite with [ٱَلْ]{.ar} then they behave just like fully-flexible nouns.
Example of the semi-flexible noun 
^2^[صَحْرَاء]{.ar} "a desert":

State  | Indefinite | Definite
:------|:-----------|:---------
u-state| [صَحْرَاءُ]{.ar} | [ٱَلصَّحْرَاءُ]{.ar}
a-state| [صَحْرَاءَ]{.ar} | [ٱَلصَّحْرَاءَ]{.ar}
i-state| [صَحْرَاءَ]{.ar} | [ٱَلصَّحْرَاءِ]{.ar}

We will now see how semi-flexible nouns behave in an annexation.

### A semi-flexible noun as the base noun

Here are examples of the semi-flexible noun ^2^[صَحْرَاء]{.ar} "a desert" as the base noun in an annexation:

[ٱَلْقَرْيَةُ فِي وَسَطِ ٱلصَّحْرَاءِ.]{.ar}  
"The village is in the middle of the desert."

[شَرِبَ ٱلْأَعْرَابِيُّ مَاءً مِنْ بِئْرِ صَحْرَاءَ.]{.ar}  
"The bedouin drank some water from a desert's well."

As you can see, when 
^2^[صَحْرَاء]{.ar}
is definite, then its i-state is indicate by an [i]{.trn}-mark [◌ِ]{.ar}, just like fully-flexible nouns. 
However, when it is indefinite, then 
its i-state is indicate by an [a]{.trn}-mark [◌َ]{.ar}.

This is consistent with the general behavior of semi-flexible nouns that we are familiar with.

### A semi-flexible noun as the annexe noun

Contrary from expected behavior, a semi-flexible annexe noun, even when indefinite, takes an [i]{.trn}-mark\ [◌ِ]{.ar} in the i-state instead of an [a]{.trn}-mark\ [◌َ]{.ar}. Example,

[قَدِمَ ٱلْأَعْرَابِيُّ مِنْ صَحْرَاءِ أَرْضٍ بَعِيدَةٍ.]{.ar}  
"The bedouin came from the desert of a far land."

In the above example,
^2^[صَحْرَاء]{.ar} "a desert" is indefinite because it is the annexe noun to an indefinite base noun [أَرْض]{.ar} "a land". 
It is in the i-state because it is preceded by the preposition [مِنْ]{.ar} "from". 
Nevertheless, it takes an [i]{.trn}-mark [مِنْ صَحْرَاءِ أَرْضٍ]{.ar}, not an [a]{.trn}-mark, which would be incorrect: $\times$\ [مِنْ صَحْرَاءَ أَرْضٍ]{.ar}.

## Annexations with more than two nouns

So far we have seen annexations with two nouns. Annexations may be arbitrarily long. Here is an example of a noun-chain with more than two nouns:

<!--
[مِفْتَاحُ بَابِ ٱلْبَيْتِ]{.ar}  
"the house's door's key"
-->

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-12-1.pdf)<!-- -->

The above annexation consists of three nouns. It may be divided into two sub-annexations:

i. [مِفْتَاحُ بَابِ]{.ar} "door's key". Its annexe noun $a_1$\ is [مِفْتَاح]{.ar} and its base noun\ $b_1$ is [بَابِ]{.ar}.
i. [بَابِ ٱلْبَيْتِ]{.ar} "the house's door". Its annexe noun $a_2$\ is [بَابِ]{.ar} and its base noun\ $b_2$ is [ٱلْبَيْتِ]{.ar}.

The noun [بَاب]{.ar} "door" is common to both sub-annexations. It is the base noun of the first sub-annexation
[مِفْتَاحُ بَابِ]{.ar} "door's key".
At the same time, it is also the annexe noun of the second sub-annexation
[بَابِ ٱلْبَيْتِ]{.ar} "the house's door".

Only the final base noun may have [ٱَلْ]{.ar} or an [n]{.trn} mark. If the final base noun has [ٱَلْ]{.ar} (as above) then all the nouns in the annexation are definite. 

And if the final base noun is indefinite, as in the example below, then all the nouns in the annexation are indefinite.

[مِفْتَاحُ بَابِ بَيْتٍ]{.ar}  
"a house's door's key"

All the nouns except the first annexe noun must be in the i-state. Consistent with 
section\ \@ref(a-semi-flexible-noun-as-the-annexe-noun)
if a semi-flexible noun is any of the annexe nouns and is in the i-state, then its i-state is indicated by an [a]{.trn}-mark [◌َ]{.ar}. Example:

[مِنْ بِئْرِ صَحْرَاءِ أَرْضٍ]{.ar}  
"from the well of the desert of a land"

## Pronouns as base nouns

Consider the expression:

"his book"

This expression is very similar to the annexation:

[كِتَابُ ٱلْغُلَامِ]{.ar}  
"the boy's book" 

The difference is that we would like to replace the base noun [ٱَلْغُلَام]{.ar} "the boy" with the pronoun "his". For this we use the attached pronoun [هُ]{.ar}. When we place this pronoun as the base noun, we get:

[كِتَابُهُ]{.ar}  
"his book"

This annexation follows the same rules as the other annexations we have been studying so far:

+ The annexe noun may be in any state, depending on its function in the sentence.
+ The base noun is in the i-state. But because the base noun is a pronoun, and pronouns are rigid nouns (see section\ \@ref(rigidity-of-pronouns) that don't change their ending based on their state, therefore it's i-state will not be apparent.

Here are some examples of this annexation used in sentences:

[كِتَابُهُ ثَقِيلٌ.]{.ar}  
"His book is heavy"

[قَرَأَ ٱلرَّجُلُ كِتَابَهُ.]{.ar}  
"The man read his book."

[كَتَبَ ٱلْمُعَلِّمُ فِي كِتَابهِ.]{.ar}  
"The teacher~m~ wrote in his book."

If the annexe noun ends with [ة]{.ar} then it is converted to a [ت]{.ar} when annexing it to an attached pronoun. For example:

[ذَهَبُوا إِلَىٰ مَدْرَسَتِهِمْ.]{.ar}  
"They went to their school."

Here are some more examples of annexing to the different attached pronouns:

[دَخَلْتَ بَيْتَكَ.]{.ar}  
"You~1,m~ entered your~1,m~ house."

[أَكَلَتَا طَعَامَهُمَا.]{.ar}  
"They~2,f~ ate their~2~ food."

[قَدِمْتُ إِلَىٰ مَدِينَتِكُمْ]{.ar}  
"I have arrived to your~3,m~ city."

[هُوَ إِمَامُ مَسْجِدِنَا.]{.ar}  
"He is the [E#imAm]{.trn2} of our mosque."

If the annexe noun is semi-flexible then it gets a [◌ِ]{.ar} in the i-state, as we've already learned. Example with the semi-flexible broken plural ^2^[حَدَائِق]{.ar} "gardens".

[لَعِبْنَ فِي حَدَائِقِهِنَّ.]{.ar}  
"They~3,f~ played in their~3,f~ gardens."

If an annexe noun ends with [ىٰ]{.ar} then it gets converted to an [Ealif]{.trn2} when annexing it to an attached pronoun. Example with ^2^[فَتَاوَىٰ]{.ar} "legal opinions":

[كَتَبَ تَلَامِذَةُ ٱلشَّيْخِ فَتَاوَاهُ فِي كُتُبِهِمْ.]{.ar}  
"The pupils of the religious scholar wrote down his legal opinions in their books."

For the singular speaker-participant there are two variants for the attached pronoun:

i. [ي]{.ar} [-I]{.trn}
ii. [يَ]{.ar} [-ya]{.trn}

The first ([ي]{.ar} [-I]{.trn}) is more commonly used. Example:

[قَرَأْتُ كِتَابِي]{.ar}  
"I read my book."

[أَقْلَامِي قَصِيرَة.]{.ar}  
"My pens are short."

If, however, the annexe noun ends in a long vowel or a semi-vowel then 
([ي]{.ar} [-I]{.trn}) is disallowed and only
([يَ]{.ar} [-ya]{.trn}) shall be used. 
Example with the semi-flexible broken plural ^2^[هَدَايَا]{.ar} "gifts":

[أَعْجَبَتْهُمْ هَدَايَايَ.]{.ar}  
"My gifts pleased them."

### Describers with annexations to pronouns

Consider the annexation:

[كِتَابُهُ]{.ar}  
"his book"

The annexe noun is [كِتَاب]{.ar} and the base noun is the pronoun [ه]{.ar}.
We would like add a describer to this expression.
Remember from section\ \@ref(definiteness-of-pronouns) that pronouns are definite nouns. That makes the annexe noun [كِتَاب]{.ar} also definite.
Therefore, any describer for this annexation will need to be definite too.

Here is a new rule: Pronouns may not be describees. That is: they are not allowed to have describers.
Even in English you may say:

"The good boy went."

but you can't say:

$\times$\ "The good _he_ went."

So, any describers for the annexation must necessarily only describe the annexe noun, not the base pronoun. Example:

[كِتَابُهُ الأَحْمَرُ]{.ar}  
"his red book"

Here are some more examples:

[كَتَبْتُ بِقَلَمِيَ ٱلْأَسْوَدِ]{.ar}  
"I wrote with my black pen."

[حَمَلَ غِلْمَانُ ٱلْقَرْيَةِ حَقَائبَهُمُ ٱلثَّقِيلَة إِلَىٰ مَدْرَسَتِهِمُ ٱلْبَعِيدَةِ.]{.ar}  
"The village boys carried their heavy bags to their distant school."  
(literally: the village's boys.)

## Duals and [Un]{.trn} sound plurals in annexations {#duals-and-sound-un-plurals-in-annexations}

We have already dealt with broken plurals and [At]{.trn} sound plurals in annexations in 
section\ \@ref(broken-plurals-and-at-sound-plurals-in-annexations).

In this section we will deal with 
duals and [Un]{.trn} sound plurals in annexations.

### Duals and [Un]{.trn} sound plurals as base nouns

As base noun, duals and [Un]{.trn} sound plurals behave no differently than other nouns. Being base nouns they will be in the i-state and this shall be indicated by:

i. [◌َيْنِ]{.ar} [-ayni]{.trn} for duals
i. [◌ِينَ]{.ar} [-Ina]{.trn} for [Un]{.trn} sound plurals

Here are some examples:

[لَجِئَ ٱلْمَظْلُومُنَ ٱلضُّعَفَاءُ فِي بِلَادِ ٱلْمُسْلِمِينَ ٱلْآمِنَةِ.]{.ar}  
"The weak wronged ones took refuge in the secure lands of the Muslims."

[أُخُتُ ٱلْغُلَامَيْنِ ٱلطَّوِيلَيْنِ صَغِيرَةِ.]{.ar}  
"The tall boys'~2~ sister is little."

[هِيَ طَالِبَةُ مُعَلِّمَتَيْنِ كَرِيمَتَيْنِ.]{.ar}  
"She is the student~f~ of noble teachers~2,f~."

### Duals and [Un]{.trn} sound plurals as annexe nouns

When duals and [Un]{.trn} sound plurals are annexe nouns, then their final [ن]{.ar} is treated as an [n]{.trn}-mark and is, therefore, deleted before annexing them to a base noun. For example:

[بَيْتَا ٱلرَّجُلِ]{.ar}  
"the man's houses~2~"  
not  
$\times$\ [بَيْتَانِ ٱلرَّجُلِ]{.ar}

Note, also, that because the base noun [ٱَلرَّجُلِ]{.ar} begins with a connecting [hamzah]{.trn2} [ٱ]{.ar}, therefore the long vowel [A]{.trn} at the end of [بَيْتَا]{.ar} is pronounced as a short vowel [a]{.trn}, thus:

[bayta -rrajuli]{.trn}  
not  
$\times$\ [baytA -rrajuli]{.trn}

If the dual annexe noun were in the i-state then the final [ي]{.ar} gets an [i]{.trn}-mark [◌ِ]{.trn} if there is following connecting [hamzah]{.trn2}. Example:

[قَرَأْتُ كِتَابَيِ ٱلرَّجُلِ.]{.ar}  
[qaraEtu kitAbayi -rrajul]{.trn}  
"I read the man's books~2~."

Here are some more examples including [Un]{.trn} sound plurals:

[مُعَلِّمُو ٱلْغُلَامِ كِرَامٌ.]{.ar}  
[mueallimu -lgulAmi kirAm.]{.trn}  
"The boy's teachers~3~ are noble."  
(Note that there is no silent [Ealif]{.trn2} after [مُعَلِّمُو]{.ar} as there is after a verb with a plural absentee-participant doer pronoun, e.g. [لَعِبُوا]{.ar} "they~3,m~ played")

[لَعِبَ ٱبْنَا ٱلرَّجُلِ مَعَ لَاعِبِي مَدِينَتِهِمْ.]{.ar}  
[laeiba -bna -rrajuli maea lAeibI madInatihim.]{.trn}  
"The man's sons~2~ played with the players of their city."

#### Annexing duals and [Un]{.trn} sound plurals to pronouns

Duals and [Un]{.trn} sound plurals can be annexed to attached pronouns, and in this case too, they will lose their final [ن]{.ar}. Examples:

[مُعَلِّمُونَا طَيِّبُونَ.]{.ar}  
"Our teachers~3,m~ are good."

[لَعِبَتِ ٱلْجَارِيَةُ مَعَ صَدِيقَتَيْهَا]{.ar}  
"The girl played with her friends~2,f~."

[بَيْتَايَ كَبِيرَانِ.]{.ar}  
"My houses~2~ are big."  
(Note that only the [يَ]{.ar} variant is allowed to be used because of [بَيْتَا]{.ar} ending with a long vowel.)

[قَرَأْتُ كِتَابَيَّ]{.ar}  
(Note how [كِتَابَيْ + يَ]{.ar} becomes [كِتَابَيَّ]{.ar}.)

There are also two special cases in this category and we will examine them below:

##### Annexing an [Un]{.trn} sound plural to the singular speaker participant pronoun {-} 

When an [Un]{.trn} sound plural is annexed to the singular speaker participant pronoun, then again, only the [يَ]{.ar} variant can be used. However, in addition, the expression will appear the same regardless of the state of the annexe noun. So for all states (u-state, a-state, and i-state), we will get:

[مُعَلِّمِيَّ]{.ar}

We don't say $\times$\ [مُعَلِّمُويَ]{.ar} for the u-state. Examples:

[مُعَلِّمِيَّ كِرَامٌ.]{.ar}  
"My teachers~3,m~ are noble."  
(u-state)

[سَأَلْتُ مُعَلِّمِيَّ]{.ar}  
"I asked my teachers~3,m~."  
(a-state)

[أَخَذْتُ كِتَابًا مِنْ مُعَلِّمِيَّ]{.ar}  
"I took a book from my teachers~3,m~."  
(i-state)

##### Annexing an dual noun to a dual pronoun {-} 

<!-- see فقد صغت قلوبكما-->
When a dual noun is to be annexed to a dual pronoun, then the dual annexe noun is often converted to a plural. For example, instead of saying 

[نَظَرْتُ إِلَىٰ رَأْسَيْهِمَا]{.ar}
"I looked at their~2~ heads~2~."

it is in fact, more common, to say

[نَظَرْتُ إِلَىٰ رُؤُوسِهِمَا]{.ar}
"I looked at their~2~ heads~3~."

Although the former is also correct. This is because the annexation of a dual to a dual is considered burdensome upon the tongue to utter, and so the plural is prefered.

<!--

Compare this with describing the base noun with the same adjectival noun.

[كِتَابُ ٱلْجَارِيَةِ ٱلصَّغِيرَةِ]{.ar}  
"the girl's small book"

As you can see, the adjectival noun [صَغِير]{.ar} "a small one" is in the same location, but its gender and state are different in both expressions because they match a different describee. 
The definiteness, however, is the same in the two expressions because the annexe noun has the same definiteness as the base noun.



If the second noun in a chain is to be described using a qualitative noun, then just like we have learned, we will place the qualitative noun after the second noun in the chain and match it definiteness, state, gender, and number (depending on whether it denotes a rational or non-rational being). Examples: 

[بَيْتُ رَجُلٍ كَبِيرٍ]{.ar}  
[baytu rajulin kabIrin]{.trn}  
"a house of an old/big man" = "an old/big man's house"

[بُيُوتُ ٱلرِّجالِ ٱلْكِبَارِ]{.ar}  
[buyUtu -rrijAli -lkibAri]{.trn}  
"houses of the old/big men" = "the old/big men's houses"

If the first noun in a chain is to be described using a qualitative noun, then we will actually place the qualitative noun after the second noun, not the first noun, in the chain. This way we don't break the chain of the two nouns. The describer will match the first noun definiteness, state, gender, and number (depending on whether it denotes a rational or non-rational being). Examples: 

[بَيْتُ رَجُلٍ كَبِيرٌ]{.ar}  
[baytu rajulin kabIrun]{.trn}  
"a big house of a man" = "a man's big house"

[بُيُوتُ  ٱلْمَرْأَةِ ٱلْكَبِيرَةُ]{.ar}  
[buyUtu -lmarEati -lkabIratu]{.trn}  
"the big houses of the woman" = "the woman's big houses"

Consider, however, the sentence:

[ذَهَبَ إِلَىٰ بَيْتِ رَجُلٍ كَبِيرٍ.]{.ar}  
[pahaba EilA bayti rajulin kabIrin.]{.trn}  

In this sentence both the first noun in the chain [بَيْتِ]{.ar} [bayti]{.trn} and second noun [رَجُلٍ]{.ar} [rajulin]{.trn} are indefinite, singular, masculine, and in the i-state. So the describer [كَبِيرٍ]{.ar} [kabirin]{.trn} could be applicable to either. And the meaning of the sentence could be either,

"He went to a man's big house."

or,

"He went to a big/old man's house."

The listener would know from context which of the two meanings is intended. If the speaker wished to explicitly disambiguate the meanings without relying on context, he could use the preposition [لِ]{.ar} instead of using a noun-chain. Here the preposition [لِ]{.ar} gives the meaning of "of", rather than "for".

[ذَهَبَ إِلَىٰ بَيْتٍ كَبِيرٍ لِرَجُلٍ.]{.ar}  
[pahaba EilA baytin kabIrin lirajulin.]{.trn}  
"He went to a big house of a man." = "He went to a man's big house."

and,

[ذَهَبَ إِلَىٰ بَيْتٍ لِرَجُلٍ  كَبِيرٍ.]{.ar}  
[pahaba EilA baytin kabIrin lirajulin.]{.trn}  
"He went to a big/old man's house."

## Duals and plurals in noun chains

### Duals

Remember that duals are expressed by suffixing [ـَانِ]{.ar} [Ani]{.trn} to the noun when it is in the u-state and [ـَيْنِ]{.ar} [ayni]{.trn} when it is in the a-state and i-state.

If a dual is the second noun in a chain, then it is not treated any differently from any other noun. For example,

[بَيْتُ ٱلرَّجُلَيْنِ]{.ar}  
[baytu -rrajulayni]{.trn}  
"the house of the two men"

If a dual is the first noun in a chain, then the [ن]{.ar} in the dual suffix is dropped. For example,

+ [بَيْتَا ٱلرَّجُلِ وَاسِعَانِ.]{.ar}  
  [bayta -rrajuli wAsieAni.]{.trn}  
  "The two houses of the man are spacious."

  Note that [بَيْتَا ٱلرَّجُلِ ]{.ar} [bayta -rrajuli]{.trn} is technically pronounced identically to [بَيْتَ ٱلرَّجُلِ]{.ar} [bayta -rrajuli]{.trn}. The [Ealif]{.trn2} in [بَيْتَا]{.ar} is not pronounced because of the connecting [hamzah]{.trn2} after it. Some say that extra stress may be placed on the vowel [ta]{.trn} in order to convey that it is the dual: [bay#t#a -rrajuli]{.trn}.

+ [ذَهَبَ إِلَىٰ مَدِنَتَيْ بَلَدٍ.]{.ar}  
  [pahaba EilA madInatay baladin.]{.trn}  
  "He went to two cities of a country."
+ [فَتَحَ بَابَيِ ٱلْبَيْتِ.]{.ar}  
  [fataHa bAbayi -lbayti.]{.trn}  
  "He opened the two doors of the house."

  Note that a helper [i]{.trn} vowel is placed on the [ي]{.ar} in [بَابَيِ]{.ar} [bAbayi]{.trn} instead of the [0]{.txt}-mark because of the connecting [hamzah]{.trn2} after it.

### Plurals

We have learned three kinds of plurals:

1. The sound [Un]{.trn} plural.
2. The sound [At]{.trn} plural.
3. The broken plural.

The sound [Un]{.trn} plural behaves similarly to the dual in that when it is the first noun in a chain, the [ن]{.ar} is dropped. Examples:

+ [مُعَلِّمُو ٱلْغُلَامِ فِي ٱلْمَدْرَسَةِ.]{.ar}  
  [mueallimu -lgulAmi fi -lmadrasati.]{.trn}  
  "The teachers of the boy are in the school."

  Note, again, that [مُعَلِّمُو ٱلْغُلَامِ]{.ar} is technically pronounced identically to [مُعَلِّمُ ٱلْغُلَامِ]{.ar} [mueallimu -lgulAmi]{.trn}, except some say that extra stress may be placed on the vowel [مُ]{.ar} in the case of the plural [muealli#m#u -lgulAmi]{.trn}. This can serve to differentiate it from the singular when heard orally:

  [مُعَلِّمُ ٱلْغُلَامِ فِي ٱلْمَدْرَسَةِ.]{.ar}  
  [mueallimu -lgulAmi fi -lmadrasati.]{.trn}  
  "The teacher of the boy is in the school."

+ [وَجَدَ مُعَلِّمي غُلَامٍ.]{.ar}  
  [wajada mueallimI gulAmin.]{.trn}  
  "He found teachers of a boy."

+ [ذَهَبَ إِلَىٰ مُعَلِّمِي ٱلْغُلَامِ.]{.ar}  
  [pahaba EilA mueallimi -lgulAmi.]{.trn}  
  "He went to the teachers of the boy."

  Here too, some say to place extra stress on the vowel [مِ]{.ar} [muealli#m#i -lgulAmi]{.trn} in order to differentiate it to the listener from the singular:

+ [ذَهَبَ إِلَىٰ مُعَلِّمِ ٱلْغُلَامِ.]{.ar}  
  [pahaba EilA mueallimi -lgulAmi.]{.trn}  
  "He went to the teacher of the boy."

The other two types of plurals: the sound [At]{.trn} plural and the broken plural are not treated any differently from other nouns when used in chains. Examples:

+ [بُيُوتِ الرَّجُلِ وَاسِعَةٌ.]{.ar}  
  [buyUtu -rrajuli wAsieatun.]{.trn}  
  "The houses of the man are spacious."

+ [ذَهَبَتِ ٱلْمَعَلِّمَةُ إِلَىٰ طَالِبَاتِ ٱلْمَدْرَسَةِ.]{.ar}  
  [pahabati -lmueallimatu EilA TAlibAti -lmadrsati.]{.trn}  
  "The (female) teacher went to the (girl) students of the school."

## Non-fully changing nouns in noun-chains

Remember that a non-fully changing noun without [ٱَلْ]{.ar} does not take an [n]{.trn}-mark and its last letter keeps an [a]{.trn} mark instead of an [i]{.trn} mark when in the i-state. When definite with [ٱَلْ]{.ar}, it is similar to fully-changing nouns.

So when a non-fully changing noun without [ٱَلْ]{.ar} is the second noun in a noun-chain, it will have an [a]{.trn}-mark instead of an [i]{.trn} mark.

For example, [صَحْرَاءُ]{.ar} [SaHrAEu]{.trn} "a desert" is a non-fully-changing noun. "A desert's sky" will be expressed as:

[سَمَاءُ صَحْرَاءَ]{.ar}  
[samAEu SaHrAEa]{.trn}

not:

[سَمَاءُ صَحْرَاءِ]{.ar}  
[samAEu SaHrAEi]{.trn}

Similarly, [جَمِيلَةُ]{.ar} "[#jamIlah]{.trn2}" as a woman's name is a proper noun and is a non-fully-changing noun. "[#jamIlah]{.trn2}'s house" will be expressed as:

[بَيْتُ جَمِيلَةَ]{.ar}  
[baytu jamIlata]{.trn}  

not:

[بَيْتُ جَمِيلَةِ]{.ar}  
[baytu jamIlati]{.trn}  

However, as an exception, when an indefinite non-full-changing noun is the first noun in a noun-chain and is in the i-state, it will actually take an [i]{.trn}-mark on its last letter. For example, [صَحْرَاءُ]{.ar} [SaHrAEu]{.trn} "a desert" is a non-fully-changing noun.

"in the desert of [#makkah]{.trn2}" will be expressed as,

[فِي صَحْرَاءِ مَكَّةَ]{.ar}  
[fI SaHrAEi makkata]{.trn}  

As you can see, [صَحْرَاءِ]{.ar} [SaHrAEi]{.trn} has an [i]{.trn}-mark despite being a non-fully-changing noun, exemplifying the exceptional rule we have just stated. Also note, by the way, that [مَكَّةَ]{.ar} [makkata]{.trn} has an [a]{.trn}-mark on it's last letter in the i-state because it is a non-fully-changing noun without [ٱَلْ]{.ar} as the second noun in a noun-chain.

## Noun chains with more than two nouns

So far we have seen noun-chains with two nouns. Noun-chains can be arbitrarily long, although practically they will usually be less than five nouns long. Here is an example of a noun-chain with more than two nouns:

+ [مِفْتَاحُ بَابِ بَيْتِ ٱلرَّجُلِ]{.ar}  
  [miftAHu bAbi bayti -rrajuli]{.trn}  
  "the key of the door of the man's house"

+ [سَمَاءُ صَحْرَاءِ مَكَّةَ]{.ar}  
  [samAEu SaHrAEi makkata]{.trn}  
  "the sky of the desert of Makkah"

+ [كِتَابَا جَارِيَتَيْ مَدِينَةِ دَمِشْقَ]{.ar}  
  [kitAbA jAriyatay madInati damicqa]{.trn}  
  "the two books of the two girls of the city of Damascus"

+ [مِنْ وَرَقَتَيْ شَجَرَةِ حَدِيقَةٍ صَغِيرَتَيْنِ]{.ar}  
  [min waraqatay cajarati HadIqatin]{.trn}  
  "from two small leaves of a tree of a garden"

Note the following:

+ Only the last noun may have [ٱَلْ]{.ar} or an [n]{.trn} mark. 
+ The definiteness of the last noun determines the definiteness of the rest of the nouns in the chain. 
+ All the nouns except the first must be in the i-state. 
+ The [ن]{.ar} of the dual and the [Un]{.trn} plural is dropped for all nouns except the last.
+ Any non-fully-changing noun in the i-state in any position but the last will take an [i]{.trn}-mark on it's last letter. If a non-fully-changing noun is the last noun in the chain, and it does not have [ٱَلْ]{.ar} then it will take an [a]{.trn}-mark on it's last letter.
+ Describers for any of the nouns in the chain will appear at the end. Practically, only one of the nouns will have a describer.

## Mismatched definiteness in noun-chains

We have learned that if the second noun is definite (either by having [ٱَلْ]{.ar}, or by being a proper noun), then both the nouns in the chain will be definite. And if the second noun is indefinite, then both the nouns in the chain will be indefinite. 

What if we need to express an of-relationship where the two nouns are not both definite or both indefinite? For example, how then do we express phrases like "a house of the man" and "the house of a man"? 
In order to express the former, we can employ the preposition [لِ]{.ar}:

[ذَهَبَ إِلَىٰ بَيْتٍ لِلرَّجُلِ.]{.ar}  
[pahaba EilA baytin lirrajuli]{.trn}  
"He went to a house of the man."

Another way to express this is that we may interpret the phrase "a house of the man" to understand that the man has more than one house and that we are talking about one of them. In this case, we can use the plural to say,

[ذَهَبَ إِلَىٰ بَيْتٍ مِنْ بُيُوتِ ٱلرَّجُلِ]{.ar}  
[pahaba EilA baytin min buyUti -rrajuli.]{.trn}  
"He went to a house from the houses of the man."

This use of the plural, although fairly common, may be more appropriate in some cases than others, depending on the meaning of the sentence. 

The question remains: how to express a phrase of the type "the house of a man", where the first noun in definite and the second noun is indefinite?

In this case we will use the same expression as we did for "a house of a man":

[بَيْتُ رَجُلٍ]{.ar}  
[baytu rajulin]{.trn}  
"a house of a man"

Technically, "house" is indefinite in this expression, but it can still be used idiomatically to translate "the house of a man." It may help to use apostrophe-s in the translation where the definiteness of "house" is not apparent: "a man's house".

## Pronouns in a noun-chain

Consider the noun-chain:

[بَيْتُ ٱلرَّجُلِ]{.ar}  
[baytu -rrajuli]{.trn}  
"the house of the man" = "the man's house"

We can replace the noun "the man" with the attached pronoun [ـهُ]{.ar} [-hu]{.trn} "him" to get:

[بَيْتُهُ]{.ar}  
[baytuhu]{.trn}  
"the house of him" = "his house"

This can be done with all the attached pronouns:

|Arabic|English|
|:---|:----|
|[بَيْتُهُ]{.ar} [baytuhu]{.trn}    |  his house |
|[بَيْتُهَا]{.ar} [baytuhA]{.trn}   |  her house |
|[بَيْتُهُمَا]{.ar} [baytuhumA]{.trn}|  their~dual\ masc.~ house |
|[بَيْتُهُمَا]{.ar} [baytuhumA]{.trn}|  their~dual\ fem.~ house |
|[بَيْتُهُمْ]{.ar} [baytuhum]{.trn}  |  their~pl.\ masc.~ house |
|[بَيْتُهُنَّ]{.ar} [baytuhunna]{.trn}|  their~pl.\ fem.~ house |
|[بَيْتُكَ]{.ar} [baytuka]{.trn}    |  your~sing.\ masc.~ house |
|[بَيْتُكِ]{.ar} [baytuki]{.trn}    |  your~sing.\ fem.~ house |
|[بَيْتُكُمَا]{.ar} [baytukumA]{.trn}|  your~dual~ house |
|[بَيْتُكُمْ]{.ar} [baytukum]{.trn}  |  your~pl.\ masc.~ house |
|[بَيْتُكُنَّ]{.ar} [baytukunna]{.trn}|  your~pl.\ fem.~ house |
|[بَيْتِي]{.ar} [baytI]{.trn}      |  my house |
|[بَيْتُنَا]{.ar} [baytunA]{.trn}   |  our house |

Here are some notes regarding the use of pronouns in noun-chains.

+ An attached pronoun may be only the last noun in a noun-chain. It cannot be the first noun in a noun-chain.
+ A looped [tAE]{.trn2} [ة]{.ar} in the first noun becomes an open [tAE]{.trn2} [ت]{.ar} when a pronoun is attached as the second noun in the noun-chain. For example [مَدْرَسَةٌ]{.ar} [madrasatun]{.trn} "a school" becomes [مَدْرَسَتُهُ]{.ar} [madrasatuhu]{.trn} "his school".
+ The first noun in the noun-chain, before the attached pronoun, may be in any state. So, for example, we can have:
  + [دَخَلَ بَيْتَهُ.]{.ar} (a-state)  
    [daxala baytahu]{.trn}  
    "He entered his house."
  + [فِي بَيْتِهِ.]{.ar} (i-state)  
    [fI baytihi]{.trn}  
    "in his house"
+ With the pronoun [ـِي]{.ar} [-I]{.trn}, the first noun in the noun-chain will generally appear the same in all states. For example,
  + [بَيْتِي كَبِيرٌ]{.ar} (u-state)  
    [baytI kabIrun.]{.trn}  
    "My house is big."
  + [دَخَلَ بَيْتِي.]{.ar} (a-state)  
    [daxala baytI]{.trn}  
    "He entered my house."
  + [فِي بَيْتِي]{.ar} (i-state)  
    [fI baytI]{.trn}  
    "in my house"
+ We have mentioned that when a dual noun or sound [Un]{.trn} plural noun is first noun in a noun-chain its [ن]{.ar} is dropped. This rule remains valid when the last noun in the noun-chain is an attached pronoun. So we get:
  + [بَيْتَاهُ]{.ar}  
    [baytAhu]{.trn}  
    "his two houses"
  + [إِلَىٰ بَيْتَيْهِمَا]{.ar}  
    [EilA baytayhimA]{.trn}  
    "to their~dual~ two houses"
  + [مُعَلِّمُوكَ]{.ar}  
    [mueallimUka]{.trn}
    "your~sing.\ masc.~ (male) teachers"
  + [مِنْ مُعَلِّمِيهِ]{.ar}  
    [min mueallimIhi]{.trn}  
    "from his (male) teachers"

+ With dual nouns and sound [Un]{.trn} plural nouns, when the last noun in the noun-chain is [ـِي]{.ar} [-I]{.trn} "my", the [ـِي]{.ar} [-I]{.trn} becomes a [يَ]{.ar} [ya]{.trn} when preceded by an unvowelled [ا]{.ar} [Ealif]{.trn2} or [ي]{.ar} [yAE]{.trn2}. The [يَ]{.ar} gets doubled when preceded by an unvowelled [ي]{.ar}. Examples:
  + [مُعَلِّمَايَ طَيِّبَانِ.]{.ar}  
    [mueallimAya TayyibAni.]{.trn}  
    "My two (male) teachers are good."
  + [مِنْ مُعَلِّمَيَّ]{.ar}  
    [min mueallimayya]{.trn}  
    "from my two (male) teachers"
  + [إِلَىٰ مُعَلِّمِيَّ]{.ar}  
    [EilA mueallimiyya]{.trn}  
    "to my (male) teachers"

+ As a special rule, however, when the sound [Un]{.trn} plural is in the u-state and is the first-noun in a noun-chain followed by [ـِي]{.ar} [-I]{.trn} "my", the ending will not become [ـُويَ]{.ar} [-Uya]{.trn} as we might expect. Instead, it will become identical to the a-state and i-state [ـِيَّ.]{.ar} [-iyya]{.trn}. For example:
  + [مُعَلِّمِيَّ طَيِّبُونَ.]{.ar}  
    [mueallimiyya TayyibUna.]{.trn}  
    "My (male) teachers~pl.~ are good."

+ Pronouns are always definite. So when a pronoun is the last noun in a noun-chain, all preceding nouns will be definite. This is important to know because if a describer is to be used for any of the preceding nouns, it will be definite too and will therefore have [ٱَلْ]{.ar}. Examples:
  + [بَيْتِي ٱلْكَبِيرُ وَاسِعٌ.]{.ar}  
    [bayti -lkabIru wAsieun.]{.trn}  
    "My big house is spacious."
  + [قَرَءَا كِتَابَيْهِمَا ٱلْجَدِيدَيْنِ.]{.ar}  
    [qaraEA kitAbayhima -ljadIdayni.]{.trn}  
    "They~dual~ read their two new books."
  + [مُعَلِّمِيَّ ٱلْكِرَامُ فِي مَدْرَسَتِهِمُ ٱلْقَدِيمَةِ.]{.ar}  
    [mueallimiyya -lkirAmu fI madrasatihimu -lqadImati.]{.trn}  
    "My noble (male) teachers are in their old school."

  By the way, describers will obviously only be for nouns preceding the pronoun and never for the pronoun itself.
-->

## Annexations with "and"

### Multiple annexe nouns and one base noun

In English we can have an expression like "the pen and the book of the boy" = "the boy's pen and book". In this sentence there are two annexe nouns and one base noun.

In order to express this in Arabic, we will say:

[قَلَمُ ٱلْغُلَامِ وَكِتَابُهُ]{.ar}  
[qalamu -lgulAmi wa kitAbuhu]{.trn}  
"the boy's pen and his book" = "the boy's pen and book"

Note that the annexation is not broken by the insertion of [وَ]{.ar} [wa]{.trn} "and". Rather a second annexation is used and the two are separated by [وَ]{.ar} [wa]{.trn} "and". This is the preferred way of expressing such expressions.

There is another, less preferred way of expressing this. And this is by breaking the first annexation and inserting [وَ]{.ar} [wa]{.trn} "and":

[قَلَمُ وَكِتَابُ ٱلْغُلَامِ]{.ar}  
[qalamu wa kitAbu -lgulAmi]{.trn}  
"the boy's pen and book"

This second method is not considered as eloquent. Some even consider it incorrect. So we advise you to use the first method whenever possible.

#### With pronouns

If the base noun in the first annexation is replaced with a pronoun then only the first method is allowed. For example,

[قَلَمُهُ وَكِتَابُهُ]{.ar}  
[qalamuhu wakitAbuhu]{.trn}  
"his pen and his book"

### One annexe noun and multiple base nouns

We can also have expressions like "the house of the boy and the girl". In this sentence there is one annexe noun and two base nouns.

To express this in Arabic we will say:

[بَيْتُ ٱلْغُلَامِ وَٱلْجَارِيَةِ]{.ar}  
[baytu -lgulAmi wa-ljAriyati]{.trn}  
"the house of the boy and the girl"

Note that both 
[ٱلْغُلَامِ]{.ar} [EalgulAmi]{.trn} and [ٱَلْجَارِيَةِ]{.ar} [EaljAriyati]{.trn} are in the i-state because they are both base nouns in the annexation.

#### With pronouns

If one or both of the base nouns in the annexation is replaced with a pronoun then the first noun must be repeated. For example,

[بَيْتُ ٱلْغُلَامِ وَبَيْتُهَا]{.ar}  
"the boy's house and her house"

[بَيْتُهُ وَبَيْتُهَا]{.ar}  
[baytuhu wabaytuhA]{.trn}  
"his house and her house"

<!--
However, it must be said that these expressions are ambiguous because they could be interpreted to mean that there are two houses: one that is "his" and the second that is "her's". One way to remove this ambiguity, when only a single house is intended, is to use the dual pronoun instead:

[بَيْتُهُمَا]{.ar}  
[baytuhumA]{.trn}  
"their~dual~ house"

## Non-possessive noun-chains

piece of bread, man of wealth, rule of law, nahru -lEurdunn

-->

## Usage of the annexation

### Primarily belonging

### [نحو، مثل، شبه]{.ar}

Don't become definite when annexed to pronoun

### [نفس]{.ar} "self"

[ضَرَبا أنفسهما]{.ar}

[قالت لِي نَفسي]{.ar}

### annexation of material

[خاتمُ ذَهَبٍ]{.ar}

[خاتمٌ ذَهَبٌ]{.ar}

[خاتمٌ مِن ذَهَبٍ]{.ar}

### [مَدينَةُ دَمشق]{.ar}

### [مجرد ترفيه]{.ar}


<!--chapter:end:srcrmd/idafa.Rmd-->

# Irregular nouns

## Introduction

There are some nouns in Arabic which are _irregular_ and behave a little differently than other _regular_ nouns. In this chapter we will study these irregular nouns.

## The five nouns

There are five nouns in Arabic which are irregular in the same basic way. Collectively, they are called "the five nouns".
They behave a little differently from regular nouns in how they display their state.

We have learned that regular nouns have three states: the u-state, a-state, and i-state. For singular nouns, the u-state is marked by the [u]{.trn}-mark [◌ُ]{.ar}, the a-state is marked by the [a]{.trn}-mark [◌َ]{.ar}, and the i-state is marked by the [i]{.trn}-mark [◌ِ]{.ar}. The [n]{.trn}-marks [◌ٌ]{.ar}, [◌ً]{.ar} and [◌ٍ]{.ar} are only but extensions of [◌ُ]{.ar}, [◌َ]{.ar}, and [◌ِ]{.ar} respectively.

We now present the five irregular nouns that behave differently.

### [أَبٌ]{.ar} [Eab]{.trn}, [أَخٌ]{.ar} [Eax]{.trn}, and [حَمٌ]{.ar} [Ham]{.trn}

The first three nouns that we will talk about are:

i. [أَب]{.ar} [Eab]{.trn} "a father"        (root: [أبو]{.arroot}) 
i. [أَخ]{.ar} [Eax]{.trn} "a brother"       (root: [أخو]{.arroot}) 
i. [حَم]{.ar} [Ham]{.trn} "a father-in-law" (root: [حمو]{.arroot}) 

The final root letter of all three of these nouns is [و]{.ar}. However, irregularly, it is omitted in most formations of the word. It does resurface in some cases as we will describe below.

Without the final root letter [و]{.ar}, these nouns display their state like regular nouns. Here are some examples:

[لِلْجَارِيَةِ أَبٌ كَبِيرٌ وَأَخٌ صَغِيرٌ.]{.ar}  
[liljAriyati Eabun kabIrun waEaxun SagIr]{.trn}  
"The girl has an old father and a young brother."

[ضَرَبَ ٱلْغُلَامُ أَخًا لَهُ.]{.ar}  
[Daraba -lgulAmu Eaxan lahu.]{.trn}  
"The boy beat a brother of his."

[ٱَلْحَمُ وَٱلْأَبُ فِي بَيْتِ ٱلْأَخِ.]{.ar}  
[EalHamu walEabu fI bayti -lEax.]{.trn}  
"The father-in-law and the father are in the brother's house."

Where the nouns behave irregularly is when they are an annexe noun in an annexation. Then instead of displaying their state with [◌ُ]{.ar}, [◌َ]{.ar}, and [◌ِ]{.ar}, they display their state using the long vowels [و]{.ar} [U]{.trn}, [ا]{.ar} [A]{.trn}, and [ي]{.ar} [I]{.trn} instead. Here are some examples:

[هُوَ أَخُو ٱلْجَارِيَةِ.]{.ar}  
[huwa Eaxu -ljAriyah]{.trn}  
"He is the girl's brother."
<!--
[زَيدٌ أَخُو عَمْرٍو.]{.ar}  
[zaydun EaxU eamrin.]{.trn}  
"Zayd is [#eamr]{.trn2}'s brother."
-->

[سَأَلْتُ أَبَا صَدِيقِي عَنْ أَمْرٍ.]{.ar}  
[saEaltu EabA SadIqI ean Eamr.]{.trn}  
"I asked my friend's father about a matter."

<!--
[شَكَرْتُ لِحَمِي زَيْدٍ.]{.ar}  
[cakartu liHamI zaydin.]{.trn}  
"I thanked Zayd's father-in-law."
-->

[ذَهَبْتُ إِلَىٰ بَيْتِ حَمِي ٱلرَّجُلِ.]{.ar}  
[pahabtu EilA bayti Hami -rrajul.]{.trn}  
"I went to the man's father-in-law's house."

When these nouns are annexed to attached pronouns, then in most cases they will behave as above. So, for example,

[أَبُوهُ]{.ar}  
[EabUhu]{.trn}  
"his father" (u-state).

[أَخَانَا]{.ar}  
[EaxAnA]{.trn}  
"our brother" (a-state).

However, if the attached pronoun is [ي]{.ar} (for the singular speaker participant), then in that case, the attached pronoun [ي]{.ar} attaches to the annexe noun directly, without any intervening long vowel:

<!--
Even when the base noun in the noun-chain is an attached pronoun, these nouns behave in this irregular way, except if the attached pronoun is for the speaking person [ي]{.ar}. In that case, the attached pronoun [ي]{.ar} attaches to the annexe noun directly, without any intervening long vowel. Examples:
-->

[أَخِي]{.ar}  
[EaxI]{.trn}  
"my brother" (u-state, a-state, and i-state).

[أَبِي]{.ar}  
[EabI]{.trn}  
"my father" (u-state, a-state, and i-state).

[حَمِي]{.ar}  
[HamI]{.trn}  
"my father-in-law" (u-state, a-state, and i-state).

Here are some more examples in sentences:

[أَخُوهُ طَوِيلٌ وَأَخُوهَا قَصِيرٌ وَأَخِي كَبِيرٌ.]{.ar}  
[EaxUhu TawIlun waEaxUhA qaSIrun waEaxI kabIr.]{.trn}  
"His brother is tall and her brother is short and my brother is big."

[سَأَلَ أَخَاهُمْ وَأَخَانَا.]{.ar}  
[saEaltu EaxAhum waEaxAnA.]{.trn}  
"I asked their~m,3+~ brother and our brother."

[شَكَرَ أَخِي أَبِي.]{.ar}  
[cakara EaxI EabI.]{.trn}  
"My brother thanked my father."

[ذَهَبْتُ إِلَىٰ بَيْتِ أَخِيهِنَّ.]{.ar}  
[pahabtu EilA bayti EaxIhinn.]{.trn}  
"I went to their~f,3+~ brother's house."

The above irregular behavior of these three nouns is only when they are annexe nouns. When they happen to be base nouns in annexations, then they again they behave like regular nouns and their state is displayed by the short vowel marks [◌ُ]{.ar}, [◌َ]{.ar}, and [◌ِ]{.ar}, when definite, and by the [n]{.trn}-marks 
[◌ٌ]{.ar}, 
[◌ً]{.ar}, and
[◌ٍ]{.ar}, when indefinite.
. Examples:

[بَيْتُ ٱلْأَخِ كَبِيرٌ.]{.ar}  
[baytu -lEaxi kabIr.]{.trn}  
"The brother's house is big."

[ذَهَبْتُ إِلَىٰ بَيْتِ أَخٍ.]{.ar}  
[pahabtu EilA bayti Eax.]{.trn}  
"I went to a brother's house."

When these nouns form their duals and plurals, then the final root letter [و]{.ar} is resurfaces.
In forming the broken plural, the final root letter [و]{.ar}, being a weak letter, sometimes converts to a [ء]{.ar}.
The following table shows their duals and plurals.

|Word | Dual (u-state) | Dual (a-state and i-state)|Plural|
|:-|:--|:---|:---|
|[أَب]{.ar} [Eab]{.trn}|[أَبَوَانِ]{.ar} [EabawAni]{.trn}|[أَبَوَيْنِ]{.ar} [Eabawayni]{.trn}|[آبَاء]{.ar} [EAbAE]{.trn}|
|[أَخ]{.ar} [Eax]{.trn}|[أَخَوَانِ]{.ar} [EaxawAni]{.trn}|[أَخَوَيْنِ]{.ar} [Eaxawayni]{.trn}|[إِخْوَة]{.ar} [Eixwah]{.trn}, [إِخْوَان]{.ar} [EixwAn]{.trn}|
|[حَم]{.ar} [Ham]{.trn}|[حَمَوَانِ]{.ar} [HamawAni]{.trn}|[حَمَوَيْنِ]{.ar} [Hamawayni]{.trn}|[أَحْمَاء]{.ar} [EaHmAE]{.trn}|

One special note regarding the dual [أَبَوَانِ]{.ar}/[أَبَوَيْنِ]{.ar}: in addition to meaning "two fathers", they can also mean "both parents", i.e., "a father and a mother". Here are examples of these words in sentences:

[ذَهَبَ ٱلْأَخَوَانِ إِلَى ٱلْمَسْجِدِ.]{.ar}  
[pahaba -lEaxawAni fi -lmasjidi.]{.trn}  
"The brothers~2~ went to the mosque."

[سَأَلْتُ أَخَوَيَّ عَنْ أَمْرٍ]{.ar}  
[saEaltu Eaxawayya ean Eamrin.]{.trn}  
"I asked my brothers~2~ about a matter."

[شَكَرْتُ لِأَبَوَيْهِ]{.ar}  
[cakartu liEabawayhi.]{.trn}  
"I thanked his parents."

### [ذُو]{.ar} [pU]{.trn} and [ذَات]{.ar} [pAt]{.trn} {#zu}

The fourth irregular noun from "the five nouns" is the masculine noun [ذُو]{.ar} [pU]{.trn} and its feminine counterpart [ذَات]{.ar} and [pAt]{.trn}. The words [ذُو]{.ar} [pU]{.trn} and [ذَات]{.ar} [pAt]{.trn} mean "owner of" or "possessor of". 

So, for example, [ذُو ٱلْمَالِ]{.ar} [pu -lmAli]{.trn} means "possessor~m~ of wealth" or "wealthy person~m~". The singular, dual, and plural of [ذُو]{.ar} [pU]{.trn} in all three states is shown in the table below:

|State|Singular|Dual|Plural|
|:--|:---|:---|:---|
|u-state|[ذُو]{.ar} [pU]{.trn} |[ذَوَا]{.ar} [pawA]{.trn}|[ذَوُو]{.ar} [pawU]{.trn}|
|a-state|[ذَا]{.ar} [pA]{.trn} |[ذَوَيْ]{.ar} [paway]{.trn}|[ذَوِي]{.ar} [pawI]{.trn}|
|i-state|[ذِي]{.ar} [pI]{.trn} |same as a-state|same as a-state|

The noun [ذُو]{.ar} [pU]{.trn} and its duals and plurals are only ever used as annexe nouns in annexations. Furthermore, they may not be annexed to pronouns. Here are some examples:

[ٱَلرَّجُلُ ذُو ٱلْمَالِ.]{.ar}  
[Earrujulu pu -lmAl.]{.trn}  
"The man is the possessor of wealth." = "This man is wealthy."

The word [ذَات]{.ar} is the feminine of [ذُو]{.ar}. When used as an annexe noun, its states, duals, and plurals are as in the table below:

|State|Singular|Dual|Plural|
|:--|:---|:---|:---|
|u-state|[ذَاتُ]{.ar} [pAtu]{.trn} |[ذَوَاتَا]{.ar} [pawAtA]{.trn} |[ذَوَاتُ]{.ar} [pawAtu]{.trn}|
|a-state|[ذَاتَ]{.ar} [pAta]{.trn} |[ذَوَاتَيْ]{.ar} [pawAtay]{.trn}|[ذَوَاتِ]{.ar} [pawAti]{.trn}|
|i-state|[ذَاتِ]{.ar} [pAti]{.trn} |same as a-state|same as a-state|

Examples:

[هَـٰذِهِ ٱلشَّجَرَةُ ذَاتُ ثَمَرٍ كَثِيرٍ.]{.ar}  
[hApihi -ccajaratu pAtu vamarin kavIrin.]{.trn}  
"This tree is the possessor of much fruit." = "This tree is very fruitful."

As opposed to [ذُو]{.ar} which is only an annexe noun, [ذَات]{.ar} may be used a noun in its own right. In this case it means "personality" or "essence". This usage is often found in theological or philosophical works. And, as such, unlike [ذُو]{.ar} which can't be annexed to attached pronouns, [ذَات]{.ar} can be annexed to attached pronouns. Examples:

### [فَم]{.ar} [fam]{.trn}

The fifth of "the five nouns" is [فَم]{.ar} [fam]{.trn} "a mouth". It is the most irregular of "the five nouns".

In some ways, the word [فَم]{.ar} [fam]{.trn} is regular. It is only irregular when it is a singular annexe noun. Let's first see its regular bahavior.

[عَلَى ٱلْوَجْهِ فَمٌ وَفِي ٱلْفَمِ لِسَانٌ.]{.ar}  
[eala -lwajhi famun wafi -lfami lisAn]{.trn}  
"On the face is a mouth, and in the mounth is a tongue."

It is a base noun in an annexation regularly:

[نَطَقَ لِسَانُ ٱلْفَمِ.]{.ar}  
[naTaqa lisAnu -lfam.]{.trn}  
"The mouth's tongue articulated [speech]."

It forms duals regularly, which are used in annexations regularly

[فَمَا ٱلنَّهْرَيْنِ كَبِيرَانِ.]{.ar}  
[fama -nnahrayni kabIrAni.]{.trn}  
"The mouths~2~ of the rivers~2~ are big."

Let's now see its irregular behavior.

When [فَم]{.ar} is a singular annexe noun, then it is usual for it to follow the example of the rest of the five nouns.

<!--
In addition to the above regular behavior of [فَمٌ]{.ar} [famun]{.trn} "mouth", when the word is singular and is the first noun in a noun-chain, it is common to replace it with [فُو]{.ar} [fU]{.trn}. This is also done when the second noun in the noun-chain is a pronoun. 

The three states of the singular [فُو]{.ar} [fU]{.trn} are shown in the table below:
-->

Here is how it will appear as a singular annexe noun in the three states:

|u-state|a-state|i-state|
|:---|:---|:---|
|[فُو]{.ar} [fU]{.trn} |[فَا]{.ar} [fA]{.trn} |[فِي]{.ar} [fI]{.trn}|

Examples of usage:

[فُو ٱلنَّهْرِ كَبِيرٌ.]{.ar}  
[fu -nnahri kabIr.]{.trn}  
"The mouth of the river is big."

[فُوهَا جَمِيلٌ.]{.ar}  
[fUhA jamIl.]{.trn}  
"Her mouth is beautiful."

[فَتَحَ فَاهُ.]{.ar}  
[fataHa fAh.]{.trn}  
"He opened his mouth."

[جَعَلَتِ ٱلْأُمُّ لُقْمَةَ طَعَامٍ فِي فِي ٱبْنَتِهَا.]{.ar}  
[jaealati -lEummu luqmata TaeAmin fI fi -bnatihA.]{.trn}  
"The mother put a morsel of food in her daughter's mouth."

When the attached pronoun for the speaking person [ي]{.ar} is attached to [فُو]{.ar} [fU]{.trn}, [فَا]{.ar} [fA]{.trn}, or [فِي]{.ar} [fI]{.trn} the combination is always [فِيَّ]{.ar} [fiyya]{.trn} in all three states. Examples:

[فِيَّ مَفْتُوحٌ.]{.ar}  
[fiyya maftUh.]{.trn}  
"My mouth is open."

[فَتَحْتُ فِيَّ.]{.ar}  
[fataHtu fiyy.]{.trn}  
"I opened my mouth."

[أَكَلْتُ بِفِيَّ.]{.ar}  
[Eakaltu bifiyy.]{.trn}  
"I ate with my mouth."

In addition to the above irregular behavior, it is permissible, but less common, to treat [فَم]{.ar} regularly as an annexe noun in an annexation. So it is permissible to also say:

[فَمُ ٱلنَّهْرِ كَبِيرٌ.]{.ar}  
[famu -nnahri kabIr.]{.trn}  
"The river's mouth is big."

[فَمِي مَفْتُوحٌ.]{.ar}  
[famI maftUhun.]{.trn}  
"My mouth is open."

[فَمُهَا جَمِيلٌ.]{.ar}  
[famuhA jamIlun.]{.trn}  
"Her mouth is beautiful."

[فَتَحَ فَمَهُ.]{.ar}  
[fataHa famahu.]{.trn}  
"He opened his mouth."

[جَعَلَتِ ٱلْأُمُّ لُقْمَةَ طَعَامٍ فِي فَمِ ٱبْنَتِهَا.]{.ar}  
[jaealati -lEummu luqmata TaeAmin fI fami -bnatihA.]{.trn}  
"The mother put a morsel of food in her daughter's mouth."

<!--
As mentioned above, [فُو]{.ar} [fU]{.trn} typically only replaces [فَمٌ]{.ar} [famun]{.trn} "mouth", when the word is singular and is the first noun in a noun-chain. Otherwise, [فَمٌ]{.ar} [famun]{.trn} continues to be used.
-->

The other irregularity of [فَم]{.ar} [fam]{.trn} "a mouth" is that its broken plural is 
[أَفْواه]{.ar} [EafwAh]{.trn}.

Note that the letter [م]{.ar} has not been used to form the broken plural, and instead a [و]{.ar}, and a [ه]{.ar} are used to form it.

## Other irregular nouns

There are more nouns that have irregularity in their own ways. We will discuss them below.

### [أُولُو]{.ar} [EulU]{.trn} and [أُولَات]{.ar} [EulAt]{.trn}

[أُولُو]{.ar} [EulU]{.trn} 
(first syllable has a short vowel with a silent [و]{.ar}) 
means "people~m~ of". It is only used as a masculine plural annexe noun, similar in meaning to
[ذَوُو]{.ar} [pawU]{.trn} which we discussed in section\ \@ref(zu) above.
There is no singular or dual of this noun.

Here is its form in the different states:

|u-state|a-and i-state|
|:---|:---|
|[أُولُو]{.ar} [EulU]{.trn}| [أُولِي]{.ar} [EulI]{.trn}|

Example:

[لِأُولِي ٱلْأَرْحَامِ حُقُوقٌ.]{.ar}  
[liEuli -lEarHAmi HuqUq.]{.trn}  
"The people of the wombs (i.e. blood relatives) have rights."

The feminine counterpart of
[أُولُو]{.ar} [EulU]{.trn} 
is
[أُولَات]{.ar} [EulAt]{.trn} "women of".
The first syllable again has a short vowel with a silent [و]{.ar}.

|u-state|a-and i-state|
|:---|:---|
|[أُولَاتُ]{.ar} [EulAtu]{.trn}| [أُولَاتِ]{.ar} [EulAti]{.trn}|

[لِأُولَاتِ ٱلْحَمْلِ حُقُوقٌ عَلَىٰ بُعُولَتِهِنَّ.]{.ar}  
[liEulAti -lHamli HuqUq ealA bueUlatihinn.]{.trn}  
"The women of pregnancy (i.e. pregnant women) have rights upon their husbands."

### [أُمّ]{.ar} [Eumm]{.trn}

The noun 
[أُمّ]{.ar} [Eumm]{.trn} "a mother"
forms two [At]{.trn} sound plural variants:

i. [أُمَّهَات]{.ar} [EummahAt]{.trn}
i. [أُمَّات]{.ar} [EummAt]{.trn}

The first variant
[أُمَّهَات]{.ar} [EummahAt]{.trn}
is more commonly used.
Example:

[أُمَّاهَاتُ ٱلْغِلْمَانِ طَيِّبَاتٌ.]{.ar}  
[EummahAtu -lgilmAni TayyibAt.]{.trn}  
"The boys' mothers are good."

### [سَنَة]{.ar} [sanah]{.trn}

The noun 
[سَنَة]{.ar} [sanah]{.trn} "a year"
forms both an [At]{.trn} sound plural
and an [Un]{.trn} sound plural.
(Remember from 
section\ \@ref(applicability-of-the-un-sound-plural)
that a few nouns that don't denote male intelligent beings have [Un]{.trn} sound plurals.)

In both plurals, the singular noun is modified irregularly.

|Singular |[At]{.trn} sound plural |[Un]{.trn} sound plural (u-state) |[Un]{.trn} sound plural (a- and i-states)|
|:--|:---|:---|:---|
|[سَنَة]{.ar} [sanah]{.trn} |[سَنَوَات]{.ar} [sanawAt]{.trn} |[سِنُونَ]{.ar} [sinUna]{.trn} |[سِنِينَ]{.ar} [sinIna]{.trn}|

Either of the two plurals may be used interchangeably.
Here are some examples:

### [مَاء]{.ar} [mAE]{.trn}

[مَاء]{.ar} [mAE]{.trn} "a water" forms its broken plural irregularly: [مِيَاه]{.ar} [miyAh]{.trn} "waters".

### [شَفَة]{.ar} [cafah]{.trn}

[شَفَة]{.ar} [cafah]{.trn} "a lip"
forms its broken plural irregularly: [شِفَاه]{.ar} [cifAh]{.trn} "lips".

Also, despite ending in the feminine marker [ة]{.ar}, it does not form an [At]{.trn} sound plural.

### [ٱِبْن]{.ar} [Eibn]{.trn}, [ٱِبْنَة]{.ar} [Eibnah]{.trn}, and [بِنْت]{.ar} [bint]{.trn}

The noun 
[ٱِبْن]{.ar} [Eibn]{.trn} "a son" is from the root [بنو]{.arroot}.
It has two feminine counterparts:

i. [ٱِبْنَة]{.ar} [Eibnah]{.trn}
i. [بِنْت]{.ar} [bint]{.trn}

which mean "a daughter".

[ٱِبْن]{.ar} [Eibn]{.trn} "a son"
forms both a broken plural
and an [Un]{.trn} sound plural.

Its broken plural is [أَبْنَاء]{.ar} [EabnAE]{.trn} "sons". 

In forming the 
[Un]{.trn} sound plural,
the singular noun is modified irregularly:

|Singular |[Un]{.trn} sound plural (u-state) |[Un]{.trn} sound plural (a- and i-states)|
|:--|:---|:---|
|[ٱِبْن]{.ar} [Eibn]{.trn} |[بَنُونَ]{.ar} [banUna]{.trn} |[بَنِينَ]{.ar} [banIna]{.trn} |

The feminine
[ٱِبْنَة]{.ar}
and
[بِنْت]{.ar}
"a daughter"
form the irregular [At]{.trn} sound plural
[بَنَات]{.trn} [banAt]{.trn} "daughters".
Note that 
[بَنَات]{.ar} [banAt]{.trn}
is not a broken plural from the root [بنت]{.arroot}. Therefore, it obeys the rules of [At]{.trn} sound plurals and does not end with [◌َ]{.ar} or [◌ً]{.ar} in the a-state.

Here are some examples using these nouns:


<!--
## Nouns that begin with connecting [hamzah]{.trn2}

When the definite article [ٱَلْ]{.ar} [Eal]{.trn} is prefixed to a noun which begins with a connecting [hamzah]{.trn2}, the [hamzah]{.trn2} is not pronounced. Instead the [lAm]{.trn} in [ٱَلْ]{.ar} will take an [i]{.trn}-mark. For example, [ٱِبْنٌ]{.ar} [Eibnun]{.trn} "a son" becomes [ٱَلِٱبْنُ]{.ar} [Ealibnu]{.trn} "the son".
-->
### [نَاس]{.ar} [nAs]{.trn}, and [أُنَاس]{.ar} [EunAs]{.trn}

[نَاس]{.ar} [nAs]{.trn}
and
[أُنَاس]{.ar} [EunAs]{.trn}
are from the root [أنس]{.arroot}.
They both mean "a people".

When indefinite, only 
[أُنَاس]{.ar} [EunAs]{.trn}
tends to be used, and
[نَاس]{.ar} [nAs]{.trn}
tends to be unused.

When definite, only
[ٱَلنَّاس]{.ar} [EannAs]{.trn}
tends to be used, and
[ٱَلْأُنَاس]{.ar} [EalEunAs]{.trn}
is unused.

Here are some examples using these nouns:

### The nouns [ٱِمْرَأ]{.ar} and [ٱِمْرَأَة]{.ar}

The nouns 
[ٱِمْرَأ]{.ar} [EimraE]{.trn} (masc.) "a man, a person" and 
[ٱِمْرَأَة]{.ar} [EimraEah]{.trn} (fem.) "a woman" 
are quite irregular.

Firstly, 
[ٱِمْرَأَة]{.ar} [EimraEah]{.trn} "a woman" 
is, from the perspective, of its meaning, the feminine counterpart of
[رَجُل]{.ar} [rajul]{.trn} "a man (male human being)".

[ٱِمْرَأ]{.ar} [EimraE]{.trn}, on the other hand, only means "a man" in a general sense. For example, in the sentence "A man is only as good as his word." It can also be translated as "a person".

Secondly, 
[ٱِمْرَأ]{.ar} [EimraE]{.trn} "a man, a person" has no plural.
[نَاس]{.ar}/[أُنَاس]{.ar} "a people" and [قَوْم]{.ar} "a population" may be used when a plural is required.

[ٱِمْرَأَة]{.ar} [EimraEah]{.trn} "a woman" irregularly forms the broken plurals 
[نِسَاء]{.ar} [nisAE]{.trn} and [نِسْوَة]{.ar} [niswah]{.trn} "women". The former
([نِسَاء]{.ar} [nisAE]{.trn}) is more commonly used.

Like [شَفَة]{.ar} [cafah]{.trn}
it also, despite ending in the feminine marker [ة]{.ar}, does not form an [At]{.trn} sound plural.

Thirdly, both nouns are very irregular in how they become definite nouns with [ٱَلْ]{.ar}.
When [ٱَلْ]{.ar} is prefixed to these nouns to make them definite, they lose the initial connecting [hamzah]{.trn2} and change their internal vowels. This table shows what we mean:

State         | Definite of [ٱِمْرَأ]{.ar}     | Definite of [ٱِمْرَأَة]{.ar}
:-------------|:----------------------------|:----------------------------
u-state       |[ٱَلْمَرْءُ]{.ar} [EalmarEu]{.trn}|[ٱَلْمَرْأَةُ]{.ar} [EalmarEatu]{.trn}
a-state       |[ٱَلْمَرْءَ]{.ar} [EalmarEa]{.trn}|[ٱَلْمَرْأَةَ]{.ar} [EalmarEata]{.trn}
i-state       |[ٱَلْمَرْءِ]{.ar} [EalmarEi]{.trn}|[ٱَلْمَرْأَةِ]{.ar} [EalmarEati]{.trn}

The masculine noun
[ٱِمْرَأ]{.ar} [EimraE]{.trn}
has an additional irregularity.
When it is indefinite, it irregularly displays its state, not only on its final letter [ء]{.ar}, but also on the letter before it [ر]{.ar}. 

It is also permissible for it to behave regularly by displaying its state on its final letter only, but this is not as commonly used.

This table shows what we mean:

State         | Regular indefinite (less common) | Irregular indefinite (more common)
:-------------|:-----------------|:--------------
u-state       |[ٱِمْرَأٌ]{.ar} [EimraEun]{.trn} |[ٱِمْرُؤٌ]{.ar} [EimruEun]{.trn}
a-state       |[ٱِمْرَءًا]{.ar} [EimraEan]{.trn}|[ٱِمْرَءًا]{.ar} [EimraEan]{.trn}
i-state       |[ٱِمْرَأٍ]{.ar} [EimraEin]{.trn} |[ٱِمْرِئٍ]{.ar} [EimriEin]{.trn}

Here are some examples of these nouns:


<!--chapter:end:srcrmd/irregular_nouns.Rmd-->

# Proper nouns

## Introduction

Proper nouns are also known as names. Here are some examples of Arabic names:

| Men's |names | Women's |names |
|--:|:---|--:|:---|
|[مُحَمَّد]{.ar}         |[#muHammad]{.trn2}      | ^2^[عَائِشَة]{.ar}     |[#eAEicah]{.trn2} |
|[سَعِيد]{.ar}         |[#saeId]{.trn2}         | ^2^[فَاطِمَة]{.ar}     |[#faTimah]{.trn2} |
|[ٱَلْحَسَن]{.ar}        |[al-#Hasan]{.trn2}      | ^2^[حَفْصَة]{.ar}      |[#HafSah]{.trn2} |
|[ٱَلنُّعْمَان]{.ar}      |[al-#nuemAn]{.trn2}     | ^2^[سُمَيَّة]{.ar}      |[#sumayyah]{.trn2} |
|^2^[طَلْحَة]{.ar}      |[#TalHah]{.trn2}        | ^2^[جَمِيلَة]{.ar}     |[#jamIlah]{.trn2} |
|^2^[أُسَامَة]{.ar}     |[#usAmah]{.trn2}        | ^2^[زَيْنَب]{.ar}      |[#zaynab]{.trn2} |
|^2^[عُثْمَان]{.ar}     |[#euvmAn]{.trn2}        | ^2^[مَرْيَم]{.ar}      |[#maryam]{.trn2} |
|^2^[عُمَر]{.ar}       |[#eumar]{.trn2}         | ^2^[سُعَاد]{.ar}      |[#sueAd]{.trn2} |
|^2^[إِبْرَاهِيم]{.ar}   |[#ibrAhIm]{.trn2}       | ^2^[أَسْمَاء]{.ar}     |[#asmAE]{.trn2} |
|[عَبْد ٱللَّـٰه]{.ar}    |[#eabd #allAh]{.trn2}   | ^2^[لَيْلَىٰ]{.ar}      |[#laylA]{.trn2} |
|[أَبُو بَكْر]{.ar}      |[#abU #bakr]{.trn2}     | ^2^[أُمّ حَبِيبَة]{.ar}  |[#umm #HabIbah]{.trn2} |

| Place |names | Misc. |names |
|-:|:--|-:|:---|
|^2^[مَكَّة]{.ar}   |Mecca     |^2^[رَمَضَان]{.ar} |[#ramadAn]{.trn2} (a month) |
|^2^[دِمَشْق]{.ar}  |Damascus  |[أُحُد]{.ar}      |[#uHud]{.trn2} (a mountain)    |
|^2^[مِصْر]{.ar}   |Egypt     |[ٱَلنِّيل]{.ar}    |the Nile (a river)             |
|[ٱَلْقَاهِرَة]{.ar}  |Cairo     |[ٱَلْفَاتِحَة]{.ar}  |the [#fAtiHah]{.trn2} (a [sUrah]{.trn2}) |
|[ٱَلْهِنْد]{.ar}    |India     |[ٱَلْجُمُعَة]{.ar}   |Friday                  |

Note the following points from the list abobe:

+ Although some names begin with [ٱَلْ]{.ar}, most don't.
+ Many names are semi-flexible (indicated by ^2^[◌]{.ar}).
+ Some names consist of more than a single word, like [عَبْد ٱللَّـٰه]{.ar}    [#eabd #allAh]{.trn2}

We will explain these and more details regarding proper nouns in this chapter.

## Definiteness of proper nouns

Proper nouns differ from common nouns and adjectival nouns in a couple of important ways:

+ All proper nouns, even if they don't begin with [ٱَلْ]{.ar}, are definite. 
+ A proper noun which does not begin with [ٱَلْ]{.ar}, and which is fully-flexible, shall have an [n]{.trn} mark, despite being definite.

The above points are exemplified in the following sentence:

[ذَهَبْتُ إِلَىٰ بَيْتِ مُحَمَّدٍ ٱلْكَرِيمِ وَزَيْنَبَ ٱلطَّيِّبَةِ.]{.ar}  
[pahabtu EilA bayti muHammadini -lkarImi wazaynaba -TTayyibah.]{.trn}  
"I went to the house of the noble [#muHammad]{.trn2} and the good [#zaynab]{.trn2}."

Note the above from the above example:

+ [مُحَمَّدٍ]{.ar} is fully-flexible so it has an [in]{.trn}-mark [◌ٍ]{.ar} in the i-state.
+ [زَيْنَبَ]{.ar} is semi-flexible so it does not have an [n]{.trn}-mark, and instead has an [a]{.trn} mark [◌َ]{.ar} in the i-state.
+ The proper nouns [مُحَمَّد]{.ar} and [زَيْنَب]{.ar} are describees in descriptive noun phrases.
+ Their describers ([ٱلْكَرِيمِ]{.ar} and [ٱلطَّيِّبَةِ.]{.ar}, respectively) have [ٱَلْ]{.ar} to match the definiteness of the definite proper noun describees. Furthermore, they both end with [◌ِ]{.ar} because they match the i-state of their describees.

## Meanings of names

Many names are re-used from common nouns and adjectival nouns with positive meanings. Examples:

+ [مُحَمَّد]{.ar}         [#muHammad]{.trn2}      "a highly praised one~m~"
+ [سَعِيد]{.ar}         [#saeId]{.trn2}         "a happy (fortunate) one~m~"
+ [ٱَلْحَسَن]{.ar}        [al-#Hasan]{.trn2}      "the good one~m~"
+ [طَلْحَة]{.ar}      [#TalHah]{.trn2}    "an acacia (tree)"
+ [جَمِيلَة]{.ar}     [#jamIlah]{.trn2}   "a beautiful one~f~"

It is possible for these names to sometimes (technically) cause a sentence to have an ambiguous meaning. For example,

[جَلَسَ ٱلْحَسَنُ مَعَ سَعِيدٍ.]{.ar}  
[jalsa -lhasanu maea saeId]{.trn}  
"[al-#Hasan]{.trn2} sat with [#saeId]{.trn2}."  
or  
"The good one~m~ sat with a happy (fortunate) one~m~."  

Context would tell us whether the proper noun or the common/adjectival noun meaning is intended.

Note however the following sentence:

[ذَهَبَتْ جَمِيلَةُ إِلَىٰ ٱلْبَيْتِ.]{.ar}  
[pahabat jamIlatu Eila -lbayt.]{.trn}

This sentence can only be understood to use [جَمِيلَة]{.ar} with its proper noun meaning:

"[#jamIlah]{.trn2} went to the house."

This is because [جَمِيلَة]{.ar} is semi-flexible as a proper noun and fully-flexible as an adjectival/common noun. If [جَمِيلَة]{.ar} were intended to be used with its adjectival/common noun meaning then it would have an [un]{.trn}-mark [◌ٌ]{.ar} and the sentence would be:

[ذَهَبَتْ جَمِيلَةٌ إِلَىٰ ٱلْبَيْتِ.]{.ar}  
[pahabat jamIlatun Eila -lbayt.]{.trn}  
"A beautiful one~f~ went to the house."

We will learn why [جَمِيلَة]{.ar} is semi-flexible as a proper noun in section\ \@ref(proper-nouns-ending-with-looped-ta) below.

## Flexibility of proper nouns

In this section we will discuss the flexibility of proper nouns.
For now, we will deal only with proper nouns that do not begin with [ٱَلْ]{.ar}.
In terms of their flexibility, proper nouns consist of two types:

i. Fully-flexible proper nouns.
i. Semi-flexible proper nouns.

We will treat each of them below.

### Fully-flexible proper nouns

<!--
Fully-flexible proper nouns may or may not begin with [ٱَلْ]{.ar}.

#### Names that begin with [ٱَلْ]{.ar}

If a proper noun begins with [ٱَلْ]{.ar} then the question of its flexibility is pretty much moot. 
This is because noun beginning with with [ٱَلْ]{.ar} display their state fully, regardless of whether or not they are semi-flexible without the [ٱَلْ]{.ar}. Examples:

[ٱَلْحَسَنُ حَفِيدُ رَسُولِ ٱللَّـٰهِ صلى اللّه عليه وسلم.]{.ar}  
"[al-#Hasan]{.trn2} is the grandson of the messenger of [#allAh]{.trn2} (may [#allAh]{.trn2} grant peace and confer blessing upon him)."
(u-state displayed with [◌ُ]{.ar}.)

[سَأَلَ ٱلرَّجُلُ ٱلنُّعْمَانَ عَنْ أَمْرٍ.]{.ar}  
"The man asked [al-#nuemAn]{.trn2} about a matter."  
(a-state displayed with [◌َ]{.ar}.)

[ذَهَبْتُ إِلَى ٱلْقَاهِرَةِ.]{.ar}  
"I went to Cairo."  
(i-state displayed with [◌ِ]{.ar}.)

Examples of names that begin with [ٱَلْ]{.ar} are:

|||||
|--:|:---|--:|:---|
|[ٱَلْحَسَن]{.ar}      |[al-#Hasan]{.trn2}      |[ٱَلْقَاهِرَة]{.ar}    |Cairo
|[ٱَلْحُسَيْن]{.ar}     |[al-#Husayn]{.trn2}     |[ٱَلْهِنْد]{.ar}      |India 
|[ٱَلْعَبَّاس]{.ar}     |[al-#eabbAs]{.trn2}     |[ٱَلصِّين]{.ar}      |China 
|[ٱَلْزُّبَيْر]{.ar}     |[al-#zubayr]{.trn2}     |[ٱَلنِّيل]{.ar}      |the Nile 
|[ٱَلنُّعْمَان]{.ar}    |[al-#nuemAn]{.trn2}     |[ٱَلْفُرَات]{.ar}     |the Euphrates

#### Names that don't begin with [ٱَلْ]{.ar}
-->
For names that don't begin with [ٱَلْ]{.ar}, the default assumption is that they are fully-flexible, unless they fall into one of the categories of semi-flexible nouns (which we will study soon).

Examples of fully-flexible names are:

|||||
|--:|:---|--:|:---|
|[مُحَمَّد]{.ar}         |[#muHammad]{.trn2}  |[مُعَاذ]{.ar}         |[#mueAp]{.trn2}  |
|[نُوح]{.ar}          |[#nUh]{.trn2}       |[سَعْد]{.ar}          |[#saed]{.trn2}   |
|[شُعَيْب]{.ar}         |[#cueayb]{.trn2}    |[عَمَّار]{.ar}         |[#eammAr]{.trn2} |
|[عَلِيّ]{.ar}          |[#ealI]{.trn2}      |[حَسَّان]{.ar}         |[#HassAn]{.trn2} |
|[زَيْد]{.ar}          |[#zayd]{.trn2}      |[سَعِيد]{.ar}         |[#saeId]{.trn2}  | 
|[أَنَس]{.ar}          |[#anas]{.trn2}      |[أُحُد]{.ar}          |[#uHud]{.trn2} (a mountain) |

These are all masculine names.

Examples of sentences with fully-flexible proper nouns:

[زَيْدٌ غُلَامٌ طَيِّبٌّ.]{.ar}  
[zaydun gulAmun Tayyib]{.trn}  
"Zayd is a good boy."

[شَكَرَ أَنَسٌ عَلِيًّا.]{.ar}  
[cakara Eanasun ealiyyA.]{.trn}  
"Anas thanked [#ealI]{.trn2}."

[لَبِسَ سَعِيدٌ قَمِيصَ نُوحٍ ٱلأَخْضَرَ.]{.ar}  
[labisa saeIdun qamISa nUHini -lEaxDar.]{.trn}  
"[#saeId]{.trn2} wore [#nUH]{.trn2}'s green shirt."

### Semi-flexible proper nouns

The rules for the semi-flexibility of proper nouns are a little different from the rules for the semi-flexibility of common nouns and adjectival nouns that we learned in chapter\ \@ref(semi-flexible-nouns).
Proper nouns shall be semi-flexible if they fall under one of the categories below. Note that the categories are not mutually exclusive. That is: some semi-flexible proper nouns will fall into more than one category.

#### Names ending with [ة]{.ar}

All names ending with [ة]{.ar} shall be semi-flexible. This rule is specific to proper nouns. We have already seen that common nouns and adjectival nouns that end ith [ة]{.ar} are fully-flexible.

Most such proper nouns are feminine names. Examples:

|||||
|--:|:---|--:|:---|
|^2^[خَدِيجَة]{.ar}     |[#xadIjah]{.trn2}   |^2^[مَيْمُونَة]{.ar}    |[#maymUnah ]{.trn2} |
|^2^[فَاطِمَة]{.ar}     |[#faTimah]{.trn2}   |^2^[صَفِيَّة]{.ar}      |[#Safiyyah]{.trn2}  |
|^2^[عَائِشَة]{.ar}     |[#eAEicah]{.trn2}   |^2^[خَوْلَة]{.ar}      |[#xawlah]{.trn2}    |
|^2^[سُمَيَّة]{.ar}      |[#sumayyah]{.trn2}  |^2^[جَمِيلَة]{.ar}     |[#jamIlah]{.trn2}   |
|^2^[حَفْصَة]{.ar}      |[#HafSah]{.trn2}    |^2^[آسِيَة]{.ar}      |[#Asiyah]{.trn2}    |

However, some masculine names may end with [ة]{.ar} too:

|||||
|--:|:---|--:|:---|
|^2^[حَمْزَة]{.ar}     |[#Hamzah]{.trn2}   |^2^[مُعَاوِيَة]{.ar}   |[#mueAwiyah ]{.trn2}|
|^2^[أُسَامَة]{.ar}    |[#usAmah]{.trn2}   |^2^[عِكْرِمَة]{.ar}    |[#eikrimah ]{.trn2} |
|^2^[طَلْحَة]{.ar}     |[#TalHah]{.trn2}   |^2^[عُبَادَة]{.ar}    |[#eubAdah]{.trn2}   |

Example:

[طَلْحَةُ ٱلْطَّوِيلُ بَعْلُ جَمِيلَةَ ٱلْكَرِيمَةِ.]{.ar}  
"The tall [#TalHah]{.trn2} is the husband of the generous [#jamIlah]{.trn2}."

#### Names ending with an extrinsic [اء]{.ar} or [ىٰ]{.ar}

Similar to common nouns and adjectival nouns, all names ending with an extrinsic [اء]{.ar} or [ىٰ]{.ar} shall be semi-flexible. These are usually feminine names. Examples:

|||||
|--:|:---|--:|:---|
| ^2^[أَسْمَاء]{.ar}     |[#asmAE]{.trn2}  | ^2^[لَيْلَىٰ]{.ar}      |[#laylA]{.trn2} |
| ^2^[دَرْدَاء]{.ar}     |[#dardAE]{.trn2} | ^2^[سَلْمَىٰ]{.ar}      |[#salmA]{.trn2} |

Examples in sentences:

[ذَهَبَتْ سَلْمَىٰ إِلَىٰ بَيْتِ أَسْمَاءَ.]{.ar}  
"[#salmA]{.trn2} went tp [#asmAE]{.trn2}'s house."

Sentence word order is usually pretty flexible. For stylistic reasons, it is permissible for a doee to precede the doer.
For example,

[سَأَلَتْ دَرْدَاءَ أَسْمَاءُ.]{.ar}  
"[#asmAE]{.trn2} asked [#dardAE]{.trn2}"

But because words that end with [ىٰ]{.ar} never display any state, then for these words the sentence word order becomes more rigid. So the following sentence:

[سَأَلَتْ لَيْلَىٰ سَلْمَىٰ.]{.ar}  
would usually only mean
"[#laylA]{.trn2} asked [#salmA]{.trn2}."

#### Names ending with an extrinsic [ان]{.ar}

All names ending with an extrinsic [ان]{.ar} will be semi-flexible. 

This is somewhat different from the rule we learnt for common noun and adjectival nouns in section\ \@ref(adjectival-noun-an-diptote). There only adjectival nouns of the pattern [فَعْلَان]{.ar} and whose feminine was not formed by adding [ة]{.ar} to it were considered semi-flexible nouns.

Examples:

|||||
|--:|:---|--:|:---|
|^2^[عُثْمَان]{.ar}     |[#euvmAn]{.trn2}  |^2^[رَمَضَان]{.ar}     |[#ramaDAn]{.trn2} |
|^2^[سُفْيَان]{.ar}     |[#sufyAn]{.trn2}  |^2^[شَعْبَان]{.ar}     |[#caebAn]{.trn2}  |

Example:

[جَلَس عُثْمَانُ مَعَ سُفْيَانَ فِي رَمَضَانَ.]{.ar}  
"[#euvmAn]{.trn2} sat with [#sufyAn]{.trn2} in [#ramaDAn]{.trn2}."

#### Names on the pattern [أَفْعَل]{.ar}

All names on the pattern [أَفْعَل]{.ar} shall be semi-flexible. Examples:

|||||
|--:|:---|--:|:---|
|^2^[أَحْمَد]{.ar}     |[#aHmad]{.trn2}  |^2^[أَسْعَد]{.ar}     |[#asead]{.trn2} |

#### Names of the pattern [فُعَل]{.ar}

Names of the pattern [فُعَل]{.ar} shall be semi-flexible. Examples:

|||||
|--:|:---|--:|:---|
|^2^[عُمَر]{.ar}  |[#eumar]{.trn2} |^2^[مُضَر]{.ar}     |[#muDar]{.trn2} |

Interestingly, the fully-flexible name [#eamr]{.trn2} is written with a silent [و]{.ar} at its end: [عَمْرو]{.ar} when in the u- and i-states in order to distinguish it from the more common name [#eumar]{.trn2}. Otherwise, both names would appear identical when written without vowel marks, thus: [عمر]{.ar}.

Name|u-state|a-state|i-state
:-|:--|:--|:--
[#eamr]{.trn2}|[عَمْرٌو]{.ar} [eamrun]{.trn}| [عَمْرًا]{.ar} [eamran]{.trn}|[عَمْرٍو]{.ar} [eamrin]{.trn}
[#eumar]{.trn2}|[عُمَرُ]{.ar} [eumaru]{.trn}| [عُمَرَ]{.ar} [eumara]{.trn}|[عُمَرَ]{.ar} [eumara]{.trn}

#### Names that are originally verbs

Names that are originally verbs are semi-flexible. Examples:

+ ^2^[يَزِيد]{.ar} [#yazId]{.trn2} "He increases"
+ ^2^[يَعِيش]{.ar} [#yaeIc]{.trn2} "He lives"

Their origin as verbs will be apparent when we study incomplete-action verbs.

#### Names of foreign origin

Names of foreign origin are generally semi-flexible. These include the names of angels, many of the previous prophets and messengers, and other persons. Examples:

|||||
|--:|:---|--:|:---|
|^2^[جِبْرِيل]{.ar}    |[#jibrIl]{.trn2}  |^2^[زَكَرِيَّا]{.ar}    |[#zakariyyA]{.trn2}|
|^2^[إِبْرَاهِيم]{.ar}  |[#ibrAhIm]{.trn2} |^2^[يَحْيَىٰ]{.ar}     |[#yaHyA]{.trn2}    |
|^2^[إِسْمَاعِيل]{.ar}  |[#ismAeIl]{.trn2} |^2^[هَاجَر]{.ar}     |[#hAjar]{.trn2}    |
|^2^[إِسْحَاق]{.ar}    |[#isHAq]{.trn2}   |^2^[مَرْيَم]{.ar}     |[#maryam]{.trn2}   |
|^2^[يَعْقُوب]{.ar}    |[#yaeqUb]{.trn2}  |^2^[يَأْجُوج]{.ar}    |[#yaEjUj]{.trn2}   |
|^2^[يُوسُف]{.ar}     |[#yUsuf]{.trn2}   |^2^[مَأْجُوج]{.ar}    |[#maEjUj]{.trn2}   |
|^2^[يُونُس]{.ar}     |[#yUnus]{.trn2}   |^2^[إِبْلِيس]{.ar}    |[#iblIs]{.trn2}    |
|^2^[إِدْرِيس]{.ar}    |[#idrIs]{.trn2}   |^2^[فِرْعَون]{.ar}    |Pharoah            |
|^2^[أَيُّوب]{.ar}     |[#ayyUb]{.trn2}   |^2^[هِرْقَل]{.ar}     |Heraclius          |
|^2^[مُوسَىٰ]{.ar}     |[#mUsA]{.trn2}    |^2^[كِسْرَىٰ]{.ar}     |Chosroes           |
|^2^[عِيسَىٰ]{.ar}     |[#eIsA]{.trn2}    |^2^[قَيْصَر]{.ar}     |Caesar             |

Note that 
^2^[فِرْعَون]{.ar} "Pharoah" 
as ^2^[قَيْصَر]{.ar}     "Caesar",
despite being titles,
are treated as proper names.

The only exception to this rule is a masculine name of foreign origin that comprises of only three letters, and whose middle letter has an [0]{.txt}-mark. Such a name will be fully-flexible. Example:

+ [نُوح]{.ar} [#nUH]{.trn2}

#### Feminine names

All feminine names, regardless of their origin, or their ending, shall be semi-flexible. We have already given examples of semi-flexible feminine names that end with [ة]{.ar}, [اء]{.ar}, and [ىٰ]{.ar}, so we will provide other examples here:

|||||
|--:|:---|--:|:---|
^2^[زَيْنَب]{.ar}      |[#zaynab]{.trn2} |^2^[مَرْيَم]{.ar}      |[#maryam]{.trn2} |
^2^[سُعَاد]{.ar}      |[#sueAd]{.trn2}  |^2^[هَاجَر]{.ar}      |[#hAjar]{.trn2}  |

The only exception to this rule is a feminine name of native Arabic origin, that comprises of only three letters, and whose middle letter has an [0]{.txt}-mark. Such a name is permitted to be optionally fully-flexible or semi-flexible. Examples:

+ [هِنْد]{.ar} Hind
+ [دَعْد]{.ar} [#daed]{.trn2}

Example of usage:

[ذَهَبَتْ هِنْدٌ إِلَىٰ بَيْتِ دَعْدٍ.]{.ar}  
or  
[ذَهَبَتْ هِنْدُ إِلَىٰ بَيْتِ دَعْدَ.]{.ar}  
"Hind went to [#daed]{.trn2}'s house.

## The name [فُلَان]{.ar}

The fully-flexible name [فُلَان]{.ar} is used as a place-holder name in casual conversations. It may be translated into English as "so-and-so". For example,

[ظَلَمَ ٱلرَّجُلُ فُلَانًا وَغَدَرَ بِفُلَانٍ.]{.ar}
"The man wronged so-and-so and he acted treacherously with so-and-so."

For females, the name ^2^[فُلَانَة]{.ar} is used.

[صَدَقَتْ فُلَانَةُ.]{.ar}  
"So-and-so~f~ told the truth."

## The Replacement

Before we proceed with our discussion on proper nouns, we will take a short digression to discuss a grammatical concept called the _replacement_. We will only give a short preview here and will treat it fully in chapter\ \@ref(the-replacement-chapter).

A _replacement_ is a word that follows another word, the _replacee_, and replaces it from the perspective of the grammar of the sentence. The replacement is put in the same state as the replacee.
Here is an example of a sentence with a replacement and a replacee:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-13-1.pdf)<!-- -->

In the above sentence, the word [كِتَابًا]{.ar} "a book" is the replacement of 
[شَيْـًٔا]{.ar} "something". Therefore, it is put in the same a-state.

The replacement is frequently used with proper nouns. For example,

[ذَهَبَ ٱلْغُلَامُ إِلَىٰ بَيْتِ عَمِّهِ عَلِيٍّ.]{.ar}  
"The boy went to his uncle [#ealI]{.trn2}'s house."

In this sentence, the name [عَلِيّ]{.ar} [#ealI]{.trn2} is the replacement of the replacee [عَمّ]{.ar} "uncle". Note, again, that the replacement comes after the replacee and matches it in state. However, the replacement does not need to come directly after the replacee. We can see that there is the pronoun [ه]{.ar} "his" between them.

Here is another example:

[سَأَلَ ٱلطَّالِبُ مُعَاذٌ ٱلْمُعَلِّمَ سَعْدًا.]{.ar}  
"The student [#mueAp]{.trn2} asked the teacher [#saed]{.trn2}."

## Annexed names

So far we have only dealt with proper nouns that are single words. There are some proper nouns that may be formed from two words that are in an annexation. These belong to different categories:

### "Slave of" names

Some names are formed by annexing the noun [عَبْد]{.ar} [eabd]{.trn} "a slave" to one of the names of [#allAh]{.trn2}. The most common of these names are:

+ [عَبْد ٱللَّـٰه]{.ar} [#eabd #allAh]{.trn2} "the Slave of [#allAh]{.trn2}"
+ [عَبْد ٱلرَّحْمَـٰن]{.ar} [#eabd al-#raHmAn]{.trn2} "the Slave of the Most Merciful"

As usual, the base noun shall always be in the i-state. And the state of the annexe noun [عَبْد]{.ar} is variable, depending on it's function in the sentence. Example:

[عَبْدُ ٱللَّـٰهِ هُوَ أَخُو عَبْدِ ٱلرَّحْمَـٰنِ.]{.ar}
"[#eabd #allAh]{.trn2} is the brother of [#eabd al-#raHmAn]{.trn2}."

### "Parent of" names

It is common to call a man, not by his own given name, but rather by calling him the father of one of his children, usually his first born son. For example, if a man named [أَحْمَد]{.ar} "[#aHmad]{.trn2}" had a son named [زَيْد]{.ar} "Zayd", he may be called [أَبُو زَيْد]{.ar} [#abU #zayd]{.trn2} "Zayd's father". Example of usage in a sentence:

[ذَهَبْتُ إِلَىٰ بَيْتِ أَبِي زَيْدٍ.]{.ar}  
"I went to [#abU #zayd]{.trn2}'s house."  
(Note how [زَيْدٍ]{.ar} has an [in]{.trn}-mark [◌ٍ]{.ar} in the i-state because it is fully-flexible.)

While using the name of first-born son is more common, a daughter's name could be used as well. Example,

[سَأَلْتُ أَبَا رُقَيَّةَ سُؤالًا.]{.ar}  
"I asked [#abU #ruqayyah]{.trn2} a question."  
(Note how [رُقَيَّةَ]{.ar} has an [a]{.trn}-mark [◌َ]{.ar} in the i-state because it is semi-flexible.)

Women, too, are similarly called as the mother of one of their children. For example, 
the wife of the Prophet
(may [#allAh]{.trn2} grant peace and confer blessing upon him)
^2^[أُمّ حَبِيبَة]{.ar} [#umm #HabIbah]{.trn2}
was called thus because she had a daughter named
^2^[حَبِيبَة]{.ar}
from a previous marriage.
<!--a woman with a daughter named ^2^[حَبِيبَة]{.ar} could be called ^2^[أُمّ حَبِيبَة]{.ar} [#umm #HabIbah]{.trn2}.-->

By the way, a person need not literally be a father or a mother to be called in such a way. These names may be applied as nicknames.

For example, the Companion of the Prophet
(may [#allAh]{.trn2} grant peace and confer blessing upon him)
was called
^2^[أَبُو هُرَيرَة]{.ar} 
[#abU #hurayrah]{.trn2}
because it is reported that he used to have a pet kitten ([هُرَيْرَة]{.ar}). Here is an example of this name in a sentence.

[أَبُو هُرَيْرَةَ صَحَابِيٌّ جَلِيلٌ.]{.ar}  
"[#abU #hurayrah]{.trn2} is a great Companion."  
(Note how [هُرَيْرَةَ]{.ar} is now considered a semi-flexible proper noun even though it may originally have been derived from the common noun "a kitten".)

Similarly, the Companion [أَبُو بَكْرٍ]{.ar} [#abU #bakr]{.trn2} is not known to have a son named [بَكْر]{.ar}.

It is often the case that a "parent of" name overtakes the actual given name of person in popularity, and becomes the person's name for all intents and purposes. Such is indeed the case for the Companions 
[أَبُو بَكْرٍ]{.ar} [#abU #bakr]{.trn2}
and
^2^[أَبُو هُرَيرَة]{.ar} 
[#abU #hurayrah]{.trn2}.

### "Son of" names

In a manner similar to "parent of" names, a person may be referred to as the son of his parent. For example, the Companion ^2^[عُمَر]{.ar} [#eumar]{.trn2} had a son named 
[عَبْد ٱللَّـٰه]{.ar} [#eabd #allAh]{.trn2}. He is commonly known as ^2^[ٱِبْن عُمَر]{.ar} [#ibn #eumar]{.trn2} "[#eumar]{.trn2}'s son".

Attributing a son to his father is most common. But attributing him to a mother or other ancestor is also possible.

Examples:

+ the Companion [عَمَّار]{.ar} was affectionately called ^2^[ٱِبْن سُمَيَّة]{.ar} [#ibn #sumayyah]{.trn2} "[#sumayyah]{.trn2}'s son" by the Prophet
(may [#allAh]{.trn2} grant peace and confer blessing upon him). His mother [#sumayyah]{.trn2} was an early martyr in [#islAm]{.trn2}.
+ the famous scholar [ٱِبْن كَثِير]{.ar} [#ibn #kavIr]{.trn2} is referred to by his grandfather's name [كَثِير]{.ar} [#kavIr]{.trn2}.
+ a human being is called ^2^[ٱِبْن آدَم]{.ar} based on his being a descendent of the first man, the Prophet [#adam]{.trn2}.

#### Full names

The full name of a person is formed by putting his given name first, and then his "son of" name after it as a replacement. Here is an example of a full name:

[زَيْدُ بْنُ عَلِيٍّ]{.ar}  
Zayd the son of [#ealI]{.trn2}

Note some peculiarities of the full name:

+ The name [زَيْد]{.ar} "Zayd" has lost its [n]{.trn} mark.
+ The word [بْن]{.ar} "son" is not written with its initial connecting [hamzah]{.trn2} [ٱ]{.ar}.

These peculiarities are only when forming a full name in this manner. Consider for example the following sentence:

[زَيْدٌ ٱبْنُ عَلِيٍّ.]{.ar}  
"Zayd is the son of [#ealI]{.trn2}."

In the above example, the name [زَيْدٌ]{.ar} has its [n]{.trn}-mark and [ٱبْن]{.ar} is written with its connecting [hamzah]{.trn2} [ٱ]{.ar}. Therefore this is not an expression of the full name in a replacee-replacement format. Rather, [ٱبْنُ أَحْمَدَ]{.ar} here is the information of the sentence.

For women, the word [بِنْت]{.ar} is used instead of [بْن]{.ar}. 

Example:

[قَرَأَتِ ٱلْمُعَلِّمَةُ كِتَابَ ٱلطَّالِبَةِ زَيْنَبَ بِنْتِ أَحْمَدَ.]{.ar}  
"The teacher read the book of the student Zaynab the daughter of [#aHmad]{.trn2}."

The names of multiple forefathers may be strung together in this way separated by [بْن]{.ar}. For example:

[ٱِسْمُ نَبِيِّنَا مُحَمَّدُ بْنُ عَبْدِ ٱللَّـٰهِ بْنِ عَبْدِ ٱلْمُطَّلِبِ.]{.ar}  
"Our prophet's name is [#muHammad]{.trn2} the son of [#eabd #allAh]{.trn2} the son of [#eabd al-#muTTalib]{.trn2}."  
(Note that the second [بْنِ]{.ar} is in the i-state to match the state of the annexe noun [عَبْدِ]{.ar} in [عَبْدِ ٱللّـٰه]{.ar}.)

We will deal with complete full names in section\ \@ref(complete-full-names) below.

### Other annexed names

Other words besides
[عَبْد]{.ar},
[أَب]{.ar},
[أُمّ]{.ar},
and
[ٱِبْن]{.ar}
may be used in annexed names too. Here are some examples:

+ [ذُو ٱلْقَرْنَينِ]{.ar} [#pu l-#qarnayn]{.trn2} "He of the two horns"
+ [مَدِينَة ٱلنَّبِي]{.ar} [madinatu -nnabiyyi]{.trn} "The City of the Prophet", frequently reduced to simply [ٱَلْمَدِينَة]{.ar} "Medina". 

  Context is used to infer whether by [ٱَلْمَدِينَة]{.ar} is meant "Medina" or "the city".
+ [ٱمْرُؤُ ٱلْقَيْس]{.ar} [#imruE al-#qays]{.trn2} "The man of al-Qays", a pre-[#islAm]{.trn2}ic poet.

## Names beginning with [ٱَلْ]{.ar}

Most names do not begin with [ٱَلْ]{.ar}. Some, however, do begin with [ٱَلْ]{.ar}. Examples:

|||||
|--:|:---|--:|:---|
|[ٱَلْحَسَن]{.ar}      |[al-#Hasan]{.trn2}      |[ٱَلزُّبَيْر]{.ar}     |[al-#zubayr]{.trn2}|
|[ٱَلْحُسَيْن]{.ar}     |[al-#Husayn]{.trn2}     |[ٱَلنُّعْمَان]{.ar}    |[al-#nuemAn]{.trn2}|
|[ٱَلْعَبَّاس]{.ar}     |[al-#eabbAs]{.trn2}     |[ٱَلْحَارِث]{.ar}     |[al-#HAriv]{.trn2} |

If a proper noun begins with [ٱَلْ]{.ar} then the question of its flexibility is mostly irrelevant.
This is because noun beginning with with [ٱَلْ]{.ar} display their state fully, regardless of whether or not they are semi-flexible without the [ٱَلْ]{.ar}. Examples:

[ٱَلْحَسَنُ حَفِيدُ رَسُولِ ٱللَّـٰهِ صلى اللّه عليه وسلم.]{.ar}  
"[al-#Hasan]{.trn2} is the grandson of the messenger of [#allAh]{.trn2} (may [#allAh]{.trn2} grant peace and confer blessing upon him)."  
(u-state displayed with [◌ُ]{.ar}.)

[سَأَلَ ٱلرَّجُلُ ٱلنُّعْمَانَ عَنْ أَمْرٍ.]{.ar}  
"The man asked [al-#nuemAn]{.trn2} about a matter."  
(a-state displayed with [◌َ]{.ar}.)

[ذَهَبْتُ إِلَى بَيْتِ ٱلنُّعْمَانِ.]{.ar}  
"I went to [al-#nuemAn]{.trn2}'s house."  
(i-state displayed with [◌ِ]{.ar}.)

Names that begin with [ٱَلْ]{.ar} can sometimes lose their initial [ٱَلْ]{.ar}. Sometimes, this is systematic, as we will lear in section\ \@ref(calling-names-with-al).
Other times, it's hard to tell why. 

Conversely, names that don't begin with [ٱَلْ]{.ar} can sometimes gain it.

Examples:

+ The name of the daughter of the Companion [أَبُو ٱلدَّرْدَاء]{.ar} [#abu l-#dardAE]{.trn2} is actually ^2^[دَرْدَاء]{.ar} [#dardAE]{.trn2}, not [ٱَلدَّرْدَاء]{.ar}.

+ The son of the uncle of the Prophet
(may [#allAh]{.trn2} grant peace and confer blessing upon him)
[ٱَلْعَبَّاس]{.ar} [al-#eabbAs]{.trn2}
is called
[ٱِبْن عَبَّاس]{.ar} [#ibn eabbAs]{.trn2}, not [ٱِبْن ٱلْعَبَّاس]{.ar}.


However, the son of 
[ٱَلْزُّبَيْر]{.ar}     [al-#zubayr]{.trn2}|
is called
[ٱِبْن ٱلْزُّبَيْر]{.ar}     [#ibn al-#zubayr]{.trn2} with the [ٱَلْ]{.ar}.

## Place names

Place names are generally feminine. Because of their feminine gender, those not beginning with [ٱَلْ]{.ar} will be semi-flexible according to section\ \@ref(feminine-names) above.

Examples of place names are:

|||||
|--:|:---|--:|:---|
|^2^[مَكَّة]{.ar}    |Mecca             |[ٱَلْمَدِينَة]{.ar}   |Medina|
|^2^[دِمَشْق]{.ar}   |Damascus          |[ٱَلْقَاهِرَة]{.ar}   |Cairo |
|^2^[بَغْدَاد]{.ar}  |[#bagdAd]{.trn2}  |[ٱَلْهِنْد]{.ar}     |India |
|^2^[مِصْر]{.ar}    |Egypt             |[ٱَلصِّين]{.ar}     |China |
|^2^[فَارِس]{.ar}   |Persia            |[ٱَلرُّوم]{.ar}     |Rome  |
|^2^[تَبُوك]{.ar}   |[#tabUk]{.trn2}   |[ٱَلْبَصْرَة]{.ar}    |[#baSrah]{.trn2}|

Example of use:

[ذَهَبَ ٱلرَّجُلُ إِلَىٰ مَكَّةَ ٱلْمُكَرَّمَةِ وَٱلْمَدِينَةِ ٱلْمُنَوَّرَةِ.]{.ar}  
"The man went to the ennobled Mecca and the illuminated Medina."

While most place names are feminine, a few are masculine. Among these are:

|||||
|--:|:---|--:|:---|
|[ٱَلْيَمَن]{.ar}  |Yemen  |[ٱَلشَّام]{.ar}  |the Levant |
|[ٱَلْعِرَاق]{.ar} |Iraq   ||

## Names of tribes

Here are examples of names of tribes:

|||||
|--:|:---|--:|:---|
|[قُرَيش]{.ar}           | [#qurayc]{.trn2}      |[ٱَلْأَوْس]{.ar}          | [al-#aws]{.trn2}        |
|[بَنُو تَمِيم]{.ar}       | [#banU #tamIm]{.trn2} |[ٱَلْخَزْرَج]{.ar}         | [al-#xazraj]{.trn2}     |
|^2^[هَوَازِن]{.ar}       | [#hawAzin]{.trn2}     |^2^[بَنُو إِسْرَائِيل]{.ar} | [#banU #isrAEIl]{.trn2} |

Tribes are usually called by the name of their progenitor. For example, ^2^[إِسْرَائِيل]{.ar} [#isrAEIl]{.trn2} is a name of the Prophet ^2^[يَعْقُوب]{.ar} [#yaeqUb]{.trn2}. 
The [Un]{.trn} sound plural [بَنُونَ]{.ar} "sons/children" is annexed to the name 
^2^[إِسْرَائِيل]{.ar} [#isrAEIl]{.trn2}
to get the name of the tribe
^2^[بَنُو إِسْرَائِيل]{.ar} [#banU #isrAEIl]{.trn2} "the children of [#isrAEIl]{.trn2}". In the a- and i-states, this becomes
^2^[بَنِي إِسْرَائِيل]{.ar} [#banI #isrAEIl]{.trn2}.

Not all tribe names have [بَنُونَ]{.ar} "sons" annexed to them, but many do. And often it is optional to keep or drop the annexed [بَنُونَ]{.ar}. Examples:

+ [قُرَيْش]{.ar} [#qurayc]{.trn2} usually does not have [بَنُونَ]{.ar} annexed to it.
+ [بَنُو تَمِيم]{.ar} [#banU #tamIm]{.trn2} may optionally drop the annexed [بَنُونَ]{.ar} and be called simply [تَمِيم]{.ar} [#tamIm]{.trn2}.

### Flexibility of tribe names

The flexibility of tribe names depends on the name. Here are some examples:

+ ^2^[إِسْرَائِيل]{.ar} [#isrAEIl]{.trn2} is a name of foreign origin and is therefore semi-flexible. Example:

  [بَعَثَ ٱللَّـٰهُ مُوسَىٰ إِلَىٰ بَنِي إِسْرَائِيلَ.]{.ar}  
  "[#allAh]{.trn2} sent [#mUsA]{.trn2} to the children of [#isrAEIl]{.trn2}."

+ [قُرَيْش]{.ar}            [#qurayc]{.trn2}     and [تَمِيم]{.ar}        [#tamIm]{.trn2} are native Arabic masculine names and are therefore fully-flexible. Example:

  [قُرَيشٌ وَبَنُو تَمِيمٍ قَبِيلَتَانِ.]{.ar}  
  "[#qurayc]{.trn2}     and [#banU #tamIm]{.trn2} are tribes~2~."

+ ^2^[هَوَازِن]{.ar} [#hawAzin]{.trn2} is on the semi-flexible noun pattern ^2^[فَفَافِف]{.ar} and is therefore semi-flexible.

### Gender of tribe names

Tribe names are unusual in that they are treated as both singular feminine and plural masculine.
If the tribe name is the doer of a verb then it is usually treated as singular feminine.
Otherwise, for example, if it comes before the verb, then the plural masculine pronouns are used for it.

Example:

[سَكَنَتْ قُرَيْشٌ مَكَّةَ وَعَبَدُوا ٱلْأَصْنَامَ.]{.ar}  
"[#qurayc]{.trn2} dwelled in Mecca and they worshipped idols."

## Titles

Titles are common nouns that denote a rank or position of a person. Titles in English include: Doctor, Mister, and King. For example:

+ King David
+ Mr. Smith
+ Dr. Adams

Here are some examples of titles in Arabic:

|||||
|--:|:---|--:|:---|
|[ٱَلنَّبِيّ]{.ar}   |Prophet    |[ٱَلْإِمَام]{.ar}  |[#imAm]{.trn2} |
|[ٱَلْمَلِك]{.ar}   |King       |[ٱَلشَّيْخ]{.ar}   |[#cayx]{.trn2} |
|[ٱَلْأَمِير]{.ar}  |Commander  |[ٱَلْحَافِظ]{.ar}  |[#HAfiP]{.trn2}|
|[ٱَلْقَاضِي]{.ar}  |Judge      |[ٱَلْأُسْتَاذ]{.ar} |Professor      |

Some Arabic titles are left untranslated in English like

+ [ٱَلْإِمَام]{.ar}  [#imAm]{.trn2} (a leader)
+ [ٱَلشَّيْخ]{.ar}   [#cayx]{.trn2} (a venerable man)
+ [ٱَلْحَافِظ]{.ar}  [#HAfiP]{.trn2} (one who has memorized, and preserved religious texts)

### Titles as replacees

Titles are usually placed in front a proper noun and made definite with [ٱَلْ]{.ar} to match the proper noun. For example,

[سَأَلَ رَجُلٌ ٱلْإِمَامَ مَالِكًا عَنْ أَمْرٍ.]{.ar}  
"A man asked [#imAm #mAlik]{.trn2} about a matter."

In the above sentence, the title [ٱَلْإِمَامَ]{.ar} [#imAm]{.trn2} is a replacee and the name [مَالِكًا]{.ar} [#mAlik]{.trn2} is the replacement.

Some titles are formed from annexations. Examples:

|||||
|--:|:---|--:|:---|
|[خَلِيفَةُ رَسُولِ ٱللَّـٰهِ]{.ar}  | the Successor of the Messenger of [#allAh]{.trn2}  |[سَيْفُ ٱللَّـٰهِ]{.ar}         | the Sword of [#allAh]{.trn2}  |
|[أَمِيرُ ٱلْمُؤْمِنِينَ]{.ar}     | the Commander of the Believers                     |[عِمَادُ ٱلدِّينِ]{.ar}        | the Pillar of the Faith  |
|[أُمُّ ٱلْمُؤْمِنِينَ]{.ar}       | the Mother of the Believers                        |[صَلَاحُ ٱلدِّينِ]{.ar}        | the Righteousness of the Faith  |

Example:

[أُمُّ ٱلْمُؤْمِنِينَ عَائِشَةُ هِيَ ٱِبْنَةُ خَلِيفَةِ رَسُولِ ٱللَّـٰهِ أَبِي بَكْرٍ.]{.ar}  
"The Mother of the Believers [#eAEicah]{.trn2} is the daughter of the Successor of the Messenger of [#allAh]{.trn2} [#abU #bakr]{.trn2}."

### Titles in annexations

Some prominent inanimate objects, like mountains, rivers, and cities, may have titles. For example:

+ Mount Everest
+ the river Nile
+ the city of Damascus

In Arabic, the titles for these objects usually don't occur as replacees as they do for persons. Rather, the title is annexed to the proper noun in an annexation. Examples:

|||||
|--:|:---|--:|:---|
|[جَبَلُ أُحُدٍ]{.ar}      |Mount [#uHud]{.trn2} |[مَدِينَةُ دِمَشْقَ]{.ar}   |the city of Damascus |
|[نَهْرُ ٱلنِّيلِ]{.ar}    |the river Nile       |[شَهْرُ رَمَضَانَ]{.ar}    |the month of [#ramaDAn]{.trn2} |
|[يَوْمُ ٱلْجُمُعَةِ]{.ar}   |the day of Friday    |[سُورَةُ ٱلْفَاتِحَةِ]{.ar} |the [#sUrah]{.trn2} of [al-#fAtiHah]{.trn2} |

Example:

[قَرَأَتِ ٱلْجَارِيَةُ سُورَةَ ٱلْفَاتِحَةِ فِي شَهْرِ رَمَضَانَ.]{.ar}  
"The girl read the [#sUrah]{.trn2} of [al-#fAtiHah]{.trn2} in the month of [#ramaDAn]{.trn2}."

## Nicknames

Nicknames are often given to people. They are usually descriptive of some physical quality or character trait of the person. For example, the Companion [#abU #bakr]{.trn2} was given the  nickname [ٱلصِّدِّيق]{.ar} "the steadfast affirmer of the truth".

Nicknames usually come after a person's name as a replacement.

[أَبُو بَكَرٍ ٱلصِّدِّيقُ هُوَ خَلِيفَةُ رَسُولِ ٱللَّـٰهِ.]{.ar}  
"[#abU #bakr]{.trn2} the steadfast affirmer of the truth is the successor of the messenger of [#allAh]{.trn2}."

[قَرَأَ سُلَيْمَانُ ٱلأَعْمَشُ ٱلْقُرْآنَ.]{.ar}  
"[#sulaymAn]{.trn2} the weak-sighted read the [#qurEAn]{.trn2}."

## The affiliate adjectival noun

The affiliate adjectival noun is a kind of adjectival noun that indicates an affiliation.

Here are some examples of affiliate adjectival nouns:

|||||
|--:|:---|--:|:---|
|[عِرَاقِيّ]{.ar}    |an Iraqi            |[قُرَشِيّ]{.ar}     |a [#qurayc]{.trn2}ite |
|[مَكِّي]{.ar}      |a Meccan            |[تَمِيمِيّ]{.ar}    |a [#tamIm]{.trn2}ian  |
|[دِمَشْقِيّ]{.ar}    |a Damascan          |[إِسْرَائِيلِيّ]{.ar} |an [#isrAEIl]{.trn2}ite|
|[شَافِعِيّ]{.ar}    |a [#cAfie]{.trn2}ite |[حَنَفِيّ]{.ar}     |a [#HanafI]{.trn2}    |
|[مَالِكِيّ]{.ar}    |a [#mAlikI]{.trn2}   |[حَنْبَلِيّ]{.ar}    |a [#HanbalI]{.trn2}   |

Note the following about affiliate adjectival nouns:

+ Generally, the ending [◌ِيّ]{.ar} [-iyy]{.trn} is suffixed to a noun to create an affiliate adjectival noun. 
+ The [ة]{.ar} ending is removed before adding the [◌ِيّ]{.ar} [-iyy]{.trn} suffix.
+ Sometimes there are other internal changes to the word before this suffix is added. For example,
  + [قُرَيْش]{.ar} becomes [قُرَشِيّ]{.ar}
+ The affiliate adjectival noun may be formed from any of the names of a person. (Usually, one of the more distinctive names is chosen.) For example:
  + A follower of the school of thought of [ٱَلْإِمَام أَبُو حَنِيفَة]{.ar} [#imAm #abU #HanIfah]{.trn2} is called [حَنَفِيّ]{.ar} "a [#HanafI]{.trn2}".
  + A follower of the school of thought of [ٱَلْإِمَام أَحْمَد بْن حَنْبَل]{.ar} [#imAm #aHmad ibn #Hanbal]{.trn2} is called [حَنْبَلِيّ]{.ar} "a [#HanbalI]{.trn2}".

We will treat adjectival nouns more fully in chapter\ \@ref(the-affiliate-adjective-chapter).

Afflilate adjectival nouns frequently occur with proper nouns. They come after the proper noun as a replacement, and are made definite by [ٱَلْ]{.ar} to match the proper noun in definiteness. Examples:

[ٱِبْن كَثِيرٍ ٱلدِّمَشْقِيُّ مُفَسِّرٌ وَمُؤَرِّخٌ.]{.ar}  
"[#ibn #kavIr]{.trn2} the Damascan is an exegete and a historian."

## Complete full names

We have already studied how a basic full name is formed in section\ \@ref(full-names). Here, we will expand on that topic.

The complete full name of a person is formed by placing some or all of his different names in a particular order. Each name in the order is a replacement of one of the names before it. Generally, the order is:

i. Titles
i. "Father of" name
i. Given name
i. "Son of" names
i. Affiliate names

The nickname's position is variable.

Here are some examples of full names in varying degrees of completeness:

[عَائِشَةُ هِيَ ٱبْنَةُ خَلِيفَةِ رَسُولِ ٱللَّـٰهِ أَبِي بَكْرٍ ٱلصِّدِّيقِ.]{.ar}  
"[#eAEicah]{.trn2} is the daughter of the  Successor of the Messenger of [#allAh]{.trn2}, [#abU #bakr]{.trn2}, the steadfast affirmer of the truth."

[قَتَلَ أَبُو لُؤْلُؤَةَ ٱلْمَجُوسِيُّ أَمِيرَ ٱلْمُؤْمِنِينَ أَبَا حَفْصٍ عُمَرَ بْنَ ٱلْخَطَّابِ.]{.ar}  
"[#abU #luEluEah]{.trn2}, the Magian killed the Commander of the Believers, [#abU #HafS]{.trn2}, [#eumar]{.trn2} the son of [al-#xaTTAb]{.trn2}."

[كَتَبَ ٱلْحَافِظُ ٱلْمُؤَرِّخُ ٱلْمُفَسِّرُ عِمَادُ ٱلدِّينِ أَبُو ٱلْفِدَاءِ إِسْمَاعِيلُ بْنُ عُمَرَ بْنِ كَثِيرٍ ٱلْقُرَشِيُّ ٱلدِّمَشْقِيُّ ٱلشَّافِعِيُّ تَفْسِيرًا.]{.ar}  
"The [#HAfiP]{.trn2}, the historian, the exegete, the Pillar of the Faith, the father of [al-#fidAE]{.trn2}, [#ismAEIl]{.trn2} the son of [#eumar]{.trn2} the son of [#kavIr]{.trn2}, the [#qurayc]{.trn2}ite, the Damascan, the [#cAfie]{.trn2}ite wrote an exegesis."  
(Note how the second [بْنِ]{.ar} is in the i-state because it is a replacement of [عُمَرَ]{.ar} which is in the i-state because it is a base noun of the first [بْنُ]{.ar}.)
  

<!--chapter:end:srcrmd/proper_nouns.Rmd-->

# Addressing by name

## Introduction

When directly addressing soneone in Arabic and calling out to him by name, the particle [يَا]{.ar} [yA]{.trn} is usually prefixed to the person's name. For example,

[ٱَلسَّلَامُ عَلَيْكُمْ يَا زَيْنَبُ.]{.ar}  
[EassalAmu ealaykum yA zaynabu.]{.trn}  
"Peace be upon you, O Zaynab."

There are different rules regarding the state markings of the noun following [يَا]{.ar} [yA]{.trn} and we will describe them in the following sections.

## Calling out to specific persons

### Using single word personal names

When a specific person is called out to, and the name used to call him consists of a single word, then that word shall be in the u-state. The sentence above is an example of this rule where the name [زَينَبُ]{.ar} [zaynabu]{.trn} "Zaynab" is in the u-state.

If the word would have an [n]{.trn}-mark, then the [n]{.trn}-mark is dropped. So, for example, the name [زَيْدٌ]{.ar} [zaydun]{.trn} "Zayd" usually has an [n]{.trn}-mark. But when used for being called out to, the [n]{.trn}-mark is dropped and it becomes:

[ٱَلسَّلَامُ عَلَيْكُمْ يَا زَيْدُ.]{.ar}  
[EassalAmu ealaykum yA zaydu.]{.trn}  
"Peace be upon you, O Zayd."

### Using single word indefinite common nouns

The examples above show the person being called out to using a personal name. Instead of a personal name, a common noun can also be used with the same rule. Examples:

[ٱَلسَّلَامُ عَلَيْكُمْ يَا غُلَامُ.]{.ar}  
[EassalAmu ealaykum yA gulAmu.]{.trn}  
"Peace be upon you, O you boy."

[ٱَلسَّلَامُ عَلَيْكُمْ يَا جَارِيَةُ.]{.ar}  
[EassalAmu ealaykum yA jAriyatu.]{.trn}  
"Peace be upon you, O you girl."

In English, we have shown that a specific person is being called using the word "you", e.g., "O you boy". Duals and plurals are also allowed, again with the same rule:

[يَا رِجَالُ، قَدْ حَدَثَ أَمْرٌ.]{.ar}  
[yA rijAlu qad Hadava Eamrun.]{.trn}  
"O you men, a matter has occurred."

Note how the word [رِجَالُ]{.ar} [rijAlu]{.trn} "men" does not have an [n]{.trn}-mark because the word is used to call out to the specific persons.

Similarly,

[يَا لَاعِبَانِ بَدَأْتُمَا ٱللَّعِبَ وَمَا فَعَلْتُمَا ٱلْعَمَلَ.]{.ar}  
[yA lAeibAni badaEtuma -llaeiba wamA faealtuma -leamal.]{.trn}  
"O you players~2~, you have started playing and you have not done the work."

### Using single word definite common nouns

When using a common noun to call out to a person, especially if the common noun is a title, it is often desired to make the common noun definite with [ٱَلْ]{.ar}. In this case, the particle [يَا]{.ar} [yA]{.trn} is modified to [أَيُّهَا]{.ar} [EayyuhA]{.trn}, or sometimes [يَا أَيُّهَا]{.ar} [yA EayyuhA]{.trn}. Examples:

[يَا أَيُّهَا ٱلْأُسْتَاذُ، قَدْ فَعَلْتُ ٱلْوَاجِبَ.]{.ar}  
[yA Eayyuha -lEustApu, qad faealtu -lwAjiba]{.trn}  
"O you the Professor, I have done the obligatory [work]."

[أَنَا سَقِيمٌ أَيُّهَا ٱلطَّبِيبُ.]{.ar}  
[Eana saqImun, Eayyuha -TTabIbu.]{.trn}  
"I am ill, O you the Doctor."

If the person being called out to is feminine, then [أَيُّهَا]{.ar} [EayyuhA]{.trn} is modified to [أَيَّتُهَا]{.ar} [EayyatuhA]{.trn}. For example:

[أَيَّتُهَا ٱلْمُعَلِّمَةُ، هَـٰذَا كِتَابِي.]{.ar}  
[Eayyatuha -lmueallimatu, hApA kitAbi.]{.trn}  
"O you the teacher~f~, this is my book."


### Using multiple words

The above discussion pertains to calling out to the addressed person with a single word. Often times a person's name may consist of multiple words. For example:

+ [عَبْدُ ٱللَّـٰهِ]{.ar}  
  [eabdu -llAhi]{.trn}  
  "[#eabd #allAh]{.trn2}"

+ [أَبُو بَكْرٍ]{.ar}  
  [EabU bakrin]{.trn}  
  "[#abU #bakr]{.trn2}"

+ [صَلَاحُ ٱلدِّينِ]{.ar}  
  [SalAHu -ddIni]{.trn}  
  "[#salAH ad-#dIn]{.trn2}"

In this case, then instead of the u-state, the word is put into the a-state. Furthermore, the [n]{.trn}-mark, if any, is preserved. Examples:

[مَا عَرَفْتُ ذَ ٰلِكَ ٱلرَّجُلَ، يَا عَبْدَ ٱللَّـٰهِ.]{.ar}  
[mA earaftu pAlika -rrajula, yA eabda -llAhi.]{.trn}  
"I have not recognized that man, O [#eabd #allAh]{.trn2}."

[يَا أَبَا بَكْرٍ، أَنْتَ رَجُلٌ كَرِيمٌ.]{.ar}  
[yA EabA bakrin, Eanta rajulun karImun]{.trn}  
"O [#abU #bakr]{.trn2}, You are a noble man."

[يَا صَلَاحَ ٱلدِّينِ، صَبَرْتَ فَنَصَرَكَ ٱللَّـٰهُ.]{.ar}  
[yA SalAHa -ddIni, Sabarta fanaSaraka -llAhu.]{.trn}  
"O [#salAH ad-#dIn]{.trn2}, you were patient so [#allAh]{.trn2} gave you victory."


If, instead of a personal name, a noun phrase consisting of multiple words is used to call out to a person, then in this case as well, the first noun shall be in the a-state. Examples:

[يَا أَمِيرَ ٱلْمُؤمِنِينَ، قَدْ حَضَرَ ٱلْقَوْمُ.]{.ar}  
[yA EamIra -lmuEminIna, qad HaDara -lqawmu.]{.trn}  
"O Commander of the Believers, the people are present."

[يَا ٱبْنَ أَخِي، قَدْ سَقَطَ قَلَمُكَ عَلَى ٱلْأَرْضِ.]{.ar}  
[ya -bna EaxI, qad saqaTa qalamuka.]{.trn}  
"O my nephew, your pen has fallen on the ground."

[يَا تَلَامِيذَ ٱلْمَدْرَسَةِ، ٱلْعِلْمُ أَمَانَةٌ.]{.ar}  
[yA talAmIpa -lmadrasati, -leilmu EamAnatun.]{.trn}  
"O pupils of the school, knowledge is a trust."

When multiple words are used to call out to a person, the second word in the noun-chain may be a pronoun. Here too, the first noun shall be in the a-state. Examples:

[يَا أَبانا]{.ar}  
[yA EabAnA]{.trn}  
"O our father"

## Calling out to unspecified persons

All the discussion so far has pertained to calling out to specific persons. So for example, when you say,

<!--[يَا ظَالِمُ، عَذَابُ ٱللَّـٰهِ وَاقِعٌ.]{.ar}  -->
[يَا مُسْلِمُ، نَصْرُ ٱللَّـٰهِ قَرِيبٌ.]{.ar}  
[yA muslimu, naSru -llAhi qarIbun.]{.trn}  
"O you Muslim, the victory of [#allAh]{.trn2} is near."

then you are addressing a specific Muslim, who is perhaps in front of you. 

If an unspecified person or persons are being called out, then the word used to call out is put into the a-state. Furthermore, the [n]{.trn}-mark, if any, is preserved. So if you want to address any unspecific Muslim, you will say:

[يَا مُسْلِمًا، نَصْرُ ٱللَّـٰهِ قَرِيبٌ.]{.ar}  
[yA musliman, naSru -llAhi qarIbun.]{.trn}  
"O [any] Muslim, the victory of [#allAh]{.trn2} is near."

If multiple words are used, whether or not the person called out to is specific or unspecified, then too the first noun is put in the a-state.

[يَا لَاعِبِي لُعَبٍ، ٱلْوَقْتُ ثَمِينٌ.]{.ar}  
[yA lAeibI lueabini, -lwaqtu vamInun.]{.trn}  
"O [any] players of games, time is precious."

## Omitting [يَا]{.ar} [yA]{.trn}

When calling out to someone, it is permissible to omit the [يَا]{.ar} [yA]{.trn}, especially when the person being called is very near. So, instead of saying,

[يَا زَيْدُ، سُؤالُكَ جَيِّدٌ.]{.ar}  
[yA zaydu, suEAluka jayyidun.]{.trn}  
"O Zayd, your question is excellent."

it is permissible to say:

[زَيْدُ، سُؤالُكَ جَيِّدٌ.]{.ar}  
[zaydu, suEAluka jayyidun.]{.trn}  
"Zayd, your question is excellent."

Note that even when [يَا]{.ar} [yA]{.trn} is ommitted the name [زَيْدُ]{.ar} [zaydu]{.trn} "Zayd" is in the u-state without any [n]{.trn}-mark.

This usage is especially common when supplicating to [#allAh]{.trn2} with the word [رَبٌّ]{.ar} [rabbun]{.trn} "lord", to emphasize the closeness of [#allAh]{.trn2} to the supplicator. For example,

[رَبَّنا لَكَ ٱلْحَمْدُ.]{.ar}  
[rabbanA laka -lHamdu.]{.trn}  
"Our Lord, for you is [all] praise."

## Shortening the attached pronoun [ي]{.ar} [I]{.trn} "my"

When calling someone with the pronoun "my", for example "O my people", it is common to shorten the attached pronoun [ي]{.ar} [I]{.trn} "my" to an [i]{.trn}-mark [◌ِ]{.ar}. So while the following is permissible,

[يَا قَوْمِي]{.ar}  
[yA qawmI]{.trn}  
"O my people"

it is more common to say:

[يَا قَوْمِ]{.ar}  
[yA qawmi]{.trn}  
"O my people"

This usage is especially common when supplicating to [#allAh]{.trn2} with the phrase [رَبِّ]{.ar} [rabbi]{.trn} "my Lord".

## Calling out to [#allAh]{.trn2} by name

When calling out to [#allAh]{.trn2} by name, it is permissible to prefix the name [#allAh]{.trn2} with [يَا]{.ar}. So we can say:

[يَا أَللَّـٰهُ]{.ar}  
[yA EallAhu]{.trn}  
"O [#allAh]{.trn2}"

Note that the word [أَللَّـٰهُ]{.ar} [EallAhu]{.trn} now has a regular [hamzah]{.trn2} [أ]{.ar} instead of a connecting [hamzah]{.trn2} [ٱ]{.ar}.

However, instead of saying [يَا أَللَّـٰهُ]{.ar} [yA EallAhu]{.trn} for "O [#allAh]{.trn2}", it is in fact more common to use a special word:

[ٱَللَّـٰهُمَّ]{.ar}  
[EallAhumma]{.trn}  
"O [#allAh]{.trn2}"

Examples:

[ٱَللَّـٰهُمَّ أَنْتَ ٱلسَّلَامُ وَمِنْكَ ٱلسَّلَامُ.]{.ar}  
[EallAhumma Eanta -ssalAmu waminka -ssalAmu.]{.trn}  
"O [#allAh]{.trn2}, You are Peace and from You is peace."

[ٱَللَّـٰهُمَّ أَنْتَ ٱلصَّاحِبُ فِي ٱلسَّفَرِ.]{.ar}  
[EallAhumma Eanta -SSAHibu fi -ssafari.]{.trn}  
"O [#allAh]{.trn2}, You are the companion in the journey."


<!--chapter:end:srcrmd/vocative.Rmd-->

# Pointing nouns

## Introduction

Consider the following expression:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-14-1.pdf)<!-- -->

The word "this" is what we will call a _pointing noun_. We call it this because we can imagine standing next to a book and pointing to it and saying "this book".

The word "book" here is similarly called the _pointed-to_ noun. It refers to the object being pointed to.

## The pointing nouns in Arabic

There are two types of pointing nouns:

i. Near pointing nouns: "this-one" (singular) and "these-ones" (dual and plural).
i. Far  pointing nouns: "that-one" (singular) and "those-ones" (dual and plural).

The following are the pointing nouns in Arabic:

| Participant |State| Near pointing  noun || Far pointing  noun ||
|:----|:-|--:|:----|--:|:----|
|sing. masc.|all|[هَـٰذَا]{.ar}  |this one~m~    |[ذَ ٰلِكَ]{.ar}  |that one~m~  |
|sing. fem. |all|[هَـٰذِهِ]{.ar}  |this one~f~    |[تِلْكَ]{.ar}   |that one~f~  |
|dual masc. |u  |[هَـٰذَانِ]{.ar} |these ones~2,m~|[ذَ ٰنِكَ]{.ar}  |those ones~2,m~|
|dual masc. |a,i|[هَـٰذَيْنِ]{.ar} |these ones~2,m~|[ذَيْنِكَ]{.ar}  |those ones~2,m~|
|dual fem.  |u  |[هَاتَانِ]{.ar} |these ones~2,f~|[تَانِكَ]{.ar}  |those ones~2,f~|
|dual fem.  |a,i|[هَاتَيْنِ]{.ar} |these ones~2,f~|[تَيْنِكَ]{.ar}  |those ones~2,f~|
|plural     |all|[هَـٰؤُلَاءِ]{.ar}|these ones~3~  |[أُولَـٰئِكَ]{.ar}|those ones~3~  |

Note the following:

+ Many of the pointing nouns contain small [Ealif]{.trn2} [◌ٰ]{.ar}. For most of them, this is how they must be written. It would be incorrect to write [هَـٰذَا]{.ar} [hApA]{.trn} as [هَاذَا]{.ar}.
+ All the near pointing nouns begin with a [ه]{.ar}. And all the far pointing nouns end with [ك]{.ar}.
+ The [و]{.ar} in [أُولَـٰئِكَ]{.ar} [EulAEika]{.trn} is silent and not pronounced. That is, the first syllable has a short vowel [u]{.trn}, not the long vowel [U]{.trn}.
+ Most of the pointing nouns are rigid nouns. That is: their endings are not modified for their state. 

  The dual pointing nouns, however, are flexible nouns, for example: [هَـٰذَانِ]{.ar}  (u-state)   / [هَـٰذَيْنِ]{.ar}  [hApayni]{.trn} (a- and i-states).

+ The pointing nouns for the plural are the same for both masculine and feminine genders.

## Definiteness of pointing nouns

The pointing nouns share some similarities with pronouns [هُوَ]{.ar}, [هِيَ]{.ar}, etc. Just like pronouns, pointing nouns, too, are definite nouns even though they don't have [ٱَلْ]{.ar}.

Remember, however, from section\ \@ref(describers-with-annexations-to-pronouns), that pronouns may not be describees.
Pointing nouns are different from pronouns in this regard. It is allowed to describe a pointing noun with a describer in a noun phrase.

Both these facts will prove useful in the next section.

## Pointing noun for plurals of non-intelligent beings

Consistent with how we have been dealing with the so far,
, we can choose between the following pointing nouns for 
the plurals of non-intelligent beings:

||Near pointing noun |Far pointing noun|
|:----|:-|--:|:----|--:|:----|
|sing. fem. |all|[هَـٰذِهِ]{.ar}  |this one~f~    |[تِلْكَ]{.ar}   |that one~f~  |
|plural     |all|[هَـٰؤُلَاءِ]{.ar}|these ones~3~  |[أُولَـٰئِكَ]{.ar}|those ones~3~  |

The singular feminine pointing noun is usually preferred, unless the plural plural pointing noun is needed to indicate that there is more than one.
We will be giving examples throughout this chapter.

## The pointing noun phrase

Remember from chapter\ \@ref(adjectival-nouns-and-descriptive-noun-phrases) that a descriptive noun-phrase consists of a describer and a describee. The describer follows the describer and matches it in definiteness, state, gender, and number. 

Here is an example of a descriptive noun-phrase in a sentence.

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-15-1.pdf)<!-- -->

We will now see how this same descriptive noun-phrase can be used with pointing nouns.

### Pointing to a single noun

We will first deal with nouns that are single words, like [ٱَلْكِتَابَيْنِ]{.ar} above. 
In section\ \@ref(pointing-to-an-annexation)
below, we will deal with nouns that are part of an annexation, like [كِتَابَيِ ٱلرَّجُلِ]{.ar}.

#### The pointed-to noun is definite with [ٱَلْ]{.ar} {#phrase-single-pointed-to-noun-with-al}

Just like an adjectival noun, a pointing noun can be a describer in a noun-phrase. But remember from 
section\ \@ref(definiteness-of-pointing-nouns)
above that pointing nouns are definite.
So, if a pointing noun is a describer in a noun-phrase, the describee has to be definite too.
Example:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-16-1.pdf)<!-- -->

In the above example, the pointed-to noun [ٱَلْكِتَابَيْنِ]{.ar} is the describee in a descriptive noun-phrase. It is definite, in the a-state, masculine, and dual.

The pointing noun [هَـٰذَيْنِ]{.ar} is its describer. It follows the describee and matches it being dual, in the a-state, masculine, and dual.

As a special case, when the pointed-to noun has [ٱَلْ]{.ar} (as in this case: [ٱَلْكِتَابَيْنِ]{.ar}), then the order of the pointing noun and the pointed to noun is permitted to be reversed. 
<!--The pointing noun can be the describee, and the pointed-to noun can be the describer.-->

The pointing noun is then a replacee (see section\ \@ref(the-replacement)), and the pointed-to noun is its replacement.

Example:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-17-1.pdf)<!-- -->

In the above example, the 
pointing noun [هَـٰذَيْنِ]{.ar} 
is a replacee. It is definite, in the a-state, masculine, and dual.

The 
pointed-to noun [ٱَلْكِتَابَيْنِ]{.ar} 
is its replacement. It follows the replacee and matches it being dual, in the a-state, masculine, and dual.

As a matter of fact, even though both orders are permitted, this reverse order of placing the pointing noun first and following it with the pointed-to noun is more common.

Here are some more examples of pointing noun phrases when the pointed-to noun is definite with [ٱَلْ]{.ar}:

[هَـٰذَا ٱَلرَّجُلُ ٱلْكَرِيمُ إِمَامٌ.]{.ar}  
[ٱَلرَّجُلُ ٱلْكَرِيمُ هَـٰذَا إِمَامٌ.]{.ar}  
"This noble man is an [imAm]{.trn2}."

#### The pointed-to noun is a proper noun

Remember that proper noun are definite nouns, even though they usually don't begin with [ٱَلْ]{.ar}. For example:

|||||
|--:|:---|--:|:---|
|[زَيْد]{.ar}     |Zayd   |[ٱَلْحَارِث]{.ar}  |[al-#HAriv]{.trn2}|
|^2^[زَيْنَب]{.ar} |Zaynab |[قُرَيْش]{.ar}    |[#qurayc]{.trn2}  |

Such names may also be part of a pointing noun phrase. 
If they don't begin with [ٱَلْ]{.ar} then only the [pointed-to noun first, then pointing noun] order is permitted.
Example:

[زَيْدٌ هَـٰذَا أَخُو زَيْنَبَ تِلْكَ.]{.ar}  
"This Zayd is that Zaynab's brother."

[قُرَيْشٌ هَـٰؤُلَاءِ سَكَنُوا بِمَكَّةَ.]{.ar}  
"These [#qurayc]{.trn2} dwelled in Mecca."

If the name begins with [ٱَلْ]{.ar} then both orders are permitted.

[هَـٰذَا ٱلْحَارِث]{.ar}  
[ٱلْحَارِث هَـٰذَا]{.ar}  
"this [al-#HAriv]{.trn2}"

<!--Wright, ii Sect 136 277B-->

### Pointing to an annexation

Consider the following expression:

"the man's book"

We can apply the pointing noun "this" to either "the book" or to "the man" in a pointing noun phrase. So we have two options:

i. "the book of this man"
i. "this book of the man"

Similarly, consider the following expression:

"Zayd's book"

We can, again, apply the pointing noun "this" to either "the book" or to "Zayd":

i. "the book of this Zayd"
i. "this book of Zayd"

In this section we will learn how to construct these pointing noun phrases in Arabic.
Arabic uses annexations to express the above meanings. So we will discuss annexations like:

[كِتَابُ ٱلرَّجُلِ]{.ar}  
"the book of the man"

and

[كِتَابُ زَيْدٍ]{.ar}  
"the book of Zayd"

Note that both the above annexations are definite because their base nouns are definite.

Indefinite annexations like 
[كِتَاب رَجُلٍ]{.ar} "a man's book"
cannot be used in pointing noun phrases.

#### The definite base noun begins with [ٱَلْ]{.ar}

We will first consider annexations where the definite base noun begins with [ٱَلْ]{.ar}, like:

[كِتَابُ ٱلرَّجُلِ]{.ar}  
"the book of the man"

##### Pointing to the base noun  

We would like to express the phrase:

"the book of this man"

In order to point to the base noun [ٱَلرَّجُل]{.ar} "the man" with the pointing noun [هَـٰذَا]{.ar} "this-one~m~", we can put the pointing noun either before or after the base noun, thus:

[كِتَابُ هَـٰذَا ٱلرَّجُلِ]{.ar}  
[كِتَابُ ٱلرَّجُلِ هَـٰذَا]{.ar}  
"the book of this man"

Both these pointing noun phrases give the same meaning: "the book of this man".
However, the first phrase
[كِتَابُ هَـٰذَا ٱلرَّجُلِ]{.ar}
is preferred, consistent with what we learned in 
section\ \@ref(phrase-single-pointed-to-noun-with-al), above.

The second phrase
[كِتَابُ ٱلرَّجُلِ هَـٰذَا]{.ar},
although correct, would only rarely be used with this meaning.
(In fact, it has another meaning: "this book of the man" which we will learn in
section\ \@ref(pointing-to-the-annexe-noun), below.)

Here is how these phrases could be used in complete sentences:

[كِتَابُ هَـٰذَا ٱلرَّجُلِ جَدِيدٌ.]{.ar}  
[كِتَابُ ٱلرَّجُلِ هَـٰذَا جَدِيدٌ.]{.ar}  
"The book of this man is new."

Before we give more examples, let's analyze these phrases in detail.

Consider the first pointing noun phrase:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-18-1.pdf)<!-- -->

As you can see the pointing noun
[هَـٰذَا]{.ar} has taken the place of 
[ٱَلرَّجُل]{.ar} as the base noun in the annexation.
In addition to being the base noun,
[هَـٰذَا]{.ar} is also a replacee, whose replacement is 
[ٱَلرَّجُل]{.ar}.
The literal, word-for-word, translation of this phrase is:

"the book of this-one: the man"

The more natural translation is:

"the book of this man"

Consider, now, the second pointing noun phrase:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-19-1.pdf)<!-- -->

[ٱَلرَّجُل]{.ar}, here, keeps its place as the base noun in the annexation.
In addition to being the base noun,
[ٱَلرَّجُل]{.ar}
is also a describee, whose describer is the pointing noun
[هَـٰذَا]{.ar}.
The literal, word-for-word, translation of this phrase is:

"the book of the this-one man"

The more natural translation is:

"the book of this man"

##### Pointing to the annexe noun  

Consider, again, the annexation:

[كِتَابُ ٱلرَّجُلِ]{.ar}  
"the book of the man"

We have already discussed how to point to the base noun
[ٱَلرَّجُل]{.ar}
in a pointing noun phrase.
Now, we would like to point to the annexe noun 
[كِتَاب]{.ar}
in a pointing noun phrase.

In other words, we would like to express the meaning:

"this book of the man"

<!--
There are three possible locations to place the pointing noun
[هَـٰذَا]{.ar}:

i. $\times$ [هَـٰذَا كِتَابُ ٱلرَّجُلِ]{.ar},
i. $\times$ [كِتَابُ هَـٰذَا ٱلرَّجُلِ]{.ar},
i. [كِتَابُ ٱلرَّجُلِ هَـٰذَا]{.ar},

The first two options are incorrect, and the third option is correct. We will explain why below.
-->

The way to express this in Arabic is

[كِتَابُ ٱلرَّجُلِ هَـٰذَا]{.ar}  
"this book of the man"

But wait! Didn't we see in section\ \@ref(pointing-to-the-base-noun) above that this expression has the meaning
"the book of this man"?

It turns out that this expression supports both meanings.

But it will generally only be used for the meaning: "this book of the man"

In order to express
"the book of this man"
we will typically use the expression [كِتَابُ هَـٰذَا ٱلرَّجُلِ]{.ar}.

Let's analyze the expression
[كِتَابُ ٱلرَّجُلِ هَـٰذَا]{.ar}
"this book of the man"
in detail:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-20-1.pdf)<!-- -->

[كِتَاب]{.ar}, here, is both and annexe noun and a describee.
Its describer is the pointing noun
[هَـٰذَا]{.ar}.
The literal, word-for-word, translation of this phrase is:

"the this-one book of the man"

The more natural translation is:

"this book of the man"

Here is this pointing noun phrase in a complete sentence:

[كِتَابُ ٱلرَّجُلِ هَـٰذَا أَخْضَر.]{.ar}  
"This book of the man is green."

###### Ambiguity of this phrase {-}

A quick note about the ambiguity of this expression:

[كِتَابُ ٱلرَّجُلِ هَـٰذَا]{.ar}  
"this book of the man" (usual)  
"the book of this man" (rare)

The ambiguity of whether the pointing noun [هَـٰذَا]{.ar} points to the annexe noun 
[كِتَابُ]{.ar}
or the base noun
[ٱلرَّجُلِ]{.ar}
only exists because the annexe noun and the base noun match each other in gender and number: singular masculine.
If the annexe noun and the base noun were different in gender and number, then there would be no ambiguity. Examples:

[كِتَابَا ٱلرَّجُلِ هَـٰذَانِ]{.ar}  
"these books~2~ of the man"

[كِتَابُ ٱلرَّجُلَيْنِ هَـٰذَا]{.ar}  
"this book of the men~2~"

[كِتَابُ ٱلْمَرْأَةِ هَـٰذَا]{.ar}  
"this book of the woman"

[كِتَابُ ٱلْمَرْأَةِ هَـٰذِهِ]{.ar}  
"the book of this woman"

Here are some more examples of pointing to annexe nouns:

##### The base noun is a proper noun beginning with [ٱَلْ]{.ar}  

Consider the annexation:

[كِتَابُ ٱلزُّبَيْرِ]{.ar}  
"the book of [al-#zubayr]{.trn2}"

We can apply the preceding discussion of pointing to the annexe noun and base noun to this annexation as well. So we get:

[كِتَابُ هَـٰذَا ٱلزُّبَيْرِ]{.ar}  
"the book of this al-Zubayr"

[كِتَابُ ٱلزُّبَيْرِ هَـٰذَا]{.ar}  
"this book of al-Zubayr" (usual)  
"the book of this al-Zubayr" (rare)

#### The definite base noun does not begin with [ٱَلْ]{.ar}

Consider, now, that the base noun is definite but does not begin with [ٱَلْ]{.ar}. There are two such types of nouns that we will discuss:

i. Proper nouns not beginning with [ٱَلْ]{.ar}
i. Pronouns

##### The base noun is a proper noun not beginning with [ٱَلْ]{.ar}  

<!--Consider, now, that the base noun is a proper noun that does not begin with [ٱَلْ]{.ar}, for example:-->

We will first deal with proper nouns  that don't begin with [ٱَلْ]{.ar}.
Consider the annexation:

[كِتَابُ زَيْدٍ]{.ar}  
"the book of Zayd"

Because the base noun [زَيْد]{.ar} does not begin with [ٱَلْ]{.ar}, any pointing nouns can come only after the entire annexation, thus:

[كِتَابُ زَيْدٍ هَـٰذَا]{.ar}

In theory, this supports two meanings:

i. "this book of Zayd"
i. "the book of this Zayd"

In practice, however, the first meaning 
("this book of Zayd")
is much more likely.
Pointing to a proper noun in a pointing noun phrase 
("the book of this Zayd")
is uncommon, generally.

##### The base noun is a pronoun

We have learned, in 
section\ \@ref(definiteness-of-pronouns),
that pronouns are always definite, despite not beginning with [ٱَلْ]{.ar}.

We have also learned, in
section\ \@ref(pronouns-as-base-nouns),
that a pronoun may be a base noun in an annexation.
Example:

[كِتَابُهُ]{.ar}  
"his book"

Neither the annexe noun [كِتَاب]{.ar}, nor the attached pronoun [هُ]{.ar} begin with [ٱَلْ]{.ar}.
So if we want to add the pointing noun [هَـٰذَا]{.ar} to this annexation to form a pointing noun phrase,
then we have to place it at the end, after the annexation, thus:

[كِتَابُهُ هَـٰذَا]{.ar}  

The pointing noun [هَـٰذَا]{.ar}, here, is a describee. But what is its describer?

We have also learned, in
section\ \@ref(describers-with-annexations-to-pronouns)
that pronouns may not be describees in a descriptive noun phrase.

So, we are left with only one option: the annexe noun [كِتَاب]{.ar} is the desceibee. And the meaning of the phrase is:

[كِتَابُهُ هَـٰذَا]{.ar}  
"this book of his"

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-21-1.pdf)<!-- -->

Here are some more examples:

## Pointing nouns as subjects

Besides their use in pointing noun phrases, pointing nouns are very often used as the subject of a sentence. For example:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-22-1.pdf)<!-- -->

The pointing noun is (usually) made to match the information in number and gender. Examples:

[هَاتَانِ جَارِيَتَانِ.]{.ar}  
"These are girls~2~."

[أُولَـٰئِكَ مُعَلِّمُونَ.]{.ar}  
"Those are teachers."

[هَـٰؤُلَاءِ أَقْلَامٌ.]{.ar}  
"These are pens."

[تِلْكَ بُيُوتٌ.]{.ar}  
"Those are houses."

[هَـٰذَانِ صَغِيرَانِ.]{.ar}  
"These are small ones~2~."

The information may be a single word (as above) or more complex (as below):

[ذَ\ ٰلِكَ أَمِيرُ ٱلْمُؤِْمِنِينَ.]{.ar}  
"That is the commander of the believers."

[أُولَـٰئِكَ أَكَلْنَ ٱلطَّعَامَ..]{.ar}  
"Those-ones ate~3,f~ the food."

[هَـٰذَا ثَوْبُ رَجُلٍ.]{.ar}  
"This is a man's garment."

[هَـٰذِهِ كُتُبُهُ.]{.ar}  
"These are his books."

[هَـٰذَانِ بَيْتَانِ كَبِيرَانِ..]{.ar}  
"These are big houses~2~."

If the information is a noun that begins with [ٱَلْ]{.ar} then it may be placed after the pointing noun subject in the same manner:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-23-1.pdf)<!-- -->

While the this is permitted and correct, it may be sometimes confused with for the pointing noun phrase "this man". So, in the same way that we learned in
section\ \@ref(chap-smp-sent-sec-def-info),
we insert a detached pronoun between the subject and the information, thus:

[هَـٰذَا هُوَ ٱلرَّجُلُ.]{.ar}  
"This is the man."

Here are some more examples:

[هَاتَانِ هُمَا ٱلْجَارِيَتَانِ.]{.ar}  
"These are the girls~2~."

[أُولَـٰئِكَ هُمُ ٱلْمُعَلِّمُونَ.]{.ar}  
"Those are the teachers."

[هَـٰؤُلَاءِ هُنَّ ٱلْأَقْلَامٌ.]{.ar}  
"These are the pens."

[تِلْكَ هِيَ ٱلْبُيُوتٌ.]{.ar}  
"Those are the houses."

[هَـٰذَانِ هُمَ ٱلصَّغِيرَانِ.]{.ar}  
"These are the small ones~2~."

### Mismatched pointing noun subject

When the pointing noun is a subject we usually match its number and gender with the number and gender of the information, as we have been doing so far. However, when the pointing noun subject refers to a noun in a previous sentence, then we may prefer to match to the previous noun than to the the following information. Example:

[بَلَغَنَا خَبَرُ ٱلْمَطَرِ عَلَى ٱلْجَبَالِ. ذَ\ ٰلِكَ بُشْرَىٰ لِلزُّرَّاعِ.]{.ar}  
"The news of the rain on the mountains has reached us. That is a good tiding for the sowers."

Note that the second sentence's subject and information mismatch: 

[ذَ\ ٰلِكَ بُشْرَىٰ]{.ar}  
"That is a good tiding."

The information
[بُشٌرَىٰ]{.ar} "a good tiding" is a feminine noun but the subject
[ذَ\ ٰلِكَ]{.ar} is masculine.
This is because
[ذَ\ ٰلِكَ]{.ar}
is actually referring to [خَبَر]{.ar} in the previous sentence which is a masculine noun.

## Pointing nouns as other parts of speech

Besides their use in pointing noun phrases and as subjects, pointing nouns may be used as other parts of speech as well, typically where one would expect pronouns. Here are some examples:

[أَخَذْتُ ٱلْكِتَابَيْنِ مِنَ ٱلْمَكْتَبَةِ. قَرَأْتُ هَـٰذا وَمَا قَرَأْتُ ذَ\ ٰلِكَ.]{.ar}  
"I took the books~2~ from the library. I read this one and I didn't read that one."

[شَغَلَنِي ٱلْعَمَلُ ٱلصَّعْبُ وَمَا فَرَغْتُ مِنْ ذَ\ ٰلِكَ.]{.ar}  
"The difficult work occupied me and I did not get done with that."


<!--chapter:end:srcrmd/ism_ishara.Rmd-->

# u-state incomplete-action verbs

## Introduction

We had mentioned that there are approximately 10 commonly used verb forms. And we have already studied the completed-action verb for form 1. In this chapter we will study incomplete-action form 1 verbs. Incomplete-action verbs are used when the action of a verb is on-going at present or will occur in the future.

## Pattern for form 1

Using the root paradigm [فعل]{.arroot}, we have already seen that completed-action verbs for form 1 occur in the patterns [فَعَلَ]{.ar} [faeala]{.trn}, [فَعِلَ]{.ar} [faeila]{.trn}, and [فَعُلَ]{.ar} [faeula]{.trn}. The patterns for form 1 incomplete-action verbs are [يَفْعَلُ]{.ar} [yafealu]{.trn}, [يَفْعِلُ]{.ar} [yafeilu]{.trn}, and [يَفْعُلُ]{.ar} [yafeulu]{.trn}.

Note that the incomplete-action verb forms add an extraneous [يَـ]{.ar} [ya-]{.trn} to the beginning of the verb. This extra letter can change, as we will see soon, to the letters [تَـ]{.ar} [ta-]{.trn}, [نَـ]{.ar} [na]{.trn}, or [أَ]{.ar} [Ea-]{.trn} depending on the doer.

## Vowel-mark on the middle root letter

We have seen that vowel on the middle root letter in a completed-action verb can vary depending on the verb. So we can have,

+ [كَتَبَ]{.ar} [kataba]{.trn} "he wrote"
+ [عَمِلَ]{.ar} [eamila]{.trn} "he worked"
+ [كَبُرَ]{.ar} [kabura]{.trn} "he became big"

Similarly, the vowel on the middle letter in an incomplete-action verb can also vary depending on the verb. Generally, this will need to be looked up in a dictionary and memorized. But there are the following rules which limit the variation:

1. If the completed-action verb has an [a]{.trn}-mark on the middle letter, the incomplete-action verb's middle letter can have either an [a]{.trn}-mark, [i]{.trn}-mark, or an [u]{.trn}-mark, depending on the verb. For example,

   + [كَتَبَ يَكْتُبُ]{.ar} [kataba yaktubu]{.trn} "he wrote, he writes"
   + [ذَهَبَ يَذْهَبُ]{.ar} [pahaba yaphabu]{.trn} "he went, he goes"
   + [كَشَفَ يَكْشِفُ]{.ar} [kacafa yakcifu]{.trn} "he uncovered, he uncovers"

2. If the completed-action verb has an [i]{.trn}-mark on the middle letter, the incomplete-action verb's middle letter will usually have an [a]{.trn}-mark. Rarely, for a few verbs, it may be an [i]{.trn}-mark instead. For example,

   + [عَمِلَ يَعْمَلُ]{.ar} [eamila yaemalu]{.trn} "he worked, he works"
   + [حَسِبَ يَحْسِبُ]{.ar} [Hasiba yaHsibu]{.trn} "he deemed, he deems" <!--see Lane root Hsb for more examples. Also here: https://www.alukah.net/literature_language/0/136210/%D8%A7%D9%84%D9%85%D8%AC%D8%B1%D8%AF-%D8%A7%D9%84%D8%AB%D9%84%D8%A7%D8%AB%D9%8A/-->

3. If the completed-action verb has an [u]{.trn}-mark on the middle letter, the incomplete-action verb's middle letter shall have a [u]{.trn}-mark. For example,

   + [كَبُرَ يَكْبُرُ]{.ar} [kabura yakburu]{.trn} "he grew big, he grows big"

It is possible for some incomplete-action verbs to have more than option for the vowel mark on the middle letter. Both variants give the same meaning for the verb. For example, the completed-action verb [حَسِبَ]{.ar} [Hasiba]{.trn} "he deemed" has as its incomplete-verb both [يَحْسِبُ]{.ar} [yaHsibu]{.trn} and [يَحْسَبُ]{.ar} [yaHsabu]{.trn}.

## Verb state

As you know, nouns in Arabic have a state that is determined by the function of the noun in the sentence. For example, consider the following sentence:

[سَأَلَ ٱلْغُلَامُ ٱلرَّجُلَ عَنْ شَيْءٍ.]{.ar}  
[saEala -lgulAmu -rrajula Ean cayEin.]{.trn}  
"The boy asked the man about something."

In the above sentence, [ٱَلْغُلَامُ]{.ar} [EalgulAmu]{.trn} is the doer of the verb so it is in the u-state and this is indicated by the [u]{.trn}-mark on its final letter.
[ٱَلرَّجُلَ]{.ar} [Earrujala]{.trn} is the direct doee of the verb so it is in the a-state and this is indicated by the [a]{.trn}-mark on its final letter.
[شَيْءٍ]{.ar} [cayEin]{.trn} is directly preceded by a preposition so it is in the i-state and this is indicated by the [in]{.trn}-mark on its final letter.
The ending of the completed-action verb [سَأَلَ]{.ar} is not determined based on the function of the verb in the sentence, and therefore, it does not have any state. (Its ending can change depending on whether a pronoun is attached to it but this is not related to the function of the verb in the sentence and does not represent any state.)

As opposed to completed-action verbs, which don't have any state, incomplete-action verbs do have a state which is determinined by the function of the verb in a sentence. Similar to nouns, the state of an incomplete-action verb is indicated by the vowel mark or suffix at the end of the verb.

Incomplete action verbs have three states, just like nouns. These states are called:

i. The u-state
i. The a-state
i. The [0]{.txt}-state

Two of the states have their names in common with nouns: the u-state and the a-state. The the [0]{.txt}-state (null-state) is named differently.

The [u]{.trn}-mark on the final letter of [يَفُعَلُ]{.ar} [yafealu]{.trn} indicates that it is in the u-state. We will study only the u-state of incomplete-action verbs in this chapter. And we will study the a-state and [0]{.txt}-state in later chapters if [#allAh]{.trn2} wills.

## With doer nouns

As with completed-action verbs, doer nouns are placed after the verb in sentence word order. However, the gender of the doer noun affects the beginning of the incomplete-action verb. If the doer noun is masculine, then the incomplete-action verb shall begin with used is [يَـ]{.ar} [ya-]{.trn}. And if the doer noun is feminine, then the incomplete-action verb shall begin with [تَـ]{.ar} [ta-]{.trn}. Examples:

[يَكْتُبُ ٱلْغُلَامُ فِي كِتابِهِ.]{.ar}  
[yaktubu -lgulAmu fI kitAbihi]{.trn}  
"The boy writes in his book."

[يَعْمَلُ ٱلرَّجُلَانِ فِي ٱلْمَدِينَةِ.]{.ar}  
[yaemalu -rrajulAni fi -lmadInati.]{.trn}  
"The men~dual.~ work in the city."

[يَكْتُبُ ٱلْجَارِيَةُ فِي كِتابِهَا.]{.ar}  
[yaktubu -ljAriyatu fI kitAbihA.]{.trn}  
"The girl writes in her book."

[تَعْمَلُ ٱلنِّسَاءُ فِي بُيُوتِهِنَّ.]{.ar}  
[taemalu -nnisAEu fI buyUtihinna.]{.trn}  
"The women work in their houses."

## With doee nouns and pronouns

Doee nouns and pronouns with incomplete-action verbs work exactly as with completed-action verbs.

[يَسْأَلُ ٱلْغُلَامُ ٱلرَّجُلَ سُؤَالًا.]{.ar}  
[yasEalu -lgulAmu -rrajula suEAlan.]{.trn}  
"The boy asks the man a question."

[يَسْأَلُهَا ٱلْغُلَامُ سُؤَالًا.]{.ar}  
[yasEaluha -lgulAmu suEAlan.]{.trn}  
"The boy asks her a question."

## With doer pronouns

When we studied completed-action verbs, we saw that doer pronouns are either visible or invisible. Visible doer pronouns are added to the end of the verb, modifying the end of the verb in the process.

The doer pronouns for incomplete-action verbs are different from the doer pronouns for completed-action verbs.
Incomplete-action verbs' doer pronouns are also added to the end of the verb, but in addition to modifying the end of the verb, they modify the beginning of the verb as well. Futhermore, additional letters may be added after the doer pronoun to indicate the state of the verb. 

We'll show what all this means in the table below of verbs with doer pronouns. Completed-action verbs are included as well so that you can contrast them with their incomplete-action counterparts.

|Person|Completed-action doer pronoun|Completed-action verb with doer pronoun|Incomplete-action verb doer pronoun|Incomplete-action verb with doer pronoun in the u-state|
|:---|:--|:----|:--|:----|
| he          |_invisible_         |[فَعَلَ]{.ar}    [faeala]{.trn}     |_invisible_         |[يَفْعَلُ]{.ar}   [yafealu]{.trn} |
| she         |_invisible_         |[فَعَلَتْ]{.ar}   [faealat]{.trn}    |_invisible_         |[تَفْعَلُ]{.ar}   [tafealu]{.trn} |
| you~1,m~    |[تَ]{.ar} [-ta]{.trn}   |[فَعَلْتَ]{.ar}   [faealta]{.trn}    |_invisible_         |[تَفْعَلُ]{.ar}   [tafealu]{.trn} |
| you~1,f~    |[تِ]{.ar} [-ti]{.trn}   |[فَعَلْتِ]{.ar}   [faealti]{.trn}    |[ي]{.ar} [-I]{.trn} |[تَفْعَلِينَ]{.ar} [tafealIna]{.trn} |
| I           |[تُ]{.ar} [tu]{.trn}   |[فَعَلْتُ]{.ar}   [faealtu]{.trn}    |_invisible_         |[أَفْعَلُ]{.ar}   [Eafealu]{.trn} |
| they~2,m~   |[ا]{.ar} [-A]{.trn}   |[فَعَلَا]{.ar}   [faealA]{.trn}     |[ا]{.ar} [-A]{.trn}   |[يَفْعَلَانِ]{.ar} [yafealAni]{.trn} |
| they~2,f~   |[ا]{.ar} [-A]{.trn}   |[فَعَلَتَا]{.ar}  [faealatA]{.trn}   |[ا]{.ar} [-A]{.trn}   |[تَفْعَلَانِ]{.ar} [tafealAni]{.trn} |
| you~2~      |[تُمَا]{.ar} [-tumA]{.trn} |[فَعَلْتُمَا]{.ar} [faealtumA]{.trn}  |[ا]{.ar} [-A]{.trn}   |[تَفْعَلَانِ]{.ar} [tafealAni]{.trn} |
| they~3+,m~  |[و]{.ar} [-U]{.trn}   |[فَعَلُوا]{.ar}  [faealU]{.trn}     |[و]{.ar} [-U]{.trn}   |[يَفْعَلُونَ]{.ar} [yafealUna]{.trn} |
| they~3+,f~  |[نَ]{.ar} [-na]{.trn}   |[فَعَلْنَ]{.ar}   [faealna]{.trn}    |[نَ]{.ar} [-na]{.trn}   |[يَفْعَلْنَ]{.ar}  [yafealna]{.trn} |
| you~3+,m~   |[تُمْ]{.ar} [-tumA]{.trn}  |[فَعَلْتُمْ]{.ar}  [faealtum]{.trn}   |[و]{.ar} [-U]{.trn}   |[تَفْعَلُونَ]{.ar} [tafealUna]{.trn} |
| you~3+,f~   |[تُنَّ]{.ar} [-tunna]{.trn}  |[فَعَلْتُنَّ]{.ar}  [faealtunna]{.trn} |[نَ]{.ar} [na]{.trn}   |[تَفْعَلْنَ]{.ar} [tafealna]{.trn} |
| we          |[نَا]{.ar} [nA]{.trn}  |[فَعَلْنَا]{.ar}  [faealnA]{.trn}    |_invisible_         |[نَفْعَلُ]{.ar}   [nafealu]{.trn} |

Note the following:

+ The verb [تَفْعَلُ]{.ar} is used both for "she" and "you~2m~" doers. Only context will be able to help us differentiate between the two.
+ In incomplete action verbs which have invisible doer pronouns, the u-state of the verb is indicated by the [u]{.trn}-mark [◌ُ]{.ar} on the final letter of the verb. 
+ For incomplete-action verbs that have [ا]{.ar}, [و]{.ar}, or [ي]{.ar} as the doer pronoun, the u-state is indicated by an extraneous [ن]{.ar} added to the end of the verb. 
+ And for the remaining incomplete action verbs whose doer pronoun is [نَ]{.ar}, there is no indication of the state of the verb.

Here are some examples of the usage of the doer pronouns:

Remember that in Arabic, each verb must have it's own doer, so when there are multiple verbs associated with the same doer, the first verb can be used with the doer noun and the rest with doer pronouns. This is the same behavior as with completed-action verbs. For example:

[يَجْلِسُ ٱلرِّجَالُ وَيَأْكُلُونَ وَيَشْرَبُونَ.]{.ar}  
[yajlisu -rrijAlu wa yaEkulUna wa yacrabUna.]{.trn}  
"The men sit and (they) eat and (they) drink."

## Future

The incomplete-action verb is used to express both the present (habitual and progressive) and future tenses. Sometimes all meanings are meant in the same expression. And if only one of the meanings is intended, context can be sufficient to determine which is intended. So, for example,

[يَذْهَبُ ٱلرَّجُلُ]{.ar}  
[yaphabu -rrajulu.]{.trn}

can mean, either one, or even all, of:

"The man goes." or  
"The man is going." or  
"The man will go."

Arabic does provide a mechanism for specifying that the use of an incomplete-action verb is solely to intend a future action. This is by means of the particles [سَـ]{.ar} [sa-]{.trn} and [سَوْفَ]{.ar} [sawfa]{.trn} that can be placed before the verb. They provide a meaning of "will" or "will soon". [سَـ]{.ar} [sa-]{.trn}, being a single letter particle, is attached to the verb.

For example, 

[سَيَذْهَبُ ٱلرَّجُلُ]{.ar}  
[sayaphabu -rrajulu.]{.trn}  
and  
[سَوْفَ يَذْهَبُ ٱلرَّجُلُ]{.ar}  
[sawfa yaphabu -rrajulu.]{.trn}  
"The man will go." or  
"Soon the man will go."

The difference in usage of [سَـ]{.ar} [sa-]{.trn} and [سَوْفَ]{.ar} [sawfa]{.trn} can be thought of as one of emphasis. [سَوْفَ]{.ar} [sawfa]{.trn} is more emphatic than [سَـ]{.ar} [sa-]{.trn}. This emphasis can translate to more definiteness in the action or even that the action is farther in the future.

## Negation

### Negation using [مَا]{.ar} [mA]{.trn}

As with completed-action verbs, incomplete-action verbs too can be negated by placing the particle [مَا]{.ar} before them. This negates the meaning of the verb usually for the present tense. For example,

[مَا يَذْهَبُ ٱلرَّجُلُ]{.ar}  
[mA yaphabu -rrajulu.]{.trn}  
"The man does not go." or,  
"The man is not going."

### Negation using [لَا]{.ar} [lA]{.trn} {#u-state-verb-negation-la}

In addition to [مَا]{.ar} [mA]{.trn}, incomplete-action verbs can be negated using [لَا]{.ar} [lA]{.trn} in the same manner. In addition to negating the meaning of the verb for the present tense, it can also negate the meaning for the future tense.

[لَا يَذْهَبُ ٱلرَّجُلُ]{.ar}  
[lA yaphabu -rrajulu.]{.trn}  
"The man does not go." or,  
"The man is not going." or,  
"The man will not go."

The particles [سَـ]{.ar} [sa-]{.trn} and [سَوْفَ]{.ar} [sawfa]{.trn} may not be combined with [مَا]{.ar} [mA]{.trn} and [لَا]{.ar} [lA]{.trn} when negating verbs.


<!--chapter:end:srcrmd/imperfect_verb_indic.Rmd-->

# The verbal-noun of doing

## Introduction

Every verb has a set of _verbal-nouns_ derived from it that, despite being nouns, have a verbal meaning to them. One of these verbal-nouns is the "doing" verbal-noun, that we shall study in this chapter.

Consider the following form\ 1 verb:

| Root | Completed-action verb | Incomplete-action verb (u-state)| Doing verbal-noun|
|:--|:----|:-----|:----|
|[ذهب]{.arroot} | [ذَهَبَ]{.ar}  "he went" | [يَذْهَبُ]{.ar}  "he goes"|[ذَهَاب]{.ar} "going"|

The doing verbal-noun associated with this verb is [ذَهَاب]{.ar} [pahAb]{.trn}. It denotes "the action of going", or simply "going". In this section we shall learn how this and other verbal-nouns are used.

Before we proceed, we present a new method to present a verb and its meaning in this book. 
<!--Instead of giving the above table when presenting a verb, we will say:-->
We will often give a new verb in the format:

[ذَهَبَ يَذْهَبُ ذَهَابًا]{.ar} "to go"

The completed-action verb for the singular masculine absentee participant "he", the corresponding incomplete-action verb, and their doing verbal-noun are given together, in sequence. The doing verbal-noun is given in the a-state, because of a usage that we shall learn in a later chapter, if [#allAh]{.trn2} wills. This is how verb definitions are traditionally found in Arabic dictionaries. And the English meaning is given using the dictionary definition, in this case, the phrase: "to go". 

## Patterns of the doing verbal-noun for form\ 1 verbs

The patterns of the doing verbal-noun for form\ 1 verbs are very variable. It is best to learn the doing verbal-noun when you learn a new verb. Having said that, there are some general trends which may be useful to keep in mind:

1. If the verb takes a direct doee, then the completed-action verb must necessarily be of the pattern [فَعَلَ]{.ar} [faeala]{.trn} or [فَعِلَ]{.ar} [faeila]{.trn} (because completed-action verbs of the pattern [فَعُلَ]{.ar} [faeula]{.trn} never take a direct doee). In this case:
   a. The doing verbal-noun for many verbs, in general, tends to be [فَعْل]{.ar} [fael]{.trn}. Examples:
      + [فَتَحَ يَفْتَحُ فَتْحًا]{.ar}  "to open ([هـ]{.ar} s.th.)"
      + [أَخَذَ يَأْخُذُ أَخْذًا]{.ar}  "to take ([هـ]{.ar} s.th.)"
      + [حَمِدَ يَحْمَدُ حَمْدًا]{.ar}  "to praise ([ه]{.ar} s.o.)"
2. If the verb does not take a direct doee, then:
   a. If the completed-action verb is of the pattern [فَعِلَ]{.ar} [faeila]{.trn}, then:
      i. If the meaning of the verb does not fall under the cases ii., iii., and iv. (below), then the doing verbal-noun tends to be, in general, of the pattern [فَعَل]{.ar} [faeal]{.trn}. Examples:
         + [تَعِبَ يَتْعَبُ تَعَبًا]{.ar}  "to become tired"
         + [جَزِعَ يَجْزَعُ جَزَعًا]{.ar}  "to be impatient"
         + [أَسِفَ يَأْسَفُ أَسَفًا]{.ar}  "to be sorrowful"
      ii. If, instead, the meaning of the verb denotes being a color, then the doing verbal-noun is usually of the pattern [فُعْلَة]{.ar} [fuelah]{.trn}. Examples:
          + [خَضِرَ يَخْضَرُ خُضْرَةً]{.ar}  "to be green"
          + [سَمِرَ يَسْمَرُ سُمْرَةً]{.ar}  "to be brown"
      iii. If, instead, the meaning of the verb denotes some work or effort, then the doing verbal-noun tends to be of the pattern [فُعُول]{.ar} [fueUl]{.trn}. Example:
           + [قَدِمَ يَقْدَمُ قُدُومًا]{.ar}  "to arrive"
      iv. If, instead, the meaning of the verb denotes some static quality, then the doing verbal-noun tends to be of the pattern [فُعُولَة]{.ar} [fueUlah]{.trn}. Example:
          + [يَبِسَ يَيْبَسُ يُبُوسَة]{.ar}  "to be dry"
   a. If the completed-action verb is of the pattern [فَعَلَ]{.ar} [faeala]{.trn}, then:
      i. If the meaning of the verb does not fall under the cases ii., iii., and iv. (below), then the doing verbal-noun tends to be, in general, of the pattern [فُعُول]{.ar} [fueUl]{.trn}. Examples:
         + [قَعَدَ يَقْعُدُ قُعُودًا]{.ar}  "to sit, stay back"
         + [سَجَدَ يَسْجُدُ سُجُودًا]{.ar}  "to prostrate down"
         + [خَضَعَ يَخْضَعُ خُضُوعًا]{.ar}  "to be humble"
      ii. If, instead, the meaning of the verb denotes an ailment, then the doing verbal-noun is usually of the pattern [فُعَال]{.ar} [fueAl]{.trn}. Examples:
          + [سَعَلَ يَسْعُلُ سُعَالً]{.ar}  "to cough"
      iii. If, instead, the meaning of the verb denotes travelling, then the doing verbal-noun is usually of the pattern [فَعِيل]{.ar} [faeIl]{.trn}. Examples:
           + [رَحَلَ يَرْحَلُ رَحِيلًا]{.ar}  "to depart"
      iv. If, instead, the meaning of the verb denotes a sound, then the doing verbal-noun is usually of the pattern [فَعِيل]{.ar} [faeIl]{.trn} or [فُعَال]{.ar} [fueAl]{.trn}, or both. Examples:
          + [صَرَخَ يَصْرُخُ صَرِيخًا وَصُرَاخًا]{.ar}  "to scream"
3. If the verb denotes a craft or a profession or a rank, then the doing verbal-noun is often of the pattern [فِعَالَة]{.ar} [fieAlah]{.trn}. Examples:
   + [تَجَرَ يَتْجُرُ تِجَارَةً]{.ar}  "to trade"
   + [أَمِرَ يَأْمَرُ إِمَارَةً]{.ar}  "to be a commander"
4. If the completed-action verb is of the pattern [فَعُلَ]{.ar} [faeula]{.trn}, then the doing verbal noun tends to be of the pattern [فُعُولَة]{.ar} [fueUlah]{.trn} or [فَعَالَة]{.ar} [faeAlah]{.trn}. Examples:
   + [صَعُبَ يَصْعُبُ صُعُوبَةً]{.ar}  "to be difficult"
   + [شَجُعَ يَشْجُعُ شَجَاعَةً]{.ar}  "to be brave"

As mentioned earlier, these are only general trends and there are many verbs that have doing verbal-nouns which don't fall under the above rules.

## Usage of the doing verbal-noun

### State and definiteness

The doing verbal noun has properties of a noun, like state and definiteness. But it gives the meaning of a verb. For example, consider the verb [أَكَلَ يَأْكُلُ أَكْلًا]{.ar}  "to eat". We can use its doing verbal noun in a sentence like this:

[فَرَغَ زَيْدٌ مِنَ ٱلْأَكْلِ.]{.ar}  
[faraga zaydun mina -lEakli.]{.trn}  
"Zayd got done with eating."

Note how the doing verbal noun [ٱلْأَكْلِ]{.ar} [EalEakli]{.trn} gives the meaning of the action of the verb "eating". But since it is a noun, it obeys the rules for nouns, like being in the i-state when preceded by the preposition [مِنْ]{.ar} [min]{.trn}.

Another point worth noting is that we have made it definite by saying [ٱَلْأَكْلِ]{.ar} [EalEakli]{.trn} instead of saying [أَكْلٍ]{.ar} [Eaklin]{.trn} for the meaning of "eating". This is because, as we explained in section 
\@ref(usage-of-definite-and-indefinite-nouns),
the definite noun is usually used in Arabic to give a general meaning, where in English we would not use "the". This may be a good time to re-read that section.

Having said that, the indefnite doing verbal-noun may be used too, and this will give the meaning of "a certain", or "a specific". For example, with the verb [عَمِلَ يَعْمَلُ عَمَلًا]{.ar}  "to work", we can say:

[فَرَغَ مِنْ عَمَلٍ صَعْبٍ.]{.ar}  
[faraga min eamalin Saebin.]{.trn}  
"He got done with a [certain] difficult work."

### With a doer

A doer may be used with the doing verbal-noun to show who is doing the action. In this case, the doing verbal-noun and the doer are usually placed in an annexation. The doing verbal-noun shall be the annexe noun and the doer shall be in the i-state as the base noun in the annexation. For example, consider the verb [قَرَأَ يَقْرَأُ قِرَاءَةً]{.ar}  "to read". We can say:

[سَمِعْتُ قِرَاءَةَ زَيْدٍ.]{.ar}  
[samietu qirAEata zaydin.]{.trn}  
"I heard Zayd's reading."

The doer may similarly be a pronoun, in which case, as usual, attached pronouns are used. So we can say:

[سَمِعْتُ قِرَاءَتَهُ.]{.ar}  
[samietu qirAEatahu.]{.trn}  
"I heard his reading."

### With an indirect doee

If a verb uses a particular preposition with indirect doees, and the doing verbal-noun of that verb is to be used with an indirect doee, then that same preposition is used with the doing verbal-noun.

For example the verb [ذَهَبَ يَذْهَبُ ذَهَابًا]{.ar}  "to go" is used with the preposition [إِلَىٰ]{.ar} [EilA]{.trn} "to" with an indirect doee to give the place to which the doer is going. This same preposition is then used with the doing verbal noun, thus:

[تَعِبْتُ مِنَ ٱلذَّهَابِ إِلَىٰ ٱلْمَدِينَةِ  ٱلْبَعِيدَةِ.]{.ar}  
[taeibtu mina -ppahAbi Eila -lmadInati -lbaeIdati.]{.trn}  
"I became tired from going to the far city."

If a doer is used along with the indirect doee, then the doer shall be placed in a noun chain with the doer verbal-noun, as explained in the previous section. For example,

[حَزِنْتُ مِنْ ذَهَابِ زَيْدٌ إِلَىٰ مَدِينَةٍ بَعِيدَةٍ.]{.ar}  
[Hazintu min pahAbi zaydin EilA madInatin baeIdatin.]{.trn}  
"I became sad from Zayd's going to a far city."

### With a direct doee

If a verb takes a direct doee, and we wish to use the direct doee with the verb's doing verbal noun, then we may deal with it in one of three ways:

#### The direct doee in the i-state in an annexation with the doing verbal noun

In the first method, the direct doee is in the i-state as the base noun in an annexation with the doing verbal-noun. This method is used when the doer of the verbal noun is not mentioned with the doing verbal-noun, or when there is no other phrase between the doing verbal-noun and the direct doee. For example,

[فَرَغَ زَيْدٌ مِنْ قِرَاءَةِ ٱلْكِتَابِ.]{.ar}  
[faraga zaydun min qirAEati -lkitAbi.]{.trn}  
"Zayd got done with reading the book."

In this sentence, [ٱَلْكِتَابِ]{.ar} [EalkitAbi]{.trn} "the book" is the direct doee of the doing verbal-noun [قِرَاءَةِ]{.ar} [qirAEati]{.trn} "reading". The doer [زَيْدٌ]{.ar} [zayd]{.trn} "Zayd" is only mentioned in the beginning of the sentence but not again with the doing verbal-noun. Therefore, the direct doee [ٱَلْكِتَابِ]{.ar} [EalkitAbi]{.trn} "the book" is allowed to be put in an annexation with the doing verbal noun thus: [قِرَاءَةِ ٱلْكِتَابِ]{.ar}  [qirAEati -lkitAbi]{.trn}  "reading the book".

Instead of a noun, the direct doee may be a pronoun instead. For example,

[قَرَأ زَيْدٌ ٱلْكِتَابَ فَفَرَغَ مِنْ قِرَاءَتِهِ.]{.ar}  
[qaraEa zayduni -lkitAba fafaraga min qirAEatihi]{.trn}  
"Zayd read the book, and then he got done with reading it."

Remember from the previous section, that a doer is handled in the same way with a doing verbal-noun by placing it in an annexation with the doing verbal-noun. So how do we know whether the base noun in an annexation with a doing verbal-noun is a doer or a doee? Well, for many verbs the meaning of the verbal-noun and the noun is sufficient. For example, in the phrase [قِرَاءَةِ ٱلْكِتَابِ]{.ar} [qirAEati -lkitAbi]{.trn} "reading the book", the meaning of "reading" makes it clear that [ٱَلْكِتَابِ]{.ar} [EalkitAbi]{.trn} can only be a doee, because a book can't be the one doing the reading.

But there are some verbs, however, where the meaning of the verbal-noun itself is not sufficient to tell us whether the noun following it in an annexation is a doer or a doee. Consider the verb 
<!--[قَتَلَ يَقْتُلُ قَتْلًا]{.ar} [qatala yaqtulu qatlan]{.trn} "to kill ([ه]{.ar} s.o.)".-->
[ضَرَبَ يَضْرِبُ ضَرْبًا]{.ar}  "to beat ([ه]{.ar} s.o.)". If we form an annexation using its doing verbal-noun, thus: [ضَرْبُ زَيْدٍ]{.ar} [Darbu zaydin]{.trn}, we cannot know whether Zayd is the doer (the one doing the beating), or the doee (the one getting beaten). In this case, we will need more context to help us determine whether Zayd is the doer or the doee. Here are a few sentences that may help illustrate this point:

[ضَرَبَ زَيْدٌ عَمْرًا. سَمِعَ ٱلْأَبُ **ضَرْبَ زَيْدٍ** فَغَضِبَ عَلَيْهِ. فَنَدِمَ زَيْدٌ مِنْ **ضَرْبِ عَمْرٍو**.]{.ar}  
[Daraba zaydun eamran. samiea -lEabu Darba zaydin fagaDiba ealayhi. fa nadima zaydun min Darbi eamrin.]{.trn}  
"Zayd beat [#eamr]{.trn2}. The father heard Zayd's beating so he became angry with him. So, Zayd became remorseful of beating [#eamr]{.trn2}."

We can see that the meaning of the sentences help us determine that in the phrase
[ضَرْبَ زَيْدٍ ]{.ar}
[Darba zaydin]{.trn}, Zayd is the doer, and in 
[ضَرْبِ عَمْرٍو]{.ar}
[Darbi eamrin]{.trn}, [#eamr]{.trn2} is the doee.

<!-- The masdar naSr may also be useful here:  نصر الله. نصر العبد-->

#### The direct doee in a-state following the doing verbal-noun

The second way to deal with a direct doee and a doing-verbal noun is to put it in the a-state after the doing verbal-noun. This is usually done when the doer is mentioned with the doing verbal-noun in an annexation with it. The direct doee is then placed after the doer in the a-state. For example, we can re-word the previous example:

<!--[سَمِعْتُ ضَرْبَ زَيْدٍ عَمْرًا.]{.ar}  
[samietu Darba zaydin eamran.]{.trn}  
"I heard Zayd's beating [#eamr]{.trn2}."-->

[ضَرَبَ زَيْدٌ عَمْرًا. سَمِعَ ٱلْأَبُ **ضَرْبَ زَيْدٍ عَمْرًا** فَغَضِبَ عَلَيْهِ. فَنَدِمَ زَيْدٌ مِنْ **ضَرْبِهِ عَمْرًا**.]{.ar}  
[Daraba zaydun eamran. samiea -lEabu Darba zaydin eamran fagaDiba ealayhi. fa nadima zaydun min Darbihi eamran.]{.trn}  
"Zayd beat [#eamr]{.trn2}. The father heard Zayd's beating [#eamr]{.trn2} so he became angry with him. So, Zayd became remorseful of his beating [#eamr]{.trn2}."

Notice that in [ضَرْبِهِ عَمْرًا]{.ar} [Darbihi eamran]{.trn} "his beating [#eamr]{.trn2}", the doer is a pronoun instead of a noun. This is permissible, and is in line with other usages we have learned so far.

The doee noun in the a-state, too, may be replaced with a pronoun, but just like when the attached doee pronoun is separated from its verb it has to instead be attached to the prefix [إِيَّا]{.ar} [EiyyA]{.trn}, here too this prefix is used. For example,

[أَلِمَ عَمْرٌو مِنْ ضَرْبِ زَيْدٍ إِيَّاهُ.]{.ar}  
[Ealima eamrun min Darbi zaydin EiyyAhu.]{.trn}  
"[#eamr]{.trn2} was in pain from Zayd's beating him."

This usage of putting the direct doee in the a-state after the doing verbal noun is not only done when the doer is mentioned with the doing verbal-noun. But it is also done when the direct doee is separated from the doing verbal-noun by some other words, like a prepositional phrase. For example,

[فَرَغْتُ مِنَ ٱلْقِرَاءَةِ فِي ٱلْمَكْتَبَةِ كِتَابًا.]{.ar}  
[faragtu mina -lqirAEati fi -lmaktabati kitAban.]{.trn}  
"I got done with reading, in the library, a book."

The prepositional phrase [فِي ٱلْمَكْتَبَةِ]{.ar} [fi -lmaktabati]{.trn} in the above example is placed between the doing verbal-noun and the doee for effect. It could, of course, also have been placed after the doee, in a more normal fashion. In this case, it would be preferred for the doing verbal-noun and the doee to be placed in an annexation, in the manner we have already learned.

[فَرَغْتُ مِنْ قِرَاءَةِ كِتَابٍ فِي ٱلْمَكْتَبَةِ .]{.ar}  
[faragtu min qirAEati kitAbin fi -lmaktabati.]{.trn}  
"I got done with reading a book in the library."

#### The direct doee in i-state preceded by the preposition [لِ]{.ar} [li]{.trn}

The third way to deal with a direct doee and a doing-verbal noun is to put it in the i-state preceded by the preposition [لِ]{.ar} [li]{.trn}. This is usually done in one of the following scenarios:

1. When the doing verbal-noun is indefinite and immediately precedes the direct doee. Example:

   [فَرَغْتُ مِنْ قِرَاءَةٍ لِلْكُتُبِ.]{.ar}  
   [faragtu min qirAEatin lilkutubi.]{.trn}  
   "I got done with a reading of the books."

   This sentence can be used to indicate one particular instance of reading the books. As opposed to saying [قِرَاءَةِ ٱلْكُتُبِ]{.ar} [qirAEati -lkutubi]{.trn} which would indicate that the reading was general or complete.

2. When the doer comes between the doing verbal-noun and the doee. Example,

   [أَلِمَ عَمْرٌو مِنْ ضَرْبِ زَيْدٍ لَهُ.]{.ar}  
   [Ealima eamrun min Darbi zaydin lahu.]{.trn}  
   "[#eamr]{.trn2} was in pain from Zayd's beating him."

   This is as an optional alternative to putting the doee in the a-state, in the manner we have already learned in the previous section:

   [أَلِمَ عَمْرٌو مِنْ ضَرْبِ زَيْدٍ إِيَّاهُ.]{.ar}  
   [Ealima eamrun min Darbi zaydin EiyyAhu.]{.trn}  
   "[#eamr]{.trn2} was in pain from Zayd's beating him."

## Multiple doing verbal-nouns for the same verb

It is possible, and fairly common, for verbs to have more than one doing verbal-noun. Usually, each of the doing verbal-nouns has its own meaning, distinct from each other.

For example, the verb [حَمَلَ يَحْمِلُ حَمْلًا]{.ar}  means "to carry ([هـ]{.ar} s.th.)" Here is an example of its doing verbal noun in a sentence:

[تَعِبَ زَيْدٌ مِنْ حَمْلِهِ لِلْكُتُبِ ٱلثَّقِيلَةِ.]{.ar}  
[taeiba zaydun min Hamlihi lilkutubi -vvaqIlati.]{.trn}  
"Zayd became tired from his carrying the heavy books."

There exists another meaning for this verb with its own doing verbal-noun: [حَمَلَ يَحْمِلُ حَمْلَةً]{.ar}  which means "to launch an attack ([عَلَىٰ]{.ar} on s.o.)" Here is an example of its doing verbal noun in a sentence:

[دَهِشَ ٱلْقَوْمُ مِنْ حَمْلَةِ ٱلْعَدُوِّ عَلَيْهِمْ.]{.ar}  
[dahica -lqawmu min Hamlati -leaduwwi ealayhim.]{.trn}  
"The people were astonished at the attack launched by the enemy on them."

Sometimes the meaning between the multiple doing verbal-nouns is only slight. Consider, for example, the verb [جَهِلَ يَجْهَلُ]{.ar}  "to not know, or to be ignorant ([هـ]{.ar} of s.th.)"

It has two doing verbal-nouns: [جَهْلٌ]{.ar} [jahl]{.trn} and [جَهَالَة]{.ar} [jahAlah]{.trn} which have meanings that are close to each other.

[جَهْلٌ]{.ar} [jahl]{.trn} is the more simple doing verbal-noun used for not knowing something. For example,

[مَا فَعَلَ زَيْدٌ ٱلْوَاجِبَ لِجَهْلِهِ إِيَّاهُ.]{.ar}  
[mA faeala zayduni -lwAjiba lijahlihi EiyyAhu.]{.trn}  
"Zayd did not do the obligatory [work] because of his not knowing it."

[جَهَالَة]{.ar} [jahAlah]{.trn} has the more abstract meaning of "ignorance". For example,

[نَفَرَ ٱلْمُسْلِمُ مِنْ جَهَالَةِ ٱلْمُشْرِكِينَ.]{.ar}  
[nafara -lmuslimu min jahAlati -lmucrikIna.]{.trn}  
"The Muslim was repulsed by the ignorance of the pagans."

As a general rule of thumb, the fewer letters in a doing verbal-noun, the simpler its meaning. And doing verbal-nouns of the pattern [فَعَالَة]{.ar} [faeAlah]{.trn} tend to have an abstract meaning.

## Doing verbal-nouns re-used as common nouns

There are many doing verbal-nouns, that in addition to their verbal meaning, are also re-used as common nouns. Their common noun meaning is typically associated, in some manner, with their verbal meaning.

<!--For example, the verb [عَلِمَ يَعْلَمُ عِلْمًا]{.ar} [ealima yaelamu eilman]{.trn} means "to know". The doing verbal-noun [عِلْمٌ]{.ar} [eilmun]{.trn} can be used with its verbal meaning: "knowing". For example,-->

For example, the verb [سَأَلَ يَسْأَلُ سُؤَالًا]{.ar}  means "to question or ask ([ه عن]{.ar} s.o. about s.th.)". The doing verbal-noun [سُؤَالٌ]{.ar} [suEAlun]{.trn} can be used with its verbal meaning: "questioning". For example,

[سَئِمَ ٱلْأَبُ مِنْ كَثْرَةِ سُؤَالِ ٱبْنِهِ إِيَّاهُ.]{.ar}  
[saEima -lEabu min kavrati suEAli -bnihi EiyyAhu.]{.trn}  
"The father became weary from the excessiveness of his son's questioning him."

[سُؤَالٌ]{.ar} [suEAlun]{.trn}, in addition to being a doing verbal-noun "questioning" is re-used as a common noun with the meaning "a question" and the broken plural [أَسْئِلَة]{.ar} [EasEilah]{.trn} "questions". So, for example, we can say:

[كَتَبَ ٱلْأُسْتَاذُ سُؤَالًا عَلَى ٱلسَّبُّورَةِ.]{.ar}  
[kataba -lEustApu suEAlan eala -ssabbUrati.]{.trn}  
"The professor wrote a question on the board."

## Common nouns re-used as doing verbal-nouns

Just as some doing verbal-nouns are re-used as common nouns, there are some common nouns that may be re-used as doing verbal-nouns. For example, the verb [فَعَلَ يَفْعَلُ]{.ar}  "to do ([هـ]{.ar} an action)" has the doing verbal-noun [فَعْلٌ]{.ar} [faelun]{.trn}.

There is an associated common noun from this root: [فِعْلٌ]{.ar} [fielun]{.trn} "an act". This common noun is frequently used in place of the doing verbal-noun [فَعْلٌ]{.ar} [faelun]{.trn}. For example:

[طَلَبَ ٱلْأُسْتَاذُ مِنَ ٱلتَّلَامِيذِ فِعْلَ ٱلْوَاجِبِ.]{.ar}  
[Talaba -lEustApu mina -ttalAmIpa fiela -lwAjibi.]{.trn}  
"The professor wanted from his students the doing of the obligatory [work]."

## TODO

Add multiple doees with masdar


<!--chapter:end:srcrmd/doing_verbal_noun.Rmd-->

# The verbal-nouns of the doer and the doee

## Introduction

In the previous chapter we studied the verbal-noun of doing. In this chapter we shall study two more kinds of verbal-nouns. These are the doer verbal-noun and the doee-verbal noun. These, too, are nouns that can give the meaning of the verb they are derived from. In places, they may even replace the verb, thereby adding some nuances in meaning.

The doer verbal-noun gives the meaning of the doer, that is the person doing the action of the verb. For example, for the verb [قَرَأَ يَقْرَأُ قِرَاءَةً]{.ar}  "to read", the doer verbal-noun is [قَارِئ]{.ar} [qAriE]{.trn} "a reader".

## Pattern of the doer verbal-noun

We saw in the previous chapter that the pattern for the doing verbal-noun for form\ 1 verbs was very variable. In contrast, the pattern for the doer verbal-noun for form\ 1 verbs is fixed. It is always on the pasttern [فَاعِل]{.ar} [fAeil]{.trn}. Also, the doer verbal-noun is modified for gender and number. Its forms its feminine by appending [ة]{.ar} thus: [فَاعِلَة]{.ar}. It takes sound plurals: the [-Un]{.trn} for the masculine, and the [-At]{.trn} plural for the feminine. In many case, it may also have broken plurals. Here is a table showing these modifications for the u-state. You should be able to extend them for the a-state and i-state.

| Number | Masculine | Feminine |
|:---|:---|:---|
|singular|[فَاعِلٌ]{.ar} [fAeilun]{.trn}|[فَاعِلَةٌ]{.ar} [fAeilatun]{.trn}|
|dual|[فَاعِلَانِ]{.ar} [fAeilAni]{.trn}|[فَاعِلَتَانِ]{.ar} [fAeilatAni]{.trn}|
|plural|[فَاعِلُونَ]{.ar} [fAeilUna]{.trn}|[فَاعِلَاتٌ]{.ar} [fAeilAtun]{.trn}|

## The doer verbal-noun as a noun

Like the doing verbal-noun, the doer verbal noun occupies a place that is between a noun and a verb. The basic, most essential, meaning of the doer verbal noun is that of a noun which denotes the doer of the verb.

So, for example, consider the verb [سَأَلَ يَسْأَلُ سُؤَالًا]{.ar}  "to question". Its doer verbal-noun is [سَائِل]{.ar}. Since it refers to the doer of this verb, we can translate it as "a questioner~m.~".

By itself, the word [سَائِل]{.ar}  "a questioner" just denotes a noun. It does not indicate when the doer does the action of the verb: has the questioner already asked the question, is he asking it at present, or will he ask it in the future? So, for example, we can say:

[سَيَقْدَمُ سَائِلٌ وَسَيَسْأَلُ سُؤَالًا.]{.ar}  
[sayaqdamu sAEilun wasayaqdamu suEAlan.]{.trn}  
"A questioner~m.~ will arrive and he will ask a question."

In the above sentence, the doer verbal-noun is being described as performing the action of the verb in the future.

Here is another example:

[سَأَلَتِ ٱلْفَقِيهَ سَائِلَةٌ عَنْ أَمْرٍ.]{.ar}  
[saEalati -lfaqIha sAEilatun ean Eamrin.]{.trn}  
"A questioner~f.~ asked the jurist about a matter."

In the above sentence, the doer verbal-noun is being described as having performed the action of the verb in the past.

Doer verbal-nouns of form\ 1 verbs, when used with this nounal meaning, often have broken plurals, in addition to their sound plurals. Generally, either could be used in most cases, but the usage of the broken plurals is preferred.

For example, consider the verb [قَتَلَ يَقْتُلُ قَتْلًا]{.ar}  "to kill ([ه]{.ar} s.o.)". Its doer verbal-noun is [قَاتِل]{.ar} "a killer~m.~". Its sound plural is [قَاتِلُونَ]{.ar} [qAtilUna]{.trn} and its broken plurals are [قُتَّال]{.ar} [quttAl]{.trn} and [قَتَلَة]{.ar} [qatalah]{.trn}. Any of these could be used but the broken plural is often preferred.

[هَرَبَ قَتَلَةُ ٱلرَّجُلِ إِلَىٰ مَخْبَئِهِمْ.]{.ar}  
[haraba qatalatu -rrajuli EilA maxbaEihim.]{.trn}  
"The killers of the man fled to their hideout."

## The doer verbal-noun as a verb

We have learned that the essential meaning of the doer verbal-noun is the doer of the action of the verb from which it is derived. In addition to this essential meaning, the doer verbal-noun can also be used in place of the verb from which it is derived. This is only done when the verb to be replaced is the incomplete-action verb. The doer verbal-noun does not replace the completed-action verb. We will now explain this usage.

### Usage of the doer verbal-noun as a present tense verb

Consider the following sentence:

[يَذْهَبُ زَيْدٌ إِلَى ٱلْمَدْرَسَةِ.]{.ar}  
[yaphabu zaydun Eila -lmadrasati.]{.trn}  
"Zayd goes to school."

The above sentence does not explicitly specify whether Zayd is actually going to school at present, or that he goes to school habitually and not necessarily right now.

If we wish to indicate that Zayd is actually going to school at present we can replace the incomplete-action verb with the indefinite doer verbal-noun. So we get:

[زَيْدٌ ذَاهِبٌ إِلَى ٱلْمَدْرَسَةِ.]{.ar}  
[yaphabu zaydun Eila -lmadrasati.]{.trn}  
"Zayd is going to school."

Note that the same preposition [إِلَىٰ]{.ar} [EilA]{.trn} "to" is used with the doer verbal-noun as is used with the verb.
Also note that this is now a subject-information sentence instead of a verbal sentence. [زَيْدٌ]{.ar} [zaydun]{.trn} "Zayd" is the subject, and [ذَاهِبٌ]{.ar} [pAhibun]{.trn} is part of the information.

This usage of the doer verbal-noun to indicate that the action of the verb is ocurring at present is mostly done for what we call _verbs of posture_ and _verbs of motion_.

Verbs of posture denote a static position or activity of the doer's body and include verbs like sitting, standing, lying down, sleeping, etc.

Verbs of motion denote a moving action of the doer's body and include verbs like
going, coming, running, etc.

So, if, for example, we say,

[زَيْنَبُ جَالِسَةٌ عَلَى هَـٰذَا ٱلْكُرْسِيِّ.]{.ar}  
[zaynabu jAlisatun eala hApa -lkursiyyi.]{.trn}  
"Zaynab is sitting on this chair."

this indicates that Zaynab is sitting on this chair at present. And if we say,

[تَجْلِسُ زَيْنَبُ عَلَى هَـٰذَا ٱلْكُرْسِيِّ.]{.ar}  
[tajlisu zaynabu eala hApa -lkursiyyi.]{.trn}  
"Zaynab sits on this chair."

this indicates that Zaynab usually sits on this chair.

If this usage of the doer verbal-noun to indicate a present action is mostly only for verbs of posture and motion, how then do we indicate this distinction for other verbs? We have answered this in section [TODO: add section to incomplete-action verb] where we said that in order to give the meaning that the action of the verb is happening right now, a verbal sentence can be converted to a subject-information sentence. 

### Usage of the doer verbal-noun as a future tense verb {#doer-verbal-noun-for-intended-future-action}

The doer verbal-noun may be used in place of the verb it is derived from to indicate an intent on the part of the doer, or to indicate that the action will occur in the future.

This usage of the doer verbal-noun is not just for verbs of posture and motion like the present tense usage. Rather, it is for all verbs in general.

And since intention is something that is mostly expressed by the speaker for himself, rather than for someone else, we will often find this usage with the subject [أَنَا]{.ar} [Eana]{.trn} "I".

#### With an indirect doee

Here is an example of the usage of the doer verbal-noun as a future tense verb with an indirect doee:

<!--
[فَرَغْتُ مِنْ عَمَلِي فَأَنا ذَاهِبٌ  إِلَى ٱلْبَيْتِ.]{.ar}  
[faragtu min eamalI faEana pAhibun Eila -lbayti.]{.trn}  
"I have got done with my work so I'm going home."

The context would tell us whether the person is talking about his intention to go home in the immediate future, or whether he has already started and is going home at present.
-->

[أَنَا ذَاهِبٌ إِلَىٰ بَيْتِ صَدِيقِي فِي ٱلصَّبَاحِ.]{.ar}  
[Eana pAhibun EilA bayti SadIqI fi -SSabAHi.]{.trn}  
"I'm going to go to my friend's house in the morning."

In the above sentence it is possible for the phrase 
[فِي ٱلصَّبَاحِ]{.ar}
[fi -SSabAHi]{.trn}
"in the morning"
to be ommitted for the same meaning. In that case, surrounding context could tell us that the person is intending to go in the future, and is not actually in the process of going there at present.

Here is another example (by a female speaker):

[عِنْدِي كُرَةٌ فِي ٱلْبَيْتِ فَأَنَا رَاجِعَةٌ إِلَى ٱلْبَيْتِ وَلَاعِبَةٌ بِهَا.]{.ar}  
[eindI kuratun fi -lbayti faEana rAjieatun Eila -lbayti walAeibatun bihA.]{.trn}  
"I have a ball at home, so I'm going to go home and play with it."

#### Difference with the particles [سَـ]{.ar} [sa-]{.trn} and [سَوْفَ]{.ar} [sawfa]{.trn}

We have already learned a method to express a future action using the particles [سَـ]{.ar} [sa-]{.trn} and [سَوْفَ]{.ar} [sawfa]{.trn} with the incomplete-action verb. So we could also have said:

[سَأَذْهَبُ إِلَىٰ بَيْتِ صَدِيقِي.]{.ar}  
[saEaphabu EilA bayti SadIqI.]{.trn}  
"I will to go to my friend's house."

The difference between using the particles [سَـ]{.ar} [sa-]{.trn} and [سَوْفَ]{.ar} [sawfa]{.trn} and using the doer verbal-noun is that using the doer verbal-noun signifies more emphasis, or, as a possible consequence of the emphasis, that the action is more imminent. That is:

[أَنَا ذَاهِبٌ ...]{.ar}  
[Eana pAhibun ...]{.trn}  
"I will [definitely] go ..."  
or  
"I'm going to go ..."

[سَأَذْهَبُ ...]{.ar}  
[saEaphabu ...]{.trn}  
"[Soon] I will go ..."

#### With a direct doee

If a verb takes a direct doee, and we wish to use the direct doee with the verb's doer verbal-noun when the doer verbal-noun is acting as a verb, then we may deal with it in one of three ways:

1. The direct doee in a-state following the doer verbal-noun

   The most basic method of dealing with a direct doee of a doer verbal noun is by placing it in the a-state right after the doer verbal-noun. Here is an example,
   
   [قَدْ دَخَلَ ٱلْمَدِينَةَ رَجُلٌ شَرِيرٌ. هُوَ **قَاتِلٌ سُكَّانَهَا**.]{.ar}  
   [qad daxala -lmadInata rajulun carIrun. hua qAtilun sukkAnahA.]{.trn}  
   "An evil man has entered the city. He is going to kill its residents."
   
   <!-- Wright says: When the اسم الفاعل is indefinite then مفعول به منصوب is only allowed under certain scenarios: The اسم الفاعل is a خبر or other attribute, or a negative sentence, or a question. (vol. ii, § 30, p. 65). This seems similar to prohibition of indef subjects so I don't think it is necessary to add that detail here. It seems like doer verbal-noun will naturally be a predicate.-->

2. The direct doee in i-state annexed to the doer verbal-noun

   The combination of the doer verbal-noun and following direct doee in the a-state is often replaced with an annexation of the doer verbal-noun to the i-state direct doee. So, for example, instead of the above example, we can say:
   
   [قَدْ دَخَلَ ٱلْمَدِينَةَ رَجُلٌ شَرِيرٌ. هُوَ **قَاتِلُ سُكَّانِهَا**.]{.ar}  
   [qad daxala -lmadInata rajulun carIrun. hua qAtilu sukkAnihA.]{.trn}  
   "An evil man has entered the city. He is going to kill its residents."

   Note that [قَاتِلُ سُكَّانِهَا]{.ar} [qAtilu sukkAnihA.]{.trn} can also support the non-verbal meaning of the doer verbal-noun: "killer of its residents", i.e., he has already killed its residents in the past. So, when an annexation is used with a doer verbal-noun, we will often need surrounding context to tell us whether the verbal (incomplete-action) meaning is intended, or the noun  meaning.

   This usage of annexing the doer verbal-noun to the i-state direct doee instead of employing the more basic usage of the doer verbal-noun and a following a-state direct doee is optional, but fairly common. In fact, when the doer-verbal noun ends with an [n]{.trn}-mark, and the direct doee begins with [ٱَلْ]{.ar} [Eal]{.trn} "the", then the annexation usage becomes predominant over the basic a-state usage. So we will be more likely to see:

   [أَنَا فَاعِلُهُ.]{.ar}  
   [Eana fAeiluhu.]{.trn}  

   instead of:

   [أَنَا فَاعِلٌ إِيَّاهُ.]{.ar}  
   [Eana fAeilun EiyyAhu.]{.trn}  

   for the meaning: "I will do it." Note again, that the latter sentence could also support the nounal meaning of the doer-verbal noun: "I am its doer.", i.e., "the one who did it."

   Similarly, it will be more common to find:

   [هُوَ قَاتِلُ ٱلنَّاسِ.]{.ar}  
   [huwa qAtilu -nnAsi.]{.trn}  

   instead of:

   [هُوَ قَاتِلٌ ٱلنَّاسَ.]{.ar}  
   [huwa qAtiluni -nnAsa.]{.trn}  

   for the meaning: "He is going to kill the people." Note, once again, that the former sentence also supports the meaning: "He is the people's killer.", i.e., "the one who killed them", and that context would be needed to tell us which of the two meanings is intended.

   The annexation of a doer verbal-noun to its direct doee in the i-state is not the kind of "proper" annexation that we have learned so far. In fact, it is called an _improper annexation_ and we shall study it in more detail in chapter [TODO], if [#allAh]{.trn2} wills.

3. Quite similar to what we learned in section\ \@ref(the-direct-doee-in-i-state-preceded-by-the-preposition-%D9%84-li) for doing verbal-nouns, the direct doee can follow the doer verbal-noun in the i-state preceded by the preposition [لِ]{.ar} [li]{.trn}.

   <!--Quran:  إنل له لحافظون -->
   This is often optional, as an alternative to the above two methods. For example,
   
   [هُوَ قَاتِلٌ لَهُمْ.]{.ar}  
   [huwa qAtilun lahum.]{.trn}  
   "He will kill them."
   
   Using [لِ]{.ar} [li]{.trn} in this manner is also a technique to move the direct doee before the doer verbal-noun for effect, if desired. For example,
   
   [هُوَ لَهُمْ قَاتِلٌ.]{.ar}  
   [huwa lahum qAtilun.]{.trn}  
   "He will kill them."

### The definite doer verbal-noun as a verb

<!-- from Quran:  الكاظمين الغيظ ، المؤتون الزكاة , many be improper annexxation too -->
So far we have seen only an indefinite doer verbal-noun being used with the meaning of an incomplete-action verb. However, the definite doer verbal-noun, too, can give this meaning. The meaning is often in the present tense. Here are some examples:

With an indirect doee:

[قَدِمَ زَيْدٌ ٱلذَّاهِبُ إِلَى ٱلْجَامِعَةِ.]{.ar}  
[qadima zayduni -ppAhibu Eila -ljAmieati.]{.trn}  
"Zayd, the one who goes to the university, has arrived."

With a direct doee in the a-state:

[هَرَبْتُ مِنَ ٱلْأَسَدِ ٱلْآكِلُ ٱلْإِنْسَانَ.]{.ar}  
[harabtu mina -lEasadi -lEAkilu -lEinsAna.]{.trn}  
"I fled from the lion, the one that eats man."

With a direct doee in the i-state preceded by the preposition [لِ]{.ar} [li]{.trn}:
<!--[قَدْ سَفِهَ ٱلْفَاسِقُ ٱلشَّارِبُ لِلْخَمْرِ.]{.ar}  
[qad safiha -lfAsiqu -ccAribu lilxamri.]{.trn}  
"The evil-doer, the one who drinks wine, has become foolish."-->

[سَيَنْجَحُ ٱلطَّالِبُ ٱلتَّارِكُ لِلَّهْوِ.]{.ar}  
[sayanjaHu -TTAlibu -ttAriku lillahwi.]{.trn}  
"The student, the one who leaves idle amusement, will succeed."

### Plurals of the doer verbal-noun when used as a verb

We mentioned in section\ \@ref(the-doer-verbal-noun-as-a-noun) that doer-verbal nouns when used with their nounal meaning often have broken plurals along with their sound plural.
We gave the example of the doer verbal-noun
[قَاتِل]{.ar} [qAtil]{.trn} "a killer~m.~" with the sound plural is [قَاتِلُونَ]{.ar} [qAtilUna]{.trn} and the broken plurals [قُتَّال]{.ar} [quttAl]{.trn} and [قَتَلَة]{.ar} [qatalah]{.trn}.

When the doer verbal-noun is used as a verb, only the sound plural is permitted to be used, and the broken plurals, if any are not used. So we can only say:

[هُمْ قَاتِلُونَ ٱلنَّاسَ.]{.ar}  
[hum qAtilUna -nnAsa.]{.trn}  
and  
[هُمْ قَاتِلُو ٱلنَّاسِ.]{.ar}  
[hum qAtilu -nnAsi.]{.trn}  
for  
"They will kill the people."  
not, for example  
$\times$\ [هُمْ قُتَّالٌ ٱلنَّاسَ.]{.ar}  

(In the second sentence, the [ن]{.ar} of [قَاتِلُونَ]{.ar} is ommitted because it is an annexe noun).

## The doee verbal-noun

The doee verbal-noun for form\ 1 verbs is on the pattern [مَفْعُول]{.ar} [mafeUl]{.trn}. It carries the meaning of the person or thing to whom the action of the verb has been done. For example, the doee verbal-noun for the verb
[قَتَلَ يَقْتُلُ قَتْلًا]{.ar}  "to kill ([ه]{.ar} s.o.)"
is [مَقْتُول]{.ar} [maqtUl]{.trn} and means "a killed person".

### The plural of the doee verbal noun

The doee verbal-noun almost always takes the sound plurals [-Un]{.trn} for masculine intelligent beings, and [-At]{.trn} otherwise. Therefore the plural of the doee verbal-noun 
[مَقْتُول]{.ar} [maqtUl]{.trn} "a killed person~m.~" is [مَقْتُولُونَ]{.ar} [maqtUlUna]{.trn} "killed persons~m.~".
and the plural of the doee verbal-noun 
[مَقْتُولَة]{.ar} [maqtUlah]{.trn} "a killed person~f.~" is [مَقْتُولَات]{.ar} [maqtUlAt]{.trn} "killed persons~f.~".

There are a only a few doee verbal-nouns that, as an exception, have broken plurals. The broken plural for these exceptions is than always on the pattern ^2^[مَفَاعِيل]{.ar} [mafAeIl]{.trn}^2^. For example, the doee verbal-noun for the verb
[لَعَنَ يَلْعَنُ لَعْنًا]{.ar}  "to curse ([ه]{.ar} s.o.)" is [مَلْعُون]{.ar} [maleUn]{.trn} "accursed" and its plural is ^2^[مَلَاعِين]{.ar} [malAeIn]{.trn}^2^.

### Usage of the doee verbal-noun

Much of what has been said regarding the doer verbal-noun applies to the doee verbal-noun as well: The doee verbal-noun may be used with a verbal meaning for the incomplete-action verb only. So if we say:

[هُوَ مَقْتُولٌ.]{.ar}  
[huwa maqtUl]{.trn}

with a verbal meaning, then it means "He will be killed." And if we say it using its nounal meaning, then it means "He is the person killed."

Unlike the doer verbal-noun which can take doees, since the doee verbal-noun is itself the doee, there is no question of it taking other doees. So this does simplify matters.

### The doee verbal-nouns of indirect doee verbs

Consider the verb
[سَأَلَ يَسْأَلُ سُؤَالًا]{.ar}  "to question ([ه عن]{.ar} s.o. about s.th.)".

Here it is used in a sentence:

[سَأَلَ زَيْدٌ زَيْنَبَ عَنْ حَادِثَةٍ.]{.ar}  
[saEala zaydun zaynaba ean HAdivah.]{.trn}  
"Zayd questioned Zaynab about an accident."

In this sentence, [زَيْدٌ]{.ar} [zaydun]{.trn} "Zayd" is the doer. The corresponding doer verbal-noun that refers to him is [سَائِل]{.ar} [sAEil]{.trn} "a questioner~m.~".
Next, [زَيْنَبَ]{.ar} [zaynaba]{.trn} "Zaynab" is the direct doee. The corresponding doee verbal-noun that refers to her is [مَسْؤُولَة]{.ar} [masEUlah]{.trn} "a questioned person~f.~".
But how, now, do we refer to the indirect doee: [حَادِثَةٍ]{.ar} [Hadivatin]{.trn} "an accident"? The answer is that the doee verbal-noun referring to this indirect doee is [مَسْؤُول عَنْهَا]{.ar} [masEUl eanhA]{.trn} "a thing~f.~ questioned about".

Let's analyze this term [مَسْؤُول عَنْهَا]{.ar} [masEUl eanhA]{.trn} "a thing questioned about" carefully. The first word is [مَسْؤُول]{.ar} [masEUl]{.trn} which shall always be singular masculine, regardless of the gender and number of the indirect doee. The second word is [عَنْهَا]{.ar} [eanhA]{.trn} "about it". Here [عَنْ]{.ar} [ean]{.trn} is the same preposition that has been used with the verb. And [هَا]{.ar} [hA]{.trn} is the pronoun that refers to the indirect doee [حَادِثَةٍ]{.ar} [Hadivatin]{.trn} "an accident". If the number or gender of the indirect doee were to change then this would be reflected in this pronoun. 

So, for example, if we say,

[نَظَرَ زَيْدٌ إِلَى ٱلرِّجَالِ.]{.ar}  
[naPara zaydun Eila -rrijAli.]{.trn}  
"Zayd looked at the men."

then, the doee verbal-noun that refers to [ٱلرِّجَالِ]{.ar} [EarrijAli]{.trn} "the men" is [مَنْظُور إِلَيْهِمْ]{.ar} [manPUr Eilayhim]{.trn} "persons~m.~ looked at".

If doee verbal-nouns of indirect doees are used in sentences then it is the first word (in this case [مَنْظُور]{.ar} [manPUrun]{.trn}) that changes for definiteness and state (but not for gender or number, as already discussed). Here are some examples:

From the verb [لَعِبَ يَلْعَبُ لَعِبًا]{.ar} "to play ([هـ]{.ar} s.th.)":

[هَـٰذِهِ ٱلْكُرىٰ هِيَ ٱلْمَلْعُوبُ بِهَا.]{.ar}  
[hApi -lkurA hiya -lmaleUbu bihA.]{.trn}  
"These balls are the ones played with."

From the verb [أَمَرَ يَأْمُرُ أَمْرًا]{.ar}  "to order ([ه]{.ar} s.o. [ب]{.ar} to do s.th.)":

[فَعَلَ ٱلْغُلَامُ ٱلْمأمُورَ بِهِنَّ.]{.ar}  
[faeala -lgulAmu -lmaEmUra bihinna.]{.trn}  
"The boy did the [things] ordered to do."

(Remember that the feminine plural pronouns may be used to refer to plural non-intelligent beings, regardless of their grammatical gender, in order to indicate plurality.)

Having said all this, in practice, you may find that indirect doees are sometimes treated as direct doees when forming their doee verbal-noun. This is especially common when forming plurals for terms that are very common. So instead of referring to "[things] ordered to do" in the above example as 
[ٱَلْمأمُورَ بِهِنَّ]{.ar}
[EalmaEmUra bihinna]{.trn}, you may find the word [ٱَلْمَأْمُورَاتِ]{.ar} [EalmaEmUrAti]{.trn} used instead.

TODO: The doee verbal noun for indirect doees may have some ambiguity with the doee verbal for direct doees. [مسؤول عنه]{.ar} can also be "the person who is asked about it" where the pronoun has been substituted for a noun, for example [مسؤول عن الأمر]{.ar} . In this case it is the word [مسؤول]{.ar} which will be feminized and pluralized. [المسؤولون عنه]{.ar} "the persons asked about it."

For that matter [ساءل عنه]{.ar} is also valid as "the questioner about it".
<!--[سَأَلَ زَيْدٌ زَيْنَبَ عَنِ ٱلرِّجَالِ.]{.ar}  
[saEala zaydun zaynaba eani -rrijAli.]{.trn}  
"Zayd questioned Zaynab about the men."

then, the doee verbal-noun that refers to [ٱلرِّجَالِ]{.ar} [EarrijAli]{.trn} "the men" is [مَسْؤُولٌ عَنْ
-->

<!--[أَمْرٌ]{.ar} [Eamrun]{.trn} "a matter"? It is -->

## Doer and doee verbal-nouns re-used as adjectival-nouns

Doer and doee verbal-nouns are often re-used as adjectival-nouns with meanings that are directly formed from their doer and doee meaning respectively. Here are some examples:

|Verb | Doer/doee verbal-noun | Adjectival-noun meaning|
|:------|:-|:--|
|[نَعُمَ يَنْعُمَ نُعُومَةً]{.ar} "to be soft" | [نَاعِم]{.ar} | "soft" |
|[يَبِسَ يَيْبَسُ يُبُوسَةً]{.ar} "to be dried up" | [يَابِس]{.ar} | "dried up" |
|[حَضَرَ يَحْضُرُ حُضُورًا]{.ar} "to be present" | [حَاضِر]{.ar} | "present (attending)" |
|[جَمَعَ يَجْمَعُ جَمْعًا]{.ar} "to gather ([هـ]{.ar} s.th.)"| [جَامِع]{.ar}  | "comprehensive" |
|[لَمَعَ يَلْمَعُ لَمْعًا وَلَمَعَانًا]{.ar} "to be shiny" | [لَامِع]{.ar} | "shiny" |
|[فَتَحَ يَفْتَحُ فَتْحًا]{.ar} "to open ([هـ]{.ar} s.th.)" | [مَفْتُوح]{.ar} | "open" |
|[شَهَرَ يَشْهَرُ شَهْرًا]{.ar} "to make famous ([ه، هـ]{.ar} s.o., s.th.)" | [مَشْهُور]{.ar} | "famous" |

### Genderizability of doer and doee verbal-nouns when re-used as adjectival-nouns

When a doer or doee verbal-noun is re-used as an adjectival-noun, then it generally retains its genderizability. For example,

[بَابٌ مَفَتُوحٌ]{.ar}  
[bAbun maftUHun]{.trn}  
"an open door"

and

[نَافِذَةٌ مَفَتُوحَةٌ]{.ar}  
[nAfipatun maftUHatun]{.trn}  
"an open window"

If, however, the adjectival-noun is only applicable to females, then, only a female adjectival-noun is formed but, peculiarly, without the feminine marker [ة]{.ar}. The most common example is from the verb:
[حَمَلَ يَحْمِلٌ حَمْلًا]{.ar} "to carry ([هـ]{.ar} s.th.)". The doer verbal-noun is [حَامِل]{.ar} [HAmil]{.trn} "a carrier". The adjectival-noun formed from the doer verbal-noun is "pregnant", but because it is only applicable to females, it does not get the feminine marker [ة]{.ar}. For example,

[ٱَلْمَرْأَةُ حَامِلٌ.]{.ar}  
[EalmarEatu HAmil.]{.trn}  
"The woman is pregnant."

This does not affect the doer verbal-noun when it is not used with this adjectival-noun meaning. For example,

[ٱَلْمَرْأَةُ حَامِلَةُ ٱلْمَاءِ.]{.ar}  
[EalmarEatu HAmilatu -lmAE.]{.trn}  
"The woman will carry the water."  
or  
"The woman is the water-carrier."

### Corresponding with English adjectives

Sometimes both the doer verbal-noun and the doee verbal-noun are used in Arabic with distinct meanings where we would use the same word in English. For example, the verb
[عَقَلَ يَعْقِلُ عَقْلًا]{.ar} [eaqala yaeqilu eaqlan]{.trn} means "to make sense ([هـ]{.ar} of s.th.)".
Its doer verbal-noun [عَاقِل]{.ar} [eAqil]{.trn} means "one who makes sense (of something)" and may be re-used as an adjectival noun meaning "sensible" when it refers to a person who makes sense of something. For example,

[زَيْدٌ غُلَامٌ عَاقِلٌ.]{.ar}  
[zaydun gulAmun eAqil.]{.trn}  
"Zayd is a sensible boy."

Its doee verbal-noun [مَعْقُول]{.ar} [maeqUl]{.trn} means "something which makes sense" and may be re-used as an adjectival noun meaning "sensible" when it refers to a something which makes sense. For example,

[هَـٰذَا مَنْهَجٌ مَعْقُولٌ.]{.ar}  
[hApA manhajun maeqUl.]{.trn}  
"This is a sensible approach."

## Doer and doee verbal-nouns re-used as common nouns

The doer verbal-noun is often re-used as a common noun with a meaning that is either directly, or indirectly related to the meaning of the verb. For example, the doer verbal-noun of the verb [سَأَلَ يَسْأَلُ سُؤَالًا]{.ar} [saEala yasEalu suEAlan]{.trn} is [سَائِل]{.ar} "a questioner" with the sound plural [سَائِلُونَ]{.ar} [sAEilUna]{.trn} and the broken plurals [سُؤَّال]{.ar} [suEEAl]{.trn} and [سَأَلَة]{.ar} [saEalah]{.trn}.

The word [سَائِل]{.ar} [sAEil]{.trn} "a questioner" is re-used with the meaning "a beggar". The association in meaning is that a beggar continually asks people for money. 

The re-use of a doer verbal-noun or doee verbal-noun as a common noun does not prevent it from being used with its doer/doee or verbal meaning any more. 
[سَائِل]{.ar} [sAEil]{.trn} may be used to mean both "a questioner" and "a beggar", and context will help us determine which of the meanings is intended.

When a doer verbal-noun is re-used as a common noun then only the broken plural, if it exists, may be used. The sound plural is only permitted to be used if no broken plurals exist. Here are some more examples of doer verbal-nouns re-used as common nouns:
<!--
|Verb | Doer verbal-noun | Plural | Common noun meaning|
|:------|:--|:--|:--|
|[عَلِمَ يَعْلَمُ عِلْمًا]{.ar} [ealima yaelamu eilman]{.trn} "to know ([هـ]{.ar} s.th.)" | [عَالِمٌ]{.ar} [eAlimun]{.trn} | [عُلَمَاءُ]{.ar} [eAlimun]{.trn}| "a scholar"|
|[لَعِبَ يَلْعَبُ لَعِبًا]{.ar} [laeiba yaleabu laeiban]{.trn} "to play ([هـ]{.ar} s.th.)" | [لَاعِبٌ]{.ar} [lAeibun]{.trn} | [لَاعِبُونَ]{.ar} [lAeibUna]{.trn} | "a player"|
|[جَمَعَ يَجْمَعُ جَمْعًا]{.ar} [jamaea yajmaeu jamean]{.trn} "to gather ([هـ]{.ar} s.th.)"| [جَامِعَةٌ]{.ar} [jAmieatun]{.trn} | [جَامِعَاتٌ]{.ar} [jAmieAtun]{.trn} | "a university" |
|[حَدَثَ يَحْدُثُ حُدُوثًا]{.ar} [Hadava yaHduvu HudUvan]{.trn} "to happen" | [حَادِثَةٌ]{.ar} [Hadivatun]{.trn} | [حَوَادِثُ]{.ar} [HawAdivu]{.trn} | "an accident" |
-->

|Verb | Doer/doee verbal-noun | Plural | Common noun meaning|
|:------|:-|:-|:--|
|[عَلِمَ يَعْلَمُ عِلْمًا]{.ar} "to know ([هـ]{.ar} s.th.)" | [عَالِم]{.ar}  | ^2^[عُلَمَاء]{.ar} | "a scholar"|
|[طَلَبَ يَطْلُبُ طَلَبًا]{.ar} "to seek ([هـ]{.ar} s.th.)" | [طَالِب]{.ar}  | [طُلَّاب، طَلَبَة]{.ar} | "a student"|
|[لَعِبَ يَلْعَبُ لَعِبًا]{.ar} "to play ([هـ]{.ar} s.th.)" | [لَاعِب]{.ar}  | [لَاعِبُونَ]{.ar}  | "a player"|
|[جَمَعَ يَجْمَعُ جَمْعًا]{.ar} "to gather ([هـ]{.ar} s.th.)"| [جَامِعَة]{.ar}  | [جَامِعَات]{.ar}  | "a university" |
|[جَمَعَ يَجْمَعُ جَمْعًا]{.ar} "to gather ([هـ]{.ar} s.th.)"| [جَامِع]{.ar}  | ^2^[جَوَامِع]{.ar}  | "a mosque (in which the Friday prayers are performed)" |
|[حَدَثَ يَحْدُثُ حُدُوثًا]{.ar} "to happen" | [حَادِثَةٌ]{.ar}  | ^2^[حَوَادِث]{.ar}  | "an accident" |
|[شَرِبَ يَشْرَبُ شُرْبًا]{.ar} "to drink ([هـ]{.ar} s.th.)" | [شَارِب]{.ar}  | ^2^[شَوَارِب]{.ar}  | "a moustache" |
|[سَحَلَ يَسْحَلُ سَحْلًا]{.ar} "to abrade ([هـ]{.ar} s.th.)" | [سَاحِلٌ]{.ar}  | ^2^[سَوَاحِل]{.ar}  | "a seashore" |
|[ضَمِنَ يَضْمَنُ ضَمَانًا]{.ar} "to guarantee ([هـ]{.ar} s.th.)" | [مَضْمُوxk]{.ar} | ^2^[مَضَامِين]{.ar} | "a content (of a letter, etc.)"|
|[دَخَلَ يَدْخُلُ دُخُولًا]{.ar} "to enter" | [دَاخِل]{.ar} | none | "inside" |
|[خَرَجَ يَخْرُجُ خُرُوجًا]{.ar} "to exit" | [خَارِج]{.ar} | none | "outside" |

The last two [دَاخِلٌ]{.ar} "inside" and  [خَارِجٌ]{.ar} "outside" are notable. Here, for example, is how they can be used:

[غَسَلَ ٱلْكُوبَ مِنْ دَاخِلٍ.]{.ar}  
[gasala -lkUba min dAxilin.]{.trn}  
"He washed the tumbler from inside."

### Genderizability of doer and doee verbal-nouns when re-used as common nouns

When a doer or doee verbal-noun is re-used as a common noun, then it loses its genderizability. For example, if we wish to say "The building is a university." we will say:

[ٱَلْبِنَاءُ جَامِعَةٌ.]{.ar}  
[EalbinAEu jAmieah.]{.trn}  
"The building is a university."

We cannot masculinize [جَامِعَة]{.ar} [jAmieah]{.trn} "a university" to [جَامِع]{.ar} [jAmie]{.trn} in order to make it match the gender of [بِنَاء]{.ar} [binAE]{.trn} (masc.) "a building". Were we to do so, then 
[جَامِع]{.ar} [jAmie]{.trn} would get interpreted with either:

1. Its doer verbal-noun meaning "a gatherer":

   "The building is a gatherer."

   which doesn't make sense as a sentence.

2. Or, with the common noun meaning of [جَامِع]{.ar} [jAmie]{.trn}, if one happens to exist. There is such a meaning in this case: "a mosque (in which the Friday prayers are performed)". So then we would get:

   [ٱَلْبِنَاءُ جَامِعٌ.]{.ar}  
   [EalbinAEu jAmieun.]{.trn}  
   "The building is a mosque (in which the Friday prayers are performed)."

3. Or, with the adjectival noun meaning of [جَامِع]{.ar} [jAmie]{.trn}, if one happens to exist. There is such a meaning in this case: "comprehensive". So then we would get:

   [ٱَلْبِنَاءُ جَامِعٌ.]{.ar}  
   [EalbinAEu jAmieun.]{.trn}  
   "The building is comprehensive."

None of these give the original meaning we intended: "The building is a university." So, in summary,
once a doer or doee verbal-noun is re-used as a common noun, it loses its genderizability. 

Having said this, when a doer verbal-noun is re-used as a common noun that applies to humans, both the masculine and feminine common-noun typically exist together. So for example,

[عَالِم]{.ar} [eAlim]{.trn} is re-used as the common-noun for "a (male) scholar" with the plural ^2^[عُلَمَاء]{.ar} [eulamAE]{.trn}. 
And  
[عَالِمَة]{.ar} [eAlimah]{.trn} is re-used as the common-noun for "a (female) scholar" with the plural [عَالِمَات]{.ar} [eAlimAt]{.trn}.

In such cases, i.e., when applicable to humans, the dictionary will generally only list, and supply the definition for the masculine common-noun. The reader is expected to know that its feminine exists and how to form it.

There are exceptions, however. The verb [جَرَىٰ يَجْرِي جَرْيًا]{.ar} [jarA yajrI jaryan]{.trn} "to run" is formed from the root [جري]{.arroot}. This is a weak root because of the letter [ي]{.ar} in it, and we will study it in more detail later in chapter\ \@ref(roots-with-weak-final-letter). In any case, its feminine doer verbal-noun is [جَارِيَة]{.ar} [jAriyah]{.trn} and is re-used for the common noun meaning "a girl". The masculine doer verbal noun is not re-used as a common noun for the meaning "a boy".

<!--Unless, the common-noun is biologically or professionally applied to one of the genders, in which case, only one may exist.-->


<!--chapter:end:srcrmd/doer_verbal_noun.Rmd-->

# a-state incomplete-action verbs

## Introduction

In 
chapter\ \@ref(u-state-incomplete-action-verbs)
we mentioned that incomplete action verbs have three states (like nouns). 
These states are called:

i. The u-state
i. The a-state
i. The [0]{.txt}-state

We introduced the u-state incomplete-action verb in
chapter\ \@ref(u-state-incomplete-action-verbs).
In this chapter we will study the 
a-state
incomplete-action verb.

The u-state incomplete-action verb makes a plain statement.
The a-state incomplete-action verb implies a wish or purpose.
The a-state incomplete-action verb is used after the following articles:

+ [أَنْ]{.ar} [Ean]{.trn}
+ [لَنْ]{.ar} [lan]{.trn}
+ [لِ]{.ar} [li]{.trn}
+ [كَيْ]{.ar} [kay]{.trn}
+ [حَتَّىٰ]{.ar} [HattA]{.trn}
+ [إِذَنْ]{.ar} [Eipan]{.trn}

We will go over these cases in this chapter.

## Forming the a-state incomplete-action verb

Here is the u-state incomplete action verb for the singular masculine absentee participant doer "he":

[يَفْعَلُ]{.ar}  
[yafealu]{.trn}  
"he does"

Note that, because it is in the u-state, the its final letter ends with a [u]{.trn}-mark [◌ُ]{.ar}.
In order to form the 
a-state
incomplete-action verb,
we change the [u]{.trn}-mark into a
a-mark [◌َ]{.ar}, thus:

[يَفْعَلَ]{.ar}  
[yafeala]{.trn}  

This is done for all participants whose doer pronoun is invisible and u-state verb ends with a [u]{.trn}-mark [◌ُ]{.ar}.

For participants whose doer pronoun is followed by an extra [ن]{.ar} in the u-state verb, this final [ن]{.ar} is dropped in order to form the 
a-state
incomplete-action verb.
So, for example, the u-state
incomplete-action verb:

[يَفْعَلَانِ]{.ar}  
[yafealAni]{.trn}  
"they~2,m~ do"

becomes, for the 
a-state:

[يَفْعَلَا]{.ar}  
[yafealA]{.trn}  

Here is the complete table of the 
a-state
incomplete-action verb
for all doer participants.

|Participant|Incomplete-action verb doer pronoun|u-state incomplete-action verb | a-state incomplete-action verb|
|:---|:--|:---|:---|
| he        |_invisible_         |[يَفْعَلُ]{.ar}    |[يَفْعَلَ]{.ar}    |
| she       |_invisible_         |[تَفْعَلُ]{.ar}    |[تَفْعَلَ]{.ar}    |
| you~1m~   |_invisible_         |[تَفْعَلُ]{.ar}    |[تَفْعَلَ]{.ar}    |
| you~1f~   |[ي]{.ar}            |[تَفْعَلِينَ]{.ar}  |[تَفْعَلِي]{.ar}   |
| I         |_invisible_         |[أَفْعَلُ]{.ar}    |[أَفْعَلَ]{.ar}    |
| they~2m~  |[ا]{.ar}            |[يَفْعَلَانِ]{.ar}  |[يَفْعَلَا]{.ar}   |
| they~2f~  |[ا]{.ar}            |[تَفْعَلَانِ]{.ar}  |[تَفْعَلَا]{.ar}   |
| you~2~    |[ا]{.ar}            |[تَفْعَلَانِ]{.ar}  |[تَفْعَلَا]{.ar}   |
| they~3m~  |[و]{.ar}            |[يَفْعَلُونَ]{.ar}  |[يَفْعَلُوا]{.ar}  |
| they~3f~  |[نَ]{.ar}            |[يَفْعَلْنَ]{.ar}   |[يَفْعَلْنَ]{.ar} (same)   |
| you~3m~   |[و]{.ar}            |[تَفْعَلُونَ]{.ar}  |[تَفْعَلُوا]{.ar}  |
| you~3f~   |[نَ]{.ar}            |[تَفْعَلْنَ]{.ar}   |[تَفْعَلْنَ]{.ar} (same)  |
| we        |_invisible_         |[نَفْعَلُ]{.ar}    |[نَفْعَلَ]{.ar}    |

Take note the following:

+ The u-state and a-state verbs are the same for the feminine plural absentee and addressee participants: 
  + [يَفْعَلْنَ]{.ar} (they~3f~)
  + [تَفْعَلْنَ]{.ar} (you~3f~)
+ The a-state verbs for the masculine plural absentee and addressee participants have a final silent [Ealif]{.trn2}: 
  + [يَفْعَلُوا]{.ar} (they~3m~) 
  + [تَفْعَلُوا]{.ar} (you~3m~)

<!--
### Doubled and weak roots

The following table lists the a-state incomplete-action verb for some roots with a weak final letter. These are the only roots that have any complications in forming the a-state. The rest of the doubled and weak root verbs are straightforward. For a complete listing, including the higher forms, see Appendix\ \@ref(chapter-verb-tables).

Root: [سعي]{.arroot}

|Participant|u-state verb | a-state verb
|:---|:--|:---|:---|
| he        |_invisible_         |[يَفْعَلُ]{.ar}    |[يَفْعَلَ]{.ar}    |
| she       |_invisible_         |[تَفْعَلُ]{.ar}    |[تَفْعَلَ]{.ar}    |
| you~1m~   |_invisible_         |[تَفْعَلُ]{.ar}    |[تَفْعَلَ]{.ar}    |
| you~1f~   |[ي]{.ar}            |[تَفْعَلِينَ]{.ar}  |[تَفْعَلِي]{.ar}   |
| I         |_invisible_         |[أَفْعَلُ]{.ar}    |[أَفْعَلَ]{.ar}    |
| they~2m~  |[ا]{.ar}            |[يَفْعَلَانِ]{.ar}  |[يَفْعَلَا]{.ar}   |
| they~2f~  |[ا]{.ar}            |[تَفْعَلَانِ]{.ar}  |[تَفْعَلَا]{.ar}   |
| you~2~    |[ا]{.ar}            |[تَفْعَلَانِ]{.ar}  |[تَفْعَلَا]{.ar}   |
| they~3m~  |[و]{.ar}            |[يَفْعَلُونَ]{.ar}  |[يَفْعَلُوا]{.ar}  |
| they~3f~  |[نَ]{.ar}            |[يَفْعَلْنَ]{.ar}   |[يَفْعَلْنَ]{.ar} (same)   |
| you~3m~   |[و]{.ar}            |[تَفْعَلُونَ]{.ar}  |[تَفْعَلُوا]{.ar}  |
| you~3f~   |[نَ]{.ar}            |[تَفْعَلْنَ]{.ar}   |[تَفْعَلْنَ]{.ar} (same)  |
| we        |_invisible_         |[نَفْعَلُ]{.ar}    |[نَفْعَلَ]{.ar}    |
-->

## After [أَنْ]{.ar} [Ean]{.trn}

[أَنْ]{.ar} [Ean]{.trn} "that" is the main article which causes the following
incomplete-action verb to be in the a-state.
The other articles that we listed in the introduction are all either derived from 
[أَنْ]{.ar} 
or include its meaning implicitly without expressing it.

### Basic usage of [أَنْ]{.ar} [Ean]{.trn} with the a-state incomplete-action verb

[أَنْ]{.ar} often follows verbs that have a meaning of wishing or hoping. For example,

[أَمَلَ ٱلطَّالِبُ أَنْ يَنْجَحَ.]{.ar}  
[Eamala -TTAlibu Ean yanjaH.]{.trn}  
"The student hoped that he succeed."

[لَا]{.ar} can be used to negate the following a-state incomplete-action verb.
[لَا]{.ar} combines with [أَنْ]{.ar} and assimilates with it to form [أَلَّا]{.ar} [EallA]{.trn} "that not".
For example,

[أَمَرَ ٱلْأَبُ ٱلِٱبْنَ أَلَّا يَكْسَلَ.]{.ar}  
[Eamara -lEabu li-bna EallA yaksal.]{.trn}  
"The father ordered the son that he not be lazy."

Other than this [لَا]{.ar},
[أَنْ]{.ar} must directly precede the following a-state incomplete-action verb and must not be separated from it.

### Grammatical equivalence of [أَنْ]{.ar} clause with a doing verbal noun

In grammatical theory,
[أَنْ]{.ar} 
and the following verb form a clause that is equivalent in meaning to the doing verbal-noun of the verb. So in the example,
[أَمَلَ ٱلطَّالِبُ أَنْ يَنْجَحَ.]{.ar}, the 
[أَنْ]{.ar} clause
([أَنْ يَنْجَحَ]{.ar})
is equivalent to the doing verbal noun [ٱلنَّجَاح]{.ar}.
So the sentence is grammatically equivalent to

[أَمَلَ ٱلطَّالِبُ ٱلنَّجَاحَ.]{.ar}  
[Eamala -TTAlibu -nnajAH.]{.trn}  
"The student hoped [for] success."

This grammatical equivalence of the 
[أَنْ]{.ar} clause
with a noun aloows the 
[أَنْ]{.ar} clause to take the place of a noun in various positions in a sentence.
So, in the above example, the 
[أَنْ]{.ar} clause
is in place of the direct doee of the verb [أَمَلَ]{.ar}:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-24-1.pdf)<!-- -->

We show other examples below where the
[أَنْ]{.ar} clause
occurs in place of other noun positions.

As the subject:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-25-1.pdf)<!-- -->

As the information:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-26-1.pdf)<!-- -->

As a doer noun:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-27-1.pdf)<!-- -->

In the i-state as the base noun in an annexation:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-28-1.pdf)<!-- -->

In the i-state after a preposition:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-29-1.pdf)<!-- -->

### Option to drop the preposition before [أَنْ]{.ar}

In the above example the verb [رَغِبَ يَرْغَبُ]{.ar} takes an indirect doee after the preposition [فِي]{.ar}.
In such cases, where the 
[أَنْ]{.ar} clause
occurs after a preposition, it is common to drop the preposition as long as there is not resulting confusion in meaning.
So, we can also say (without the preposition [فِي]{.ar}) for the same meaning:

[رَغِبَ ٱلْغُلَامُ آَنْ يَأْكُلَ.]{.ar}  
"The boy desired that he eat."

### Uncommon usages of [أَنْ]{.ar}

Ocassionally, [أَنْ]{.ar} is used with the meaning "lest". For example:

[قَتَلْتُ ٱلثُّعْبَانَ أَنْ يَقْتُلَنِي.]{.ar}  
"I killed the serpent lest it kill me."

[أَنْ]{.ar} may also occur before a completed-action verb. Example:

[بَلَغَنِي أَنْ رَجَعْتَ.]{.ar}  
"That you have returned has reached me."

### Other types of [أَنْ]{.ar}

There are other types of [أَنْ]{.ar} in the Arabic language. They all have the basic meaning "that". But they are used in different grammatical ways.

The [أَنْ]{.ar} we have learned here is called the _verbal noun [أَنْ]{.ar}_ because of the equivalence of its clause with a doing verbal noun.

There is also another type of [أَنْ]{.ar} called the _lightened [أَنْ]{.ar}_ that we will learn in section\ \@ref(lightened-an).

There is also the _explanatory [أَنْ]{.ar}_ and the _extra [أَنْ]{.ar}_ that we will cover in chapter\ \@ref(types-of-an).

## After [لِ]{.ar} [li]{.trn}

### The [لِ]{.ar} of purpose

The article [أَنْ]{.ar} may be attached to the preposition [لِ]{.ar} [li]{.trn} thus: [لِأَنْ]{.ar} [liEan]{.trn} to give the purpose of the following verb. This [لِ]{.ar} may be translated as "so that". For example:

[أَكَلَ لِأَنْ يَشْبَعَ.]{.ar}  
"He ate so that he be sated."

When [لِ]{.ar} is thus used, [أَنْ]{.ar} is optionally allowed to be dropped while its meaning is retained.
[لِ]{.ar} is then attached to the verb.
So we can say, for the same meaning:

[أَكَلَ لِيَشْبَعَ.]{.ar}  
"He ate so that he be sated."

But when using [لَا]{.ar} to negate the verb, then [أَنْ]{.ar} must be expressed, and the combination of [لِ]{.ar}, [أَنْ]{.ar}, and [لَا]{.ar} is written as [لِئَلَّا]{.ar} [liEallA]{.trn}. For example,

[شَرِبَ ٱلْمَاءَ لِئَلَّا يَعْطَشَ.]{.ar}  
"He drank the water so that he not be thirsty."

<!--
By the way, this [لِ]{.ar}, which is used with a-state incomplete-action verbs, is different from 
the [لِ]{.ar} we learned in section\ \@ref(indirect-commands), which is used with the [0]{.txt}-state incomplete-action verbs for indirect commands.
-->

### The [لِ]{.ar} of denial

There is a specific [لِ]{.ar}, called the [لِ]{.ar} of denial,  which is used with a-state incomplete-action verbs and the verb [كَانَ]{.ar} that we will discuss in section (TODO in [كَانَ]{.ar} chapter).

## After [كَيْ]{.ar} [kay]{.trn}

[كَيْ]{.ar} [kay]{.trn}
is a preposition similar to [لِ]{.ar} in meaning. It may be translated as "in order that", or also as "so that".
It is also used before the a-state incomplete-action verb.
The difference from [لِ]{.ar} is that, when [لِ]{.ar} is used with the a-state incomplete-action verb, expressing or dropping the [أَنْ]{.ar} was optional.
But with [كَيْ]{.ar}, dropping the [أَنْ]{.ar} is mandatory, while its meaning is retained. For example:

[أَكَلَ كَيْ يَشْبَعَ.]{.ar}  
"He ate in order that he be sated."

[لَا]{.ar} is used, as usual, to negate the verb and is attached to [كَيْ]{.ar} thus: [كَيْلَا]{.ar} [kaylA]{.trn}. Example:

[شَرِبَ ٱلْمَاءَ كَيْلَا يَعْطَشَ.]{.ar}  
"He drank the water in order that he not be thirsty."

The preposition [لِ]{.ar} may be combined with [كَيْ]{.ar} thus: [لِكَيْ]{.ar} [likay]{.trn}, for more or less the same meaning. For example:

[أَكَلَ لِكَيْ يَشْبَعَ.]{.ar}  
"He ate in order that he be sated."

With [لَا]{.ar} the whole combination is written as [لِكَيْلَا]{.ar} [likaylA]{.trn}. [أَنْ]{.ar} must again be not be expressed.

Example:

[شَرِبَ ٱلْمَاءَ لِكَيْلَا يَعْطَشَ.]{.ar}  
"He drank the water in order that he not be thirsty."

## After [حَتَّىٰ]{.ar} [HattA]{.trn}

The preposition 
[حَتَّىٰ]{.ar} [HattA]{.trn}
is unusual in that the incomplete-action verb following it may either be in the a-state or the u-state, with slightly different meanings.
When the incomplete-action verb following it is in the u-state then
[حَتَّىٰ]{.ar} gives the meaning "until".
And when the incomplete-action verb following it is in the a-state then
[حَتَّىٰ]{.ar} gives the meaning "for the result that".
A mandatorily unexpressed [أَنْ]{.ar} is assumed with
[حَتَّىٰ]{.ar} 
when the verb following it is in the a-state.
Examples:

[يَأْكُلُ حَتَّىٰ يَشْبَعَ.]{.ar} (a-state, unexpressed [أَنْ]{.ar} assumed)  
"He eats for the result that he be sated."

[يَأْكُلُ حَتَّىٰ يَشْبَعُ.]{.ar} (u-state, no [أَنْ]{.ar})  
"He eats until he is sated."

[حَتَّىٰ]{.ar} 
is also used with completed-action verbs. Example:

[أَكَلَ حَتَّىٰ شَبِعَ.]{.ar} (completed-action, no [أَنْ]{.ar})  
"He ate until he was sated."

## After [لَنْ]{.ar} [lan]{.trn}

[لَا]{.ar} and [أَنْ]{.ar} are combined to form [لَنْ]{.ar} [lan]{.trn} with the meaning "shall not". [لَنْ]{.ar} is used with the a-state incomplete-action verb to emphatically negate the future.

[لَنْ تَذْهَبَ.]{.ar}  
"You~1m~ shall not go."

## After [إِذَنْ]{.ar} [Eipan]{.trn}

TODO

## After [وَ]{.ar}, [فَ]{.ar}, [أَوْ]{.ar}, and [ثُمَّ]{.ar}

### As connectors

If the connectors
[وَ]{.ar}, [فَ]{.ar}, [أَوْ]{.ar}, and [ثُمَّ]{.ar}
occur after an a-state incomplete-action verb, then 
a second a-state incomplete-action verb
(that doesn't have its own [أَنْ]{.ar}, etc.)
may be either in the a-state or the u-state.
For example,

[أَرْغَبُ أَنْ أَحْضُرَ ٱلْمَجْلِسَ وَأَسْمَعَ.]{.ar} ([أَسْمَعَ]{.ar} in a-state)  
"I desire that I attend the session and [that] I listen."

or

[أَرْغَبُ أَنْ أَحْضُرَ ٱلْمَجْلِسَ وَأَسْمَعُ.]{.ar} ([أَسْمَعَ]{.ar} in u-state)  
"I desire that I attend the session and I will listen."

<!--
 كتاب شرح المفصل لابن يعيش
 vol. 4, p. 259
 https://shamela.ws/book/13301/1623
-->

### With special meanings

[وَ]{.ar}, [فَ]{.ar}, [أَوْ]{.ar}, and [ثُمَّ]{.ar} also cause the following incomplete-action verb to be in the a-state in their own right, not simply as connectors. This is discussed in more detail in chapter TODO.


<!--chapter:end:srcrmd/imperfect_verb_subj.Rmd-->

# [0]{.txt}-state incomplete-action verbs

## Introduction

In 
chapter\ \@ref(u-state-incomplete-action-verbs)
we mentioned that incomplete action verbs have three states (like nouns). 
These states are called:

i. The u-state
i. The a-state
i. The [0]{.txt}-state

We have already studied the u-state of incomplete-action verbs in 
chapter\ \@ref(u-state-incomplete-action-verbs).
And we will defer the study of 
a-state of incomplete-action verbs to
chapter\ \@ref(a-state-incomplete-action-verbs).
In this chapter we will study the 
[0]{.txt}-state
incomplete-action verb.

We will also study the _verb of command_ which is very similar to the 
[0]{.txt}-state
incomplete-action verb.

## Forming the [0]{.txt}-state incomplete-action verb

Here is the u-state incomplete action verb for the singular masculine absentee participant doer "he":

[يَفْعَلُ]{.ar}  
[yafealu]{.trn}  
"he does"

Note that, because it is in the u-state, the its final letter ends with a [u]{.trn}-mark [◌ُ]{.ar}.
In order to form the 
[0]{.txt}-state
incomplete-action verb,
we change the [u]{.trn}-mark into a
[0]{.txt}-mark [◌ْ]{.ar}, thus:

[يَفْعَلْ]{.ar}  
[yafeal]{.trn}  

This is done for all participants whose doer pronoun is invisible and u-state verb ends with a [u]{.trn}-mark [◌ُ]{.ar}.

For participants whose doer pronoun is followed by an extra [ن]{.ar} in the u-state verb, this final [ن]{.ar} is dropped in order to form the 
[0]{.txt}-state
incomplete-action verb.
So, for example, the u-state
incomplete-action verb:

[يَفْعَلَانِ]{.ar}  
[yafealAni]{.trn}  
"they~2,m~ do"

becomes, for the 
[0]{.txt}-state:

[يَفْعَلَا]{.ar}  
[yafealA]{.trn}  

Here is the complete table of the 
[0]{.txt}-state
incomplete-action verb
for all doer participants.

|Participant|Incomplete-action verb doer pronoun|u-state incomplete-action verb | [0]{.txt}-state incomplete-action verb|
|:---|:--|:---|:---|
| he          |_invisible_         |[يَفْعَلُ]{.ar}    |[يَفْعَلْ]{.ar}    |
| she         |_invisible_         |[تَفْعَلُ]{.ar}    |[تَفْعَلْ]{.ar}    |
| you~1,m~    |_invisible_         |[تَفْعَلُ]{.ar}    |[تَفْعَلْ]{.ar}    |
| you~1,f~    |[ي]{.ar}            |[تَفْعَلِينَ]{.ar}  |[تَفْعَلِي]{.ar}   |
| I           |_invisible_         |[أَفْعَلُ]{.ar}    |[أَفْعَلْ]{.ar}    |
| they~2,m~   |[ا]{.ar}            |[يَفْعَلَانِ]{.ar}  |[يَفْعَلَا]{.ar}   |
| they~2,f~   |[ا]{.ar}            |[تَفْعَلَانِ]{.ar}  |[تَفْعَلَا]{.ar}   |
| you~2~      |[ا]{.ar}            |[تَفْعَلَانِ]{.ar}  |[تَفْعَلَا]{.ar}   |
| they~3+,m~  |[و]{.ar}            |[يَفْعَلُونَ]{.ar}  |[يَفْعَلُوا]{.ar}  |
| they~3+,f~  |[نَ]{.ar}            |[يَفْعَلْنَ]{.ar}   |[يَفْعَلْنَ]{.ar} (same)   |
| you~3+,m~   |[و]{.ar}            |[تَفْعَلُونَ]{.ar}  |[تَفْعَلُوا]{.ar}  |
| you~3+,f~   |[نَ]{.ar}            |[تَفْعَلْنَ]{.ar}   |[تَفْعَلْنَ]{.ar} (same)  |
| we          |_invisible_         |[نَفْعَلُ]{.ar}    |[نَفْعَلْ]{.ar}    |

Take note the following:

+ The u-state and [0]{.txt}-state verbs are the same for the feminine plural absentee and addressee participants: 
  + [يَفْعَلْنَ]{.ar} (they~3+,f~)
  + [تَفْعَلْنَ]{.ar} (you~3+,f~)
+ The u-state and [0]{.txt}-state verbs for the masculine plural absentee and addressee participants have a final silent [Ealif]{.trn2}: 
  + [يَفْعَلُوا]{.ar} (they~3+,m~) 
  + [تَفْعَلُوا]{.ar} (you~3+,m~)
+ When the 
[0]{.txt}-state
incomplete-action verb
ends with a 
[0]{.txt}-mark [◌ْ]{.ar}, and the next word begins with a connecting [hamzah]{.trn2} [ٱ]{.ar} then the
[0]{.txt}-mark [◌ْ]{.ar} is converted to an [i]{.trn} mark [◌ِ]{.ar}. For example:
  + [يَفْعَلْ + ٱلرَّجُلُ = يَفْعَلِ ٱلرَّجُلُ]{.ar}

## Uses of the [0]{.txt}-state incomplete-action verb

The u-state is the default state for incomplete-action verbs. The 
[0]{.txt}-state
is used only in specific cases. We will explain these below.

### With [لِ]{.ar} for indirect commands {#indirect-commands}

The particle [لِ]{.ar} when connected to the front of a 
incomplete-action verb
causes it to be in the
[0]{.txt}-state
and gives it the meaning of an indirect command. In English this can be translated using "should" or "let":

[لِيَذْهَبِ ٱَلرَّجُلُ]{.ar}  
"The man should go!"  
or  
"Let the man go!"  
("Let" is being used here as a command for the man, not for the addressee of this speech.)

The particles [فَ]{.ar} "so" and [وَ]{.ar} "and" are frequently used before this [لِ]{.ar}. 
The [لِ]{.ar} then loses its [i]{.trn}-mark and gets a
[0]{.txt}-mark. Examples:

[فَلْنَأْكُلْ طَعَامَنَا وَلْنَشْرَبْ شَرَابَنَا.]{.ar}  
"So let us eat our food and drink our drink!"

[لِتَجْلِسُوا عَلَى ٱلْأَرْضِ.]{.ar}  
"You should sit on the ground!"

FIXME: Use with the addressee is exceedingly rare. Rather the verb of command should be used (below). See [كتاب شرح المفصل لابن يعيش]{.ar} vol 4 p. 691. Add (perhaps in passive verbs chapter), how [لام الأمر]{.ar} can be used with passive verbs for all three deputy doers, including addressee, and is infact the only way to command the deputy doer.

Also, jussive without [لام الأمر]{.ar} is only by poetic license.  See same source in the next following pages.

<!--فمن ذلك ما ليس للفاعل، وهو فعلُ ما لم يسمّ فاعلُه، إذا أمرت به، لزمتْه اللام، نحوُ: "لتُعْنَ بحاجتي"، و"لتُوضَعْ في تجارتك"، و"لتُزْهَ علينا يا رجلُ". فهذا القبيل لا بد فيه من اللام، وإن كان مخاطبًا حاضرًا؛ لأنّ هذا الفعل قد لحقه التغييرُ بحذف فاعله وتغييرِ بنيته، فلم تحذف منه اللام أيضًا وحرف المضارعة لئلا يكون إجحافًا به، وإذا لم يجز الحذف مع المخاطب، فان لا يجوز مع الغائب أولى
-->

https://shamela.ws/book/13301/1655#p1

### With [لَا]{.ar} for prohibitions {#la-of-prohibition}

The word [لَا]{.ar} when in front of a 
[0]{.txt}-state
incomplete-action verb
gives the meaning of a prohibition. 
In English this can be translated using "Don't".

For example,

[لَا تَكْتُبُوا]{.ar}  
"Don't write~3,m~!"

[يَا زَيْدُ، لَا تَدْخُلِ ٱلْبَيْتَ!]{.ar}  
"Don't~1,m~ enter the house!"

The particles [فَ]{.ar} "so" and [وَ]{.ar} "and" may be used before this [لَا]{.ar}. 
Example:

[فَلَا تَأْكُلْ وَلَا تَشْرَبْ!]{.ar}  
"So don't eat~1,m~ and don't drink~1,m~!"

Such prohibitions are generally for the addressee participant. 
However, rarely, they may be issued for the absentee participant as well. Example:

[لَايَمْنَعْ زَيْدًا ٱلدُّخُولَ.]{.ar}  
"Let him not prevent Zayd from entering!"

<!-- Example from Quran:
[لَا تُسْرِفْ فِي ٱلْقَتْلِ]{.ar}

http://www.alfaseeh.com/vb/showthread.php?t=72471&p=558734&viewfull=1#post558734
-->

By the way, [لَا]{.ar} does not force a verb to be in the u-state
[0]{.txt}-state. We have already seen in 
section\ \@ref(u-state-verb-negation-la)
that [لَا]{.ar} can be used to negate a u-state incomplete-action verb for the present and future tense.
Example:

[لَا يَذْهَبُ ٱلرَّجُلُ]{.ar}  
[lA yaphabu -rrajulu.]{.trn}  
"The man does not go." or,  
"The man is not going." or,  
"The man will not go."

### With [لَمْ]{.ar} for "did not"

The particle [لَمْ]{.ar} when in front of an
incomplete-action verb
causes it to be in the
[0]{.txt}-state
and gives it the meaning of
negating the past tense
In English this can be translated using "did not".
For example,

[لَمْ يَذْهَبِ ٱلرَّجُلُ.]{.ar}  
"The man did not go."

We have already learned in 
section\ \@ref(negating-completed-action-verbs) that the completed-action verb is negated using the particle [مَا]{.ar}. For example:

[مَا ذَهَبَ ٱلرَّجُلُ.]{.ar}  
[mA pahaba -rrajulu.]{.trn}  
"The man did not go."  
or,  
"The man has not gone."

Both [لَمْ]{.ar} and [مَا]{.ar} are used commonly to negate the past tense.
[مَا]{.ar} has a more emphatic meaning than [لَمْ]{.ar}.

Here are some more examples:

### With [لَمَّا]{.ar} for "did not yet"

The word [لَمَّا]{.ar} when in front of a 
[0]{.txt}-state
incomplete-action verb
gives the meaning "did not yet". 
For example,

[لَمَّا يَذْهَبْ زَيْدٌ.]{.ar}  
"Zayd did not go yet."

### Other uses of the [0]{.txt}-state incomplete-action verb

The [0]{.txt}-state incomplete-action verb is also used for _consequential actions_ and in _conditional statements_. We will deal with these in
chapters\ \@ref(the-consequential-action)
and\ \@ref(conditional-statements)
respectively

## The verb of command

In order to give a direct command to an addressee, Arabic uses the verb of command. The verb of command is very similar to the 
[0]{.txt}-state
incomplete-action verb.
The verb of command is only available for the addressee participant. 

### Forming the verb of command

Here is the verb of command for the addressee participants:

|Participant| Verb of command|
|:---|:---|
| you~1,m~    |[ٱفْعَلْ]{.ar}    |
| you~1,f~    |[ٱفْعَلِي]{.ar}   |
| you~2~      |[ٱفْعَلَا]{.ar}   |
| you~3+,m~   |[ٱفْعَلُوا]{.ar}  |
| you~3+,f~   |[ٱفْعَلْنَ]{.ar}   |

In order to form the verb of command, we remove the initial [ت]{.ar} from the addressee particpant verb. The verb then begins with an [0]{.txt}-mark so we place a connecting [hamzah]{.trn2} in front of it.

When the verb of command occurs in the beginning of a sentence, then the vowel mark for the connecting [hamzah]{.trn2} is selected according to the following criteria:

i. When the middle root letter of the verb of command has an [u]{.trn}-mark\ [◌ُ]{.ar}, then the connecting [hamzah]{.trn2} gets an [u]{.trn}-mark\ too. Examples:

   | Verb | Verb of command for "he" |
   |:------|:-----|
   |[نَظَرَ يَنْظُرُ نَظَرًا]{.ar}  | [ٱُنْظُرْ]{.ar} "Look!"|
   |[قَتَلَ يَقْتُلُ قَتْلًا]{.ar}  | [ٱُقْتُلْ]{.ar} "Kill!"|
   |[مَكَثَ يَمْكُثُ مُكُوثًا]{.ar} | [ٱُمْكُثْ]{.ar} "Stay!"|

i. Otherwise, when the middle root letter of the verb of command has an [a]{.trn}-mark\ [◌َ]{.ar} or an [i]{.trn}-mark\ [◌ِ]{.ar}, then the connecting [hamzah]{.trn2} gets an [i]{.trn}-mark\ [◌ِ]{.ar}. Examples:

   | Verb | Verb of command for "he" |
   |:------|:-----|
   |[عَمِلَ يَعْمَلُ عَمَلًا]{.ar}  | [ٱِعْمَلْ]{.ar} "Work!"|
   |[ذَهَبَ يَذْهَبُ ذَهَابًا]{.ar} | [ٱِذْهَبْ]{.ar} "Go!"  |
   |[جَلَسَ يَجْلِسُ جُلُوسًا]{.ar} | [ٱِجْلِسْ]{.ar} "Sit!" |

<!--
### Usage of the verb of command
-->

Here are some examples of using the verb of command:


The verb of command is not used to issue negative commands, like "Don't go!". 
Instead, the 
[0]{.txt}-state verb is used with [لَا]{.ar}
as described in
section\ \@ref(la-of-prohibition)
above.

[لَا تَذْهَبْ]{.ar}  
"Don't go!"

### The verb of command for roots begin with [hamzah]{.trn2}

Appendix\ \@ref(hamzarules) details the rules for speeling words that contain [hamzah]{.trn2} generally.
In addition to those rules, the verb of command for roots that begin with [hamzah]{.trn2} warrant additional discussion.

Consider the following form\ 1 verbs and their verbs of command
for the singular masculine addressee doer "he":

|Root|Verb| Verb of command|
|:-|:----|:---|
| [أمل]{.arroot} | [أَمَلَ يَأْمُلُ أَمَلًا]{.ar} "to hope"   | [ٱؤْمُلْ]{.ar} | 
| [أذن]{.arroot} | [أَذِنَ يَأذَنُ أَذَنًا]{.ar} "to permit" | [ٱئْذَنْ]{.ar} | 

Here are examples of these verbs of commands in the middle of a sentence:

[يَا أُمِّي ٱئْذَنِي لِي ٱللَّعِبَ!]{.ar}  
[yA Eummi -EpanI li -llaeib!]{.trn}  
"O my mother, permit me to play!"

[يَا زَيْدُ ٱؤْمُلِ ٱلْخَيْرَ!]{.ar}  
[yA zaydu -Emuli -lxayr!]{.trn}  
"O Zayd, hope for good!"

When these verbs of command occur in the beginning of the sentence, then there would be two [hamzah]{.trn2}s occuring next to each other which is not permitted. So the second [hamzah]{.trn2} is pronounced as a long vowel, though it may still be written as a [hamzah]{.trn2}. Examples:

[ٱُؤمُلِ ٱلْخَيْرَ يَا زَيْدُ!]{.ar}  
[EUmul]{.trn}  
not  
$\times$\ [EuEmul]{.trn}

[ٱِئذَنِي لِي ٱللَّعِبَ يَا أُمِّي!]{.ar}  
[EIpanI]{.trn}  
not  
$\times$\ [EiEpanI]{.trn}  

As a further complication, when the verb of command is preceded by
[وَ]{.ar} "and"
or
[فَ]{.ar} "so"
then the connecting [hamza]{.trn} is not written
and the [hamzah]{.trn2} of the first root letter is written seated on an [Ealif]{.trn2}.
Examples:

[وَأْمُلْ]{.ar}  
[waEmul]{.trn}  
"And hope!"

[فَأْذَنْ]{.ar}  
[faEpan]{.trn}  
"So permit!"

### Irregular verbs of command

In addition to the rules states above there are four verbs of command (all containing [hamzah]{.trn2}) that are irregular. We will discuss them below:

#### The verbs [أَكَلَ]{.ar}\ , [أَخَذَ]{.ar}\ , and [أَمَرَ]{.ar}

The verbs of command for the  following three verbs are irregular:

|Root|Verb| Verb of command|
|:-|:----|:---|
| [أكل]{.arroot} | [أَكَلَ يَأْكُلُ أَكْلًا]{.ar} "to eat"   | [كُلْ]{.ar} | 
| [أخذ]{.arroot} | [أَخَذَ يَأْخُذُ أَخْذًا]{.ar} "to take"  | [خُذْ]{.ar} | 
| [أمر]{.arroot} | [أَمَرَ يَأْمُرُ أَمْرًا]{.ar} "to order" | [مُرْ]{.ar} | 

As you can see, the initial [hamzah]{.trn2} has been completely deleted for the verbs of command.
However, of these verbs, the verb of command for 
[أَمَرَ يَأْمُرُ أَمْرًا]{.ar}
is permitted to retain its initial [hamzah]{.trn2} when preceded by
[وَ]{.ar} "and"
or
[فَ]{.ar} "so". Then, it becomes

[وَأْمُرْ]{.ar} [waEmur]{.trn}  
and  
[فَأْمُرْ]{.ar} [faEmur]{.trn}

This retaining of the initial [hamzah]{.trn2} is not done for the other two verbs.

Here are some examples of these verbs of command:

#### The verb [سَأَلَ]{.ar}

The verb [سَأَلَ يَسْأَلُ سُؤَالًا]{.ar} "to question" forms its verb of command both regularly, and irregularly:

i. Regular: [ٱسْأَلْ]{.ar} [EisEal]{.trn}
i. Irregular: [سَلْ]{.ar} [sal]{.trn}

If the verb of command is preceded by
[وَ]{.ar} "and"
or
[فَ]{.ar} "so", then the regular verb of command 
[ٱسْأَلْ]{.ar} [EisEal]{.trn} is often preferred.

Otherwise, the irregular verb of command
[سَلْ]{.ar} [sal]{.trn} is often preferred.

Examples of usage:


<!--chapter:end:srcrmd/imperfect_verb_juss.Rmd-->

# [إِنَّ]{.ar} and its sisters

## Introduction

In the basic subject-information sentence, both the subject and the information are in the u-state. For example:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-30-1.pdf)<!-- -->

"This man is a teacher."

In the above sentence both the subject [ٱَلرَّجُلَ]{.ar} "the man", and the information [مُعَلِّمٌ]{.ar} "a teacher" are in the u-state. In this chapter we will study a family of particles, called
[إِنَّ]{.ar} and its sisters,
that modify the subject-information sentence by placing the subject in the a-state instead of the u-state. For example,

[إِنَّ ٱلرَّجُلَ مُعَلِّمٌ.]{.ar}  
[Einna -rrajula mueallimun.]{.trn}  
"Indeed the man is a teacher."

Note how, in the above example, the subject [ٱَلرَّجُلَ]{.ar} "the man" is now in the a-state. The information [مُعَلِّمٌ]{.ar} "a teacher" remains in the u-state. 

The particles constituting the family of 
[إِنَّ]{.ar} and its sisters
are:

1. [إِنَّ]{.ar}  [Einna]{.trn}     \vphantom{\huge J}
1. [أَنَّ]{.ar}  [Eanna]{.trn}     \vphantom{\huge J}
1. [كَأَنَّ]{.ar}  [kaEanna]{.trn}  \vphantom{\huge J}
1. [لَـٰكِنَّ]{.ar}  [lAkinna]{.trn} \vphantom{\huge J}
1. [لَيْتَ]{.ar}  [layta]{.trn}    \vphantom{\huge J}
1. [لَعَلَّ]{.ar}  [laealla]{.trn}  \vphantom{\huge J}

We shall now study each of these particles.

## [إِنَّ]{.ar} [Einna]{.trn}

[إِنَّ]{.ar} [Einna]{.trn} is used to begin independent sentences. It has an emphatic meaning, as if the speaker is asserting the information about the subject. It is often translated into English as "indeed" or "verily", but it is also often left untranslated.

[إِنَّ]{.ar} [Einna]{.trn} is only used to begin subject-information sentences. Verbal sentences cannot be introduced by [إِنَّ]{.ar} [Einna]{.trn} directly. (Later, in section\ \@ref(damiir-al-shan), we shall see how to overcome this restriction.). For example,

[إِنَّ ٱلدِّينَ عِنْدَ ٱللَّـٰهِ ٱلْإِسْلَامُ.]{.ar}  
[Einna -ddIna einda -llAhi -lEislAmu.]{.trn}  
"Indeed, the religion in the sight of [#allAh]{.trn2} is [#islAm]{.trn2}." ([#qurEAn]{.trn2}\ 3:19, trans. Saheeh International)

[إِنَّ]{.ar} [Einna]{.trn} 
may be preceded by other particles like [وَ]{.ar} "and", [فَ]{.ar} "so", and [ثُمَّ]{.ar} "then". For example,

[ٱُطْلُبِ ٱلْعِلْمَ ٱلنَّافِعَ. فَإِنَّ طَلَبَ ٱلْعِلْمَ ٱلنَّافِعَ عَمَلٌ صَالِحٌ. وَإِنَّ تَرْكَهُ غَفْلَةٌ.]{.ar}
"Seek the useful knowledge. For indeed the seeking of the useful knowledge is a good deed. And indeed leaving it is a negligence."

The subject of
[إِنَّ]{.ar} [Einna]{.trn} 
may be a noun phrase, in which case, any describers or replacements of the subject are also in the a-state. Examples:

[إِنَّ هَـٰؤُلَاءِ ٱلرِّجَالَ ٱلْكِرَامَ أَصْدِقَائِي.]{.ar}  
"Indeed these noble men are my friends."

[إِنَّ]{.ar} [Einna]{.trn} may have multiple subjects, each in the a-state, separated by [وَ]{.ar}. Example,

[إِنَّ ٱلْمُسْلِمِينَ وَٱلْمُسْلِمَاتِ يَعْبُدُونَ ٱللَّـٰهَ.]{.ar}  
"Indeed the Muslim men and Muslim women worship [#allAh]{.trn2}."

If the information of the first subject has been mentioned before the second subject, then the second subject may optionally be in the a-state or the u-state. For example:

[إِنَّ زَيْدًا جَالِسٌ وَعَمْرًا.]{.ar}  
or  
[إِنَّ زَيْدًا جَالِسٌ وَعَمْرٌو.]{.ar}  
"Indeed Zayd is sitting and [#eamr]{.trn2} [as well]."

[إِنَّ هَـٰذَا ٱلْكِتَابَ لِي وَذَ ٰلِكَ ٱلْكِتَابَ لَكَ.]{.ar}  
or  
[إِنَّ هَـٰذَا ٱلْكِتَابَ لِي وَذَ ٰلِكَ ٱلْكِتَاكُ لَكَ.]{.ar}  
"Indeed this book is for me and that book is for you."

[إِنَّ]{.ar} [Einna]{.trn} may be used to begin sentences with an indefinite subject. For example,

[إِنَّ مَلِكًا مِنَ ٱلْهِنْدِ كَتَبَ إِلَىٰ أَحَدِ وُزَرَائِهِ.]{.ar}  
"Indeed a king from India wrote to one of his ministers."

Note that in all the above examples that
[إِنَّ]{.ar} [Einna]{.trn} is only used to begin subject-information sentences. Verbal sentences cannot be introduced by [إِنَّ]{.ar} [Einna]{.trn} directly. (Later, in section\ \@ref(damiir-al-shan), we shall see how to overcome this restriction.).
By default, the subject of [إِنَّ]{.ar} [Einna]{.trn} must directly follow it with no intervening words or particles. The only exception is when the information consists of a prepositional or adverbial phrase, it is then allowed to precede the subject. The subject, in any case, shall be in the a-state. For example,

[إِنَّ فِي ٱلْبَيْتِ رَجُلًا.]{.ar}  
"Indeed, in the house, is a man."

[إِنَّ تَحْتَ ٱلشَّجَرَةِ كَنْزًا ثَمِينًا.]{.ar}  
"Indeed, under the tree, is a precious treasure."

This reverse order is permitted even when the subject is definite. For example,

[إِنَّ مَعَكَ صَاحِبَكَ.]{.ar}  
"Indeed, with you, is _your companion_."

This puts the logical accent on the subject [صَاحِبَكَ]{.ar} "your companion". If the subject is placed first then this puts the logical accent on the information:

[إِنَّ صَاحِبَكَ مَعَكَ.]{.ar}  
"Indeed your companion is _with_ you."

If the subject contains a pronoun that refers to a noun in the information then the information must precede the subject. For example,

[إِنَّ فِي ٱلْمَصْنَعِ عُمَّالَهُ.]{.ar}  
"Indeed, in the factory, are its workers."

[إِنَّ أَمَامَ ٱلدَّارِ حَارِسَهَا.]{.ar}  
"Indeed, in front of the door, is its guard."

### Pronoun subjects

<!--In the examples above, the subject of [إِنَّ]{.ar} has been a noun. -->
The subject of [إِنَّ]{.ar} may be a pronoun instead of a noun. For this the attached pronouns are used. For example,

[لَا تَقْطَعْ تِلْكَ ٱلشَّجَرَةَ فَإِنَّهَا ظَلِيلَةٌ.]{.ar}  
"Don't cut that tree, for it is shady."

[إِنَّكُمَا صَدِيقَايَ.]{.ar}  
"You~2~ are my friends."

The speaker pronouns, both singular and plural, may optionally keep or drop their [ن]{.ar}. 
So for the singular speaker pronoun both [إِنَّنِي]{.ar} [EinnanI]{.trn} and [إِنِّي]{.ar} [EinnI]{.trn} may be used.
And for the plural speaker pronoun both [إِنَّنَا]{.ar} [EinnanA]{.trn} and [إِنَّا]{.ar} [EinnA]{.trn} may be used.
Examples:

[إِنِّي مُسْلِمٌ.]{.ar}  
or  
[إِنَّنِي مُسْلِمٌ.]{.ar}  
"Indeed I am a Muslim."

[إِنَّنَا كَاتِبُو هَـٰذَا ٱلْكِتَابَ.]{.ar}  
or  
[إِنَّا كَاتِبُو هَـٰذَا ٱلْكِتَابَ.]{.ar}  
"Indeed we are the writers of this book."

[إِنَّ]{.ar} with the speaker pronouns are often used with doer verbal nouns to signify that the speaker intends to to the action of the verb. For example,

[إِنِّي ذَاهِبٌ إِلَىٰ ٱلْمَسْجِدِ.]{.ar}  
"I'm going to the mosque."

We also mentioned this point in section\ \@ref(doer-verbal-noun-for-intended-future-action).

### [إِنَّ]{.ar} [Einna]{.trn} with a strengthening [لَ]{.ar} {#inna-strengthening-la}

The strengthening particle [لَ]{.ar} adds extra emphasis and may optionally be used between the subject of [إِنَّ]{.ar} and its information.
If the subject occurs first (as is the default) then [لَ]{.ar} is connected to and placed directly before the information. For example:

[إِنَّ زَيْدًا لَقَائِمٌ.]{.ar}  
"Indeed Zayd is definitely standing."

If the information precedes the subject, then then [لَ]{.ar} is connected to and placed directly before the subject. For example:

[إِنَّ فِي ٱلْبَيْتِ لَرَجُلًا.]{.ar}  
"Indeed, in the house, is definitely a man."

The strengthening particle [لَ]{.ar} is only used with [إِنَّ]{.ar} and not for any of its other sisters
([إِنَّ]{.ar},
[أَنَّ]{.ar},
[كَأَنَّ]{.ar},
[لَـٰكِنَّ]{.ar},
[لَيْتَ]{.ar}, and
[لَعَلَّ]{.ar}).

### Commonality of rules for [إِنَّ]{.ar} and its sisters

Unless otherwise noted, the rules we have presented above for 
[إِنَّ]{.ar},
for example, the subject being in the a-state, the order of the subject and the predicate, the use of attached pronouns for the subject, etc.,
apply also to its other sisters. 

The strengthening particle [لَ]{.ar}, as mentioned above, is only used with [إِنَّ]{.ar} and not for any of its other sisters.

## [أَنَّ]{.ar} [Eanna]{.trn}

The particle 
[أَنَّ]{.ar} [Eanna]{.trn}
can be translated as "that".
It is similar to [إِنَّ]{.ar} in that it is asserts the information about the subject.
But 
[أَنَّ]{.ar} is different from [إِنَّ]{.ar} in that [إِنَّ]{.ar}, its subject, and its information together constitute a complete sentence.
Whereas 
the
[أَنَّ]{.ar}
clause
([أَنَّ]{.ar}
, its subject, and its information together) does not constitute a complete sentence. For example, consider the expression:

[زَيْدٌ صَادِقٌ.]{.ar}  
"Zayd is truthful."

This is a complete sentence. But if we add 
[أَنَّ]{.ar} "that" to its beginning, it no longer remains a complete sentence:

[أَنَّ زَيْدًا صَادِقٌ]{.ar}  
"that Zayd is truthful"

We need to additional words, external to the 
[أَنَّ]{.ar}
clause
to complete the sentence. We will see examples of this below.

### The [أَنَّ]{.ar} clause in place of the direct doee

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-31-1.pdf)<!-- -->

"I know that Zayd is truthful."

Note how, in the example above the 
[أَنَّ]{.ar}
clause
([أَنَّ زَيْدًا صَادِقٌ]{.ar})
has occupied the place of the direct doee of the verb [أَعْلَمُ]{.ar}.

In a similar manner,
[أَنَّ]{.ar}
clauses can be placed where one would expect other noun positions, such as: a subject, an information, a doer, and more. Here are some examples:

### The [أَنَّ]{.ar} clause in place of the doer

Example:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-32-1.pdf)<!-- -->

"That you are sick has reached me." ("It has reached me that you are sick.")

### The [أَنَّ]{.ar} clause in place of the subject

Example (with information before subject in sentence word order):

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-33-1.pdf)<!-- -->

"From his characteristeics is that he is noble."

### The [أَنَّ]{.ar} clause in place of the information

Example:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-34-1.pdf)<!-- -->

"The truth is that he went."

### [أَنَّ]{.ar} with [كَانَ]{.ar}

As you know, [كَانَ]{.ar}'s doer is also its subject, and its doee is also its information.
The [أَنَّ]{.ar} clause can occur in either the subject or the information of [كَنَ]{.ar}. 
For example, the [أَنَّ]{.ar} clause as the information:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-35-1.pdf)<!-- -->

"The matter was that he didn't do his obligation."

Now, the [أَنَّ]{.ar} clause as the subject:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-36-1.pdf)<!-- -->

"That he didn't do his obligation was the matter."

Note that in the latter case, the information precedes the subject.

### The [أَنَّ]{.ar} clause in place of an i-state noun

The [أَنَّ]{.ar} clause can occur in place of an i-state base noun in an annexation. Example:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-37-1.pdf)<!-- -->

"The highway robbers (literally: the cutters of the way) have increased to the degree that the journey is dangerous."

The [أَنَّ]{.ar} clause can occur in place of an i-state  noun directly following a preposition. Example:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-38-1.pdf)<!-- -->

"I wondered at that Zayd is asleep."

#### Optionally deleting the preposition directlt before an [أَنَّ]{.ar} clause

If an
[أَنَّ]{.ar} clause
directly follows a preposition, it is permissible to optionally delete the preposition as long as the meaning remains clear.
So the previous example can be expressed without the preposition [مِنْ]{.ar} with the same meaning:

[عَجِبْتُ أَنَّ زَيْدًا نَائِمٌ.]{.ar}  
"I wondered at that Zayd is asleep."

#### [لِأَنَّ]{.ar} "because"

The combination of the preposition [لِ]{.ar} "for" and [أَنَّ]{.ar} is used to mean "because". For example,

[أَكَلْتُ ٱلطَّعَامَ لِأَنَّنِي كُنْتُ جَائِعًا.]{.ar}  
"I ate the food because I was hungry."

### Equivalence of the [أَنَّ]{.ar} clause with a verbal noun of doing

As a matter of grammatical theory, the
[أَنَّ]{.ar} clause, i.e. ([أَنَّ]{.ar} itself, its subject, and its information) is considered equivalent to a verbal noun of doing (typically in an annexation, and possibly with a doee as well). It is this equivalalence that allows it to thake the place of a doer, direct doee, and the other categories we have given above.
For instance, consider the example:

[عَجِبْتُ مِنْ أَنَّ زَيْدًا ذَهَب.]{.ar}  
"I wondered at that Zayd went."

Here, the clause
[أَنَّ زَيْدًا ذَهَب]{.ar}
is equivalent to the verbal noun phrase [ذَهَابِ زَيْدٍ]{.ar} "Zayd's going". So the grammatically equivalent sentence with this verbal noun phrase is:

[عَجِبْتُ مِنْ ذَهَابِ زَيْدٍ.]{.ar}  
"I wondered at Zayd's going."

Similarly, in the example,

[مِنْ صِفَاتِهِ أَنَّهُ كَرِيمٌ.]{.ar}  
"From his characteristics is that he is generous."

the clause
[أَنَّهُ كَرِيمٌ]{.ar}
is equivalent to the verbal noun phrase [كَرَامَتِهِ]{.ar} "his generosity". So the grammatically equivalent sentence with this verbal noun phrase is:

[كَرَامَتِهِ مِنْ صِفَاتِهِ.]{.ar}  
"His generosity is from his characteristics."

This grammatical equivalence is more a matter of theory than of practical usefulness to us.
And you have seen this grammatical equivalence before with [أَنْ]{.ar} and a-state incomplete action verbs in chanpter\ \@ref(a-state-incomplete-action-verbs-verbal-noun).

## [كَأَنَّ]{.ar} [kaEanna]{.trn}

[كَأَنَّ]{.ar} [kaEanna]{.trn}
may be translated as "[It is] as if".
It is actually simply the preposition [كَ]{.ar} "like" attached to [أَنَّ]{.ar}. But it is treated separately because, unlike [أَنَّ]{.ar},
[كَأَنَّ]{.ar} [kaEanna]{.trn}, its subject, and its information constitute a complete sentence. For example,

[كَأَنَّ ٱلْأُمُّ مَدْرَسَةٌ.]{.ar}  
"[It is] as if the mother is a school."

TODO: add more info

## [لَـٰكِنَّ]{.ar} [lAkinna]{.trn}

TODO

## [لَيْتَ]{.ar}  [layta]{.trn}

TODO

## [لَعَلَّ]{.ar}  [laealla]{.trn}

TODO

## Topic-comment sentences and the pronoun of the fact

### Topic-comment sentences

There is a sub-type of subject-information sentence called a topic-comment sentence. Here is an example:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-39-1.pdf)<!-- -->

"The tree: its branches are long."

In these kinds of sentences, the subject introduces a topic, and the information is itself a sentence which comments on the topic/subject.
We have, in fact, already seen sentences like this in section\ \@ref(past-verbs-order-of-words), when we take a verbal sentence and convert it to a subject-information sentence. This is the example we discussed there:

[ٱَلرَّجُلُ كَتَبَ كِتَابًا.]{.ar}  
"The man: he wrote a book."

#### The linker pronoun

A topic-comment sentence typically requires a pronoun in the comment that links back to the comment. 
In the example
[ٱَلشَّجَرَةُفُرُوعُهَا طَوِيلَةٌ.]{.ar}, the attached pronoun [هَا]{.ar} "it" in [فُرُوعُهَا]{.ar} "its tree" is the linker pronoun that links back to the topic [ٱَلشَّجَرَةُ]{.ar} "the tree".

Similarly, in the example
[ٱَلرَّجُلُ كَتَبَ كِتَابًا.]{.ar}
the linker pronoun is the invisible doer pronoun "he" of the verb [كَتَبَ]{.ar} "he wrote" that links back to the topic [ٱَلرَّجُلُ]{.ar} "the man".

#### Topic-comment sentences with [إِنَّ]{.ar} and its sisters

[إِنَّ]{.ar} and its sisters are very often used in topic-comment sentences. (With [أَنَّ]{.ar} it is, as usual, an incomplete sentence.) Here are some examples:

[إِنَّ زَيْدًا لَهُ أَخٌ وَأُخْتٌ.]{.ar}  
"Indeed Zayd: he has a brother and sister."

[ٱِعْلَمْ أَنَّ ٱلْعِلْمَ حُصُولُهُ يَتَطَلَّبُ جُهْدًا.]{.ar}  
"Know that knowledge: its obtaining requires effort."

#### Topic-comment sentences with a pronoun topic

The topic, in a topic-comment sentence, is frequently a pronoun. For example,

[أَنَا ٱسْمِي زَيْدٌ.]{.ar}  
"I: my name is Zayd."

[أَكَلْتُ ٱلطَّعَامَ لَـٰكِنَّكَ لَمْ تَأْكُلْ.]{.ar}  
"I ate the food but you: you didn't eat."

### The pronoun of the fact

Mostly, pronouns are used in place of nouns when it is already known to whom the noun refers to. So if you say:

[أَنَا ٱسْمِي زَيْدٌ.]{.ar}  
"I: my name is Zayd."

the pronoun [أَنَا]{.ar} "I" refers to the speaker, who is known.

There is a special pronoun, called the _pronoun of the fact_ that begins topic-comment sentences. This pronoun does not refer to any previously known entity, but rather refers to the comment that follows it. It is sometimes translated as "the fact is" but is often left untranslated. Here is an example:

![](Learn-Standard-Arabic_files/figure-html/unnamed-chunk-40-1.pdf)<!-- -->

"The fact is: the cold is intense."

This pronoun is usually the singular masculine pronoun (as above) but it is also sometimes the singular feminine pronoun [هِيَ]{.ar}.
It is typically used with statements of import, to which the speaker wishes to draw attention.
The comment does not contain a linker pronoun because the whole comment refers back to the topic.
The pronoun of the fact is frequently used with [إِنَّ]{.ar} and its sisters. 
Here are some examples:

[إِنَّهُ لَا يُفْلِحُ ٱلْكَافِرُونَ.]{.ar}  
"Indeed, the disbelievers will not succeed."  
([#qurEAn]{.trn2} 23:117, trans. Saheeh International)

Sometimes, one can choose between using the pronoun of the fact and a pronoun matching the participant resulting in different emphasis. For example,

[إِنِّهُ هُمُ ٱلْفَاعِلُونَ]{.ar}  
"Indeed, the fact is: they are the doers."

[إِنِّهُمْ هُمُ ٱلْفَاعِلُونَ]{.ar}  
"Indeed, _they_ are the doers."

## The lightened versions [إِنْ]{.ar}, [أَنْ]{.ar}, [كَأَنْ]{.ar}, and [لَـٰكِنْ]{.ar}

The particles [إِنَّ]{.ar}, [أَنَّ]{.ar}, [كَأَنَّ]{.ar}, and [لَـٰكِنَّ]{.ar}, because of the doubled [نّ]{.ar} are considered _heavy_.
There exist _lightened_ versions of these particles that are:
[إِنْ]{.ar}, [أَنْ]{.ar}, [كَأَنْ]{.ar}, and [لَـٰكِنْ]{.ar}.
These lightened versions have similar meanings to their heavy counterparts but they have somewhat different rules. We will discuss them below.
In terms of their usage 
[إِنْ]{.ar} and
[كَأَنْ]{.ar} are not very commonly used except in the [#qurEAn]{.trn2}, poetry, and other rhetorical texts.
[أَنْ]{.ar} and
[لَـٰكِنْ]{.ar}
are relatively more common.

### The lightened [إِنْ]{.ar}

The lightened
[إِنْ]{.ar}
is used in two different ways.
In the more common way, the subject is not put in the a-state but is rather in the u-state.
However, the strengthening [لَ]{.ar} (see section\ \@ref(inna-strengthening-la) above), that was optional with the heavy [إِنَّ]{.ar}, is now mandatory with the lightened [إِنْ]{.ar}. For example,

[إِنْ زَيْدٌ لَمُسْلِمٌ.]{.ar}  
"Indeed Zayd is a Muslim."

The other notable difference between 
the lightened [إِنْ]{.ar}
and
the heavy [إِنَّ]{.ar}
is that 
the heavy [إِنَّ]{.ar} is only used to introduce subject-information sentences.
The lightened [إِنْ]{.ar},
however, can be used to introduce verbal sentences, but only those that begin with the verbs:
[كَانَ]{.ar} and its sisters,
[كَادَ]{.ar} and its sisters, and
[ظَنَّ]{.ar} and its sisters.
For example,

[قَرَأْتُ ٱلْكِتَابَ وَإِنْ كَانَ ٱلْكِتَابُ لَجَيِّدًا.]{.ar}  
"I read the book and indeed the book was good."

The second, less common way, of using
the lightened [إِنْ]{.ar}
is following the same rules as the 
the heavy [إِنَّ]{.ar}.
Where the subject is in the a-state and the use of the strengthening [لَ]{.ar} is optional. For example,

[إِنْ زَيْدًا مُسْلِمٌ.]{.ar}  
"Indeed Zayd is a Muslim."

### The lightened [أَنْ]{.ar} {#lightened-an}

As we know, the heavy [أَنَّ]{.ar} is an emphatic particle and is frequently used with the pronoun of the fact, thus:

[أَعْلَمُ أَنَّهُ ٱلْبَرْدُ شَدِيدٌ.]{.ar}  
"I know that the fact is: the cold is intense."

When we wish not to use much emphasis, we may replace
the heavy [أَنَّ]{.ar} along with its following pronoun of the fact ([أَنَّهُ]{.ar}/[أَنَّهَا]{.ar}) with
a lightened [أَنْ]{.ar}, thus:

[أَعْلَمُ أَنِ ٱلْبَرْدُ شَدِيدٌ.]{.ar}  
"I know that the cold is intense."

Note that
the lightened [أَنْ]{.ar} replaces 
[أَنَّهُ]{.ar},
which is the combination of
heavy [أَنَّ]{.ar} _and_ the pronoun of the fact [هُ]{.ar}.
So the pronoun of the fact ([هُ]{.ar}) does not appear with
the lightened [أَنْ]{.ar}.

<!--
The combination of a heavy [أَنَّ]{.ar} with a following pronoun of the fact ([أَنَّهُ]{.ar}/[أَنَّهَا]{.ar}) may be replaced with
a lightened [أَنْ]{.ar}. 
The pronoun of the fact ([هُ]{.ar}/[هَا]{.ar}) is then deleted.

only introduces topic-comment clauses whose topic is understood to be a deleted pronoun of the fact. 
The lightened [أَنْ]{.ar} only introduces topic-comment clauses whose topic is understood to be a deleted pronoun of the fact. 
The comment is, as usual, a complete sentence. 
For example, consider the following sentence with a heavy [أَنَّ]{.ar}:

[أَعْلَمُ أَنَّهُ ٱلْبَرْدُ شَدِيدٌ.]{.ar}  
"I know that the fact is: the cold is intense."

If we replace the heavy [أَنَّ]{.ar} in the above example with the lightened [أَنْ]{.ar} then we pronoun of the fact topic is deleted, thus:

[أَعْلَمُ أَنِ ٱلْبَرْدُ شَدِيدٌ.]{.ar}  
"I know that the cold is intense."
-->

In the above example, 
the lightened [أَنْ]{.ar}
introduces a comment which is a subject-predicate sentence.
But the more common use of 
the lightened [أَنْ]{.ar}
is to introduce comments that are verbal sentences.

When the comment of the 
lightened [أَنْ]{.ar}
is a verbal sentence, then it is  preferred to separate the verb from [أَنْ]{.ar} with one of the following:

1. [قَدْ]{.ar}. Example:
   
   [أَظُنُّ أَنْ قَدْ غَرَبَتِ ٱلشَّمْسُ.]{.ar}  
   "I think that the sun has set."

2. [سَ]{.ar} or [سَوْفَ]{.ar}. Example:

   [أَعْلَمُ أَنْ سَيَذْهَبُ.]{.ar}  
   "I know that he will go."

3. A negative particle like [لَا]{.ar}, [لَنْ]{.ar}, or [لَمْ]{.ar}.

   [أَعْلَمُ أَنْ لَا يَذْهَبُ.]{.ar}  
   "I know that he does/will not go."

   Note that, in writing, we have not combined the lightened [أَنْ]{.ar} and [لَا]{.ar} to form [أَلَّا]{.ar}, as is done for the a-state-verbal [أَنْ]{.ar} (for example: [أَلَّا يَذْهَبَ]{.ar} "that he not go") in chapter\ \@ref(chapter-a-state-incomplete-action-verbs). This distinction in spelling is not obligatory, but some authorities recommend it. In any case, they are both pronounced the same: [EallA]{.trn}. <!--al nahw al wafi 4/298, cited by Arik Sadan p.30 -->

   More examples:

   [أَعْلَمُ أَنْ لَنْ يَذْهَبَ.]{.ar}  
   "I know that he shall not go."

   [أَعْلَمُ أَنْ لَمْ يَذْهَبْ.]{.ar}  
   "I know that he did not go."

   Note that the [لَنْ]{.ar} and [لَمْ]{.ar}, even when after the lightened [أَنْ]{.ar}, change the state of the following incomplete-action verb to the a-state and [0]{.txt}-state respectively.

4. The conditional particle [لَوْ]{.ar}. We will study conditional sentences in chapter\ \@ref(conditional-sentences). TODO: add example.

Rigid verbs like [لَيْسَ]{.ar} and verbs expressing supplications are exempted from needing to be separated from the lightened [أَنْ]{.ar}. Example:

[ظَنَنْتُ أَنْ لَيْسَ ٱلْبَرْدُ شَدِيدًا.]{.ar}  
"I thought that the cold is not intense."

#### Distinguishing between the lightened [أَنْ]{.ar} and the a-state-verbal [أَنْ]{.ar} 

Although they are similar in meaning,
care must be taken to distinguish between this lightened [أَنْ]{.ar} and the a-state-verbal [أَنْ]{.ar} 
(that we learned in chapter\ \@ref(chapter-a-state-incomplete-action-verbs)),
The a-state-verbal [أَنْ]{.ar} puts the following incomplete action verb in the a-state.
Whereas the incomplete action verb directly after the lightened [أَنْ]{.ar} remains in the u-state.
The following guidelines can help to distinguish  between these two [أَنْ]{.ar}s:

+ If the verb before [أَنْ]{.ar} signifies certainty then only [أَنَّ]{.ar} and its lightened version [أَنْ]{.ar} is used. For example,

  [أَعْلَمُ أَنْ قَدْ ذَهَبَ وَأَنْ سَيَرْجِعُ.]{.ar}  
  "I know that he has gone and that he will return."

+ If the verb before [أَنْ]{.ar} signifies wanting, hoping, or expecting, then the [أَنْ]{.ar} puts the following verb in the a-state. For example,

  [أَطْمَعُ أَلَّا يَذْهَبَ.]{.ar}  
  "I hope that he not go."

  Note that the verb [يَذْهَبَ]{.ar} is in the a-state.

+ If the verb before [أَنْ]{.ar} reflects a view of something going to occur, and signifies neither certainty nor expectation, but rather doubt or neutrality, then either of the [أَنْ]{.ar}s may be used, depending on the intended meaning. Such verbs include [ظَنَّ يَظُنُّ]{.ar} "to think" and [حَسِبَ يَحْسِبُ]{.ar} "to deem". For example,

  a-state-verbal [أَنْ]{.ar}:  
  [ظَنَنْتُ أَنْ يَرْجِعَ.]{.ar}  
  "I thought that he should return."  

  lightened [أَنْ]{.ar}:  
  [ظَنَنْتُ أَنْ يَرْجِعُ.]{.ar}  
  "I thought that he will return."

+ If the verb before [أَنْ]{.ar} does not reflect a view of something going to occur then the [أَنْ]{.ar} is typically the a-state-verbal [أَنْ]{.ar}. For example,

  [سَرَّنِي أَنْ تَنْجَحَ]{.ar}  
  "That you succeed [will have] gladdened me."

  Remember from chapter\ \@ref(chapter-a-state-incomplete-action-verbs)), that the a-state-verbal [أَنْ]{.ar} can occur with completed-action verbs as well. Example:

  [سَرَّنِي أَنْ نَجَحْتَ]{.ar}  
  "That you have succeeded [has] gladdened me."

### The lightened [كَأَنْ]{.ar}

The lightened [كَأَنْ]{.ar} is similar to the lightened [أَنْ]{.ar} in that it introduces a topic-comment sentence and the topic is usually a deleted pronoun of the fact. For example,

[كَأَنْ ٱلْبَرْدُ ذَهَبَ.]{.ar}  
"[It is] as if the cold has gone."

Also similar to the lightened [أَنْ]{.ar}, the lightened [كَأَنْ]{.ar} may introduce a verbal sentence but it must be separated from [كَأَنْ]{.ar} by either [قَدْ]{.ar} or [لَمْ]{.ar}. For example,

[ذَهَبَ كَأَنْ لَمْ يَسْمَعْ.]{.ar}  
"He went as if he did not hear."

### The lightened [لَـٰكِنْ]{.ar}

The lightened [لَـٰكِنْ]{.ar} has the same meaning as the heavy [لَـٰكِنَّ]{.ar} but it has no grammatical effect on the word or sentence after it. It may introduce either subject-information or verbal sentences. For example,

[نَجَحَ زَيْدٌ لَـٰكِنْ صَدِيقُهُ لَمْ يَنْجَحْ.]{.ar}  
"Zayd succeeded but his friend did not succeed."


<!--chapter:end:srcrmd/inna_and_its_sisters.Rmd-->

# Nouns of superiority

## Introduction

Consider the sentence:

"The book is heavier than the pen."

In this sentence a relationship of superiority is established between the two nouns: "the book" and "the pencil". The book is being described as being superior in heaviness.

By the way, we are using the "superiority" in a technical sense. For example, we can say "The donkey is weaker than the horse." Here the donkey is being described as superior in weakness.

In order to express a superiority relationship between nouns, for example, , Arabic uses qualitative nouns with a distinct form. Here is a table of some common qualitative nouns and their corresponding  nouns of superiority.

|Root|Qualitative noun | Noun of superiority|
|:--|:--|:--|
|[كبر]{.arroot}|[كَبِيرٌ]{.ar}   [kabIrun]{.trn}   "big"       | [أَكْبَرُ]{.ar} [Eakbaru]{.trn} "biger"     |
|[صغر]{.arroot}|[صَغِيرٌ]{.ar}   [SagIrun]{.trn}   "small"     | [أَصْغَرُ]{.ar} [EaSgaru]{.trn} "smaller"   |
|[حسن]{.arroot}|[حَسَنٌ]{.ar}    [Hasanun]{.trn}   "good"      | [أَحْسَنُ]{.ar} [EaHsanu]{.trn} "better"    |
|[سوء]{.arroot}|[سَيِّئٌ]{.ar}    [sayyiEun]{.trn}  "bad"       | [أَسْوَأُ]{.ar} [EaswaEu]{.trn} "worse"     |
|[قدم]{.arroot}|[قَدِيمٌ]{.ar}   [qadImun]{.trn}   "old"       | [أَقْدَمُ]{.ar} [Eaqdamu]{.trn} "older"     |
|[جد]{.arroot}|[جَدِيدٌ]{.ar}    [jadIdun]{.trn}   "new"       | [أَجَدُّ]{.ar}  [Eajaddu]{.trn} "newer"     |
|[سهل]{.arroot}|[سَهْلٌ]{.ar}    [sahlun]{.trn}    "easy"      | [أَسْهَلُ]{.ar} [Eashalu]{.trn} "easier"    |
|[صعب]{.arroot}|[صَعْبٌ]{.ar}    [Saebun]{.trn}    "difficult" | [أَصْعَبُ]{.ar} [EaSeabu]{.trn} "more difficult"|
|[طول]{.arroot}|[طَوِيلٌ]{.ar}   [TawIlun]{.trn}   "long"      | [أَطْوَلُ]{.ar} [EaTwalu]{.trn} "longer"     |
|[قصر]{.arroot}|[قَصِيرٌ]{.ar}   [qaSIrun]{.trn}   "short"     | [أَقْصَرُ]{.ar} [EaqSaru]{.trn} "shorter"    |
|[ثقل]{.arroot}|[ثَقِيلٌ]{.ar}   [vaqIlun]{.trn}   "heavy"     | [أَثْقَلُ]{.ar} [Eavqalu]{.trn} "heavier"    |
|[خف]{.arroot}|[خَفِيفٌ]{.ar}    [xafIfun]{.trn}   "light"     | [أَخَفُّ]{.ar}  [Eaxaffu]{.trn} "lighter"    |
|[وسع]{.arroot}|[وَاسِعٌ]{.ar}   [wAsieun]{.trn}   "wide"      | [أَوْسَعُ]{.ar} [Easwaeu]{.trn} "wider"      |
|[ضيق]{.arroot}|[ضَيِّقٌ]{.ar}    [Dayyiqun]{.trn}  "narrow"    | [أَضْيَقُ]{.ar} [EaDyaqu]{.trn} "narrower"   |
|[سرع]{.arroot}|[سَرِيعٌ]{.ar}   [sarIeun]{.trn}   "fast"      | [أَسْرَعُ]{.ar} [Easraeu]{.trn} "faster"     |
|[بطء]{.arroot}|[بَطِيءٌ]{.ar}   [baTIEun]{.trn}   "slow"      | [أَبْطَأُ]{.ar} [EabtaEu]{.trn} "slower"     |
|[قوي]{.arroot}|[قَوِيٌّ]{.ar}    [qawiyyun]{.trn}  "strong"    | [أَقْوَىٰ]{.ar} [EaqwA]{.trn}   "stronger"   |
|[ضعف]{.arroot}|[ضَعِيفٌ]{.ar}   [DaeIfun]{.trn}   "weak"      | [أَضْعَفُ]{.ar} [EaDeafu]{.trn} "weaker"     |
|[كثر]{.arroot}|[كَثِيرٌ]{.ar}   [kavIrun]{.trn}   "many"      | [أَكْثَرُ]{.ar} [Eakvaru]{.trn} "more"       |
|[قل]{.arroot} |[قَلِيلٌ]{.ar}   [qalIlun]{.trn}   "few/less"  | [أَقَلُّ]{.ar}  [Eaqallu]{.trn} "fewer/lesser"|

Note the following points regarding the form of the noun of superiority:

+ Nouns of superiority are regularly of the pattern [أَفْعَلُ]{.ar} [Eafealu]{.trn} using the template root [فعل]{.arroot}. 
+ Nouns of superiority are non-fully changing nouns, so they won't have [n]{.trn} marks and the indefinite noun in the i-state will have an [a]{.trn}-mark on the last letter.
+ If a root's last two letters are the same, it is shown as a two-letter root and the noun of superiority is formed by doubling the last letter. Example: [جد]{.arroot}: [أَجَدُّ]{.ar}  [Eajaddu]{.trn} "newer".
+ If a root's last letter is [و]{.ar} or [ي]{.ar}, then the noun of superiority's last letter will be [ىٰ]{.ar}. Example: [قوي]{.arroot}: [أَقْوَىٰ]{.ar} [EaqwA  ]{.trn} "stronger".

You may remember that the pattern of the identical is identical to the pattern of colors and physical characteristics. For example [أَحْمَرُ]{.ar} [EaHmaru]{.trn} "red". However, this similarity is largely superficial. We will see that nouns of superiority are feminized differently and sometimes not at all.

## Comparing two nouns

Nouns of superiority can be used to compare a qualitative quality between two nouns. Here is an example sentence:

[ٱَلْغُلَامُ أَطْوَلُ مِنَ ٱلْجَارِيَةِ.]{.ar}  
[EalgulAmu EaTwalu mina -ljAriyati.]{.trn}  
"The boy is taller than the girl."

Here you can see that the preposition [مِنْ]{.ar} [min]{.trn} is used to mean "than".

If we wish to say: "The girl is taller than the boy.", we will use the same [أَطْوَل]{.ar} [EaTwalu]{.trn} even though the subject "the girl" is now feminine:

[ٱَلْجَارِيَةِ أَطْوَلُ مِنَ ٱلْغُلَامُ.]{.ar}  
[EaljAriyati EaTwalu mina -lgulAmu.]{.trn}  
"The girl is taller than the boy."

Similarly, if the subject noun to be compared is a plural, whether masculine or feminine, rational or non-rational, the same noun of superiority is used. Examples:

[ٱَلرِّجَالُ أَطْوَلُ مِنَ ٱلنِّسَاءِ وَهُنَّ أَقْصَرُ مِنْهُمْ.]{.ar}  
[EarrijAlu Eatwalu mina -nnisAEi wa hunna EaqSaru minhum.]{.trn}  
"The men are taller than the women and they~fem.~ are shorter than them~masc.~."

[ٱلْكُتُبُ أَثُقَلُ مِنَ ٱلْأَقْلَامِ.]{.ar}  
[Ealkutubu Eavqalu mina -lEaqlAmi.]{.trn}  
"The books are heavier than the pens."

### Nouns of superiority without a second noun

The above example compared one noun to another. Often, the second noun need not be mentioned. For example,

[ٱلْكُتُبُ أَثْقَلُ.]{.ar}  
[Ealkutubu Eavqalu.]{.trn}  
"The books are heavier."

## Conveying the meaning of the highest degree

The same nouns of superiority are also used in Arabic to convey the meaning of the highest degree of a quality, like "the biggest house", "the weakest link", "the best book", etc. This can be done in a number of ways.

### With indefinite noun-chains

The most common way to express this in Arabic is using a noun-chain with the noun of superiority and an indefinite noun. Here is an example:

[هُوَ أَسْرَعُ غُلَامٍ فِي ٱلْمَدْرَسَةِ.]{.ar}  
[huwa Easraeu gulAmin fi -lmadrasati.]{.trn}  
"He is the fastest boy in the school."

An important point to note is that while in English we used the definite in the translation: "the fastest boy", in Arabic the noun-phrase [أَسْرَعُ غُلَامٍ]{.ar} [Easraeu gulAmin]{.trn} is technically indefinite. It is just hard to find a suitable translation in English where the noun-phrase could be indefinite.

The same noun of superiority is used with feminine and dual/plural nouns. Examples:

[هِيَ أَطْوَلُ ٱمْرَأَةٍ.]{.ar}  
[hiya EaTwalu -mraEatin.]{.trn}  
"She is the tallest woman."

[هُمَا أَطْوَلُ رَجُلَيْنِ.]{.ar}  
[humA EaTwalu rajulayni.]{.trn}  
"They are tallest (two) men."

[هُنَّ أَطْوَلُ نِسَاءٍ.]{.ar}  
[hunna EaTwalu nisAEin.]{.trn}  
"They are the tallest women."

<!-- ^ pretty much from Wright vol. ii., sect. 93, p. 227 -->

### With definite noun-chains

The noun of superiority can also be used in definite noun-chains with a slightly different meaning. However, the second noun of the noun-chain will need to be in the plural. Examples:

[هُوَ أَطْوَلُ ٱلرِّجَالِ.]{.ar}  
[huwa EaTwalu -rrijAli.]{.trn}  
"He is the tallest of the men."

[هُمَا أَطْوَلُ ٱلنِّسَاءِ]{.ar}  
[humA EaTwalu -nnisAEi.]{.trn}  
"They (two) are the tallest of the women."

## Feminine, dual, and plural forms

So far we have used only one form of the noun of superiority: [أَفْعَلُ]{.ar} [Eafealu]{.trn}. Technically, this is the masculine singular form, although it can be used for feminine, dual, and plural nouns as we have seen above. 

However, when the meaning of the highest degree is to be conveyed for definite nouns without using noun-chains, then we will use new feminine, dual, and plurals forms for the noun of superiority. We will give these forms below:

| Number | Masc. | Fem. |
|:--|:--|:--|
|sing.        | [أَفْعَلُ]{.ar} [Eafealu]{.trn}|    [فُعْلَىٰ]{.ar} [fuelA]{.trn}|
|dual         | [أَفْعَلَانِ]{.ar} [EafealAni]{.trn}|[فُعْلَيَانِ]{.ar} [fuelayAni]{.trn}|
|sound plur.  | [أَفْعَلُونَ]{.ar} [EafealUna]{.trn}|[فُعْلَيَاتٌ]{.ar} [fuelayAtun]{.trn}|
|broken plur. | [أَفَاعِلُ]{.ar} [EafAeilu]{.trn}|  [فُعَلٌ]{.ar} [fuealun]{.trn}|

These forms are to be used when the noun of superiority is usually definite and either:

 i. by itself, or
ii. a describer.

We will give some examples below:

[هُوَ ٱلرَّجُلُ ٱلْأَطْوَلُ.]{.ar}  
[huwa -rrajulu -lEaTwalu.]{.trn}  
"He is the tallest man."

[هِيَ ٱلْمَرْأَةُ ٱلطُّولَىٰ.]{.ar}  
[hiya -lmarEatu -TTUlA.]{.trn}  
"She is the tallest woman."

[هُمَا ٱلرَّجُلَانِ ٱلْأَطْوَلَانِ.]{.ar}  
[huma -rrajulAni -lEaTwalAni.]{.trn}  
"They~masc.\ dual~ are the two tallest men."

[هُمَا ٱلْمَرْأَتَانِ ٱلطُّولَيَانِ.]{.ar}  
[huma -lmarEatAni -TTUlayAni.]{.trn}  
"They~fem.\ dual~ are the two tallest women."

[هَـٰؤُلَاءِ هُمُ ٱلرِّجَالُ ٱلْأَطْوَلُونَ وَأُولَـٰئِكَ هُمُ ٱلأَقَاصِرُ.]{.ar}  
[hAEulAEi humu -rrijAlu -lEaTwalUna waEulAEika humu -lEaqASiru.]{.trn}  
"These are the tallest men and those are the shortest [men]."  

[هَـٰؤُلَاءِ هُنَّ ٱلنِّسَاءُ ٱلطُّولَيَاتُ وَأُولَـٰئِكَ هُنَّ ٱلقُصَرُ.]{.ar}  
[hAEulAEi hunna -nnisAEu -TTUlayAtu waEulAEika hunna -lquSaru.]{.trn}  
"These are the tallest women and those are the shortest [women]."  

### Plural forms with non-rational beings

If a noun of superiority is to be used with a definite plural noun for (masculine or feminine) non-rational beings, either by itself or as a describer, then it will usually be the feminine singular form. This is consistent with what we have learned so far regarding the use of feminine singular qualitative nouns and pronouns for non-rational beings. Here is an example:

[ٱَلْكُتُبُ ٱلْكَبِيرَةُ هِيَ ٱلثُّقْلَىٰ.]{.ar}  
[Ealkutubu -lkabIratu hiya -vvuqlA.]{.trn}  
"The big books are the heaviest."  

Sometimes, however, if the plural noun is not mentioned in a sentence we can use the broken plural of the feminine noun of superiority to convey the meaning of plurality. For example,

[قَسَمْتُ ٱلْأَقْلَامَ. هَـٰؤُلَاءِ هُنَّ ٱلطُّوَلُ وَأُولَـٰئِكَ هُنَّ ٱلقُصَرُ.]{.ar}  
[qasamtu -lEaqlAma. hAEulAEi hunna -TTuwalu waEulAEika hunna -lquSaru.]{.trn}  
"I divided the pens. These are the tallest and those are the shortest."  

<!-- تلك الغرانيق العلى 
فقرأ ببسورة من الطُّوَل
-->

<!--[قَسَمْتُ ٱلْأَقْلَامَ. هَـٰؤُلَاءِ هُنَّ ٱلطُّولَيَاتُ وَأُولَـٰئِكَ هُنَّ ٱلقُصْرَيَاتُ.]{.ar}  
[qasamtu -lEaqlAma. hAEulAEi hunna -TTUlayAtu waEulAEika hunna -lquSrayAtu.]{.trn}  
"I divided the pens. These are the tallest and those are the shortest."  -->

<!--https://majles.alukah.net/t78123/

هذه المباني / الحدائق هي الكبرى/ الكبريات (ولا يجوز: هي الأكبر!!!).
-->

### Dual and plural forms in definite noun-chains

In section X above we learned that that definite noun-chains use the form [أَفْعَلُ]{.ar} [Eafealu]{.trn}. We gave the following examples:

[هُوَ أَطْوَلُ ٱلرِّجَالِ.]{.ar}  
[huwa EaTwalu -rrijAli.]{.trn}  
"He is the tallest of the men."

[هُمَا أَطْوَلُ ٱلنِّسَاءِ]{.ar}  
[humA EaTwalu -nnisAEi.]{.trn}  
"They (two) are the tallest of the women."

We now modify this rule to state that dual and plural forms of the noun of superiority can be used as well, especially when no other indication of number is present.

For example, in the sentence,

[هُمْ أَطْوَلُ ٱلرِّجَالِ.]{.ar}  
[hum EaTwalu -rrijAli.]{.trn}  
"They~masc.\ plur.~ are the tallest of the men."

the pronoun [هُمْ]{.ar} tells us that we are talking about multiple persons who are the tallest of the men. But if we have a sentence like:

[ذَهَبَ أَطْوَلُ ٱلرِّجَالِ.]{.ar}  
[pahaba EaTwalu -rrijAli.]{.trn}  
"The tallest of the men went."

Here we cannot say that one man had gone or more than one. To remove this ambiguity we can use the plural form [أَطَاوِلُ]{.ar} [EaTAwilu]{.trn} thus:

[ذَهَبَ أَطَاوِلُ ٱلرِّجَالِ.]{.ar}  
[pahaba EaTAwilu -rrijAli.]{.trn}  
"The tallest~plur.~ of the men went."

## Comparing a noun with itself

<!--vol. ii.,Sect. 48 rem A. p. 133A-->
A noun can be compared with itself in a different respect. For example, we can say:

"The tree is closer to Zayd than it is to [#muHammad]{.trn2}."

Here the tree is being compared with itself with respect to its position near Zayd and its position near [#muHammad]{.trn2}. We will use the appropriate attached pronoun for the object being compared and attach it tp the preposition of comparison [مِنْ]{.ar} [min]{.trn} "than". So the above sentence can be expressed as:

[ٱَلشَّجَرَةُ أَقْرَبُ إِلَىٰ زَيْدٍ مِنْهَا إِلَىٰ مُحَمَّدٍ.]{.ar}  
[Eaccajaratu Eaqrabu EilA zaydin minhA EilA muHammadin.]{.trn}  

The attached pronoun [ـهَا]{.ar} [-hA]{.trn} refers to [ٱَلشَّجَرَةُ]{.ar} [Eaccajaratu]{.trn} "the tree".
The preposition [إِلَىٰ]{.ar} [EilA]{.trn} is used with the noun of superiority [أَقْرَبُ]{.ar} [Eaqrabu]{.trn} to express "nearer to".

## Attention to the definiteness and plurality of noun-chains

We have seen that if a noun of superiority is used in an indefinite noun-chain, it conveys the idea of the highest degree, and the singularity or plurality of second noun in the noun-chain conveys the number of object whose superiority is being expressed. The examples we gave were:

[هِيَ أَطْوَلُ ٱمْرَأَةٍ.]{.ar}  
[hiya EaTwalu -mraEatin.]{.trn}  
"She is the tallest woman."

[هُمَا أَطْوَلُ رَجُلَيْنِ.]{.ar}  
[humA EaTwalu rajulayni.]{.trn}  
"They are tallest (two) men."

[هُنَّ أَطْوَلُ نِسَاءٍ.]{.ar}  
[hunna EaTwalu nisAEin.]{.trn}  
"They are the tallest women."

Here we would like to stress that second-noun of the noun chain must be indefinite. So, for example, we can have a sentence:

[هَـٰذَا أَكْبَرُ بَيْتٍ.]{.ar}  
[hApA Eakbaru baytin.]{.trn}  
"This is the biggest house."

If we would like to express "This is the biggest house of the city" then we cannot simply extend the noun-chain by adding [ٱلْمَدِينَةِ]{.ar} [-lmadInati]{.trn} "of the city" to it thus:

[هَـٰذَا أَكْبَرُ بَيْتِ ٱلْمَدِينَةِ.]{.ar}  
[hApA Eakbaru bayti -lmadInati.]{.trn}  

This is because the noun-chain is now definite. This sentence can now only mean "This is the biggest [part] of the house of the city."

In order to express the desired meaning, we have a few options with similar meanings:

[هَـٰذَا بَيْتُ ٱلْمَدِينَةِ ٱلْأَكْبَرُ.]{.ar}  
[hApA baytu -lmadInati -lEakbaru.]{.trn} 
"This is the biggest house of the city."

[هَـٰذَا أَكْبَرُ بَيْتٍ فِي ٱلْمَدِينَةِ.]{.ar}  
[hApA Eakbaru baytin fi -lmadInati.]{.trn}  
"This is the biggest house in the city."

[هَـٰذَا أَكْبَرُ بُيُوتِ ٱلْمَدِينَةِ.]{.ar}  
[hApA Eakbaru buyUti -lmadInati.]{.trn}  
"This is the biggest of the houses of the city."

<!--https://forum.wordreference.com/threads/%D9%81%D9%8A-%D8%A3%D9%82%D8%B5%D9%89-%D8%B3%D8%A7%D8%AD%D9%84-%D8%A8%D8%AD%D8%B1-%D8%A7%D9%84%D8%B4%D9%85%D8%A7%D9%84.3477546/#post-17650853-->

## Expressing "better than" and "worse than"

To express the meaning "better" Arabic can use  [أَحْسَنُ]{.ar} [EaHsanu]{.trn} from [حَسَنٌ]{.ar} [Hasanun]{.trn}. There is also the word [أَفْضَلُ]{.ar} [EafDalu]{.trn} is very commonly used. Technically it means "more preferred" but it is often used where in English we would say "better".

Similarly, to express worse we can use [أَسْوَأُ]{.ar} [EaswaEu]{.trn} from [سَيِّئٌ]{.ar} [sayyiEun]{.trn}.

In addition, there are two words: [خَيْرٌ]{.ar} [xayrun]{.trn} and [شَرٌّ]{.ar} [carrun]{.trn}, which are really designative nouns meaning "goodness" and "evil" respectively. 

These same words, although they not in the pattern [أَفْعَلُ]{.ar} [Eafealu]{.trn}, are used with [مِنْ]{.ar} [min]{.trn} "than" to express "better" and "worse" respectively. Here are some examples:

## The word "other"

The word [آخَرُ]{.ar} [EAxaru]{.trn} is a qualitative noun meaning "other". It is actually on the pattern of the noun of superiority [أَفْعَلُ]{.ar} [Eafealu]{.trn} with the root [ءخر]{.arroot} but is somewhat of an anomaly because it does not have a meaning of superiority and is not used for comparison. That is to say: we cannot say that something is more "other" than something else. It shares some of the qualities of the noun of superiority in the formation of its feminine and plurals. We will describe these and their usages below.

| Number | Masc. | Fem. |
|:--|:--|:--|
|sing.        | [آخَر]{.ar}   [EAxaru]{.trn}|    [أُخْرَىٰ]{.ar} [EuxrA]{.trn}|
|dual         | [آخَرَانِ]{.ar} [EAxarAni]{.trn}|[أُخْرَيَانِ]{.ar} [EuxrayAni]{.trn}|
|sound plur.  | [آخَرُونَ]{.ar} [EAxarUna]{.trn}|[أُخْرَيَاتٌ]{.ar} [EuxrayAtun]{.trn}|
|broken plur. | [أَوَاخِرُ]{.ar} [EawAxiru]{.trn}|  [أُخَرُ]{.ar}  [Euxaru]{.trn}|

Note that the masculine broken plural [أَوَاخِرُ]{.ar} [EawAxiru]{.trn} (on the pattern [أَفَاعِلُ]{.ar} [EafAeilu]{.trn}) has replaced the [ء]{.ar} in the root with a [و]{.ar}. This is a regular replacement in order to avoid two [ء]{.ar}s next to one another in [أَءَاخِرُ]{.ar} [EaEAxiru]{.trn}. This broken plural is given here for completeness but it is actually very rarely used. The sound [Un]{.trn} plural [آخَرُونَ]{.ar} [EAxarUna]{.trn} is used instead.

Also note that the feminine broken plural [أُخَرُ]{.ar} [Euxaru]{.trn} is non-fully changing. This is irregular because the broken plural pattern [فُعَلٌ]{.ar} [fuealun]{.trn} is usually fully-changing.

We use [آخَرُ]{.ar} [EAxaru]{.trn} just like any other qualitative noun and we will give some examples below.

[جَاءَ زَيْدٌ وَرَجُلٌ آخَرُ.]{.ar}  
[jAEa zaydun warajulun EAxaru.]{.trn}  
"Zayd and another man came."

[ذَهَبَتْ زَيْنَبُ إِلَى ٱلْمَدْرَسَةِ ٱلْأُخْرَىٰ.]{.ar}  
[pahabat zaynabu Eila -lmadrasati -lEuxrA.]{.trn}  
"Zaynab went to the other school."

[قَرَأْتُ هَـٰذَا ٱلْكِتَابَ وَكِتَابَيْنِ آخَرَيْنِ.]{.ar}  
[qaraEtu hApa -lkitAba wakitAbayni EAxarayni.]{.trn}  
"I read this book and two other books."

[ذَهَبَ رِجَالٌ آخَرُونَ.]{.ar}  
[pahaba rijAlun EAxarUna]{.trn}  
"Other men went."

[ذَهَبَتْ زَيْنَبُ مَعَ ٱلنِّسَاءِ ٱلْأُخْرَيَاتِ.]{.ar}  
[pahabat zaynabu maea -nnisAEi -lEuxrayAti.]{.trn}  
"Zaynab went with the other women."

With non-rational nouns, just like other qualitative nouns, the feminine singular is usually used. Example:

[قَرَأْتُ هَـٰذَا ٱلْكِتَابَ وَكُتُبًا أُخْرَىٰ.]{.ar}  
[qaraEtu hApa -lkitAba wakutuban EuxrA.]{.trn}  
"I read this book and other books."

However, the feminine broken plural [أُخَرُ]{.ar} [Euxaru]{.trn} can also be used, especially if there is no other indication of plurality. Examples:

[هَـٰذَا ٱلْكِتَابُ خَفِيفٌ وَٱلْأُخَرُ ثَقِيلَةٌ.]{.ar}  
[hApa -lkitAbu xafIfun wa-lEuxaru vaqIlatun.]{.trn}  
"This book is light and the others are heavy."

[قَرَأَ هَـٰذَا ٱلْكِتَابَ وَقَرَأَ أُخَرَ.]{.ar}  
[qaraEa -lkitAba waqaraEa Euxara.]{.trn}  
"He read this book and and he read others."


<!--chapter:end:srcrmd/elatives.Rmd-->

# (APPENDIX) Appendix {-}


<!--chapter:end:srcrmd/appendix.Rmd-->

# Rules for writing hamzah {#hamzarules}

## Seats of hamzah

Hamzah is written in four different ways:

1. Seated on an [Ealif]{.trn}: [أ]{.tradar} or [إ]{.tradar}
2. Seated on an [wAw]{.trn}: [ؤ]{.tradar}
3. Seated on an [yAE]{.trn}: [ئ]{.tradar}
4. Unseated: [ء]{.tradar}

Here are some of notes about writing hamzah in the above four methods:

+ When unseated hamzah comes between two letters that are joined, then it is written above the line that joins them, for example: [خَطِيءَة]{.tradar} [xaTIEah]{.trn}. In this word, the [yAE]{.trn} [ي]{.tradar} joins to the [tAE marbUTah]{.trn} [ة]{.tradar}.

+ When unseated hamzah is followed by an [Ealif]{.trn}: [ءا]{.tradar},  the combination of hamzah and [Ealif]{.trn} is usually written as [آ]{.tradar} as a convention. Examples: [آمَنَ]{.tradar} [EAmana]{.trn}, [ظَمْآن]{.tradar} [PamEAn]{.trn}, [شَنَآن]{.tradar} [canaEAn]{.trn}. However, when the [Ealif]{.trn} is a suffix or part of a suffix, or the hamzah is doubled, or there is an [Ealif]{.trn} before the hamzah then we will write [ءا]{.tradar}, not [آ]{.tradar}. Examples: [شَيْءَانِ]{.tradar} [cayEAni]{.trn}, [سَءَّال]{.tradar} [saEEAl]{.trn}, [قِرَاءَات]{.tradar} [qirAEAt]{.trn}. 

+ When hamzah is seated on [Ealif]{.trn}, if it has an [i]{.trn}-mark, it is written below the [Ealif]{.trn}: [إِ]{.tradar}. Otherwise, it is written above the [Ealif]{.trn}: [أَ]{.tradar}, [أُ]{.tradar}, [أْ]{.tradar}.

+ When hamzah is seated on [yAE]{.trn} [ئ]{.tradar} the dots of the [yAE]{.trn} are no longer written. Here's how it will appear in different positions:

  Isolated | End | Middle | Beginnning
  :--------|:----|:-------|:----------
  [ئ]{.tradar}| [ـئ]{.tradar}| [ـئـ]{.tradar}| [ئـ]{.tradar}

  Note that hamzah is seated on [yAE]{.trn} in the middle position [ـئـ]{.tradar} is different from unseated hamzah between two joining letters [ـءـ]{.tradar}.

So how do we know when to write hamzah unseated and when seated? And how do we choose between its three different seats? There are a set of rules that we need to follow in order to correctly write hamzah. Before we give the rules we will first present the underlying principle behind the rules.

## Rules for determining the seat of hamzah

### Separate main word from prefixes and suffixes

In order to determine the seat of hamzah for a words, we must first separate the main word from any prefixes and suffixes.
We will determine the seat of hamzah for the main word first.
Hamzah can occur in three positions in the main word:

1. At the beginning of the word
1. In the middle of the word
1. At the end of the word

We will treat each of these positions below.

####  At the beginning of the word

When hamzah occurs in the beginning of a word, then:

a. If the hamzah carries a long-[A]{.trn} vowel, it is written unseated followed by an [Ealif]{.trn} and written as [آ]{.tradar}, for example [آمَنَ]{.tradar} [EAmana]{.trn}.
b. If the hamzah carries any other vowel, it is written seated on an [Ealif]{.trn}, and is marked with the appropriated vowel mark, for example [أَسْلَمَ]{.tradar} [Easlama]{.trn}, [أُرِيدُ]{.tradar} [EurIdu]{.trn}, [إِسْلَام]{.tradar} [EislAm]{.trn}, [إِيمَان]{.tradar} [EImAn]{.trn}, [أُوخِذَ]{.tradar} [EUxipa]{.trn}. 

#### In the middle of the word

The most general case is when hamzah is in the middle of a word. 

Arabic has three short vowels, three long vowels, two diphthongs, and a [sukUn]{.trn}. Each of these has an order of precedence and a hamzah seat.

Precedence | Vowel | Seat 
:--|:------|:--------|:------
1. | [I]{.trn}/[ay]{.trn} | [ء]{.tradar}
2. | [i]{.trn}            | [ئ]{.tradar}
3. | [U]{.trn}/[aw]{.trn} | [ء]{.tradar}
4. | [u]{.trn}            | [ؤ]{.tradar}
5. | [A]{.trn}            | [ء]{.tradar}
6. | [a]{.trn}            | [أ]{.tradar}
7. | [◌ْ]{.tradar}             | [ء]{.tradar}

**Main rule:** Disregard any doubling mark [◌ّ]{.tradar} and consider the vowel on the consonant before the hamzah and the _shortened_ vowel on the hamzah itself. Determine which of the two vowels wins by being higher in precedence in the above table. The winning vowel's seat will be the seat of the hamzah.

**Sub-rule:** If the main rule determines that hamzah is to be seated on [Ealif]{.trn}, and there is a long [A]{.trn} vowel on the hamzah using an [Ealif]{.trn}, then hamzah shall be unseated. And the combination of [ءَا]{.tradar} will usually be written as [آ]{.tradar}.

Examples:

| Word | Vowel on consonant before hamzah | Shortened vowel on hamzah | Winning vowel | Seated hamzah |
|:-----|:-|:-|:-|:------|
| [هَيْءَة]{.tradar} [hayEah]{.trn}     | [ay]{.trn} | [a]{.trn}  | [ay]{.trn} | [ء]{.tradar} |
| [خَطِيءَة]{.tradar} [xaTIEah]{.trn}   | [I]{.trn}  | [a]{.trn}  | [I]{.trn}  | [ء]{.tradar} |
| [اسْتِيءَاس]{.tradar} [EistIEAs]{.trn}| [I]{.trn}  | [a]{.trn}  | [I]{.trn}  | [ء]{.tradar} (Exception: [ءَا]{.tradar} is not written as [آ]{.tradar} when the preceding vowel is [I]{.trn}.)|
| [تَوْءَم]{.tradar} [tawEam]{.trn}     | [aw]{.trn} | [a]{.trn}  | [aw]{.trn} | [ء]{.tradar} |
| [سَائِل]{.tradar} [sAEil]{.trn}      | [A]{.trn}  | [i]{.trn}  | [i]{.trn}  | [ئ]{.tradar} |
| [تَسَاؤُل]{.tradar} [tasAEul]{.trn}   | [A]{.trn}  | [u]{.trn}  | [u]{.trn}  | [ؤ]{.tradar} |
| [تَسَاءَلَ]{.tradar} [tasAEala]{.trn}  | [A]{.trn}  | [a]{.trn}  | [A]{.trn}  | [ء]{.tradar} |
| [قِرَاءَات]{.tradar} [qirAEAt]{.trn}  | [A]{.trn}  | [a]{.trn}  | [A]{.trn}  | [ء]{.tradar} |
| [مَسْؤُول]{.tradar} [masEUl]{.trn}    | [◌ْ]{.tradar}   | [u]{.trn}  | [u]{.trn}  | [ؤ]{.tradar} |
| [تَرْئِيس]{.tradar} [tarEIs]{.trn}    | [◌ْ]{.tradar}   | [i]{.trn}  | [i]{.trn}  | [ئ]{.tradar} |
| [مِرْآة]{.tradar} [mirEAh]{.trn}     | [◌ْ]{.tradar}   | [a]{.trn}  | [a]{.trn}  | [ء]{.tradar} (Using sub-rule.)|
| [ظَمْآن]{.tradar} [PamEAn]{.trn}     | [◌ْ]{.tradar}   | [a]{.trn}  | [a]{.trn}  | [ء]{.tradar} (Using sub-rule.)|
| [مَسْأَلَة]{.tradar} [masEalah]{.trn}  | [◌ْ]{.tradar}   | [a]{.trn}  | [a]{.trn}  | [أ]{.tradar} |
| [الْمَرْأَة]{.tradar} [almarEah]{.trn} | [◌ْ]{.tradar}   | [a]{.trn}  | [a]{.trn}  | [أ]{.tradar} |
| [بِئْسَ]{.tradar} [biEsa]{.trn}       | [i]{.trn}  | [◌ْ]{.tradar}   | [i]{.trn}  | [ئ]{.tradar} |
| [سُؤْلَكَ]{.tradar} [suElaka]{.trn}    | [u]{.trn}  | [◌ْ]{.tradar}   | [u]{.trn}  | [ؤ]{.tradar} |
| [كَأْس]{.tradar} [kaEs]{.trn}        | [a]{.trn}  | [◌ْ]{.tradar}   | [a]{.trn}  | [أ]{.tradar} |
| [سُئِلَ]{.tradar} [suEila]{.trn}      | [u]{.trn}  | [i]{.trn}  | [i]{.trn}  | [ئ]{.tradar} |
| [يَئِسَ]{.tradar} [yaEisa]{.trn}      | [a]{.trn}  | [i]{.trn}  | [i]{.trn}  | [ئ]{.tradar} |
| [رَئِيس]{.tradar} [raEIs]{.trn}      | [a]{.trn}  | [i]{.trn}  | [i]{.trn}  | [ئ]{.tradar} |
| [سُؤَال]{.tradar} [suEAl]{.trn}      | [u]{.trn}  | [a]{.trn}  | [u]{.trn}  | [ؤ]{.tradar} |
| [رُؤُوس]{.tradar} [ruEUs]{.trn}      | [u]{.trn}  | [u]{.trn}  | [u]{.trn}  | [ؤ]{.tradar} |
| [لُؤَيّ]{.tradar} [luEayy]{.trn}      | [u]{.trn}  | [a]{.trn}  | [u]{.trn}  | [ؤ]{.tradar} |
| [شَنَآن]{.tradar} [canaEAn]{.trn}    | [a]{.trn}  | [a]{.trn}  | [a]{.trn}  | [ء]{.tradar} (Using sub-rule.)|
| [سَأَلَ]{.tradar} [saEala]{.trn}      | [a]{.trn}  | [a]{.trn}  | [a]{.trn}  | [أ]{.tradar} |
| [رَأَىٰ]{.tradar} [raEA]{.trn}        | [a]{.trn}  | [a]{.trn}  | [a]{.trn}  | [أ]{.tradar} |
| [رَأَّسَ]{.tradar} [raEEasa]{.trn}     | [a]{.trn}  | [a]{.trn}  | [a]{.trn}  | [أ]{.tradar} |
| [يُرَئِّسُ]{.tradar} [yuraEEisu]{.trn}  | [a]{.trn}  | [i]{.trn}  | [i]{.trn}  | [ئ]{.tradar} |
| [رُئِّسَ]{.tradar} [ruEEisa]{.trn}     | [u]{.trn}  | [i]{.trn}  | [i]{.trn}  | [ئ]{.tradar} |
| [تَفَؤُّل]{.tradar} [tafaEEul]{.trn}   | [a]{.trn}  | [u]{.trn}  | [u]{.trn}  | [ؤ]{.tradar} |
| [سَءَّال]{.tradar} [saEEAl]{.trn}     | [a]{.trn}  | [a]{.trn}  | [a]{.trn}  | [ء]{.tradar} (Using sub-rule.)|
| [لَءَّال]{.tradar} [laEEAl]{.trn}     | [a]{.trn}  | [a]{.trn}  | [a]{.trn}  | [ء]{.tradar} (Using sub-rule.)|

#### At the end of the word

When hamzah occurs at the end of a word, disregard the vowel on hamzah itself, and consider only the vowel on preceding consonant.
Plug it into the table as above, and determine to determine the seat of hamzah.

| Word | Vowel on consonant before hamzah | Seated hamzah |
|:-----|:-|:------|
| [دُعَاءُ]{.tradar} [dueAEu]{.trn}     | [A]{.trn}  | [ء]{.tradar} |
| [سُوءُ]{.tradar} [sUEu]{.trn}        | [U]{.trn}  | [ء]{.tradar} |
| [جِيءَ]{.tradar} [jIEa]{.trn}        | [I]{.trn}  | [ء]{.tradar} |
| [ضَوْءَ]{.tradar} [DawEa]{.trn}       | [aw]{.trn} | [ء]{.tradar} |
| [شَيْءَ]{.tradar} [cayEa]{.trn}       | [ay]{.trn} | [ء]{.tradar} |
| [بُطْءُ]{.tradar} [buTEu]{.trn}       | [◌ْ]{.tradar}   | [ء]{.tradar} |
| [عِبْءُ]{.tradar} [eibEu]{.trn}       | [◌ْ]{.tradar}   | [ء]{.tradar} |
| [شَطْءُ]{.tradar} [caTEu]{.trn}       | [◌ْ]{.tradar}   | [ء]{.tradar} |
| [يُهَدِّئُ]{.tradar} [yuhaddiEu]{.trn}  | [i]{.trn}  | [ئ]{.tradar} |
| [سَيِّئُ]{.tradar} [sayyiEu]{.trn}     | [i]{.trn}  | [ئ]{.tradar} |
| [بَطُؤَ]{.tradar} [baTuEa]{.trn}      | [u]{.trn}  | [ؤ]{.tradar} |
| [يَهْدَأُ]{.tradar} [yahdaEu]{.trn}    | [a]{.trn}  | [أ]{.tradar} |
| [مُبْتَدَإِ]{.tradar} [mubtadaEi]{.trn} | [a]{.trn}  | [إ]{.tradar} |

The exception to this rule is when the previous letter is a doubled [wAw]{.trn} with an [u]{.trn}-mark.
In this case the hamzah will again be unseated. Example [تَبَوُّءُ]{.tradar} [tabawwuEu]{.trn}.

Note also that [مُبْتَدَإِ]{.tradar} [mubtadaEi]{.trn} can be written with the hamzah below the [Ealif]{.trn} because of the [i]{.trn}-mark on the hamzah.
But it is also common to write it as [مُبْتَدَأ]{.tradar} [mubtadaE]{.trn}, especially when the hamzah is unvoweled.

### Prefixes and suffixes

#### Prefixes

If hamzah is in the beginning of a word, adding a prefix to the word will not alter the writing of the hamzah. Examples:  

+ [لِ + أُسْتَاذِ = لِأُسْتَاذِ]{.tradar}  
+ [الْ + آخِرَة = الْآخِرَة]{.tradar}

#### Suffixes

If hamzah is at the end of a word, adding a suffix to the word can, in general, alter the writing of the hamzah. 
Hamzah is now, generally, treated as if it is in the middle of the word, and the rules for hamzah in the middle of a word apply.
Examples:  

| Word | Vowel on consonant before hamzah | Shortened vowel on hamzah | Winning vowel | Seated hamzah |
|:-----|:-|:-|:-|:------|
| [بَرِيءُونَ]{.tradar} [barIEUna]{.trn}     | [I]{.trn}  | [u]{.trn} | [I]{.trn}   | [ء]{.tradar} |
| [بَرِيءَانِ]{.tradar} [barIEAni]{.trn}     | [I]{.trn}  | [a]{.trn} | [I]{.trn}   | [ء]{.tradar} |
| [بَرِيءِينَ]{.tradar} [barIEIna]{.trn}     | [I]{.trn}  | [i]{.trn} | [I]{.trn}   | [ء]{.tradar} |
| [بَرِيءَيْنِ]{.tradar} [barIEayni]{.trn}    | [I]{.trn}  | [a]{.trn} | [I]{.trn}   | [ء]{.tradar} |
| [شَيْءُهُ]{.tradar} [cayEuhu]{.trn}        | [ay]{.trn} | [u]{.trn} | [ay]{.trn}  | [ء]{.tradar} |
| [شَيْءَهُ]{.tradar} [cayEahu]{.trn}        | [ay]{.trn} | [a]{.trn} | [ay]{.trn}  | [ء]{.tradar} |
| [شَيْءِهِ]{.tradar} [cayEihi]{.trn}        | [ay]{.trn} | [i]{.trn} | [ay]{.trn}  | [ء]{.tradar} |
| [شَيْءَانِ]{.tradar} [cayEAni]{.trn}       | [ay]{.trn} | [a]{.trn} | [ay]{.trn}  | [ء]{.tradar} |
| [شَيْءَيْنِ]{.tradar} [cayEayni]{.trn}      | [ay]{.trn} | [a]{.trn} | [ay]{.trn}  | [ء]{.tradar} |
| [مَجِيءُهُ]{.tradar} [majIEuhu]{.trn}      | [I]{.trn}  | [u]{.trn} | [I]{.trn}   | [ء]{.tradar} |
| [مَجِيءَهُ]{.tradar} [majIEahu]{.trn}      | [I]{.trn}  | [a]{.trn} | [I]{.trn}   | [ء]{.tradar} |
| [مَجِيءِهِ]{.tradar} [majIEihi]{.trn}      | [I]{.trn}  | [i]{.trn} | [I]{.trn}   | [ء]{.tradar} |
| [سُوئِهِ]{.tradar} [sUEihi]{.trn}         | [U]{.trn}  | [i]{.trn} | [i]{.trn}   | [ئ]{.tradar} |
| [ضَوْئِهِ]{.tradar} [DawEihi]{.trn}        | [aw]{.trn} | [i]{.trn} | [i]{.trn}   | [ئ]{.tradar} |
| [سُوءَهُ]{.tradar} [sUEahu]{.trn}         | [U]{.trn}  | [a]{.trn} | [U]{.trn}   | [ء]{.tradar} |
| [سُوءَانِ]{.tradar} [sUEAni]{.trn}        | [U]{.trn}  | [a]{.trn} | [U]{.trn}   | [ء]{.tradar} |
| [ضَوْءَهُ]{.tradar} [DawEahu]{.trn}        | [aw]{.trn} | [a]{.trn} | [aw]{.trn}  | [ء]{.tradar} |
| [ضَوْءَانِ]{.tradar} [DawEAni]{.trn}       | [aw]{.trn} | [a]{.trn} | [aw]{.trn}  | [ء]{.tradar} |
| [سُوءُهُ]{.tradar} [sUEuhu]{.trn}         | [U]{.trn}  | [u]{.trn} | [U]{.trn}   | [ء]{.tradar} |
| [يَسُوءُونَ]{.tradar} [yasUEUna]{.trn}     | [U]{.trn}  | [u]{.trn} | [U]{.trn}   | [ء]{.tradar} |
| [نُوآنٌ]{.tradar} [nUEAnun]{.trn}.       | [U]{.trn}  | [a]{.trn} | [U]{.trn}   | [ء]{.tradar} |
| [مُتَّكِئِينَ]{.tradar} [muttakiEIna]{.trn}  | [i]{.trn}  | [i]{.trn} | [i]{.trn}   | [ئ]{.tradar} |
| [يُبَرِّئُونَ]{.tradar} [yubarriEUna]{.trn}  | [i]{.trn}  | [u]{.trn} | [i]{.trn}   | [ئ]{.tradar} |
| [يُبَرَّؤُونَ]{.tradar} [yubarraEUna]{.trn}  | [a]{.trn}  | [u]{.trn} | [u]{.trn}   | [ؤ]{.tradar} |

There are some exceptions:

If the letter before the hamzah has a [sukUn]{.trn} and is not [wAw]{.trn} or [yAE]{.trn},
then the hamzah will be written unseated. Examples:

+  [جُزْءَانِ]{.tradar} [juzEAni]{.trn}  
+  [عِبْءَانِ]{.tradar} [eibEAni]{.trn}  
+  [عِبْءَيْنِ]{.tradar} [eibEayni]{.trn}  
+  [بُطْءَهُ]{.tradar} [buTEahu]{.trn}  
+  [بُطْءُهُ]{.tradar} [buTEuhu]{.trn}  
+  [بُطْءِهِ]{.tradar} [buTEihi]{.trn}

([انِ]{.tradar}, [يْنِ]{.tradar}, [هُ]{.tradar}, and [هِ]{.tradar} are suffixes.)

### [n]{.trn}-marks on final hamzah

[n]{.trn}-marks on a final hamzah does not affect the writing of the hamzah except in the case of [an]{.trn}-mark. When writing [an]{.trn}-mark on a hamzah at the end of a word:

1. If there is an [Ealif]{.trn} before a unseated hamzah [اء]{.tradar}, then we don't add a silent [Ealif]{.trn} when writing [an]{.trn}-mark. For example [دَاء]{.tradar} becomes [دَاءً]{.tradar} [dAEan]{.trn}, not [دَاءًا]{.tradar}.

2. Otherwise, we add the silent [Ealif]{.trn} after the hamzah so that the hamzah is now in the middle of the word with a suffix [Ealif]{.trn} after it. We now pretend that the hamzah has an [a]{.trn}-mark and that the [Ealif]{.trn} after it is a long-[A]{.trn} vowel. Then we go through the rules for writing hamzah in the middle of a word (given above) to determine how hamzah will be written. We then write the [an]{.trn}-mark on the hamzah. Examples:

+ [مُبْتَدَأ]{.tradar} becomes [مُبْتَدَأٌ، مُبْتَدَءًا، مُبْتَدَإٍ]{.tradar} 
+ [مَلْجَأ]{.tradar} becomes [مَلْجَأٌ، مَلْجَءًا، مَلْجَإٍ]{.tradar}
+ [جُزْء]{.tradar} becomes [جُزْءٌ، جُزْءًا، جُزْءٍ]{.tradar}
+ [شَيْء]{.tradar} becomes [شَيْءٌ، شَيْءًا، شَيْءٍ]{.tradar}

### Variants

There are some historical and regional variants to the above rules. The main one is a variant of rule 2.b.ii above. In this variant, when the letter before hamzah has a [sukUn]{.trn}, the hamzah is generally written unseated. So they write:

+ [مَسْءُول]{.tradar} instead of [مَسْؤُول]{.tradar}
+ [أَسْءِلَة]{.tradar} instead of [أَسْئِلَة]{.tradar}
+ [مَسْءَلَة]{.tradar} instead of [مَسْأَلَة]{.tradar}

However, this rule appears to be not consistently followed. For example, [al-nacEah]{.trn} is generally always written [النَّشْأَة]{.tradar} never [النَّشْءَة]{.tradar}.

A second variant is to avoid the repetition of vowel letters like [و]{.tradar} and [ي]{.tradar}. So they write:

+ [رُءُوس]{.tradar} instead of [رُؤُوس]{.tradar}.
+ [رَءِيس]{.tradar} instead of [رَئِيس]{.tradar}.


<!--chapter:end:srcrmd/hamzarules.Rmd-->

