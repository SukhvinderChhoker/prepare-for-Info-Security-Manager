from pypdf import PdfReader
import re
from collections import Counter

def text(p):
    r = PdfReader(p)
    return ' '.join((pg.extract_text() or '') for pg in r.pages)

docs = {
    'SOC 2 doc':    r'C:\Users\Hacker-CeTF\Documents\gg\soc2-nbfc\SOC2_for_NBFC_Playbook.pdf',
    'PCI DSS doc':  r'C:\Users\Hacker-CeTF\Documents\gg\pci-dss-nbfc\PCI_DSS_v4_for_NBFC_Playbook.pdf',
    'Joint doc':    r'C:\Users\Hacker-CeTF\Documents\gg\soc2-pci-joint\SOC2_PCI_DSS_Joint_Companion_Playbook.pdf',
}

txts = {k: text(v) for k,v in docs.items()}
print('=== Word counts ===')
for k,v in txts.items():
    print('  ' + k + ': ' + str(len(v.split())))

print()
print('=== Unique tokens per doc (>= 4 chars) ===')
PAT = re.compile(r'[a-zA-Z]{4,}')
counters = {k: Counter(PAT.findall(v.lower())) for k,v in txts.items()}
for k,c in counters.items():
    others = set().union(*(set(counters[o]) for o in counters if o != k))
    unique = set(c) - others
    print('  ' + k.ljust(14) + ': total=' + str(len(c)) + ', unique-to-doc=' + str(len(unique)))

print()
print('=== Overlap analysis ===')
def unique_to(doc, *others):
    return set(counters[doc]) - set().union(*(set(counters[o]) for o in others))

j_only  = unique_to('Joint doc',   'SOC 2 doc', 'PCI DSS doc')
soc_only = unique_to('SOC 2 doc',  'PCI DSS doc', 'Joint doc')
pci_only = unique_to('PCI DSS doc','SOC 2 doc', 'Joint doc')
all_three = set(counters['Joint doc']) & set(counters['SOC 2 doc']) & set(counters['PCI DSS doc'])

print('  Words unique to joint   doc:', len(j_only))
print('  Words unique to SOC 2   doc:', len(soc_only))
print('  Words unique to PCI DSS doc:', len(pci_only))
print('  Words in all three           :', len(all_three), '->', sorted(all_three)[:30])

print()
print('=== Joint doc distinctive words ===')
distinctive_j = sorted(j_only - {'pci','soc','audit','control','joint'})[:40]
print('  Sample:', distinctive_j)

# look for very specific titles in each
soc_only_distinctive = sorted(soc_only - {'soc','audit','control','joint','iso'})
pci_only_distinctive = sorted(pci_only - {'pci','audit','control','joint','soc'})
print()
print('=== SOC 2 doc distinctive ===')
print('  Sample:', sorted(soc_only_distinctive)[:30])
print()
print('=== PCI DSS doc distinctive ===')
print('  Sample:', sorted(pci_only_distinctive)[:30])
