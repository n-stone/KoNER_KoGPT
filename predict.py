import torch
import config
from transformers import AutoTokenizer, AutoModelForCausalLM
from pdata import Data

tokenizer = AutoTokenizer.from_pretrained(
  config.model_name, revision=config.model_revision,  
  bos_token='[BOS]', eos_token='[EOS]', unk_token='[UNK]', pad_token='[PAD]', mask_token='[MASK]'
)
model = AutoModelForCausalLM.from_pretrained(
  config.model_name, revision=config.model_revision,
  pad_token_id=tokenizer.eos_token_id,
  torch_dtype=config.torch_dtype, low_cpu_mem_usage=config.low_cpu_mem_usage
).to(device=config.device, non_blocking=config.non_blocking)
_ = model.eval()

class predict:
  def __init__(self):
    self.tokenizer = tokenizer
    self.model = model
    
  def generate(self, text):
    dtx_list = []
    for que in text:
      prompt = que
      with torch.no_grad():
        tokens = self.tokenizer.encode(prompt, return_tensors=config.return_tensors).to(device=config.device, non_blocking=config.non_blocking)
        gen_tokens = self.model.generate(tokens, do_sample=config.do_sample, temperature=config.temperature, max_length=config.max_length)
        generated = self.tokenizer.batch_decode(gen_tokens)[0]
        result_dtx = generated.split('. ', maxsplit=config.maxsplit)
        dtx_list.append(result_dtx)
        
    return dtx_list