# classifier_language_recognition


The purpose of creating and using this model
Diagnosis was Arabic and Persian, but tested for 6 languages:

arabic   persian    spanish      italian      french       english 


Arabic can be written in different ways
One of the problems we had was that if the Arabic text was written with a Persian keyboard, the Persian text would be recognized and categorized in the Persian language group.

What was done:
  I did a pre-processing on a body with about 2000 sentences and it made all the Arabic characters convert to Persian but the meaning of the sentence was preserved.
  We taught the model on different models of Arabic language
As a result, the output works better in recognizing the Arabic language. 

for example : 

الا تری انه بعد السبی قبل العتق کان الحکم هکذا فلا یزداد بالعتق الا وکاده  ثم رجع یعقوب عن هذا وقال  یعقل عنه همدان وهو قول محمد رحمه الله تعالی  لان المعتقه لما سبیت فاعتقت صارت منسوبه بالولاء الی قبیله معتقها  فکذلک معتقها یکون منسوبا الیهم بواسطتها  وهذا لان ولاء العتق فی الحکم اقوی من النسب


or : 


( قَوْلُهُ : وَقَدْ جَزَمَ ) إلَى قَوْلِهِ قَالَ الْأَذْرَعِيُّ : عِبَارَةُ النِّهَايَةِ وَمَا ذَكَرَاهُ فِي مَوْضِعٍ مِنْ حُرْمَتِهِ مَحْمُولٌ عَلَى لَوْ كَانَ مِنْ أَمْرَدَ أَوْ أَجْنَبِيَّةٍ وَخَافَ مِنْ ذَلِكَ فِتْنَةً 
