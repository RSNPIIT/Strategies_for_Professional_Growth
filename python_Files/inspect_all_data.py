import generate_unified_interim_reports as g

members = [
    ('Samyabrata', g.REPORT_SAMYABRATA),
    ('Abir', g.REPORT_ABIR),
    ('Rishabh', g.REPORT_RISHABH),
    ('Piyush', g.REPORT_PIYUSH),
    ('Ramrup', g.REPORT_RAMRUP),
]

for name, r in members:
    print(f"=== {name} ===")
    print("Interviewer:", r['interviewer'])
    print("Findings count:", len(r['findings']))
    print("First finding:", r['findings'][0])
