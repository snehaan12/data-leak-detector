from presidio_analyzer import AnalyzerEngine

analyzer = AnalyzerEngine()

def scan_with_presidio(text: str):
    results = analyzer.analyze(text=text, language='en')
    findings = []
    for result in results:
        findings.append({
            "entity_type": result.entity_type,
            "score": result.score,
            "text": text[result.start:result.end]
        })
    return findings
