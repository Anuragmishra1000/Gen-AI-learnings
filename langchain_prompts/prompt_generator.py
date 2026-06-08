from langchain_core.prompts import PromptTemplate


template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template=(
        'You are an expert AI researcher. Explain the research paper "{paper_input}" '
        "in a {style_input} style. Provide a {length_input} explanation covering the "
        "key contributions, methodology, and impact of the paper."
    ),
    validate_template=True
)


template.save('prompt_template.json')


