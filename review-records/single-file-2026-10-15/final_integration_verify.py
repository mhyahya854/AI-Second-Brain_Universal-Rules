"""Fresh GitHub verification of the final one-file candidate; fails on any mismatch."""
import datetime, hashlib, json, pathlib, subprocess, sys

sha, digest, clone_dir = sys.argv[1:4]
root = pathlib.Path(clone_dir)
repo = 'https://github.com/mhyahya854/Universal-Rules.git'
branch = 'constitution/single-file-integration-2026-10-14'
def run(args, cwd=None):
    return subprocess.check_output(args, cwd=cwd, stderr=subprocess.STDOUT).decode().strip()
refs = dict(line.split('\t')[::-1] for line in run(['git','ls-remote',repo]).splitlines())
assert refs['refs/heads/main'] == sha
assert refs['refs/heads/'+branch] == sha
assert refs['refs/heads/constitution/pre-ratification-working'] == 'a9c597c8f14536a4404a64494cf56e9015e1288a'
assert refs['refs/heads/review-history/universal-rules-convergence'] == 'b5ac54fb98304515ae394507ae8dbcd0f6fe54d7'
assert not root.exists(), 'Use a new checkout path'
run(['git','clone','--branch','main',repo,str(root)])
assert run(['git','rev-parse','HEAD'],root) == sha
files = run(['git','ls-files'],root).splitlines()
assert files == ['MASTER_PLAN.md']
assert sorted(p.name for p in root.iterdir()) == ['.git','MASTER_PLAN.md']
assert not run(['git','status','--porcelain'],root)
data = (root/'MASTER_PLAN.md').read_bytes()
assert hashlib.sha256(data).hexdigest() == digest
assert 'NOT RATIFIED' in data.decode()
run(['git','fsck','--full','--strict'],root)
run(['git','show','--check','--oneline','HEAD'],root)
run(['git','merge-base','--is-ancestor','c2fd9e3d8ac8c41a2ec1e336d2ec097314ef80a5',sha],root)
baseline = subprocess.check_output(['git','show','a9c597c8f14536a4404a64494cf56e9015e1288a:UNIVERSL RULES FOR ALL APPS.md'],cwd=root)
assert hashlib.sha256(baseline).hexdigest() == '1c6471ab3ec5291b9cd4ec884912ccec10431d2e35e9e514ad29574b778b082d'
old_records=run(['git','ls-tree','-r','--name-only','b5ac54fb98304515ae394507ae8dbcd0f6fe54d7','review-records/'],root).splitlines()
assert len(old_records)==6
structure=json.loads(run(['python','/workspace/work/validate_integration.py',str(root)]))
result={'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':repo,'main_sha':sha,'candidate_branch':branch,'candidate_sha':sha,'tree':run(['git','rev-parse','HEAD^{tree}'],root),'blob':run(['git','rev-parse','HEAD:MASTER_PLAN.md'],root),'sha256':digest,'bytes':len(data),'files':files,'clean_checkout':True,'historical_candidate_unchanged':True,'historical_review_branch_unchanged':True,'historical_review_records':len(old_records),'initial_main_is_ancestor':True,'git_integrity':'passed','whitespace':'passed','structure':structure,'evidence_ref_observed':refs['refs/heads/review-history/single-file-integration-2026-10-14'],'ratification':'NOT RATIFIED','scope':'Remote repository/content/integrity validation; does not substitute for independent policy review or application runtime tests.'}
print(json.dumps(result,indent=2))
