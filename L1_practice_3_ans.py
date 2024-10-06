#%%
import json

str1 = '''
{
    "recomd_id": "rg1-w4wd_normal_1726785910_781597733",
    "took": 6.0,
    "timed_out": false,
    "recomd_list": [
        {
            "id": "DICY4Z-A900GKZC9",
            "name": "eminent品牌旗艦館 - 28吋 霧面PC可擴充行李箱 KG93(多色可選)",
            "score": 191.3,
            "sale_price": 4599.0,
            "category_code": "",
            "goods_page_url": "",
            "goods_img_url": "https://cs-e.ecimg.tw/items/DICY4ZA900GKZC9/000002_1711335842.jpg",
            "ref_item_list": [
                {
                    "item_name": "Product-A",
                    "alg_name": "I2I_Model",
                    "ref_model": "cooc_pn",
                    "score": 98.0
                },
                {
                    "item_name": "Product-B",
                    "alg_name": "I2I_Model",
                    "ref_model": "content_i2i",
                    "score": 93.3
                }
            ],
            "why": "",
            "sales": null,
            "group_category_code": "",
            "msg_type": "bsim",
            "msg": "看此商品也看",
            "msg_score": 98.0
        },
        {
            "id": "DICY4Z-A900G2SXR",
            "name": "eminent品牌旗艦館 - Probeetle - 28吋 繽紛撞色PC行李箱 KJ95(共三色)",
            "score": 178.6,
            "sale_price": 4080.0,
            "category_code": "",
            "goods_page_url": "",
            "goods_img_url": "https://cs-d.ecimg.tw/items/DICY4ZA900G2SXR/003002_1677219190.jpg",
            "ref_item_list": [
                {
                    "item_name": "Product-C",
                    "alg_name": "I2I_Model",
                    "ref_model": "cooc_pn",
                    "score": 97.0
                },
                {
                    "item_name": "Product-D",
                    "alg_name": "I2I_Model",
                    "ref_model": "content_i2i",
                    "score": 80.6
                }
            ],
            "why": "",
            "sales": null,
            "group_category_code": "",
            "msg_type": "bsim",
            "msg": "看此商品也看",
            "msg_score": 98.0
        },
        {
            "id": "DICY4Z-A900GDIST",
            "name": "eminent品牌旗艦館 -  28吋 拉鍊PC行李箱 KH12 (多色可選)",
            "score": 282.9,
            "sale_price": 3599.0,
            "category_code": "",
            "goods_page_url": "",
            "goods_img_url": "https://cs-c.ecimg.tw/items/DICY4ZA900GDIST/000002_1722221699.jpg",
            "ref_item_list": [
                {
                    "item_name": "Product-E",
                    "alg_name": "I2I_Model",
                    "ref_model": "cooc_pn",
                    "score": 95.0
                },
                {
                    "item_name": "Product-F",
                    "alg_name": "I2I_Model",
                    "ref_model": "content_i2i",
                    "score": 87.8
                },
                {
                    "item_name": "Product-G",
                    "alg_name": "I2I_Model",
                    "ref_model": "tp",
                    "score": 97.1
                }
            ],
            "why": "",
            "sales": null,
            "group_category_code": "",
            "msg_type": "bsim",
            "msg": "看此商品也看",
            "msg_score": 98.0
        }
    ]
}

'''


#%%
print(f"\n《Test 1》")
J = json.loads(str1)
Product_A_Score = J['recomd_list'][0]['ref_item_list'][0]['score']
Product_B_Score = J['recomd_list'][0]['ref_item_list'][1]['score']
Product_C_Score = J['recomd_list'][1]['ref_item_list'][0]['score']
Product_D_Score = J['recomd_list'][1]['ref_item_list'][1]['score']
Product_E_Score = J['recomd_list'][2]['ref_item_list'][0]['score']
Product_F_Score = J['recomd_list'][2]['ref_item_list'][1]['score']
Product_G_Score = J['recomd_list'][2]['ref_item_list'][2]['score']

print(f"Product-A's Score is: {Product_A_Score}")
print(f"Product-B's Score is: {Product_B_Score}")
print(f"Product-C's Score is: {Product_C_Score}")
print(f"Product-D's Score is: {Product_D_Score}")
print(f"Product-E's Score is: {Product_E_Score}")
print(f"Product-F's Score is: {Product_F_Score}")
print(f"Product-G's Score is: {Product_G_Score}")

#%%
print(f"\n《Test 2》")
for I in J['recomd_list']:
    for i in I['ref_item_list']:
        if (i['score'] > 90):
            print(f"{i['item_name']} is {i['score']}: PASS")  
        else:
            print(f"{i['item_name']} is {i['score']}: FAIL")
