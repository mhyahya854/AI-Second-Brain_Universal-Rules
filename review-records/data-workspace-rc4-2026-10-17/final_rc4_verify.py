#!/usr/bin/env python3
"""Read-only final checkout receipt. Clone/fetch is the caller's responsibility."""
import argparse, hashlib, json, pathlib, subprocess, sys
ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--commit',required=True);ap.add_argument('--sha256',required=True);ap.add_argument('--branch',required=True);ap.add_argument('--main',required=True,help='Expected remote main commit');ap.add_argument('--output',required=True);a=ap.parse_args()
repo=pathlib.Path(a.repo).resolve();here=pathlib.Path(__file__).resolve().parent
checks={};errors=[]
def run(*cmd):
 p=subprocess.run(cmd,capture_output=True,text=True);return {'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
def git(*args):return run('git','-C',str(repo),*args)
def check(name,ok,evidence):
 checks[name]={'passed':bool(ok),'evidence':evidence}
 if not ok:errors.append(name)
base=json.loads((here/'rc4-baseline.json').read_text())
head=git('rev-parse','HEAD');check('checkout_commit',head['stdout'].strip()==a.commit,head)
blob=git('rev-parse','HEAD:MASTER_PLAN.md');digest=hashlib.sha256((repo/'MASTER_PLAN.md').read_bytes()).hexdigest();check('document_sha256',digest==a.sha256,digest)
tree=git('ls-tree','-r','--name-only','HEAD');check('one_file_tree',tree['stdout'].splitlines()==['MASTER_PLAN.md'],tree)
status=git('status','--porcelain');check('clean_checkout',status['returncode']==0 and not status['stdout'],status)
ancestor=git('merge-base','--is-ancestor',base['commit'],a.commit);check('former_main_ancestor',ancestor['returncode']==0,ancestor)
refs=git('ls-remote','--heads','origin');lookup={line.split()[1]:line.split()[0] for line in refs['stdout'].splitlines()}
check('remote_candidate',lookup.get('refs/heads/'+a.branch)==a.commit,lookup.get('refs/heads/'+a.branch))
check('remote_main',lookup.get('refs/heads/main')==a.main,lookup.get('refs/heads/main'))
for name,expected in base['historical_refs'].items():
 check('historical_ref:'+name,lookup.get('refs/heads/'+name)==expected,lookup.get('refs/heads/'+name))
 p=git('ls-tree','-r',expected);check('historical_tree:'+name,p['returncode']==0,p)
 # Read every blob, including all old review records, not just tree existence.
 entries=git('ls-tree','-r','--format=%(objectname) %(objecttype)',expected)
 unreadable=[]
 for line in entries['stdout'].splitlines():
  oid,typ=line.split()
  if typ=='blob':
   proc=subprocess.run(['git','-C',str(repo),'cat-file','blob',oid],stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
   if proc.returncode:unreadable.append(oid)
 check('historical_blobs:'+name,entries['returncode']==0 and not unreadable,{'unreadable':unreadable,'object_count':len(entries['stdout'].splitlines())})
for label,args in [('git_fsck',('fsck','--full','--strict')),('git_show_check',('show','--check','--oneline',a.commit))]:
 p=git(*args);check(label,p['returncode']==0,p)
structural=run(sys.executable,str(here/'validate_rc4.py'),'--repo',str(repo),'--output',str(pathlib.Path(a.output).with_name('rc4-final-structural.json')))
check('structural',structural['returncode']==0,structural)
result={'scope':'Read-only remote refs, exact checkout, recoverable history and structural receipt; not Red review or ratification','commit':a.commit,'blob':blob['stdout'].strip(),'sha256':digest,'checks':checks,'errors':errors,'passed':not errors}
pathlib.Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':not errors,'errors':errors,'output':a.output}));sys.exit(bool(errors))
