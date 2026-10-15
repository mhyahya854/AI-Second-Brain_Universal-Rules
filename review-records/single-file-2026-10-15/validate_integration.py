"""Independent structural checks for the one-file constitution; no semantic certification."""
import collections, hashlib, json, pathlib, re, subprocess, sys

root = pathlib.Path(sys.argv[1])
text = (root / 'MASTER_PLAN.md').read_text()
raw = (root / 'MASTER_PLAN.md').read_bytes()
baseline = subprocess.check_output(['git', 'show', 'a9c597c8f14536a4404a64494cf56e9015e1288a:UNIVERSL RULES FOR ALL APPS.md'], cwd=root).decode()
errors = []
def check(ok, message):
    if not ok: errors.append(message)
def rules(s):
    found = {}
    for m in re.finditer(r'^### (?:\d+(?:\.\d+)*\.?\s+)?([A-Z]+-\d+) — ([^\n]+)\n(.*?)(?=\n<a id=|\Z)', s, re.M | re.S):
        key, title, body = m.groups()
        check(key not in found, 'Duplicate rule ' + key)
        meta = re.search(r'\*\*Type:\*\* (.*?) \| \*\*Origin:\*\* (.*?) \| \*\*Applies:\*\* ([^\n]+)', body)
        check(meta is not None, 'Missing classification ' + key)
        found[key] = {'title': title, 'body': body, 'metadata': meta.groups() if meta else None}
    return found
old, new = rules(baseline), rules(text)
check(len(old) == 113, 'Unexpected baseline rule count')
check(set(old) <= set(new), 'Missing original rules: ' + str(sorted(set(old)-set(new))))
check(all(old[k]['title'] == new[k]['title'] for k in old if k in new), 'Original rule title changed')
metadata_changes = [k for k in old if k in new and old[k]['metadata'] != new[k]['metadata']]
check(not metadata_changes, 'Original metadata changed: '+str(metadata_changes))
def normalized_body(s):
    # Numbered headings are outside these bodies; link destinations alone changed for provenance.
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s).strip()
body_changes = [k for k in old if k in new and normalized_body(old[k]['body']) != normalized_body(new[k]['body'])]
old_family = baseline.split('| Universal skill family |',1)[1].strip()
new_family = text.split('| Universal skill family |',1)[1].split('<a id="s34">',1)[0].strip()
check(normalized_body(old_family) == normalized_body(new_family), 'Skill family catalog content changed')
family_count = len([x for x in new_family.splitlines()[2:] if x.startswith('|')])
check(family_count == 33, 'Skill family count differs from 33')
anchors = re.findall(r'<a id="([^"]+)"></a>', text)
check(len(anchors) == len(set(anchors)), 'Duplicate explicit anchors')
links = re.findall(r'\[[^\]\n]+\]\(([^\s)]+)\)', text)
missing = sorted({x[1:] for x in links if x.startswith('#') and x[1:] not in anchors})
check(not missing, 'Missing targets: '+str(missing))
local = [x for x in links if not x.startswith(('#','https://','http://','mailto:'))]
check(not local, 'Active local file links: '+str(local))
check('NOT RATIFIED' in text, 'Missing explicit unratified status')
sections = re.findall(r'^## (\d+)\. (.+)$', text, re.M)
nums = [int(x[0]) for x in sections]
check(nums == list(range(nums[0], nums[0]+len(nums))) and nums[0] in (0,1), 'Non-sequential sections')
check({int(x[1:]) for x in anchors if re.fullmatch(r's\d+',x)} == {n for n in nums if n>0}, 'Section anchors and main headings disagree')
for n, title in sections:
    check((n == '0' and 'contents' in anchors) or f's{int(n):02}' in anchors, 'Missing section anchor '+n)
check(not re.search(r'^(<<<<<<<|=======|>>>>>>>)', text, re.M), 'Merge conflict marker')
fence = None
last_level = 1
for i,line in enumerate(text.splitlines(),1):
    fm = re.match(r'^\s*(`{3,}|~{3,})',line)
    if fm:
        token=fm.group(1)
        if fence is None: fence=token
        elif token[0]==fence[0] and len(token)>=len(fence): fence=None
        continue
    if fence: continue
    h=re.match(r'^(#{1,6})\s',line)
    if h:
        level=len(h.group(1))
        check(level<=last_level+1, f'Heading jump at {i}')
        last_level=level
check(fence is None,'Unclosed fenced block')
tracked=subprocess.check_output(['git','ls-files'],cwd=root).decode().splitlines()
check(tracked==['MASTER_PLAN.md'],'Index is not single-file: '+str(tracked))
actual=sorted(str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts)
check(actual==['MASTER_PLAN.md'],'Worktree is not single-file: '+str(actual))
extra_dirs=sorted(str(p.relative_to(root)) for p in root.rglob('*') if p.is_dir() and '.git' not in p.relative_to(root).parts)
check(not extra_dirs, 'Unexpected worktree directories: '+str(extra_dirs))
result={'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'baseline_rules':len(old),'final_rules':len(new),'new_rules':sorted(set(new)-set(old)),'metadata_changes':metadata_changes,'original_body_changes':body_changes,'original_unchanged_bodies':len(old)-len(body_changes),'skill_families':family_count,'sections':len([n for n in nums if n>0]),'navigation_sections':sum(n==0 for n in nums),'anchors':len(anchors),'internal_links':sum(x.startswith('#') for x in links),'inline_links':len(links),'tracked_files':tracked,'errors':errors,'scope':'Structure and identity checks only; semantic/factual/authority review is separate.'}
print(json.dumps(result,indent=2))
sys.exit(bool(errors))
