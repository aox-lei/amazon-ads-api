import json

from src.ads_api.ads_v1.sp_global.campaigns import ListGlobalCampaignResponse

with open("1.json", "r") as f:
    data = json.load(f)

print(ListGlobalCampaignResponse(**data))