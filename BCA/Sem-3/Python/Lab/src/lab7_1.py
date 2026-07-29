def analyze_participants(coding_set,design_set):
	print(f"Students who attened both events: {coding_set & design_set}")
	print(f"Students who attened only the coding competition:{coding_set - design_set}")
	print(f"Total unique students across either event: {len(coding_set | design_set)}")

coding = {"25301","25302","253011","253012","253017"}
desing = {"25301","253011","25305","253010","253012"}
analyze_participants(coding,desing)
