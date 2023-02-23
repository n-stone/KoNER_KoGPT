# predict param
model_name = 'kakaobrain/kogpt'
model_revision = 'KoGPT6B-ryan1.5b-float16'
device='cuda'
torch_dtype='auto'
low_cpu_mem_usage=True
non_blocking=True
return_tensors='pt'
do_sample=True
temperature=0.8
max_length=64
maxsplit=4

