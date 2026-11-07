# Solution Task 25

المشروعان مكتملان بالتحليل والرسوم والتقرير، باستخدام بيانات روابط التاسك الأصلية.

## محتويات كل مجلد
- `Analysis.ipynb`: نوت بوك بالشرح المختصر والكود والنتائج الفعلية والرسوم.
- `Report.pdf`: تقرير إنجليزي من 3 صفحات يلخص النتائج وحدودها.
- `data/`: نسخة الداتا المستخدمة؛ لا تحتاج تنزيلها مرة أخرى.
- `figures/`: الرسوم بجودة مناسبة للاستخدام.
- `summary.json`: الأرقام الرئيسية الناتجة عن التشغيل.

## التشغيل
1. فك ضغط ZIP بالكامل، مع الحفاظ على ترتيب المجلدات.
2. افتح `Analysis.ipynb` داخل مجلد المشروع المطلوب في VS Code أو Jupyter.
3. ثبّت المكتبات بالأمر `python -m pip install -r requirements.txt` من المجلد الرئيسي.
4. اختار Python kernel واضغط Run All. لو غيّرت مكان الداتا، عدّل `DATA_PATH` في أول خلية.

النتائج محفوظة داخل النوت بوك ويمكن قراءتها بدون إعادة تشغيل. إعادة التشغيل تُحدّث الرسوم وsummary.json؛ تقارير PDF المرفقة ثابتة وتخص البيانات الحالية، ولا تتجدد تلقائيًا عند تغيير الداتا.

## نطاق التحليل
- الألعاب: استخدمنا الملف الأساسي المؤرخ 22 ديسمبر 2016، ولم ندمج ملفات PS4 وXbox الإضافية لتجنب تداخل التغطية. المبيعات بالمليون نسخة وليست أرباحًا.
- Netflix: آخر تاريخ إضافة في البيانات 25 سبتمبر 2021. البيانات لا تمثل الكتالوج الحالي ولا تتضمن المشاهدات أو التكلفة.
- لم تُختلق نتائج، ولم يُملأ المجهول بتقديرات بلا أساس. قرارات التنظيف موثقة في النوت بوك والتقرير.

## Sources
- https://www.kaggle.com/datasets/sidtwr/videogames-sales-dataset
- https://www.kaggle.com/datasets/shivamb/netflix-shows

Retrieved 2026-11-05. `provenance.json` records SHA-256 hashes and the package versions used for this run.

## Validation
Both notebooks executed all code cells without errors. Assertions check row counts, keys, cleaned values and aggregate totals. Both reports were rendered and visually reviewed. Review the analysis before submitting it and be ready to explain the cleaning decisions.
