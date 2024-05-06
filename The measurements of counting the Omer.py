seven_medot = ["hesed", "gvura", "tefert", "nezah", "hod", "yesod", "malhoot"]"""מערך של 7 הספירות"""
for i in range(49):
    day = seven_medot[i % 7]
    week = seven_medot[i // 7]
    print(f"{day} in {week}")
