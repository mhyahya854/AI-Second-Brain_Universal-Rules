"""Baseline-to-candidate preservation checks; exact normalized content, not semantic proof."""
from pathlib import Path
import collections, difflib, hashlib, json, re, subprocess, urllib.parse

root = Path('/workspace/work/integration')
work = root.parent
commit = 'a9c597c8f14536a4404a64494cf56e9015e1288a'
base = subprocess.check_output(['git', 'show', commit + ':UNIVERSL RULES FOR ALL APPS.md'], cwd=root).decode()
new = (root / 'MASTER_PLAN.md').read_text()
errors=[]
def check(ok, note):
    if not ok: errors.append(note)
def rules(s):
    return {m[1]:(m[2],m[3].strip()) for m in re.finditer(r'^### (?:\d+\.\d+\. )?([A-Z]+-\d+) — ([^\n]+)\n(.*?)(?=\n<a id=|\Z)',s,re.M|re.S)}
def normalize_old_links(s):
    def convert(m):
        path=m[2]
        if path.startswith(('#','https:','http:','mailto:')):return m[0]
        name,sep,frag=path.partition('#')
        return '['+m[1]+'](https://github.com/mhyahya854/Universal-Rules/blob/'+commit+'/'+urllib.parse.quote(urllib.parse.unquote(name),safe='/')+(('#'+frag) if sep else '')+')'
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',convert,s)
old=rules(base); current=rules(new)
changed=set(json.loads((work/'integration-changed-rules.json').read_text()))
actual_changed=[]
diffs=[]
for rid,(title,body) in old.items():
    check(rid in current,'Missing '+rid)
    if rid not in current:continue
    check(current[rid][0]==title,'Title changed '+rid)
    before=normalize_old_links(body)
    if before!=current[rid][1]:
        actual_changed.append(rid)
        diffs.extend(difflib.unified_diff((before+'\n').splitlines(True),(current[rid][1]+'\n').splitlines(True),fromfile=rid+' baseline',tofile=rid+' candidate'))
    check(re.search(r'\*\*Type:\*\*[^\n]+',body)[0]==re.search(r'\*\*Type:\*\*[^\n]+',current[rid][1])[0],'Metadata changed '+rid)
check(set(actual_changed)==changed,'Change ledger mismatch')
check(len(old)==113 and len(current)==137 and len(set(current)-set(old))==24,'Counts mismatch')
skill_old=normalize_old_links(old['SKILL-4'][1]); skill_new=current['SKILL-4'][1]
check(skill_old==skill_new,'Skill catalog differs')
# All explicit old anchors except the replaced historical status anchor remain.
old_anchors=set(re.findall(r'<a id="([^"]+)"></a>',base))
new_anchors=set(re.findall(r'<a id="([^"]+)"></a>',new))
check(old_anchors<=new_anchors,'Original anchors lost '+str(old_anchors-new_anchors))
# Every former tree file is linked immutably, with the linked object locally present.
paths=subprocess.check_output(['git','ls-tree','-r','--name-only',commit],cwd=root).decode().splitlines()
for path in paths:
    url='https://github.com/mhyahya854/Universal-Rules/blob/'+commit+'/'+urllib.parse.quote(path,safe='/')
    check(url in new,'Missing former file preservation link '+path)
historical=[]
for rev,path in re.findall(r'https://github.com/mhyahya854/Universal-Rules/blob/([a-f0-9]{40})/([^\s)#]+)',new):
    actual=urllib.parse.unquote(path)
    result=subprocess.run(['git','cat-file','-e',rev+':'+actual],cwd=root,capture_output=True)
    check(result.returncode==0,'Historical object not recoverable '+rev+':'+actual)
    historical.append((rev,actual))
# Independently check numbered subphase fields and mandatory topic list shape.
execbody=current['EXEC-2'][1]
fields=[int(x) for x in re.findall(r'^(\d+)\. \*\*',execbody,re.M)]
check(fields==list(range(1,34)),'33-field contract incomplete')
steps=[int(x) for x in re.findall(r'^(\d+)\. \*\*',current['PLAN-1'][1],re.M)]
check(steps==list(range(1,10)),'Nine-step plan incomplete')
for rid in changed:
    check(f'| [{rid}](#{rid.lower()}) |' in new,'Missing refinement explanation '+rid)
check('### 44.44.' not in new,'Research heading misnumbered')
result={'scope':'Exact rule text after only expected historical-link conversion, titles/metadata, anchors, source objects, and required numbered contracts; substantive review still required.', 'baseline_sha256':hashlib.sha256(base.encode()).hexdigest(),'candidate_sha256':hashlib.sha256(new.encode()).hexdigest(),'unchanged_original_rules':len(old)-len(actual_changed),'refined_original_rules':actual_changed,'new_rules':sorted(set(current)-set(old)),'retired_original_rules':[],'original_anchors':len(old_anchors),'preserved_original_anchors':len(old_anchors&new_anchors),'historical_sources_verified':len(set(historical)),'original_tree_files_linked':len(paths),'subphase_fields':len(fields),'planning_steps':len(steps),'errors':errors}
(work/'integration-semantic-preservation.json').write_text(json.dumps(result,indent=2)+'\n')
(work/'integration-rule-diffs.txt').write_text(''.join(diffs))
print(json.dumps(result,indent=2))
raise SystemExit(bool(errors))
