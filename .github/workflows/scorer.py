import re

def score_description(vendor_desc, internal_format=None):
    """
    Enhanced scoring function for business description comparison.
    Scores based on presence of required sections and style/grammar rules.
    """
    score = 0
    weights = {
        "primary business": 1.0,
        "name/ownership": 0.75,
        "spelling": 0.75,
        "grammar": 0.5,
        "name change": 0.25,
        "clients/distribution": 0.25,
        "formatting": 0.25,
    }

    # Section checks (add more as needed)
    sections = [
        ("primary business", r"(manufactures|provides|offers|operates|is a holding company)"),
        ("clients/distribution", r"(serves|clients|customer|industries|distribution|distributor|retail)"),
        ("products", r"(products|services|solutions|applications|equipment|software)"),
        ("geography", r"(operates in|based in|headquarters|markets|offices in)"),
        ("alliances", r"(partnership|alliance|subsidiary|parent company|strategic partner)"),
        ("name change", r"(formerly known as|was acquired by|name change|acquired by)"),
        ("bankruptcy", r"(bankruptcy|reorganization|insolvency)"),
    ]
    for label, pattern in sections:
        if re.search(pattern, vendor_desc, re.IGNORECASE):
            if label in weights:
                score += weights[label]
            else:
                score += 0.25  # default small weight

    # Style/grammar checks
    if "leading" in vendor_desc.lower() or "innovative" in vendor_desc.lower():
        score -= 0.5  # penalize promotional words
    if "doesn't" in vendor_desc or "isn't" in vendor_desc:
        score -= 0.25  # penalize contractions
    if "comprises of" in vendor_desc:
        score -= 0.25  # penalize incorrect phrase

    # Bonus for present tense (simple check)
    if re.search(r"\b(provides|offers|manufactures|serves|operates)\b", vendor_desc):
        score += 0.25

    return max(score, 0)