---
title: "Learn Standard Arabic"
subtitle:  "A self-instruction textbook with grammar, vocabulary, and exercises"
author: "Author Names"
date: "v0.1.0-738-g3538b25"
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

# (APPENDIX) Appendix {-}


<!--chapter:end:srcrmd/appendix.Rmd-->

# Rules for writing hamzah {#hamzarules}

## Seats of hamzah

Hamzah is written in four different ways:

1. Seated on an [Ealif]{.trn}: [أ]{.ar} or [إ]{.ar}
2. Seated on an [wAw]{.trn}: [ؤ]{.ar}
3. Seated on an [yAE]{.trn}: [ئ]{.ar}
4. Unseated: [ء]{.ar}

Here are some of notes about writing hamzah in the above four methods:

+ When unseated hamzah comes between two letters that are joined, then it is written above the line that joins them, for example: [خَطِيءَة]{.ar} [xaTIEah]{.trn}. In this word, the [yAE]{.trn} [ي]{.ar} joins to the [tAE marbUTah]{.trn} [ة]{.ar}.

+ When unseated hamzah is followed by an [Ealif]{.trn}: [ءا]{.ar},  the combination of hamzah and [Ealif]{.trn} is usually written as [آ]{.ar} as a convention. Examples: [آمَنَ]{.ar} [EAmana]{.trn}, [ظَمْآن]{.ar} [PamEAn]{.trn}, [شَنَآن]{.ar} [canaEAn]{.trn}. However, when the [Ealif]{.trn} is a suffix or part of a suffix, or the hamzah is doubled, or there is an [Ealif]{.trn} before the hamzah then we will write [ءا]{.ar}, not [آ]{.ar}. Examples: [شَيْءَانِ]{.ar} [cayEAni]{.trn}, [سَءَّال]{.ar} [saEEAl]{.trn}, [قِرَاءَات]{.ar} [qirAEAt]{.trn}. 

+ When hamzah is seated on [Ealif]{.trn}, if it has an [kasrah]{.trn}, it is written below the [Ealif]{.trn}: [إِ]{.ar}. Otherwise, it is written above the [Ealif]{.trn}: [أَ]{.ar}, [أُ]{.ar}, [أْ]{.ar}.

+ When hamzah is seated on [yAE]{.trn} [ئ]{.ar} the dots of the [yAE]{.trn} are no longer written. Here's how it will appear in different positions:

  Isolated | End | Middle | Beginnning
  :--------|:----|:-------|:----------
  [ئ]{.ar}| [ـئ]{.ar}| [ـئـ]{.ar}| [ئـ]{.ar}

  Note that hamzah is seated on [yAE]{.trn} in the middle position [ـئـ]{.ar} is different from unseated hamzah between two joining letters [ـءـ]{.ar}.

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

a. If the hamzah carries a long-[A]{.trn} vowel, it is written unseated followed by an [Ealif]{.trn} and written as [آ]{.ar}, for example [آمَنَ]{.ar} [EAmana]{.trn}.
b. If the hamzah carries any other vowel, it is written seated on an [Ealif]{.trn}, and is marked with the appropriated vowel mark, for example [أَسْلَمَ]{.ar} [Easlama]{.trn}, [أُرِيدُ]{.ar} [EurIdu]{.trn}, [إِسْلَام]{.ar} [EislAm]{.trn}, [إِيمَان]{.ar} [EImAn]{.trn}, [أُوخِذَ]{.ar} [EUxipa]{.trn}. 

#### In the middle of the word

The most general case is when hamzah is in the middle of a word. 

Arabic has three short vowels, three long vowels, two diphthongs, and a [sukUn]{.trn}. Each of these has an order of precedence and a hamzah seat.

Precedence | Vowel | Seat 
:--|:------|:--------|:------
1. | [I]{.trn}/[ay]{.trn} | [ء]{.ar}
2. | [i]{.trn}            | [ئ]{.ar}
3. | [U]{.trn}/[aw]{.trn} | [ء]{.ar}
4. | [u]{.trn}            | [ؤ]{.ar}
5. | [A]{.trn}            | [ء]{.ar}
6. | [a]{.trn}            | [أ]{.ar}
7. | [◌ْ]{.ar}             | [ء]{.ar}

**Main rule:** Disregard any doubling mark [◌ّ]{.ar} and consider the vowel on the consonant before the hamzah and the _shortened_ vowel on the hamzah itself. Determine which of the two vowels wins by being higher in precedence in the above table. The winning vowel's seat will be the seat of the hamzah.

**Sub-rule:** If the main rule determines that hamzah is to be seated on [Ealif]{.trn}, and there is a long [A]{.trn} vowel on the hamzah using an [Ealif]{.trn}, then hamzah shall be unseated. And the combination of [ءَا]{.ar} will usually be written as [آ]{.ar}.

Examples:

| Word | Vowel on consonant before hamzah | Shortened vowel on hamzah | Winning vowel | Seated hamzah |
|:-----|:-|:-|:-|:------|
| [هَيْءَة]{.ar} [hayEah]{.trn}     | [ay]{.trn} | [a]{.trn}  | [ay]{.trn} | [ء]{.ar} |
| [خَطِيءَة]{.tradar} [xaTIEah]{.trn}   | [I]{.trn}  | [a]{.trn}  | [I]{.trn}  | [ء]{.ar} |
| [اسْتِيءَاس]{.ar} [EistIEAs]{.trn}| [I]{.trn}  | [a]{.trn}  | [I]{.trn}  | [ء]{.ar} (Exception: [ءَا]{.ar} is not written as [آ]{.ar} when the preceding vowel is [I]{.trn}.)|
| [تَوْءَم]{.ar} [tawEam]{.trn}     | [aw]{.trn} | [a]{.trn}  | [aw]{.trn} | [ء]{.ar} |
| [سَائِل]{.ar} [sAEil]{.trn}      | [A]{.trn}  | [i]{.trn}  | [i]{.trn}  | [ئ]{.ar} |
| [تَسَاؤُل]{.ar} [tasAEul]{.trn}   | [A]{.trn}  | [u]{.trn}  | [u]{.trn}  | [ؤ]{.ar} |
| [تَسَاءَلَ]{.ar} [tasAEala]{.trn}  | [A]{.trn}  | [a]{.trn}  | [A]{.trn}  | [ء]{.ar} |
| [قِرَاءَات]{.ar} [qirAEAt]{.trn}  | [A]{.trn}  | [a]{.trn}  | [A]{.trn}  | [ء]{.ar} |
| [مَسْؤُول]{.ar} [masEUl]{.trn}    | [◌ْ]{.ar}   | [u]{.trn}  | [u]{.trn}  | [ؤ]{.ar} |
| [تَرْئِيس]{.ar} [tarEIs]{.trn}    | [◌ْ]{.ar}   | [i]{.trn}  | [i]{.trn}  | [ئ]{.ar} |
| [مِرْآة]{.ar} [mirEAh]{.trn}     | [◌ْ]{.ar}   | [a]{.trn}  | [a]{.trn}  | [ء]{.ar} (Using sub-rule.)|
| [ظَمْآن]{.ar} [PamEAn]{.trn}     | [◌ْ]{.ar}   | [a]{.trn}  | [a]{.trn}  | [ء]{.ar} (Using sub-rule.)|
| [مَسْأَلَة]{.ar} [masEalah]{.trn}  | [◌ْ]{.ar}   | [a]{.trn}  | [a]{.trn}  | [أ]{.ar} |
| [الْمَرْأَة]{.ar} [almarEah]{.trn} | [◌ْ]{.ar}   | [a]{.trn}  | [a]{.trn}  | [أ]{.ar} |
| [بِئْسَ]{.ar} [biEsa]{.trn}       | [i]{.trn}  | [◌ْ]{.ar}   | [i]{.trn}  | [ئ]{.ar} |
| [سُؤْلَكَ]{.ar} [suElaka]{.trn}    | [u]{.trn}  | [◌ْ]{.ar}   | [u]{.trn}  | [ؤ]{.ar} |
| [كَأْس]{.ar} [kaEs]{.trn}        | [a]{.trn}  | [◌ْ]{.ar}   | [a]{.trn}  | [أ]{.ar} |
| [سُئِلَ]{.ar} [suEila]{.trn}      | [u]{.trn}  | [i]{.trn}  | [i]{.trn}  | [ئ]{.ar} |
| [يَئِسَ]{.ar} [yaEisa]{.trn}      | [a]{.trn}  | [i]{.trn}  | [i]{.trn}  | [ئ]{.ar} |
| [رَئِيس]{.ar} [raEIs]{.trn}      | [a]{.trn}  | [i]{.trn}  | [i]{.trn}  | [ئ]{.ar} |
| [سُؤَال]{.ar} [suEAl]{.trn}      | [u]{.trn}  | [a]{.trn}  | [u]{.trn}  | [ؤ]{.ar} |
| [رُؤُوس]{.ar} [ruEUs]{.trn}      | [u]{.trn}  | [u]{.trn}  | [u]{.trn}  | [ؤ]{.ar} |
| [لُؤَيّ]{.ar} [luEayy]{.trn}      | [u]{.trn}  | [a]{.trn}  | [u]{.trn}  | [ؤ]{.ar} |
| [شَنَآن]{.ar} [canaEAn]{.trn}    | [a]{.trn}  | [a]{.trn}  | [a]{.trn}  | [ء]{.ar} (Using sub-rule.)|
| [سَأَلَ]{.ar} [saEala]{.trn}      | [a]{.trn}  | [a]{.trn}  | [a]{.trn}  | [أ]{.ar} |
| [رَأَىٰ]{.ar} [raEA]{.trn}        | [a]{.trn}  | [a]{.trn}  | [a]{.trn}  | [أ]{.ar} |
| [رَأَّسَ]{.ar} [raEEasa]{.trn}     | [a]{.trn}  | [a]{.trn}  | [a]{.trn}  | [أ]{.ar} |
| [يُرَئِّسُ]{.ar} [yuraEEisu]{.trn}  | [a]{.trn}  | [i]{.trn}  | [i]{.trn}  | [ئ]{.ar} |
| [رُئِّسَ]{.ar} [ruEEisa]{.trn}     | [u]{.trn}  | [i]{.trn}  | [i]{.trn}  | [ئ]{.ar} |
| [تَفَؤُّل]{.ar} [tafaEEul]{.trn}   | [a]{.trn}  | [u]{.trn}  | [u]{.trn}  | [ؤ]{.ar} |
| [سَءَّال]{.ar} [saEEAl]{.trn}     | [a]{.trn}  | [a]{.trn}  | [a]{.trn}  | [ء]{.ar} (Using sub-rule.)|
| [لَءَّال]{.ar} [laEEAl]{.trn}     | [a]{.trn}  | [a]{.trn}  | [a]{.trn}  | [ء]{.ar} (Using sub-rule.)|

#### At the end of the word

When hamzah occurs at the end of a word, disregard the vowel on hamzah itself, and consider only the vowel on preceding consonant.
Plug it into the table as above, and determine to determine the seat of hamzah.

| Word | Vowel on consonant before hamzah | Seated hamzah |
|:-----|:-|:------|
| [دُعَاءُ]{.ar} [dueAEu]{.trn}     | [A]{.trn}  | [ء]{.ar} |
| [سُوءُ]{.ar} [sUEu]{.trn}        | [U]{.trn}  | [ء]{.ar} |
| [جِيءَ]{.ar} [jIEa]{.trn}        | [I]{.trn}  | [ء]{.ar} |
| [ضَوْءَ]{.ar} [DawEa]{.trn}       | [aw]{.trn} | [ء]{.ar} |
| [شَيْءَ]{.ar} [cayEa]{.trn}       | [ay]{.trn} | [ء]{.ar} |
| [بُطْءُ]{.ar} [buTEu]{.trn}       | [◌ْ]{.ar}   | [ء]{.ar} |
| [عِبْءُ]{.ar} [eibEu]{.trn}       | [◌ْ]{.ar}   | [ء]{.ar} |
| [شَطْءُ]{.ar} [caTEu]{.trn}       | [◌ْ]{.ar}   | [ء]{.ar} |
| [يُهَدِّئُ]{.ar} [yuhaddiEu]{.trn}  | [i]{.trn}  | [ئ]{.ar} |
| [سَيِّئُ]{.ar} [sayyiEu]{.trn}     | [i]{.trn}  | [ئ]{.ar} |
| [بَطُؤَ]{.ar} [baTuEa]{.trn}      | [u]{.trn}  | [ؤ]{.ar} |
| [يَهْدَأُ]{.ar} [yahdaEu]{.trn}    | [a]{.trn}  | [أ]{.ar} |
| [مُبْتَدَإِ]{.ar} [mubtadaEi]{.trn} | [a]{.trn}  | [إ]{.ar} |

The exception to this rule is when the previous letter is a doubled [wAw]{.trn} with an [Dammah]{.trn}.
In this case the hamzah will again be unseated. Example [تَبَوُّءُ]{.ar} [tabawwuEu]{.trn}.

Note also that [مُبْتَدَإِ]{.ar} [mubtadaEi]{.trn} can be written with the hamzah below the [Ealif]{.trn} because of the [i]{.trn}-mark on the hamzah.
But it is also common to write it as [مُبْتَدَأ]{.ar} [mubtadaE]{.trn}, especially when the hamzah is unvoweled.

### Prefixes and suffixes

#### Prefixes

If hamzah is in the beginning of a word, adding a prefix to the word will not alter the writing of the hamzah. Examples:  

+ [لِ + أُسْتَاذِ = لِأُسْتَاذِ]{.ar}  
+ [الْ + آخِرَة = الْآخِرَة]{.ar}

#### Suffixes

If hamzah is at the end of a word, adding a suffix to the word can, in general, alter the writing of the hamzah. 
Hamzah is now, generally, treated as if it is in the middle of the word, and the rules for hamzah in the middle of a word apply.
Examples:  

| Word | Vowel on consonant before hamzah | Shortened vowel on hamzah | Winning vowel | Seated hamzah |
|:-----|:-|:-|:-|:------|
| [بَرِيءُونَ]{.ar} [barIEUna]{.trn}     | [I]{.trn}  | [u]{.trn} | [I]{.trn}   | [ء]{.trn} |
| [بَرِيءَانِ]{.ar} [barIEAni]{.trn}     | [I]{.trn}  | [a]{.trn} | [I]{.trn}   | [ء]{.trn} |
| [بَرِيءِينَ]{.ar} [barIEIna]{.trn}     | [I]{.trn}  | [i]{.trn} | [I]{.trn}   | [ء]{.trn} |
| [بَرِيءَيْنِ]{.ar} [barIEayni]{.trn}    | [I]{.trn}  | [a]{.trn} | [I]{.trn}   | [ء]{.trn} |
| [شَيْءُهُ]{.ar} [cayEuhu]{.trn}        | [ay]{.trn} | [u]{.trn} | [ay]{.trn}  | [ء]{.trn} |
| [شَيْءَهُ]{.ar} [cayEahu]{.trn}        | [ay]{.trn} | [a]{.trn} | [ay]{.trn}  | [ء]{.trn} |
| [شَيْءِهِ]{.ar} [cayEihi]{.trn}        | [ay]{.trn} | [i]{.trn} | [ay]{.trn}  | [ء]{.trn} |
| [شَيْءَانِ]{.ar} [cayEAni]{.trn}       | [ay]{.trn} | [a]{.trn} | [ay]{.trn}  | [ء]{.trn} |
| [شَيْءَيْنِ]{.ar} [cayEayni]{.trn}      | [ay]{.trn} | [a]{.trn} | [ay]{.trn}  | [ء]{.trn} |
| [مَجِيءُهُ]{.ar} [majIEuhu]{.trn}      | [I]{.trn}  | [u]{.trn} | [I]{.trn}   | [ء]{.trn} |
| [مَجِيءَهُ]{.ar} [majIEahu]{.trn}      | [I]{.trn}  | [a]{.trn} | [I]{.trn}   | [ء]{.trn} |
| [مَجِيءِهِ]{.ar} [majIEihi]{.trn}      | [I]{.trn}  | [i]{.trn} | [I]{.trn}   | [ء]{.trn} |
| [سُوئِهِ]{.ar} [sUEihi]{.trn}         | [U]{.trn}  | [i]{.trn} | [i]{.trn}   | [ئ]{.trn} |
| [ضَوْئِهِ]{.ar} [DawEihi]{.trn}        | [aw]{.trn} | [i]{.trn} | [i]{.trn}   | [ئ]{.trn} |
| [سُوءَهُ]{.ar} [sUEahu]{.trn}         | [U]{.trn}  | [a]{.trn} | [U]{.trn}   | [ء]{.trn} |
| [سُوءَانِ]{.ar} [sUEAni]{.trn}        | [U]{.trn}  | [a]{.trn} | [U]{.trn}   | [ء]{.trn} |
| [ضَوْءَهُ]{.ar} [DawEahu]{.trn}        | [aw]{.trn} | [a]{.trn} | [aw]{.trn}  | [ء]{.trn} |
| [ضَوْءَانِ]{.ar} [DawEAni]{.trn}       | [aw]{.trn} | [a]{.trn} | [aw]{.trn}  | [ء]{.trn} |
| [سُوءُهُ]{.ar} [sUEuhu]{.trn}         | [U]{.trn}  | [u]{.trn} | [U]{.trn}   | [ء]{.trn} |
| [يَسُوءُونَ]{.ar} [yasUEUna]{.trn}     | [U]{.trn}  | [u]{.trn} | [U]{.trn}   | [ء]{.trn} |
| [نُوآنٌ]{.ar} [nUEAnun]{.trn}.       | [U]{.trn}  | [a]{.trn} | [U]{.trn}   | [ء]{.trn} |
| [مُتَّكِئِينَ]{.ar} [muttakiEIna]{.trn}  | [i]{.trn}  | [i]{.trn} | [i]{.trn}   | [ئ]{.trn} |
| [يُبَرِّئُونَ]{.ar} [yubarriEUna]{.trn}  | [i]{.trn}  | [u]{.trn} | [i]{.trn}   | [ئ]{.trn} |
| [يُبَرَّؤُونَ]{.ar} [yubarraEUna]{.trn}  | [a]{.trn}  | [u]{.trn} | [u]{.trn}   | [ؤ]{.trn} |

There are some exceptions:

If the letter before the hamzah has a [sukUn]{.trn} and is not [wAw]{.trn} or [yAE]{.trn},
then the hamzah will be written unseated. Examples:

+  [جُزْءَانِ]{.ar} [juzEAni]{.trn}  
+  [عِبْءَانِ]{.ar} [eibEAni]{.trn}  
+  [عِبْءَيْنِ]{.ar} [eibEayni]{.trn}  
+  [بُطْءَهُ]{.ar} [buTEahu]{.trn}  
+  [بُطْءُهُ]{.ar} [buTEuhu]{.trn}  
+  [بُطْءِهِ]{.ar} [buTEihi]{.trn}

([انِ]{.ar}, [يْنِ]{.ar}, [هُ]{.ar}, and [هِ]{.ar} are suffixes.)

### [tanwIn]{.trn} on final hamzah

[tanwIn]{.trn} on a final hamzah does not affect the writing of the hamzah except in the case of [tanwIn al-fatH]{.trn}. When writing [tanwIn al-fatH]{.trn} on a hamzah at the end of a word:

1. If there is an [Ealif]{.trn} before a unseated hamzah [اء]{.ar}, then we don't add a silent [Ealif]{.trn} when writing [tanwIn al-fatH]{.trn}. For example [دَاء]{.ar} becomes [دَاءً]{.ar} [dAEan]{.trn}, not [دَاءًا]{.ar}.

2. Otherwise, we add the silent [Ealif]{.trn} after the hamzah so that the hamzah is now in the middle of the word with a suffix [Ealif]{.trn} after it. We now pretend that the hamzah has an [fatHah]{.trn} and that the [Ealif]{.trn} after it is a long-[A]{.trn} vowel. Then we go through the rules for writing hamzah in the middle of a word (given above) to determine how hamzah will be written. We then write the [an]{.trn}-mark on the hamzah. Examples:

+ [مُبْتَدَأ]{.ar} becomes [مُبْتَدَأٌ، مُبْتَدَءًا، مُبْتَدَإٍ]{.ar} 
+ [مَلْجَأ]{.ar} becomes [مَلْجَأٌ، مَلْجَءًا، مَلْجَإٍ]{.ar}
+ [جُزْء]{.ar} becomes [جُزْءٌ، جُزْءًا، جُزْءٍ]{.ar}
+ [شَيْء]{.ar} becomes [شَيْءٌ، شَيْءًا، شَيْءٍ]{.ar}

### Variants

There are some historical and regional variants to the above rules. The main one is a variant of rule 2.b.ii above. In this variant, when the letter before hamzah has a [sukUn]{.trn}, the hamzah is generally written unseated. So they write:

+ [مَسْءُول]{.ar} instead of [مَسْؤُول]{.ar}
+ [أَسْءِلَة]{.ar} instead of [أَسْئِلَة]{.ar}
+ [مَسْءَلَة]{.ar} instead of [مَسْأَلَة]{.ar}

However, this rule appears to be not consistently followed. For example, [al-nacEah]{.trn} is generally always written [النَّشْأَة]{.ar} never [النَّشْءَة]{.ar}.

A second variant is to avoid the repetition of vowel letters like [و]{.ar} and [ي]{.ar}. So they write:

+ [رُءُوس]{.ar} instead of [رُؤُوس]{.ar}.
+ [رَءِيس]{.ar} instead of [رَئِيس]{.ar}.


<!--chapter:end:srcrmd/hamzarules.Rmd-->

