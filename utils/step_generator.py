def structure_steps(text):
    sentences = text.split('. ')
    steps = [f"**Step {i+1}:** {sent.strip()}" for i, sent in enumerate(sentences) if sent]
    return "\n\n".join(steps)
