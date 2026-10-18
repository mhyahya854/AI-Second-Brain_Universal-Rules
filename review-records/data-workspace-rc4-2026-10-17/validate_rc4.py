#!/usr/bin/env python3
"""Read-only structural and byte preservation audit; does not test an application."""
import argparse,collections,difflib,hashlib,json,pathlib,re,subprocess,urllib.parse,sys
ROOT=pathlib.Path('/workspace/work/rc4'); WORK=ROOT.parent
BASE='73b2e8adb0236af7d4e503e67f9d507148cc95b7'
ORIGINAL='a9c597c8f14536a4404a64494cf56e9015e1288a'
DIGEST='07a0976686215cb68e4a0bf63d56aecfb9ec183e7946f84d4855f103fa110460'
REFS=['constitution/pre-ratification-working','constitution/single-file-integration-2026-10-14','review-history/universal-rules-convergence','review-history/single-file-integration-2026-10-14']
def git(*args): return subprocess.check_output(['git','-C',str(ROOT),*args],stderr=subprocess.STDOUT)
def sha(b): return hashlib.sha256(b).hexdigest()
def parse(b):
 t=b.decode(); lines=t.splitlines(); clean=[]; fence=None; fence_errors=[]; pairs=0
 for n,l in enumerate(lines,1):
  m=re.match(r'^\s{0,3}(`{3,}|~{3,})(.*)$',l)
  if m:
   token=m[1]
   if fence is None: fence=(token[0],len(token),n)
   elif token[0]==fence[0] and len(token)>=fence[1] and not m[2].strip(): fence=None; pairs+=1
   clean.append(''); continue
  clean.append('' if fence else l)
 if fence: fence_errors.append({'unclosed_at':fence[2]})
 c='\n'.join(clean)
 headings=list(re.finditer(r'^(#{1,6})\s+(.+)$',c,re.M)); rules={}; ids=[]
 for i,h in enumerate(headings):
  m=re.match(r'(?:\d+(?:\.\d+)*\.?\s+)?([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-\d+)\s+[—–-]\s+(.+)',h[2])
  if not m: continue
  rid=m[1]; ids.append(rid)
  # Preserve code blocks in rule text by using line offsets in original text.
  start=c[:h.start()].count('\n')
  following=next((x for x in headings[i+1:] if len(x[1])<=len(h[1])),None)
  end=c[:following.start()].count('\n') if following else len(lines)
  block='\n'.join(lines[start:end]); block=re.sub(r'\n\s*<a id="[^"]+"></a>\s*$','',block).rstrip()
  meta=re.search(r'^\*\*Type:\*\* (.+?) \| \*\*Origin:\*\* (.+?) \| \*\*Applies:\*\* (.+)$',block,re.M)
  rules[rid]={'title':m[2],'sha256':sha(block.encode()),'line':start+1,'body':block,'metadata':dict(zip(['type','origin','applies'],meta.groups())) if meta else None}
 anchors=re.findall(r'<a\s+id=["\']([^"\']+)["\']\s*></a>',c)
 links=re.findall(r'\]\(([^\s)]+)(?:\s+[^)]*)?\)',c)
 internal=[urllib.parse.unquote(x[1:]) for x in links if x.startswith('#')]
 relative=[x for x in links if not x.startswith(('#','https://','http://','mailto:'))]
 nums=[]; heading_errors=[]; seen=set(); previous={}
 for h in headings:
  m=re.match(r'(\d+(?:\.\d+)*)\.?\s',h[2])
  if not m: continue
  ns=tuple(map(int,m[1].split('.'))); nums.append(m[1])
  if ns in seen: heading_errors.append('Duplicate section '+m[1])
  if len(ns)>1 and ns[:-1] not in seen: heading_errors.append('Missing parent '+m[1])
  if len(ns)+1!=len(h[1]): heading_errors.append('Heading depth '+m[1])
  parent=ns[:-1]
  expected=previous.get(parent, -1 if not parent else 0)+1
  if ns[-1]!=expected: heading_errors.append(f'Nonsequential {m[1]} expected suffix {expected}')
  previous[parent]=ns[-1]; seen.add(ns)
 skill_start=t.find('| Universal skill family |'); skill_end=t.find('\n<a ',skill_start)
 skill_rows=[l for l in t[skill_start:skill_end].splitlines()[2:] if l.startswith('|')]
 return {'sha256':sha(b),'bytes':len(b),'rule_count':len(ids),'rules':rules,'duplicate_rule_ids':[x for x,v in collections.Counter(ids).items() if v>1],'anchors':anchors,'anchor_count':len(anchors),'duplicate_anchors':[x for x,v in collections.Counter(anchors).items() if v>1],'internal_link_count':len(internal),'unresolved_internal_links':sorted(set(internal)-set(anchors)),'relative_links':relative,'external_links':[x for x in links if x.startswith(('https://','http://'))],'substantive_section_count':len([n for n in nums if '.' not in n and n!='0']),'heading_numbers':nums,'heading_errors':heading_errors,'fence_pairs':pairs,'fence_errors':fence_errors,'skill_families':skill_rows,'skill_family_count':len(skill_rows),'metadata_missing':[k for k,v in rules.items() if not v['metadata']]}
def main():
 global ROOT
 ap=argparse.ArgumentParser(); ap.add_argument('--repo',type=pathlib.Path,default=ROOT); ap.add_argument('--baseline',type=pathlib.Path,default=WORK/'rc4-baseline.json'); ap.add_argument('--baseline-only',action='store_true'); ap.add_argument('--output',default=str(WORK/'rc4-validation.json')); args=ap.parse_args(); ROOT=args.repo.resolve()
 base=parse(git('show',BASE+':MASTER_PLAN.md')); original=parse(git('show',ORIGINAL+':UNIVERSL RULES FOR ALL APPS.md'))
 refs={r:git('rev-parse','refs/remotes/origin/'+r).decode().strip() for r in REFS}
 evidence={**base,'commit':BASE,'original_commit':ORIGINAL,'original_rule_ids':sorted(original['rules']),'historical_refs':refs,'tracked_files':git('ls-tree','-r','--name-only',BASE).decode().splitlines()}
 baseline_path=args.baseline
 if not baseline_path.exists(): baseline_path.write_text(json.dumps(evidence,indent=2)+'\n')
 saved=json.loads(baseline_path.read_text()); errors=[]
 def require(ok,msg):
  if not ok: errors.append(msg)
 require(base['sha256']==DIGEST,'Baseline SHA mismatch'); require(base['rule_count']==137,'Baseline rule count mismatch'); require(len(original['rules'])==113,'Original rule count mismatch'); require(base['skill_family_count']==33,'Baseline skill count mismatch'); require(base['anchor_count']==201,'Baseline anchor count mismatch'); require(base['internal_link_count']==709,'Baseline internal link count mismatch')
 require(saved['sha256']==DIGEST,'Saved baseline SHA mismatch'); require(set(saved['rules'])==set(base['rules']),'Saved baseline IDs mismatch'); require(all(saved['rules'][k]['title']==base['rules'][k]['title'] and saved['rules'][k]['metadata']==base['rules'][k]['metadata'] for k in set(saved['rules'])&set(base['rules'])),'Saved baseline title/metadata mismatch'); require(refs==saved['historical_refs'],'Historical refs changed')
 if args.baseline_only:
  print(json.dumps({'errors':errors,'baseline':str(baseline_path),'counts':{k:base[k] for k in ['rule_count','skill_family_count','anchor_count','internal_link_count']}})); sys.exit(1 if errors else 0)
 cur=parse((ROOT/'MASTER_PLAN.md').read_bytes()); old=set(base['rules']); new=set(cur['rules']); modified=[k for k in base['rules'] if k in new and base['rules'][k]['sha256']!=cur['rules'][k]['sha256']]
 tracked=git('ls-files').decode().splitlines(); deleted=sorted(old-new); added=sorted(new-old)
 require(tracked==['MASTER_PLAN.md'],'Active index tree not exactly MASTER_PLAN.md'); require(not deleted,'Baseline rule IDs removed'); require(set(original['rules'])<=new,'Original rule IDs removed'); require(set(base['anchors'])<=set(cur['anchors']),'Baseline anchors removed'); require(base['skill_families']==cur['skill_families'],'Skill families altered'); require(refs==saved['historical_refs'],'Historical refs changed')
 for k in ['duplicate_rule_ids','duplicate_anchors','unresolved_internal_links','relative_links','heading_errors','fence_errors','metadata_missing']: require(not cur[k],k+': '+str(cur[k]))
 title_metadata_changes={k:{'before':{f:base['rules'][k][f] for f in ['title','metadata']},'after':{f:cur['rules'][k][f] for f in ['title','metadata']}} for k in old&new if any(base['rules'][k][f]!=cur['rules'][k][f] for f in ['title','metadata'])}
 require(not title_metadata_changes,'Baseline title/metadata altered: '+str(sorted(title_metadata_changes)))
 allowed_types={'UNIVERSAL INVARIANT','CONDITIONAL','DEFAULT','ECOSYSTEM POLICY','PROHIBITION','RECOMMENDATION'}
 allowed_origins={'ARCHITECTURAL DECISION','DERIVED ENGINEERING RULE','USER POLICY'}
 invalid_metadata=[k for k,v in cur['rules'].items() if v['metadata'] and (v['metadata']['type'] not in allowed_types or v['metadata']['origin'] not in allowed_origins or not v['metadata']['applies'].strip())]
 require(not invalid_metadata,'Invalid rule metadata: '+str(invalid_metadata))
 historical_ref_checks=[]
 for ref,commit in refs.items():
  cp=subprocess.run(['git','-C',str(ROOT),'fsck','--full',commit],capture_output=True,text=True)
  files=git('ls-tree','-r','--name-only',commit).decode().splitlines()
  historical_ref_checks.append({'ref':ref,'commit':commit,'tracked_files':files,'recoverable':cp.returncode==0,'fsck_output':cp.stdout+cp.stderr})
 require(all(x['recoverable'] for x in historical_ref_checks),'Historical ref objects inaccessible')
 historical_link_checks=[]
 for url in sorted(set(base['external_links']+cur['external_links'])):
  match=re.match(r'https://github.com/mhyahya854/Universal-Rules/blob/([0-9a-f]{40})/([^#]+)',url)
  if match:
   obj=match[1]+':'+urllib.parse.unquote(match[2]); cp=subprocess.run(['git','-C',str(ROOT),'cat-file','-e',obj],capture_output=True,text=True)
   historical_link_checks.append({'url':url,'object':obj,'resolvable':cp.returncode==0})
 require(all(x['resolvable'] for x in historical_link_checks),'Historical linked objects inaccessible')
 require(set(base['external_links'])<=set(cur['external_links']),'Existing external provenance links removed')
 fsck=subprocess.run(['git','-C',str(ROOT),'fsck','--full'],capture_output=True,text=True); require(fsck.returncode==0,'git fsck failed')
 diff=subprocess.run(['git','-C',str(ROOT),'diff','--check',BASE,'--','MASTER_PLAN.md'],capture_output=True,text=True); require(diff.returncode==0,'git diff --check failed')
 result={'scope':'Markdown structure, identities, byte preservation and local Git integrity only; no application implementation tests or semantic certification','baseline_commit':BASE,'baseline_sha256':base['sha256'],'candidate':cur,'original_rules_preserved':len(set(original['rules'])&new),'baseline_rules_preserved':len(old&new),'unchanged_baseline_rules':len(old)-len(modified)-len(deleted),'modified_rules':{k:{'before':base['rules'][k],'after':cur['rules'][k]} for k in modified},'added_rules':{k:cur['rules'][k] for k in added},'deleted_rules':deleted,'historical_refs':refs,'title_metadata_changes':title_metadata_changes,'invalid_metadata':invalid_metadata,'historical_ref_checks':historical_ref_checks,'historical_link_checks':historical_link_checks,'tracked_files':tracked,'git_fsck':{'returncode':fsck.returncode,'stdout':fsck.stdout,'stderr':fsck.stderr},'git_diff_check':{'returncode':diff.returncode,'output':diff.stdout+diff.stderr},'errors':errors,'passed':not errors}
 ledger=['RC3 to candidate full rule-body diff; subordinate headings included.\n']
 for k in modified+added+deleted:
  before=base['rules'].get(k,{}).get('body',''); after=cur['rules'].get(k,{}).get('body','')
  ledger.extend(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='rc3/'+k,tofile='candidate/'+k))
  ledger.append('\n')
 pathlib.Path(args.output).parent.joinpath('rc4-rule-diff.txt').write_text(''.join(ledger))
 pathlib.Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
 report=f"RC4 structural assessment\nCandidate SHA-256: {cur['sha256']}\nResult: {'PASS' if not errors else 'FAIL'}\nRules: {cur['rule_count']}; retained {len(old&new)}/137 RC3 and {len(set(original['rules'])&new)}/113 original.\nModified: {', '.join(modified) or '(none)'}.\nAdded: {', '.join(added) or '(none)'}.\nAnchors: {cur['anchor_count']}; internal links: {cur['internal_link_count']}; Skill families: {cur['skill_family_count']}.\nChecks are structural and preservation evidence only, not semantic approval or application tests.\nErrors: {errors}\n"
 pathlib.Path(args.output).with_suffix('.txt').write_text(report); print(report); sys.exit(1 if errors else 0)
if __name__=='__main__': main()
