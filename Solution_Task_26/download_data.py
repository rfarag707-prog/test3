"""Download the course data for local analysis; do not commit raw IMDb files."""
from pathlib import Path
from urllib.request import urlopen, Request
import shutil, zipfile
ROOT=Path(__file__).resolve().parent
sources={
 'facebook':('masoodanzar/facebook-metrics',None),
 'telco':('blastchar/telco-customer-churn',None),
 'imdb':('ashirwadsangwan/imdb-dataset',['title.basics.tsv','title.ratings.tsv'])}
for name,(dataset,files) in sources.items():
 folder=ROOT/'data'/name; folder.mkdir(parents=True,exist_ok=True)
 if name=='imdb' and list(folder.glob('title.basics.part*.tsv.gz')) and (folder/'title.ratings.tsv.gz').exists():
  print('IMDb included data already present'); continue
 if name!='imdb' and list(folder.glob('*.csv')):
  print(name, 'CSV already present'); continue
 for filename in (files or ['dataset.zip']):
  dest=folder/filename
  if dest.exists():print('Already present:',dest);continue
  url='https://www.kaggle.com/api/v1/datasets/download/'+dataset+('/'+filename if files else '')
  print('Downloading',name,filename,'(IMDb metadata is over 1 GB)')
  partial=dest.with_suffix(dest.suffix+'.partial')
  with urlopen(Request(url,headers={'User-Agent':'Session26 educational analysis'}),timeout=120) as source, partial.open('wb') as target:
   shutil.copyfileobj(source,target)
  partial.replace(dest)
  if not files:
   with zipfile.ZipFile(dest) as archive:
    for member in archive.infolist():
     if member.filename.lower().endswith('.csv'):
      with archive.open(member) as source,(folder/Path(member.filename).name).open('wb') as target:shutil.copyfileobj(source,target)
   dest.unlink()
print('Done. Open notebooks and Run All. Source snapshots can change; see provenance.json for the version analyzed in the saved outputs.')
