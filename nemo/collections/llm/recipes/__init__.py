# Copyright (c) 2024, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from nemo.collections.llm.recipes import (
    baichuan2_7b,
    chatglm3_6b,
    gemma_2b,
    gemma_7b,
    gpt3_175b,
    hf_auto_model_for_causal_lm,
    llama3_8b,
    llama3_8b_16k,
    llama3_8b_64k,
    llama3_70b,
    llama3_70b_16k,
    llama3_70b_64k,
    llama31_405b,
    mamba2_1_3b,
    mamba2_2_7b,
    mamba2_8b,
    mamba2_130m,
    mamba2_370m,
    mamba2_780m,
    mamba2_hybrid_8b,
    mistral_7b,
    mistral_nemo_12b,
    mixtral_8x7b,
    mixtral_8x7b_16k,
    mixtral_8x7b_64k,
    mixtral_8x22b,
    nemotron,
    nemotron3_4b,
    nemotron3_8b,
    nemotron4_15b,
    nemotron4_15b_16k,
    nemotron4_15b_64k,
    nemotron4_22b,
    nemotron4_22b_16k,
    nemotron4_22b_64k,
    nemotron4_340b,
)
from nemo.collections.llm.recipes.log.default import default_log, default_resume
from nemo.collections.llm.recipes.optim import adam

__all__ = [
    "baichuan2_7b",
    "chatglm3_6b",
    "gemma_2b",
    "gemma_7b",
    "llama3_8b",
    "llama3_8b_16k",
    "llama3_8b_64k",
    "llama3_70b",
    "llama3_70b_16k",
    "llama3_70b_64k",
    "llama31_405b",
    "mamba2_130m",
    "mamba2_370m",
    "mamba2_780m",
    "mamba2_1_3b",
    "mamba2_2_7b",
    "mamba2_8b",
    "mamba2_hybrid_8b",
    "mistral_7b",
    "mistral_nemo_12b",
    "hf_auto_model_for_causal_lm",
    "mixtral_8x7b",
    "mixtral_8x7b_16k",
    "mixtral_8x7b_64k",
    "mixtral_8x22b",
    "nemotron",
    "nemotron3_4b",
    "nemotron3_8b",
    "nemotron4_15b",
    "nemotron4_15b_16k",
    "nemotron4_15b_64k",
    "nemotron4_22b",
    "nemotron4_22b_16k",
    "nemotron4_22b_64k",
    "nemotron4_340b",
    "gpt3_175b",
    "adam",
    "default_log",
    "default_resume",
]
