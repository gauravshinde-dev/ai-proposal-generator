from ai_generator import generate_proposal_content
from latex_exporter import save_proposal_as_pdf

if __name__ == "__main__":
    user_input = input("Enter your project idea or title: ")
    print("\nGenerating proposal using AI...\n")

    # Step 1: Generate proposal text from OpenAI
    proposal_text = generate_proposal_content(user_input)

    print("Generated Content:\n")
    print(proposal_text)

    # Step 2: Save the content to PDF
    print("\nSaving to PDF...")
    save_proposal_as_pdf(proposal_text, filename="generated_proposal")
    print("✅ Proposal saved as 'generated_proposal.pdf'")
