"""Build one self-contained ZIP per paper, with the common method library."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT=Path(__file__).resolve().parents[1]
VERSION='1.0.0'


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=Path,default=ROOT/'dist')
    args=p.parse_args();args.output.mkdir(parents=True,exist_ok=True)
    common=[ROOT/n for n in ['pyproject.toml','requirements-repro.txt','LICENSE','DATA_LICENSES.md','CITATION.md','SOURCE_PROVENANCE.json','VERIFICATION.json']]
    common+=list((ROOT/'src').rglob('*.py'))+list((ROOT/'tests').glob('*.py'))
    records=[]
    for paper in sorted((ROOT/'papers').iterdir()):
        if not paper.is_dir():continue
        files=common+[f for f in paper.rglob('*') if f.is_file() and '__pycache__' not in f.parts]
        if paper.name.startswith('01') and not (paper/'data/msc_sessions123.npz').exists():
            raise FileNotFoundError('The complete paper-01 release needs the MSC asset; see README.')
        destination=args.output/f'{paper.name}-v{VERSION}.zip'
        rootname=f'{paper.name}-v{VERSION}'
        readme=f'''# {paper.name}: version {VERSION}

This download contains the shared method library and the files for one paper.
The paper-specific instructions are in [papers/{paper.name}/README.md](papers/{paper.name}/README.md).

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-repro.txt
python -m pip install --no-deps -e .
python papers/{paper.name}/run.py --output results/example.json
python -m unittest discover -s tests -v
```

The complete code repository and the other four packages are at
https://github.com/cornada/fmri-observation-benchmarks/releases/tag/v{VERSION}.
See LICENSE, DATA_LICENSES.md and CITATION.md for reuse and attribution.
'''
        with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
            for f in sorted(set(files)):
                z.write(f,rootname+'/'+str(f.relative_to(ROOT)))
            z.writestr(rootname+'/README.md',readme)
        records.append({'paper':paper.name,'asset':destination.name,'bytes':destination.stat().st_size,
                        'sha256':hashlib.sha256(destination.read_bytes()).hexdigest()})
    (args.output/'packages.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps(records,indent=2))


if __name__=='__main__':main()
