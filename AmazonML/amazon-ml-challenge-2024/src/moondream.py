import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


def get_moondream2():
    DEVC = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    DTYP = torch.float16 if torch.cuda.is_available() else torch.float32
    mdid = "vikhyatk/moondream2"
    mdrv = "2024-08-26"
    tokenizer = AutoTokenizer.from_pretrained(mdid, revision=mdrv)
    moondream = AutoModelForCausalLM.from_pretrained(
        mdid,
        revision=mdrv,
        trust_remote_code=True,
        torch_dtype=DTYP,
        device_map={"": DEVC},
    )
    return tokenizer, moondream, DEVC, DTYP

learn_rate = 3e-5
max_epochs = 1
batch_size = 16
grad_acc_s = 2
img_tokens = 729
answer_eos = "<|endoftext|>"
    