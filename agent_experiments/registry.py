"""
A registry to define the supported datasets, models, and tasks.
"""

# Data Handlers
DATA_HANDLER_REG = {
    'dnd': ('data', 'DNDHandler'),
    'casino': ('data', 'CasinoHandler')
}

# LLM APIs
LLM_API_REG = {
    "dummy": ("misc.dummies", "DummyModelHandler"),
    "openai_generic": ("lang_models.llm_apis.open_ai", "OpenAI_Api"),
    # TODO: THESE ARE NOT YET IMPLEMENTED
    "llama_7b": ("lang_models.llm_apis.llama", "Llama7BHandler"),
    "falcon_7b": ("lang_models.llm_apis.falcon", "Falcon7BHandler"),
    "falcon_40b": ("lang_models.llm_apis.falcon", "Falcon40BHandler"),
    "gpt_4": ("lang_models.llm_apis.gpt_4", "GPT_4_Api"),
}

# Functions for Annotation
INST2ANNOT_PROMPT_FUN_REG = {
    "example": ("data.conversion.inst2p_functions", "example_inst2p_func"),  # TODO: COMMENTS EXPLAINING PATTERN IN HERE
}

INST_ANNOT2STR_PROMPT_FUN_REG = {
    "example": ("data.conversion.annot2str_functions", "example_annot2s_func")  # TODO: COMMENTS EXPLAINING PATTERN IN HERE
}

# Generator Functions (for planning)
ACT2UTT_PROMPT_FUN_REG = {
    "example": ("lang_models.llm_apis.prompting.act2utt_functions", "example_a2u_func")  # TODO: COMMENTS EXPLAINING PATTERN IN HERE
}

# Parser Functions (for planning)
UTT2ACT_PROMPT_FUN_REG = {
    "example": ("lang_models.llm_apis.prompting.utt2act_functions", "example_u2a_func")  # TODO: COMMENTS EXPLAINING PATTERN IN HERE
}

# Response Generation Functions (dialogue or choice responses)
RESPONSE_PROMPT_FUN_REG = {
    "example_dia_resp": ("lang_models.llm_apis.prompting.dia_response_funcitons", "example_dia_response_func"),  # TODO: COMMENTS EXPLAINING PATTERN IN HERE
    "example_choice": ("lang_models.llm_apis.prompting.dia_response_funcitons", "example_choice_func")  # TODO: COMMENTS EXPLAINING PATTERN IN HERE
}
