from webhook import webhook

webhook_url="https://selene.roimarmier.xyz/api/v1/webhooks"
free_mem_gb=24
high_vram=True



# webhook(url=webhook_url, event='starting', data={
#     'free_vram_gb': free_mem_gb,
#     'high_vram': high_vram,
# })

webhook(url=webhook_url, event='ready', data={
    'free_vram_gb': free_mem_gb,
    'high_vram': high_vram,
})