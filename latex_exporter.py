from pylatex import Document, Section, Command
from pylatex.utils import NoEscape

def save_proposal_as_pdf(content: str, filename: str = "proposal"):
    doc = Document("basic", document_options="12pt")
    
    # Metadata
    doc.preamble.append(Command('title', 'AI-Generated Project Proposal'))
    doc.preamble.append(Command('author', 'AI Assistant'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    # Auto-format proposal content
    lines = content.split('\n')
    current_section = None

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped[0].isdigit() and stripped[1] == '.':
            # Format numbered headers as sections
            section_title = stripped[3:]
            current_section = doc.create(Section(section_title))
        elif current_section:
            current_section.append(line + "\n")
        else:
            doc.append(line + "\n")

    # Export to PDF and keep .tex file for Overleaf
    doc.generate_pdf(filename, clean_tex=False)
